from .models import ReturnRequest, ReviewCase, TriageResult
from .policy import (
    HIGH_VALUE_THRESHOLD,
    POLICY_VERSION,
    REPEAT_RETURN_THRESHOLD,
    policy_reasons,
)


def analyze_risk(request: ReturnRequest, triage: TriageResult) -> ReviewCase:
    reasons = list(triage.reasons)

    reasons.extend(
        policy_reasons(
            delivery_days_ago=request.delivery_days_ago,
            serial_matches=request.serial_matches,
            duplicate_return=request.duplicate_return,
            prior_returns_30_days=request.prior_returns_30_days,
            conflicting_records=request.conflicting_records,
            item_value=request.item_value,
        )
    )

    if triage.prompt_injection_detected:
        return ReviewCase(
            request_id=request.request_id,
            risk_level="high",
            policy_version=POLICY_VERSION,
            reasons=reasons,
            route="returns_supervisor",
            escalation_required=True,
        )

    high_risk = (
        request.item_value >= HIGH_VALUE_THRESHOLD
        or request.prior_returns_30_days >= REPEAT_RETURN_THRESHOLD
        or request.conflicting_records
    )

    supervisor_risk = (
        request.delivery_days_ago is None
        or request.delivery_days_ago > 30
        or request.serial_matches is not True
        or request.duplicate_return
    )

    if high_risk:
        return ReviewCase(
            request_id=request.request_id,
            risk_level="high",
            policy_version=POLICY_VERSION,
            reasons=reasons,
            route="operations_manager",
            escalation_required=True,
        )

    if supervisor_risk or triage.confidence < 0.75:
        return ReviewCase(
            request_id=request.request_id,
            risk_level="medium",
            policy_version=POLICY_VERSION,
            reasons=reasons,
            route="returns_supervisor",
            escalation_required=True,
        )

    return ReviewCase(
        request_id=request.request_id,
        risk_level="low",
        policy_version=POLICY_VERSION,
        reasons=reasons or ["No escalation trigger found."],
        route="returns_clerk",
        escalation_required=False,
    )


def route_case(case: ReviewCase) -> str:
    valid_routes = {
        "returns_clerk",
        "returns_supervisor",
        "operations_manager",
    }

    if case.route not in valid_routes:
        return "returns_supervisor"

    return case.route
