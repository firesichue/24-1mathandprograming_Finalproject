from patient_info import generate_patient_info
from medical_history import generate_medical_history
from diagnostic_results import generate_diagnostic_results
from additional_info import generate_additional_info
from scenario import generate_scenario
from patient_education import generate_patient_education
from environment_and_followup import generate_environment_and_followup

def generate_full_scenario():
    patient_info = generate_patient_info()
    medical_history = generate_medical_history()
    diagnostic_results = generate_diagnostic_results()
    additional_info = generate_additional_info()
    scenario = generate_scenario()
    patient_education = generate_patient_education()
    environment_and_followup = generate_environment_and_followup()

    full_scenario = {
        "Patient Information": patient_info,
        "Medical History": medical_history,
        "Diagnostic Results": diagnostic_results,
        "Additional Information": additional_info,
        "Scenario": scenario,
        "Patient Education": patient_education,
        "Environment and Followup": environment_and_followup
    }
    
    return full_scenario

if __name__ == "__main__":
    generated_scenario = generate_full_scenario()
    print(generated_scenario)
