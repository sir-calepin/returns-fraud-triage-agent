# Deployment Decision

## Recommendation

**Conditional deploy only.**

The workflow should be used as a first-pass triage and routing system, not as an autonomous return approval or refund engine.

## Conditions before a real launch

| Condition | Verification | Owner |
|---|---|---|
| Evaluation quality | Full evaluation suite meets approved threshold | QA and workflow owner |
| Meaningful HITL | Spot audits show substantive human review | Internal audit and operations |
| Rollback readiness | Live manual-fallback drill succeeds | Operations and IT |
| Policy integrity | Approved policy source and version checks work | Policy owner |
| Privacy readiness | Data-minimization and request-routing process approved | Privacy owner |

## What would support unconditional deployment

- At least 90 days of stable operation without kill-criteria triggers
- No material increase in fraud loss or customer-resolution delays
- No sustained increase in human overturns
- Stable weekly evaluation results across all four categories
- Independent audit evidence that human reviewers remain substantive
- Successful rollback drills and incident-response exercises

## What would support do-not-deploy

- Failure to meet the approved error ceiling
- Repeated adversarial or compliance-case failures
- Evidence of rubber-stamp human review
- Persistent prompt-injection, policy-drift, or identity-mismatch problems
- Inability to operate the manual fallback reliably
- A new legal or regulatory requirement that materially changes the risk posture

## Final principle

A workflow that saves labor but creates customer harm, fraud leakage, or illusory human oversight is not a successful AI deployment. The system should be evaluated by the quality of outcomes and the reliability of controls, not by the number of cases it processes automatically.
