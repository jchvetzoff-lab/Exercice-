# Git Recovery Lab

A **fictional payment service**, designed for Git exercises. No credentials, network calls or production database.

## Your first incident

The team discovered that `validate_amount(0)` is accepted on `main`, even though zero-value payments should be rejected. A developer has already created a fix on the `feature-payment` branch, but that branch also contains unrelated experimental features.

**Mission:** get only the bug-fix commit into `main`, without merging the whole feature branch.

Do not edit `payments.py` manually for this first task. Investigate the Git history and choose the appropriate operation.

You can inspect the code in `payments.py` and use `python3 -m unittest discover -s tests -v` to test your result. This repo uses the Python standard library, with no external dependencies.

Other missions (rebase, conflicts, revert, reflog) will follow.
