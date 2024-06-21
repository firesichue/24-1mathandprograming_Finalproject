import unittest
from src.scenario import generate_scenario

class TestScenario(unittest.TestCase):

    def test_generate_scenario(self):
        scenario = generate_scenario()
        self.assertIn("scenario_type", scenario)
        self.assertIn("emergency_setting", scenario)
        self.assertIn("treatment_goal", scenario)
        self.assertIn("medication_and_dosage", scenario)
        self.assertIn("nursing_intervention", scenario)

if __name__ == '__main__':
    unittest.main()
