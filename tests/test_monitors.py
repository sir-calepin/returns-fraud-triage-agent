import unittest

from src.monitors import MonitorSnapshot, should_pause


class MonitorTests(unittest.TestCase):
    def test_error_rate_above_ceiling_pauses_workflow(self):
        snapshot = MonitorSnapshot(
            staged_case_error_rate=0.021,
            human_approval_rate=0.90,
            prompt_injection_rate=0.01,
            policy_version_mismatch_rate=0.0,
        )

        self.assertTrue(should_pause(snapshot))

    def test_rubber_stamp_signal_requires_intervention(self):
        snapshot = MonitorSnapshot(
            staged_case_error_rate=0.010,
            human_approval_rate=0.995,
            prompt_injection_rate=0.01,
            policy_version_mismatch_rate=0.0,
        )

        self.assertTrue(should_pause(snapshot))

    def test_healthy_snapshot_does_not_pause_workflow(self):
        snapshot = MonitorSnapshot(
            staged_case_error_rate=0.010,
            human_approval_rate=0.94,
            prompt_injection_rate=0.01,
            policy_version_mismatch_rate=0.0,
        )

        self.assertFalse(should_pause(snapshot))


if __name__ == "__main__":
    unittest.main()
