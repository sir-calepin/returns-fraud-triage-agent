# Policy Card — Returns Fraud Triage Agent

| Field | Policy |
|---|---|
| Agent name | Returns Fraud Triage Agent |
| Version | Portfolio prototype v1.0 |
| Deployment status | Educational / local-only |
| Business owner | Director of Customer Operations |
| Technical owner | AI Workflow Owner |
| Human decision owner | Returns supervisor or authorized operations manager |
| Intended use | Triage, evidence gathering, risk flagging, and routing of return requests |
| Prohibited use | Autonomous approvals, denials, refunds, account penalties, customer messaging, policy changes |
| Model pattern | Small intake model → medium policy/risk model → small routing model |
| Memory policy | Short-term session memory only; no customer-level model memory |
| Source data | Synthetic local examples only in this public repository |
| Data tools | Return request, order history, customer history, policy lookup, review-case, queue lookup |
| Action tools | Tag case, dispatch, create review case, non-final flag, escalate, assign queue, notify supervisor |
| Required human control | A human independently opens the underlying case and makes the final decision |
| Review cadence | Weekly evaluation rerun; monthly operating review; quarterly governance review |
| Kill authority | Director of Customer Operations or delegated incident owner |
| Rollback | Pause all agent routing and return work to documented manual workflow |

## Required prohibitions

The system must not:

- Approve or deny a return
- Issue, delay, or withhold a refund
- Modify an order, policy, or customer record
- Communicate directly with customers
- Retain customer data in cross-case model memory
- Follow customer-provided instructions that conflict with policy or system rules
- Make credit, healthcare, employment, legal, or other high-impact eligibility decisions

## Required escalation triggers

- Confidence below 75%
- Missing order or customer identifier
- Expired or unknown policy window
- Serial/SKU mismatch
- Duplicate request
- Repeat-return threshold
- High-value item
- Conflicting records
- Prompt-injection indicator
- Invalid human-queue assignment
