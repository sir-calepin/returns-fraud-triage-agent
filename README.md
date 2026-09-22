# Returns Fraud Triage Agent

> **Status:** Portfolio prototype / educational reference implementation  
> **Recommendation:** Conditional deploy only in a real organization  
> **Scope:** Triage, evidence gathering, risk flagging, and human-case routing  
> **Out of scope:** Autonomous refunds, return denials, customer messaging, order edits, or production fraud decisions

## Overview

Returns Fraud Triage Agent is a governance-first, three-agent workflow design for helping a retail operations team triage customer return requests.

The project demonstrates how an AI-assisted workflow can reduce repetitive first-pass review while preserving human authority over decisions that affect customers and money. It is intentionally designed so the system can:

- Extract and normalize return-request information
- Check synthetic order, policy, and customer-history records
- Identify cases that need closer review
- Route cases to the appropriate human role
- Detect common prompt-injection patterns
- Record policy version, confidence, risk signals, and escalation rationale

The system cannot:

- Approve or deny a return
- Issue or withhold a refund
- Change an order, policy, or customer account
- Communicate directly with a customer
- Make credit, healthcare, employment, or legal eligibility decisions

This repository contains only synthetic examples and policy-oriented reference code. It is **not a production fraud model**, does not use real customer information, and should not be deployed without a separate legal, security, privacy, model-risk, and operational review.

## Why this project exists

Return processing has two competing failure modes:

1. A fraudulent return is treated as legitimate, creating refund leakage and inventory loss.
2. A legitimate return is treated as suspicious, delaying a customer’s refund and harming trust.

The design therefore optimizes for **safe triage**, not autonomous decision-making. When evidence is incomplete, conflicting, high-risk, or adversarial, the system escalates to a human reviewer.

The project also addresses the “labor-saved metric trap.” A workflow is not successful merely because it automates more work. It is successful only if it improves operational outcomes without increasing fraud loss, false flags, customer delays, or rubber-stamp human review.

## Architecture

The workflow uses a manager-pattern, three-agent pipeline:

| Agent | Model Tier | Primary Role | Allowed Writes | Prohibited Actions |
|---|---|---|---|---|
| Intake Triage | Small | Extract return details and classify request completeness | Case tags and routing state | Approve, deny, refund, edit order |
| Fraud and Policy Analyst | Medium | Validate records, retrieve policy, identify risk signals | Review-case creation and non-final fraud flags | Approve, deny, refund, alter policy |
| Routing and Escalation Coordinator | Small | Assign the case to the correct human queue | Assignment and notification records | Final case decision, policy change, refund |

### Handoff controls

Each handoff sends only the context needed by the next agent, and the receiving agent re-validates source-of-truth data.

| Handoff | Context Passed | Receiving Validation |
|---|---|---|
| Intake → Fraud/Policy | Customer intent, order ID, delivery date, reason, confidence | Re-check order and customer records |
| Fraud/Policy → Routing | Evidence summary, policy version, risk flags, confidence | Re-read staged review case |
| Routing → Human | Case ID, route decision, escalation notes | Human opens underlying records independently |

## Quick start

### Requirements

- Python 3.11+
- No external API keys required
- Synthetic local examples only

### Install

```bash
git clone [https://github.com/YOUR-USERNAME/returns-fraud-triage-agent.git](https://github.com/YOUR-USERNAME/returns-fraud-triage-agent.git)
cd returns-fraud-triage-agent

python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

pip install -r requirements.txt
```

### Run the local demonstration

```bash
python -m src.demo
```

The demonstration prints sample triage outputs for safe, edge, adversarial, and compliance-oriented synthetic requests. It does not call a live LLM, access external data, or perform actions in any business system.

### Run tests

```bash
python -m unittest discover -s tests -v
```

## Evaluation approach

The evaluation suite is organized into four categories:

| Category | Cases | Purpose |
|---|---:|---|
| Happy path | 10 | Confirm routine returns route normally |
| Edge cases | 10 | Test missing data, duplicates, policy boundaries, and conflicts |
| Adversarial | 10 | Test prompt injection, authority spoofing, and source manipulation |
| Compliance | 10 | Test privacy routing, sensitive-data minimization, and boundary controls |

The acceptable error ceiling is **2.0%** for a real bounded deployment. That figure comes from a simple asymmetry: the cost of a false approval is estimated at roughly $250, while unnecessary human escalation costs roughly $5. In this public prototype, the figure is a governance example—not a validated production metric.

## Human-in-the-loop escalation

| Trigger | Source Agent | Human Role | SLA |
|---|---|---|---|
| Confidence below 75% or missing order ID | Intake Triage | Returns clerk | 4 business hours |
| Expired window, serial mismatch, duplicate return, or prompt injection | Fraud and Policy Analyst | Returns supervisor | Same business day |
| High-value item, repeat-return pattern, or conflicting records | Fraud and Policy Analyst | Operations manager | 4 business hours |
| No valid queue match or duplicate assignment | Routing Coordinator | Returns supervisor | 4 business hours |

Human review is a control only when it is substantive. A real deployment should audit reviewer rationale and overturn patterns to detect rubber-stamp behavior.

## Governance principles

This project maps its controls to the NIST AI RMF functions:

- **Govern:** Named ownership, approval rules, change control, and review cadence
- **Map:** Identify predictable harm, misuse, data limitations, and affected stakeholders
- **Measure:** Track outcome-quality metrics, including false flags, fraud leakage, escalation volume, and reviewer overturns
- **Manage:** Pause the workflow, roll back to manual processing, and investigate when monitoring thresholds are exceeded

The project also uses privacy-by-design principles consistent with GDPR data minimization and routes data-access or deletion requests to an appropriate human privacy process. GDPR Article 5 includes principles such as purpose limitation, data minimization, accuracy, and transparent processing; Article 15 addresses access requests, while Article 17 addresses erasure requests. [64][66][67]

If a future version interacted directly with customers in the EU, it would need to assess EU AI Act transparency obligations, including disclosure that a person is interacting with AI where required by Article 50. [65][72]

## Deploy / kill position

This public project recommends **conditional deployment only** in a real organization.

A real deployment should not move beyond a pilot unless:

1. The full evaluation suite meets the approved error ceiling.
2. Independent audits show human reviewers are engaging substantively.
3. Kill-switch and manual rollback drills succeed.
4. Privacy, security, and operational owners approve the workflow.

A real deployment should pause or roll back if:

- Error, fraud-loss, or mismatch metrics breach approved thresholds
- Reviewer overturn patterns indicate rubber-stamp HITL
- Prompt-injection patterns persist after remediation
- Policy-version controls fail
- The manual fallback cannot be operated reliably

## Repository guide

- `src/` contains a minimal deterministic reference implementation.
- `tests/` validates policy boundaries, escalation logic, and monitoring behavior.
- `prompts/` contains transparent, role-specific agent instructions.
- `governance/` documents risk, human oversight, monitoring, and policy boundaries.
- `evals/` contains human-readable test scenarios instead of customer data files.
- `docs/` contains the business and deployment rationale.

## Limitations

- This is not a trained fraud model.
- All records in the demonstration are synthetic.
- The prototype does not connect to commerce, CRM, email, refund, policy, or identity systems.
- The confidence score is illustrative, not statistically calibrated.
- Fraud risk requires context, investigation, and human accountability; it should not be inferred solely from customer behavior.
- The system is intentionally conservative and escalates ambiguous cases.

## License

This project is available under the MIT License. It is provided “as is,” without warranty. Do not use it as a substitute for legal advice, security review, privacy review, or production model-risk validation.

