# Architecture

## Pattern

The system uses a manager-pattern pipeline:

1. Intake Triage Agent
2. Fraud and Policy Analyst
3. Routing and Escalation Coordinator
4. Human reviewer or supervisor

This structure separates extraction, risk assessment, and routing. It also limits each agent’s permissions and makes handoffs auditable.

## Data versus action tools

### Data tools

Data tools retrieve information and do not change the business environment:

- Read return request
- Look up basic order status
- Look up order history
- Look up customer history
- Retrieve approved return policy
- Read staged review case
- Look up human review queue

### Action tools

Action tools write bounded internal workflow records:

- Classify case
- Dispatch to the next agent
- Create review case
- Flag case for non-final investigation
- Escalate to human review
- Assign review queue
- Notify supervisor

None of these action tools can approve a return, issue a refund, modify policy, change an order, or contact a customer.

## Blast-radius compression

The most important design decision is separating the agent’s reasoning from any final customer-impacting action.

If the Intake Triage Agent were manipulated, it could at worst misclassify or delay a case.

If the Fraud and Policy Analyst were manipulated, it could at worst under-flag or over-flag a review case.

If the Routing Coordinator were manipulated, it could at worst route a case to the wrong queue.

Those outcomes are still operationally significant, but they are recoverable because the system has no authority to approve refunds or change records.
