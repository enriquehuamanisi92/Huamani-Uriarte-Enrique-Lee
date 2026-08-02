import sys
import unittest
from pathlib import Path

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "05_pipeline" / "data"))

from create_dataset import build_zone_table, simulate_monthly_incidents  # noqa: E402


class SyntheticDataTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        rng = np.random.default_rng(42)
        cls.data = simulate_monthly_incidents(build_zone_table(rng, 8), rng)

    def test_required_columns_and_unique_panel_key(self):
        required = {"zone_id", "year", "month", "recent_incidents", "target_high_risk_next_month"}
        self.assertTrue(required.issubset(self.data.columns))
        self.assertFalse(self.data.duplicated(["zone_id", "year", "month"]).any())

    def test_binary_target_and_valid_months(self):
        self.assertTrue(set(self.data["target_high_risk_next_month"]).issubset({0, 1}))
        self.assertTrue(self.data["month"].between(1, 12).all())

    def test_lagged_features_have_no_missing_values(self):
        lagged = ["recent_incidents", "rolling_3m_incidents", "incident_trend"]
        self.assertFalse(self.data[lagged].isna().any().any())


if __name__ == "__main__":
    unittest.main()
