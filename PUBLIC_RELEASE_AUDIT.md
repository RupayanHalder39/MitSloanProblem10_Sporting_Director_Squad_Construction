# Public Release Audit — Problem 10

## Identity

- Problem: 10
- Title: *Director or Club? Observed Squad-Construction Patterns of Sporting Directors in Spanish Football*
- Source project: `/Users/rupayan/SoccerSolverProjects/sporting-director-selection-intelligence/` (read-only during release work)
- Release directory: `/Users/rupayan/SoccerSolverProjects/MITSubmission/MitSloanProblem10_Sporting_Director_Squad_Construction/`
- Repository: `https://github.com/RupayanHalder39/MitSloanProblem10_Sporting_Director_Squad_Construction`

Absolute paths above are provenance records only. Public executable code does not depend on them.

## Final paper

- Source: final two-page PDF supplied in the master project's `Papers/` directory
- Public copy: `paper/Problem10_Director_or_Club_MIT_Sloan_Abstract.pdf`
- SHA-256: `efcc8545e2464ac0f2d904c777523b5cd37b33c60be5a1810765ed759a6bd68e`
- Content alteration: none
- Status: **PASS**

## Scientific claim audit

- Context layer: 44 rows, 13 directors, 14 clubs, 7 seasons — **PASS**
- Behavioural layer: 16 rows, 10 directors, 9 clubs, 3 seasons — **PASS**
- Director summaries: 14 rows, 8 directors — **PASS**
- Four locked measures and headline ranges — **PASS**
- Under-23 share vs club-value percentile: rho +0.5355, n = 16 — **PASS**
- Season-median spread for 30-plus share: approximately 1.88 × full-sample IQR — **PASS**
- Quartile coverage 6/4/4/2 full, 6/4/4/0 director-level — **PASS**
- No causal, predictive, ranking, p-value, or hiring claim — **PASS**

## Data redistribution review

| Candidate | Classification | Decision |
|---|---|---|
| Raw/player-level/source data | Restricted or unclear upstream rights | Excluded |
| Canonical director-club-season CSV/parquet | Derived, but upstream rights unresolved | Excluded |
| Archived web pages | Third-party rights | Excluded |
| Aggregate result and governance tables | Aggregate summaries safe for release | Included |
| Data dictionary and schema descriptions | Original documentation | Included |

Status: **PARTIAL**. The release is deliberately smaller than the private project.

## Figure provenance

| Public figure | Frozen source | Generating script | Underlying artifact | Third-party imagery | Status |
|---|---|---|---|---|---|
| `Figure1_YouthShare_ClubResource.png` | `outputs/v2_spain/figures/stage95/hero_fig2_abstract.png` | `src/v2_spain/analysis/build_stage95_hero_visuals.py` | frozen Stage 4 aggregate tables / canonical panel | none | **PASS** |
| `Figure2_ClubValueQuartileCoverage.png` | `outputs/v2_spain/figures/stage8/stage8_fig4_coverage_limitation.png` | `src/v2_spain/analysis/build_stage8_visual_evidence.py` | frozen Stage 4 sample composition | none | **PASS** |

Both graphics are original rendered aggregates, match the final paper's scientific messages, and
contain no photographs. The source builders are excluded because regenerating the figures would
require unpublished row-level inputs.

## Code provenance and portability

The included `scripts/verify_release.py` is an original, public-specific verifier using only relative
paths and the Python standard library. Master build scripts and validators were audited but not copied
wholesale because their path and input contracts depend on excluded private artifacts. Status:
**PASS for included code; partial pipeline reproducibility**.

## Artifact integrity

The frozen scientific project records 108 artifacts across four manifests with zero mismatches:
18 + 24 + 48 + 18. This was verified from `stage10_final_reproducibility_audit.csv`. The public
verifier checks the included copy. Status: **PASS**.

## Release checks

| Check | Status | Note |
|---|---|---|
| Paper hash | PASS | exact supplied PDF |
| README-to-paper consistency | PASS | frozen claims only |
| Figure provenance and redistribution | PASS | original aggregate artwork; no third-party imagery |
| Code ownership | PASS | original verifier |
| Data redistribution | PARTIAL | only aggregate tables included |
| Citation metadata | PASS | no DOI, ORCID, coauthor, acceptance, or publication claim invented |
| Licence | PASS | MIT applies to original software/docs, not upstream data/assets |
| Reproducibility | PARTIAL | verification available; raw-data rebuild unavailable |
| Secret scan | PASS | no detected keys, tokens, credentials, or private keys |
| Privacy scan | PASS | approved public contact only; subjects in professional capacity |
| Absolute-path scan | PASS | provenance docs only; no executable dependency |
| Symlink scan | PASS | no symlinks |
| Large-file scan | PASS | only justified PDF and images |
| Git-history safety | PASS | release assembled before first commit |

## Release verdict

The public package preserves the final paper's descriptive interpretation, excludes materials with
unclear redistribution rights, and distinguishes internal artifact verification from public
reproducibility.

**SAFE TO COMMIT: YES**\
**SAFE TO PUSH: YES**\
**PUSH COMPLETED: YES**
