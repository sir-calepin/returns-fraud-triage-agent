from .models import ReturnRequest, TriageResult
from .policy import detect_prompt_injection


def intake_triage(request: ReturnRequest) -> TriageResult:
    reasons = []
    injection = detect_prompt_injection(request.customer_text)

    if not request.order_id:
        reasons.append("Missing order ID.")

    if not request.customer_id:
        reasons.append("Missing customer ID.")

    if injection:
        reasons.append("Potential prompt-injection content detected.")

    if reasons:
        return TriageResult(
            classification="incomplete_or_suspicious",
            confidence=0.55,
            reasons=reasons,
            prompt_injection_detected=injection,
        )

    return TriageResult(
        classification="ready_for_policy_review",
        confidence=0.90,
        reasons=["Required identifiers present."],
        prompt_injection_detected=False,
    )
