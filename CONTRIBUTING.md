# Contributing

Contributions are welcome if they preserve the project’s safety boundaries.

## Good contributions

- Additional synthetic evaluation scenarios
- Better unit tests for escalation logic
- Improvements to documentation clarity
- More explicit monitoring and governance examples
- Accessibility and readability improvements

## Contributions that require discussion first

- Any live API or commerce-platform integration
- Any automated refund, return-denial, customer-contact, or account-flagging action
- Any use of real customer data
- Any persistence layer that stores customer-level information
- Any change that expands the system’s decision authority

## Development rules

1. Use synthetic examples only.
2. Keep action authority constrained.
3. Add or update tests for behavioral changes.
4. Do not weaken prompt-injection, privacy, or escalation controls.
5. Keep the README’s limitations accurate.
