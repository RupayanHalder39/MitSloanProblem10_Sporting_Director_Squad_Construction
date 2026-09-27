# Problem 10 Public Release Handoff

## Identity and locations

- Problem: 10
- Title: Director or Club? Observed Squad-Construction Patterns of Sporting Directors in Spanish Football
- Master source: `/Users/rupayan/SoccerSolverProjects/sporting-director-selection-intelligence/` — read-only
- Final paper source: master `Papers/Problem10_Director or Club_ Observed Squad-Construction Patterns of Sporting Directors in Spanish Football.docx (2).pdf`
- Public release: `/Users/rupayan/SoccerSolverProjects/MITSubmission/MitSloanProblem10_Sporting_Director_Squad_Construction/`
- GitHub: `https://github.com/RupayanHalder39/MitSloanProblem10_Sporting_Director_Squad_Construction`

## Scientific status

Final descriptive results are frozen. Context layer: 44 rows / 13 directors / 14 clubs / 7 seasons.
Behavioural layer: 16 / 10 / 9 / 3. Director summaries: 14 rows / 8 directors. Strongest context
association: under-23 share vs club-value percentile, rho +0.5355, n = 16. The central conclusion is
that observed patterns differ, but the person cannot be separated cleanly from club, season, and
observability.

## Migrated

- exact final abstract PDF; SHA-256 `efcc8545e2464ac0f2d904c777523b5cd37b33c60be5a1810765ed759a6bd68e`;
- two frozen aggregate figures matching the paper's messages;
- nine aggregate evidence/governance CSV tables;
- standalone standard-library release verifier;
- README, citation, licence, notice, methodology, reproducibility, audit, and data notes;
- researcher photograph and SoccerSolver logo from the established Problem 6 release assets.

## Excluded

Raw/player-level/source data, canonical row-level panels, parquet, SQL/databases, archived webpages,
private correspondence, internal notes, caches, full master output trees, and builders that require
excluded data. No symlinks are used.

## Reproducibility and validators

The master final audit records 108 frozen artifacts and zero mismatches. The public package is
partially reproducible: aggregate claims and hashes can be verified, but the canonical pipeline
cannot be rebuilt without excluded inputs. Run `python scripts/verify_release.py`.

## Remaining limitations

Non-random observability; 16 behavioural rows; only two multi-club directors; no highest-value
quartile observations in director summaries; three behavioural seasons; incumbency is exposure, not
decision authority; market value is a proxy; no causal, predictive, ranking, or hiring inference.

## Publication state

- Branch: `main`
- Planned initial commit: `Initial public release for MIT Sloan Problem 10`
- Remote: exact GitHub repository above
- Push: pending final staging audit
- Data redistribution: aggregate-only release
- Safe to commit/push: yes, subject to the recorded final scans passing on staged content
