# Incident report — payment validation

A unit test added to `main` revealed that zero-value payments are accepted.

The fix exists among the commits on `feature-payment`, but the discount and loyalty experiments are not approved for release.

The immediate goal is **selective integration** of the existing fix. The tests need to pass without introducing experimental feature files to `main`.

## Acceptance criteria

- `main` rejects a zero-value payment.
- The test suite passes (`python3 -m unittest discover -s tests -v`).
- `discounts.py` and `loyalty.py` have not been merged into `main`.
- The original `feature-payment` branch remains available.
