# Privacy and Compliance Boundaries

## Public-repository posture

This repository uses synthetic examples only. Do not add real customer, order, payment, address, identity, return, or dispute data.

## Data minimization

The design follows a data-minimization approach:

- Process only the fields needed for the active triage case.
- Do not keep customer-level model memory across cases.
- Store any audit record outside the model and under the organization’s approved retention policy.
- Redact or minimize sensitive information in agent outputs.

GDPR Article 5(1)(c) states that personal data should be adequate, relevant, and limited to what is necessary for the processing purpose. [64][66]

## Privacy requests

The agent must not answer personal-data access, deletion, or export requests on its own.

| Request | Routing requirement |
|---|---|
| Request to access personal data | Route to privacy process / privacy officer |
| Request to delete personal data | Route to deletion workflow |
| Request to export case records | Route to lawful records-access process |
| Health or disability information in return note | Minimize disclosure and route to trained human reviewer |
| Payment, tax, or bank data in request | Mask in output and restrict access |

GDPR Article 15 concerns access rights, and Article 17 concerns erasure rights. [64][67]

## EU AI Act note

This local, internal, synthetic prototype does not directly interact with end users. If a future system directly interacts with customers in the EU, assess Article 50 transparency requirements, including clear disclosure that the user is interacting with AI where applicable. [65][72]

## Boundary for financial decisions

This workflow must not make credit or financing decisions. If the workflow expands into lending, eligibility, adverse action, or financial-product decisions, stop and conduct a new legal, model-risk, and governance assessment before implementation.
