import sys
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "05_pipeline" / "src"))

from train import DATA_PATH, build_features, load_comas_monthly_data  # noqa: E402


class RealSidpolPipelineTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.monthly = load_comas_monthly_data(DATA_PATH)
        cls.features, cls.feature_names = build_features(cls.monthly)

    def test_comas_series_scope(self):
        self.assertEqual(len(self.monthly), 101)
        self.assertEqual(int(self.monthly["property_crime_reports"].sum()), 47554)

    def test_months_are_unique_and_ordered(self):
        self.assertFalse(self.monthly["date"].duplicated().any())
        self.assertTrue(self.monthly["date"].is_monotonic_increasing)

    def test_features_and_target_are_complete(self):
        required = set(self.feature_names + ["target_next_month"])
        self.assertTrue(required.issubset(self.features.columns))
        self.assertFalse(self.features[list(required)].isna().any().any())


if __name__ == "__main__":
    unittest.main()
