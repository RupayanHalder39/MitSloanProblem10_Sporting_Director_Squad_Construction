# Reproducibility

## Publicly verifiable

`python scripts/verify_release.py` validates the final PDF hash, public figure hashes, and headline
claims against the included aggregate CSV files. It uses only the Python standard library and does
not access the network.

## Internally verified

The frozen master project records 108 artifacts across four manifests and zero hash mismatches at
the final audit: 18 Stage 4/canonical records, 24 Stage 8/Stage 4 records, 48 Stage 2–9 records, and
18 Stage 9.5 figure records.

## Not publicly reproducible

Canonical panel construction and full figure regeneration require upstream player, club, valuation,
and incumbency inputs whose redistribution rights are not established. Those inputs and dependent
row-level outputs are excluded. The public status is therefore **partial reproducibility**.
