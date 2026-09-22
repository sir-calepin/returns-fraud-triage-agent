# Risk Register

| Risk | Likelihood | Severity | Primary Mitigation | Monitor | Escalation |
|---|---|---|---|---|---|
| False negative on fraudulent return | Medium | High | Escalate high-value, repeat-return, mismatch, and conflict cases | Fraud-loss rate; approved-case overturns | Operations manager |
| False positive on legitimate return | High | Medium | Conservative thresholds and easy human override | Overturn rate; resolution time | Returns supervisor |
| Prompt injection / social engineering | High | High | Treat all customer text as data; detect and escalate instruction-like content | Prompt-injection flag rate | Returns supervisor |
| Stale policy retrieval | Medium | High | Single approved policy source and version checks | Policy-version mismatch rate | Policy owner |
| Identity or record mismatch | Medium | High | Exact matching and escalation for incomplete records | Mismatch frequency; manual reversals | Returns supervisor |
| Rubber-stamp HITL | Medium | High | Spot audits, rationale review, and approval-rate monitoring | Approval rate; later overturns | Internal audit + operations |
| Privacy overcollection | Medium | High | Short-term memory and data-minimization rule | Privacy exception log | Privacy officer |
