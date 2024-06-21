import unittest
from src.environment_and_followup import generate_environment_and_followup

class TestEnvironmentAndFollowup(unittest.TestCase):

    def test_generate_environment_and_followup(self):
        environment_and_followup = generate_environment_and_followup()
        self.assertIn("family_coping_ability", environment_and_followup)
        self.assertIn("environment_setting", environment_and_followup)
        self.assertIn("transfer_plan", environment_and_followup)
        self.assertIn("followup_plan", environment_and_followup)
        self.assertIn("nursing_record", environment_and_followup)
        self.assertIn("nursing_evaluation", environment_and_followup)
        self.assertIn("multidisciplinary_collaboration", environment_and_followup)

if __name__ == '__main__':
    unittest.main()
