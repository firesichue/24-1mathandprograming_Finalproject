import unittest
from src.medical_history import generate_medical_history

class TestMedicalHistory(unittest.TestCase):

    def test_generate_medical_history(self):
        medical_history = generate_medical_history()
        self.assertIn("medical_history", medical_history)
        self.assertIn("current_medications", medical_history)
        self.assertIn("allergies", medical_history)
        self.assertIn("primary_symptom", medical_history)
        self.assertIn("secondary_symptoms", medical_history)
        self.assertIn("physical_examination", medical_history)
        self.assertIn("diagnostic_results", medical_history)
        self.assertIn("EHR", medical_history)

if __name__ == '__main__':
    unittest.main()
