import unittest
from src.diagnostic_results import generate_diagnostic_results

class TestDiagnosticResults(unittest.TestCase):

    def test_generate_diagnostic_results(self):
        diagnostic_results = generate_diagnostic_results()
        self.assertIn("CT_result", diagnostic_results)
        self.assertIn("MRI_result", diagnostic_results)
        self.assertIn("neurological_exam", diagnostic_results)
        self.assertIn("EEG_result", diagnostic_results)
        self.assertIn("CSF_analysis", diagnostic_results)

if __name__ == '__main__':
    unittest.main()
