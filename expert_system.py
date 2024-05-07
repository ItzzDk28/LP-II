class ExpertSystem:
    def __init__(self):
        self.rules = {
            'Symptom1': ['Diagnosis1', 'Diagnosis2'],
            'Symptom2': ['Diagnosis2', 'Diagnosis3'],
            'Symptom3': ['Diagnosis4', 'Diagnosis5'],
            # Add more symptoms and corresponding diagnoses as needed
        }
    
    def diagnose(self, symptoms):
        possible_diagnoses = []
        for symptom in symptoms:
            if symptom in self.rules:
                possible_diagnoses.extend(self.rules[symptom])
        
        if possible_diagnoses:
            return "Possible diagnoses: " + ", ".join(set(possible_diagnoses))
        else:
            return "No specific diagnosis found."
        
# Example usage:
expert_system = ExpertSystem()
symptoms = ['Symptom1', 'Symptom3']
diagnosis = expert_system.diagnose(symptoms)
print(diagnosis)
