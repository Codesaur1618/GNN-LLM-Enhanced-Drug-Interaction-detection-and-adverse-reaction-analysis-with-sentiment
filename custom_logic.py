# custom_logic.py

harmful_combinations = {
    ("warfarin", "aspirin"): "Combining warfarin with aspirin significantly increases the risk of internal bleeding, especially gastrointestinal and intracranial hemorrhage.",
    ("viagra", "nitrate"): "This combination can cause a dangerous and potentially fatal drop in blood pressure, leading to fainting, heart attack, or stroke.",
    ("metformin", "contrast dye"): "Using contrast dye with metformin may lead to lactic acidosis, a rare but life-threatening buildup of lactic acid in the bloodstream.",
    ("clonazepam", "alcohol"): "This combination severely depresses the central nervous system, causing extreme sedation, respiratory failure, and possible death.",
    ("tramadol", "ssri"): "High risk of serotonin syndrome, characterized by confusion, agitation, rapid heart rate, dilated pupils, and even seizures or coma.",
    ("paracetamol", "alcohol"): "Chronic alcohol use increases the risk of liver damage and acute liver failure when combined with high doses of paracetamol.",
    ("ibuprofen", "aspirin"): "Ibuprofen can interfere with aspirin’s cardioprotective effects, reducing its ability to prevent heart attacks and strokes.",
    ("amoxicillin", "methotrexate"): "Amoxicillin may reduce methotrexate clearance, increasing its toxicity and causing mouth ulcers, liver damage, or kidney failure.",
    ("ciprofloxacin", "tizanidine"): "This combination can cause extreme hypotension, sedation, and impaired psychomotor function, posing serious danger.",
    ("lisinopril", "potassium"): "Concurrent use may result in dangerously high potassium levels, causing irregular heartbeat or cardiac arrest.",
    ("paracetamol", "codeine"): "Though often combined, excessive use can cause respiratory depression and liver toxicity, especially in poor metabolizers of codeine.",
    ("diazepam", "fluoxetine"): "Fluoxetine inhibits diazepam breakdown, leading to enhanced sedative effects, impaired cognition, and increased fall risk.",
    ("erythromycin", "simvastatin"): "This can raise simvastatin levels dramatically, increasing the risk of severe muscle breakdown (rhabdomyolysis).",
    ("levothyroxine", "iron supplements"): "Iron interferes with absorption of levothyroxine, reducing its effectiveness and worsening hypothyroidism symptoms.",
    ("clopidogrel", "omeprazole"): "Omeprazole may block the activation of clopidogrel, reducing its antiplatelet activity and increasing risk of blood clots.",
    ("digoxin", "verapamil"): "This may lead to dangerously slow heart rate or AV block, particularly in elderly patients or those with kidney dysfunction.",
    ("metronidazole", "alcohol"): "Can cause a disulfiram-like reaction, including flushing, nausea, vomiting, and severe abdominal cramps.",
    ("sildenafil", "erythromycin"): "Erythromycin slows sildenafil metabolism, potentially causing dangerously prolonged erection and blood pressure issues.",
    ("phenylephrine", "MAOI"): "Combining these may lead to hypertensive crisis, severe headache, chest pain, and risk of stroke.",
    ("clozapine", "carbamazepine"): "Risk of life-threatening bone marrow suppression and severe decrease in white blood cell count.",
    ("atorvastatin", "grapefruit"): "Grapefruit juice can dramatically increase blood levels of atorvastatin, raising the risk of muscle damage and liver issues.",
    ("azithromycin", "hydroxychloroquine"): "Increases the risk of QT prolongation, potentially leading to life-threatening arrhythmias.",
    ("furosemide", "digoxin"): "Can cause dangerous digoxin toxicity if potassium levels drop due to diuretic use.",
    ("insulin", "beta-blockers"): "Beta-blockers can mask hypoglycemia symptoms, putting patients at risk of unnoticed, severe low blood sugar.",
    ("prednisone", "NSAIDs"): "Combining these increases the risk of serious gastrointestinal bleeding, ulcers, and stomach pain.",
    ("paracetamol", "ibuprofen"): "This combination offers enhanced pain relief and anti-inflammatory action for short-term use.",
    ("amoxicillin", "clavulanic acid"): "Clavulanic acid protects amoxicillin from degradation, making it more effective against resistant bacteria.",
    ("metformin", "sitagliptin"): "Together, these improve glucose control with lower risk of hypoglycemia in type 2 diabetes.",
    ("losartan", "hydrochlorothiazide"): "Used to treat high blood pressure more effectively than either alone.",
    ("atorvastatin", "ezetimibe"): "Combining them helps lower LDL cholesterol better than using a statin alone.",
    ("salbutamol", "ipratropium"): "Provides dual bronchodilation for patients with COPD or asthma.",
    ("levodopa", "carbidopa"): "Carbidopa enhances levodopa’s delivery to the brain and reduces nausea.",
    ("doxycycline", "vitamin c"): "Vitamin C supports immune function and iron absorption during antibiotic treatment.",
    ("omeprazole", "domperidone"): "Helpful combo for reflux and nausea, especially in functional dyspepsia.",
    ("folic acid", "methotrexate"): "Folic acid reduces side effects of methotrexate without compromising its efficacy."
}

def check_custom_reaction(drug1, drug2):
    d1, d2 = drug1.strip().lower(), drug2.strip().lower()
    for (a, b), reaction in harmful_combinations.items():
        if {a, b} == {d1, d2}:
            return reaction
    return None
