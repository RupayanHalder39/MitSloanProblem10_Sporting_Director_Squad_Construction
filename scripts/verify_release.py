#!/usr/bin/env python3
"""Verify frozen public claims and release-file integrity for Problem 10."""

from __future__ import annotations

import csv
import hashlib
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TABLES = ROOT / "results" / "tables"

EXPECTED_HASHES = {
    "paper/Problem10_Director_or_Club_MIT_Sloan_Abstract.pdf":
        "efcc8545e2464ac0f2d904c777523b5cd37b33c60be5a1810765ed759a6bd68e",
    "figures/Figure1_YouthShare_ClubResource.png":
        "12bc9025d82e860667d51fbe8a7655bec00356b9dae183f505ccd97d92a14ccb",
    "figures/Figure2_ClubValueQuartileCoverage.png":
        "4e24aca5e15cce9a2c19c2a29e22fd2433c90c957214e2d0ef619788cca7c664",
}


def rows(name: str) -> list[dict[str, str]]:
    with (TABLES / name).open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle))


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str, errors: list[str]) -> None:
    if not condition:
        errors.append(message)


def main() -> int:
    errors: list[str] = []

    for relative, expected in EXPECTED_HASHES.items():
        path = ROOT / relative
        require(path.is_file(), f"missing required artifact: {relative}", errors)
        if path.is_file():
            require(sha256(path) == expected, f"hash mismatch: {relative}", errors)

    summary = {r["variable"]: r for r in rows("stage4_b0_summary_statistics.csv")}
    expected_ranges = {
        "median_age": (16, 22.3751, 28.3915),
        "u23_share": (16, 0.1667, 0.5455),
        "age_30plus_share": (16, 0.1136, 0.3103),
        "top5_valuation_concentration": (16, 0.2933, 0.5469),
    }
    for variable, (n, low, high) in expected_ranges.items():
        row = summary.get(variable, {})
        require(int(row.get("N", -1)) == n, f"N mismatch for {variable}", errors)
        require(float(row.get("minimum", "nan")) == low, f"minimum mismatch for {variable}", errors)
        require(float(row.get("maximum", "nan")) == high, f"maximum mismatch for {variable}", errors)

    associations = rows("stage4_b3_context_associations.csv")
    youth = next((r for r in associations if r["behavioural_variable"] == "u23_share"
                  and r["context_variable"] == "club_value_percentile"), None)
    require(youth is not None, "missing youth/resource association", errors)
    if youth:
        require(youth["N"] == "16", "youth/resource N is not 16", errors)
        require(youth["spearman_rho"] == "0.5355", "youth/resource rho is not 0.5355", errors)
        require("no p-value" in youth["status"], "association boundary lost", errors)

    survival = {r["variable"]: r for r in rows("stage4_profile_variable_survival.csv")}
    require(all("between-director spread exceeds" in r["within_vs_between"] for r in survival.values()),
            "between/within ordering is not preserved on all four measures", errors)
    require(survival.get("age_30plus_share", {}).get("season_median_range_over_full_IQR") == "1.8815",
            "30-plus season ratio is not 1.8815", errors)

    quality = rows("stage4_quality_sensitivity.csv")
    require(len(quality) == 4 and all(r["rank_ordering_preserved_for_retained_directors"] == "True"
                                      for r in quality),
            "green-only ordering was not preserved for all four measures", errors)

    composition = rows("stage4_sample_composition.csv")
    quartiles = {r["category"]: r for r in composition if r["dimension"] == "club_value_quartile"}
    require([quartiles.get(q, {}).get("n_rows") for q in ("Q1", "Q2", "Q3", "Q4")]
            == ["6", "4", "4", "2"], "full-sample quartile counts changed", errors)
    require("director-level rows (co-incumbency excluded) = 0" in quartiles.get("Q4", {}).get("note", ""),
            "director-level Q4 zero is missing", errors)

    repro = rows("stage10_final_reproducibility_audit.csv")
    total = next((r for r in repro if r["manifest"] == "TOTAL"), None)
    require(total is not None and total["artifacts_recorded"] == "108" and total["mismatches"] == "0",
            "108-artifact integrity claim does not verify", errors)

    readme = (ROOT / "README.md").read_text(encoding="utf-8").lower()
    for phrase in ("partial", "descriptive association only", "incumbency is exposure",
                   "zero mismatches", "spearman rho = +0.5355"):
        require(phrase in readme, f"README boundary/claim missing: {phrase}", errors)

    forbidden_files = list(ROOT.rglob("*.parquet")) + list(ROOT.rglob("*.sql"))
    require(not forbidden_files, f"restricted file types present: {forbidden_files}", errors)

    if errors:
        print("FAIL: public release verification")
        for error in errors:
            print(f"- {error}")
        return 1

    print("PASS: Problem 10 public claims and release artifacts verified")
    print("PASS: final PDF and both figures match frozen SHA-256 hashes")
    print("PASS: aggregate tables preserve n=16, rho=+0.5355, 1.8815x, and Q4=0")
    print("PASS: 108 frozen master artifacts recorded with zero mismatches")
    print("PASS: no parquet or SQL files included")
    return 0


if __name__ == "__main__":
    sys.exit(main())
