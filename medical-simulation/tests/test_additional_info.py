import unittest
from src.additional_info import generate_additional_info

class TestAdditionalInfo(unittest.TestCase):

    def test_generate_additional_info(self):
        additional_info = generate_additional_info()
        self.assertIn("family_history", additional_info)
        self.assertIn("lifestyle", additional_info)
        self.assertIn("GCS", additional_info)
        self.assertIn("pain_score", additional_info)
        self.assertIn("patient_cooperation", additional_info)
        self.assertIn("emotional_state", additional_info)
        self.assertIn("skin_condition", additional_info)

if __name__ == '__main__':
    unittest.main()
