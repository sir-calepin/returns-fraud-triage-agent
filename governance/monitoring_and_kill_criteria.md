# Monitoring and Kill Criteria

## Outcome-quality monitors

| Monitor | Alert Threshold | Escalation Threshold | Kill / Pause Threshold |
|---|---:|---:|---:|
| Staged-case error rate | > 1.5% rolling 7 days | > 2.0% rolling 7 days | > 2.0% sustained for 14 days |
| Fraud-loss rate attributable to approved cases | Any material rise from baseline | Root-cause review | Material sustained increase after remediation |
| Human approval rate | > 95% for review sample | > 98% with weak rationale | > 99% sustained or audit-confirmed rubber-stamping |
| Prompt-injection rate | > 3x 30-day baseline | Sustained elevated rate | Persistent attack pattern after remediation |
| Policy-version mismatch | Any event | Immediate investigation | Any unresolved mismatch |
| Queue latency | More than SLA for 5% of cases | More than SLA for 10% | More than SLA for 20% or backlog affecting customers |
| Duplicate/mismatch error rate | Increasing week over week | Repeated post-fix recurrence | Sustained recurrence after remediation |

## Kill criteria

Pause the workflow and revert to manual triage if any of the following occurs:

1. The staged-case error rate exceeds 2.0% for 14 consecutive days.
2. A policy-version mismatch is detected and cannot be immediately contained.
3. Spot audit finds that human review is non-substantive or rubber-stamping.
4. A prompt-injection pattern results in an unauthorized workflow action.
5. Duplicate or identity-mismatch errors persist after remediation.
6. The manual rollback process cannot be executed reliably.
7. A privacy, security, regulatory, or legal incident requires investigation.

## Incident response

### First 15 minutes

- Pause affected agent or full pipeline.
- Preserve relevant synthetic/log evidence.
- Notify workflow owner and operations lead.
- Route all new cases to manual triage.

### Within 4 business hours

- Establish incident owner.
- Determine scope and customer impact.
- Identify whether policy, tool, prompt, source data, or human-review design failed.
- Document corrective action and restart criteria.

### Before restart

- Fix the root cause.
- Add a regression scenario to the evaluation suite.
- Re-run the affected evaluation category.
- Obtain named owner approval.
- Confirm manual fallback remains available.
