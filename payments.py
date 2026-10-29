"""Payment validation logic for the Git Recovery Lab (fictional application)."""


def validate_amount(amount: int) -> bool:
    """Return whether an amount in cents can be charged."""
    return type(amount) is int and amount >= 0


def format_receipt(amount: int) -> str:
    """Create a human-readable receipt line."""
    return f"Payment: {amount} cents"
