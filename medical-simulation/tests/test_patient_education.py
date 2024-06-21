import unittest
from src.patient_education import generate_patient_education

class TestPatientEducation(unittest.TestCase):

    def test_generate_patient_education(self):
        patient_education = generate_patient_education()
        self.assertIn("education_content", patient_education)
        self.assertIn("ethical_issues", patient_education)

if __name__ == '__main__':
    unittest.main()
