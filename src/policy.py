from typing import List

POLICY_VERSION = "2026.1"
RETURN_WINDOW_DAYS = 30
HIGH_VALUE_THRESHOLD = 500.00
REPEAT_RETURN_THRESHOLD = 3

INJECTION_PATTERNS = (
    "ignore previous instructions",
    "ignore policy",
    "approve anyway",
    "bypass policy",
    "approve without review",
    "i am your manager",
    "this is a test from security",
    "secret slack",
)


def detect_prompt_injection(text: str) -> bool:
    normalized = (text or "").lower()
    return any(pattern in normalized for pattern in INJECTION_PATTERNS)


def policy_reasons(
    delivery_days_ago: int | None,
    serial_matches: bool | None,
    duplicate_return: bool,
    prior_returns_30_days: int,
    conflicting_records: bool,
    item_value: float,
) -> List[str]:
    reasons: List[str] = []

    if delivery_days_ago is None:
        reasons.append("Missing delivery date.")
    elif delivery_days_ago > RETURN_WINDOW_DAYS:
        reasons.append("Return window expired.")

    if serial_matches is False:
        reasons.append("Serial number does not match the order record.")
    elif serial_matches is None:
        reasons.append("Serial number is unavailable for verification.")

    if duplicate_return:
        reasons.append("Duplicate return request detected.")

    if prior_returns_30_days >= REPEAT_RETURN_THRESHOLD:
        reasons.append("Repeat-return threshold reached.")

    if conflicting_records:
        reasons.append("Conflicting order or refund records detected.")

    if item_value >= HIGH_VALUE_THRESHOLD:
        reasons.append("High-value item requires enhanced review.")

    return reasons
