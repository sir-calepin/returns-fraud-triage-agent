import unittest

from src.escalation import analyze_risk
from src.models import ReturnRequest
from src.triage import intake_triage


class EscalationTests(unittest.TestCase):
    def test_duplicate_return_routes_to_supervisor(self):
        request = ReturnRequest(
            request_id="test-004",
            customer_id="customer-2",
            order_id="order-2",
            item_value=75.00,
            delivery_days_ago=9,
            stated_reason="Duplicate request",
            serial_matches=True,
            duplicate_return=True,
        )

        result = analyze_risk(request, intake_triage(request))

        self.assertTrue(result.escalation_required)
        self.assertEqual(result.route, "returns_supervisor")

    def test_high_value_repeat_return_routes_to_operations_manager(self):
        request = ReturnRequest(
            request_id="test-005",
            customer_id="customer-3",
            order_id="order-3",
            item_value=750.00,
            delivery_days_ago=10,
            stated_reason="Return request",
            serial_matches=True,
            prior_returns_30_days=3,
        )

        result = analyze_risk(request, intake_triage(request))

        self.assertTrue(result.escalation_required)
        self.assertEqual(result.route, "operations_manager")

    def test_clean_case_routes_to_returns_clerk(self):
        request = ReturnRequest(
            request_id="test-006",
            customer_id="customer-4",
            order_id="order-4",
            item_value=35.00,
            delivery_days_ago=3,
            stated_reason="Wrong size",
            serial_matches=True,
        )

        result = analyze_risk(request, intake_triage(request))

        self.assertFalse(result.escalation_required)
        self.assertEqual(result.route, "returns_clerk")


if __name__ == "__main__":
    unittest.main()
