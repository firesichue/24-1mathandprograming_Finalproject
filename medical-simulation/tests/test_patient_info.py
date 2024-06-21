import unittest
from src.patient_info import generate_patient_info

class TestPatientInfo(unittest.TestCase):

    def test_generate_patient_info(self):
        patient_info = generate_patient_info()
        self.assertIn("name", patient_info)
        self.assertIn("age", patient_info)
        self.assertIn("gender", patient_info)
        self.assertIn("height", patient_info)
        self.assertIn("weight", patient_info)
        self.assertIn("blood_pressure", patient_info)
        self.assertIn("heart_rate", patient_info)
        self.assertIn("respiratory_rate", patient_info)
        self.assertIn("temperature", patient_info)
        self.assertIn("oxygen_saturation", patient_info)
        self.assertIn("blood_sugar", patient_info)

if __name__ == '__main__':
    unittest.main()
