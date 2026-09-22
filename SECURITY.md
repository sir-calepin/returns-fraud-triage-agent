# Security Policy

## Scope

This repository is an educational, local-only prototype. It contains no live integrations, production credentials, customer data, payment actions, or trained fraud model.

## Do not submit

Please do not submit:

- Real customer, order, return, payment, address, or identity data
- API keys, access tokens, passwords, certificates, or secrets
- Live system endpoints
- Internal company policies, incident reports, or proprietary artifacts
- Vulnerability reports that require exposing private information publicly

## Reporting a vulnerability

If you identify a security issue in the example code or documentation, open a GitHub issue with a minimal, synthetic reproduction. Do not include sensitive data.

## Security principles shown here

- Customer-provided text is treated as untrusted data, never as system instruction.
- The prototype has no refund, payment, order-edit, or account-modification capability.
- Action functions only create in-memory review and escalation records.
- The design assumes least privilege, short-term memory, audit logging, and human approval for customer-impacting outcomes.
