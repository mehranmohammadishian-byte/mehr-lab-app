# -*- coding: utf-8 -*-
"""
MEHR LAB - Laboratory Test Database
Adult reference intervals are illustrative and must be verified locally.
Analytical quality goals are included only when a source is recorded.
"""

LAB_TESTS = {}


def add_test(
    name,
    category,
    units,
    default_unit,
    reference_range=None,
    critical_low=None,
    critical_high=None,
    cva=None,
    tea=None,
    source="",
    notes="",
    clia_cva=None,
    clia_tea=None,
    clia_source="",
    westgard_cva=None,
    westgard_tea=None,
    westgard_source="",
    clsi_cva=None,
    clsi_tea=None,
    clsi_source="",
    critical_source="",
):
    source_text = str(source or "").strip()

    if "westgard" in source_text.casefold():
        if westgard_cva is None:
            westgard_cva = cva
        if westgard_tea is None:
            westgard_tea = tea
        if not westgard_source:
            westgard_source = source_text

    LAB_TESTS[name] = {
        "category": category,
        "units": units,
        "default_unit": default_unit,
        "reference_range": reference_range,
        "critical_low": critical_low,
        "critical_high": critical_high,
        "cva": cva,
        "tea": tea,
        "source": source_text,
        "notes": notes,
        "clia_cva": clia_cva,
        "clia_tea": clia_tea,
        "clia_source": clia_source,
        "westgard_cva": westgard_cva,
        "westgard_tea": westgard_tea,
        "westgard_source": westgard_source,
        "clsi_cva": clsi_cva,
        "clsi_tea": clsi_tea,
        "clsi_source": clsi_source,
        "critical_source": critical_source,
    }


# ------------------------------------------------------------------
# CLINICAL CHEMISTRY
# ------------------------------------------------------------------

add_test(
    "Glucose", "Clinical Chemistry", ["mg/dL", "mmol/L"],
    "mg/dL", [70, 99],
    critical_low=50, critical_high=450,
    cva=2.2, tea=5.5,
    source="Westgard: European Biological Goals (historical)",
    notes="Fasting adult interval; critical limits based on common US laboratory standards.",
    critical_source="Main Line Health / JMA Critical Value List (50-450 mg/dL)",
    clia_tea=10.0,
    clia_source="CLIA 2024 Proficiency Limits",
    clsi_cva=2.2,
    clsi_tea=5.5,
    clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)"
)

add_test(
    "Urea", "Renal Function", ["mg/dL", "mmol/L"],
    "mg/dL", [15, 40], cva=6.3, tea=15.7,
    source="Westgard: European Biological Goals (historical)",
    clia_tea=9.0,
    clia_source="CLIA 2024 Proficiency Limits",
    clsi_cva=6.3,
    clsi_tea=15.7,
    clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)"
)

add_test(
    "BUN", "Renal Function", ["mg/dL", "mmol/L"],
    "mg/dL", [7, 20],
    notes="BUN is not identical to total urea."
)

add_test(
    "Creatinine", "Renal Function", ["mg/dL", "µmol/L"],
    "mg/dL", [0.6, 1.3],
    critical_high=5.0,
    cva=2.2, tea=6.4,
    source="Westgard: European Biological Goals (historical)",
    critical_source="Main Line Health (High >= 5.0 mg/dL)",
    clia_tea=10.0,
    clia_source="CLIA 2024 Proficiency Limits",
    clsi_cva=2.2,
    clsi_tea=6.4,
    clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)"
)

add_test(
    "Uric Acid", "Clinical Chemistry", ["mg/dL", "µmol/L"],
    "mg/dL", [3.5, 7.2], cva=4.2, tea=10.9,
    source="Westgard: European Biological Goals (historical)",
    clia_tea=17.0,
    clia_source="CLIA 2024 Proficiency Limits",
    clsi_cva=4.2,
    clsi_tea=10.9,
    clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)"
)

add_test(
    "Total Cholesterol", "Lipid Profile", ["mg/dL", "mmol/L"],
    "mg/dL", [0, 200], cva=2.7, tea=8.6,
    source="Westgard: European Biological Goals (historical)",
    clia_tea=10.0,
    clia_source="CLIA 2024 Proficiency Limits",
    clsi_cva=2.7,
    clsi_tea=8.6,
    clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)"
)

add_test(
    "Triglycerides", "Lipid Profile", ["mg/dL", "mmol/L"],
    "mg/dL", [0, 150], cva=11.5, tea=34.6,
    source="Westgard: European Biological Goals (historical)",
    clia_tea=15.0,
    clia_source="CLIA 2024 Proficiency Limits",
    clsi_cva=11.5,
    clsi_tea=34.6,
    clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)"
)

add_test("HDL Cholesterol", "Lipid Profile", ["mg/dL", "mmol/L"],
         "mg/dL", [40, 100],
         clia_tea=30.0,
         clia_source="CLIA 2024 Proficiency Limits")

add_test("LDL Cholesterol", "Lipid Profile", ["mg/dL", "mmol/L"],
         "mg/dL", [0, 130],
         clia_tea=20.0,
         clia_source="CLIA 2024 Proficiency Limits")

add_test("Non-HDL Cholesterol", "Lipid Profile", ["mg/dL", "mmol/L"],
         "mg/dL", [0, 160])

add_test("Apolipoprotein A1", "Lipid Profile", ["mg/dL", "g/L"],
         "mg/dL", [100, 200])

add_test("Apolipoprotein B", "Lipid Profile", ["mg/dL", "g/L"],
         "mg/dL", [60, 130])

add_test(
    "Lipoprotein(a)", "Lipid Profile", ["mg/dL", "nmol/L"],
    "mg/dL",
    notes="Do not use a universal conversion between mg/dL and nmol/L."
)

add_test(
    "AST", "Liver Function", ["U/L"], "U/L", [0, 40],
    cva=7.2, tea=18.0,
    source="Westgard: European Biological Goals (historical)",
    clia_tea=20.0,
    clia_source="CLIA 2024 Proficiency Limits",
    clsi_cva=7.2,
    clsi_tea=18.0,
    clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)"
)

add_test(
    "ALT", "Liver Function", ["U/L"], "U/L", [0, 41],
    cva=13.6, tea=36.0,
    source="Westgard: European Biological Goals (historical)",
    clia_tea=20.0,
    clia_source="CLIA 2024 Proficiency Limits",
    clsi_cva=13.6,
    clsi_tea=36.0,
    clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)"
)

add_test(
    "ALP", "Liver Function", ["U/L"], "U/L", [40, 130],
    cva=3.4, tea=12.0,
    source="Westgard: European Biological Goals (historical)",
    clia_tea=30.0,
    clia_source="CLIA 2024 Proficiency Limits",
    clsi_cva=3.4,
    clsi_tea=12.0,
    clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)"
)

add_test("GGT", "Liver Function", ["U/L"], "U/L", [0, 60],
         clia_tea=15.0,
         clia_source="CLIA 2024 Proficiency Limits")

add_test("LDH", "Clinical Chemistry", ["U/L"], "U/L", [120, 250],
         clia_tea=20.0,
         clia_source="CLIA 2024 Proficiency Limits")

add_test(
    "Total Bilirubin", "Liver Function", ["mg/dL", "µmol/L"],
    "mg/dL", [0.2, 1.2],
    critical_high=15.0,
    critical_source="Main Line Health (High >= 15 mg/dL; verify local adult policy)",
    clia_tea=20.0,
    clia_source="CLIA 2024 Proficiency Limits"
)

add_test("Direct Bilirubin", "Liver Function", ["mg/dL", "µmol/L"],
         "mg/dL", [0.0, 0.3])

add_test("Indirect Bilirubin", "Liver Function", ["mg/dL", "µmol/L"],
         "mg/dL", [0.2, 0.9])

add_test(
    "Albumin", "Proteins", ["g/dL", "g/L"], "g/dL", [3.5, 5.0],
    cva=1.4, tea=3.4,
    source="Westgard: European Biological Goals (historical)",
    clia_tea=10.0,
    clia_source="CLIA 2024 Proficiency Limits",
    clsi_cva=1.4,
    clsi_tea=3.4,
    clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)"
)

add_test(
    "Total Protein", "Proteins", ["g/dL", "g/L"], "g/dL", [6.0, 8.3],
    cva=1.4, tea=3.8,
    source="Westgard: European Biological Goals (historical)",
    clia_tea=10.0,
    clia_source="CLIA 2024 Proficiency Limits",
    clsi_cva=1.4,
    clsi_tea=3.8,
    clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)"
)

add_test("Globulin", "Proteins", ["g/dL", "g/L"], "g/dL", [2.0, 3.5])

add_test("Amylase", "Clinical Chemistry", ["U/L"], "U/L", [30, 110],
         clia_tea=30.0,
         clia_source="CLIA 2024 Proficiency Limits")

add_test("Lipase", "Clinical Chemistry", ["U/L"], "U/L", [13, 60])

add_test("CK", "Clinical Chemistry", ["U/L"], "U/L", [30, 200],
         clia_tea=30.0,
         clia_source="CLIA 2024 Proficiency Limits")

add_test(
    "CK-MB", "Clinical Chemistry", ["U/L"], "U/L", [0, 25],
    notes="Interpret with the method and clinical context."
)

add_test(
    "Troponin I", "Cardiac Markers", ["ng/L", "ng/mL"],
    "ng/L",
    notes="Use the assay-specific 99th percentile; no universal range."
)

add_test(
    "Troponin T", "Cardiac Markers", ["ng/L", "ng/mL"],
    "ng/L",
    notes="Use the assay-specific 99th percentile; no universal range."
)

add_test(
    "NT-proBNP", "Cardiac Markers", ["pg/mL", "ng/L"],
    "pg/mL",
    notes="Interpretation depends on age and clinical context."
)

add_test("CRP", "Inflammation", ["mg/L"], "mg/L", [0, 5])

add_test(
    "hs-CRP", "Inflammation", ["mg/L"], "mg/L", [0, 3],
    notes="Cardiovascular risk interpretation differs from standard CRP."
)

add_test(
    "Procalcitonin", "Inflammation", ["ng/mL", "µg/L"],
    "ng/mL",
    notes="Use assay-specific decision thresholds."
)

add_test("Iron", "Iron Studies", ["µg/dL", "µmol/L"], "µg/dL", [50, 170],
         clia_tea=20.0,
         clia_source="CLIA 2024 Proficiency Limits")

add_test("TIBC", "Iron Studies", ["µg/dL", "µmol/L"], "µg/dL", [250, 450])

add_test("Transferrin", "Iron Studies", ["mg/dL", "g/L"],
         "mg/dL", [200, 360])

add_test(
    "Ferritin", "Iron Studies", ["ng/mL", "µg/L"], "ng/mL",
    notes="Reference intervals vary by sex, age and method."
)

add_test("Vitamin B12", "Vitamins", ["pg/mL", "pmol/L"],
         "pg/mL", [200, 900])

add_test(
    "Folate", "Vitamins", ["ng/mL", "nmol/L"], "ng/mL",
    notes="Serum and red-cell folate are different tests."
)

add_test(
    "25-OH Vitamin D", "Vitamins", ["ng/mL", "nmol/L"], "ng/mL",
    notes="Clinical decision thresholds vary among guidelines."
)

add_test("Lactate", "Clinical Chemistry", ["mmol/L", "mg/dL"],
         "mmol/L", [0.5, 2.2])

add_test(
    "Ammonia", "Clinical Chemistry", ["µmol/L", "µg/dL"],
    "µmol/L",
    notes="Specimen handling and method are important."
)

add_test("Osmolality", "Clinical Chemistry", ["mOsm/kg"],
         "mOsm/kg", [275, 295])


# ------------------------------------------------------------------
# ELECTROLYTES, MINERALS AND ACID-BASE
# ------------------------------------------------------------------

add_test(
    "Sodium", "Electrolytes", ["mmol/L"], "mmol/L", [135, 145],
    critical_low=120, critical_high=160,
    critical_source="Common standards (e.g., 120-160 mmol/L)",
    clia_tea=4.0,
    clia_source="CLIA 2024 Proficiency Limits",
    clsi_cva=0.3,
    clsi_tea=1.0,
    clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)"
)

add_test(
    "Potassium", "Electrolytes", ["mmol/L"], "mmol/L", [3.5, 5.1],
    critical_low=2.8, critical_high=6.0,
    cva=2.4, tea=5.6,
    source="Westgard: European Biological Goals (historical)",
    critical_source="Main Line Health (2.8-6.0 mmol/L)",
    clia_tea=8.0,
    clia_source="CLIA 2024 Proficiency Limits",
    clsi_cva=2.4,
    clsi_tea=5.6,
    clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)"
)

add_test(
    "Chloride", "Electrolytes", ["mmol/L"], "mmol/L", [98, 107],
    cva=0.7, tea=1.7,
    source="Westgard: European Biological Goals (historical)",
    clia_tea=5.0,
    clia_source="CLIA 2024 Proficiency Limits",
    clsi_cva=0.7,
    clsi_tea=1.7,
    clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)"
)

add_test("Bicarbonate", "Electrolytes", ["mmol/L"],
         "mmol/L", [22, 29])

add_test(
    "Calcium", "Electrolytes", ["mg/dL", "mmol/L"],
    "mg/dL", [8.5, 10.5],
    critical_low=6.0, critical_high=13.0,
    cva=0.9, tea=2.2,
    source="Westgard: European Biological Goals (historical)",
    critical_source="Main Line Health (6.0-13.0 mg/dL)",
    clia_tea=10.0,
    clia_source="CLIA 2024 Proficiency Limits",
    clsi_cva=0.9,
    clsi_tea=2.2,
    clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)"
)

add_test("Ionized Calcium", "Electrolytes", ["mmol/L"],
         "mmol/L", [1.12, 1.32])

add_test(
    "Magnesium", "Electrolytes", ["mg/dL", "mmol/L"],
    "mg/dL", [1.7, 2.4],
    cva=1.1, tea=3.4,
    source="Westgard: European Biological Goals (historical)",
    clsi_cva=1.1,
    clsi_tea=3.4,
    clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)"
)

add_test(
    "Phosphorus", "Electrolytes", ["mg/dL", "mmol/L"],
    "mg/dL", [2.5, 4.5],
    cva=4.0, tea=9.7,
    source="Westgard: European Biological Goals (historical)",
    clsi_cva=4.0,
    clsi_tea=9.7,
    clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)"
)


# ------------------------------------------------------------------
# RENAL AND URINE CHEMISTRY
# ------------------------------------------------------------------

add_test("Urine Creatinine", "Urine Chemistry",
         ["mg/dL", "mmol/L"], "mg/dL")

add_test("Urine Protein", "Urine Chemistry",
         ["mg/dL", "g/L"], "mg/dL")

add_test("Urine Albumin", "Urine Chemistry",
         ["mg/L", "mg/dL"], "mg/L")

add_test(
    "Urine Albumin/Creatinine Ratio", "Urine Chemistry",
    ["mg/g", "mg/mmol"], "mg/g",
    notes="Do not use a generic conversion factor."
)

add_test("Urine Protein/Creatinine Ratio", "Urine Chemistry",
         ["mg/g", "mg/mmol"], "mg/g")

add_test("Urine Calcium", "Urine Chemistry",
         ["mg/dL", "mmol/L"], "mg/dL")

add_test("Urine Uric Acid", "Urine Chemistry",
         ["mg/dL", "mmol/L"], "mg/dL")


# ------------------------------------------------------------------
# DIABETES
# ------------------------------------------------------------------

add_test(
    "HbA1c", "Diabetes", ["%", "mmol/mol"], "%", [4.0, 5.6],
    notes="NGSP/IFCC conversion is a formula, not a simple multiplier.",
    clia_tea=6.0,
    clia_source="CLIA 2024 Proficiency Limits"
)

add_test("Fructosamine", "Diabetes", ["µmol/L"],
         "µmol/L", [205, 285])

add_test("C-Peptide", "Diabetes", ["ng/mL", "nmol/L"], "ng/mL")

add_test(
    "Insulin", "Hormones", ["µIU/mL", "pmol/L"], "µIU/mL",
    notes="Conversion depends on assay-specific calibration."
)


# ------------------------------------------------------------------
# THYROID AND ENDOCRINOLOGY
# ------------------------------------------------------------------

add_test("TSH", "Thyroid", ["mIU/L", "µIU/mL"], "mIU/L", [0.4, 4.0],
         clia_tea=20.0,
         clia_source="CLIA 2024 Proficiency Limits",
         clsi_cva=9.7,
         clsi_tea=24.3,
         clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)")

add_test("Free T4", "Thyroid", ["ng/dL", "pmol/L"], "ng/dL", [0.8, 1.8],
         clia_tea=15.0,
         clia_source="CLIA 2024 Proficiency Limits",
         clsi_cva=2.9,
         clsi_tea=7.3,
         clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)")

add_test(
    "Total T4", "Thyroid", ["µg/dL", "nmol/L"], "µg/dL", [5.0, 12.0],
    cva=3.4, tea=9.7,
    source="Westgard: European Biological Goals (historical)",
    clia_tea=20.0,
    clia_source="CLIA 2024 Proficiency Limits",
    clsi_cva=3.4,
    clsi_tea=9.7,
    clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)"
)

add_test("Free T3", "Thyroid", ["pg/mL", "pmol/L"], "pg/mL", [2.0, 4.4],
         clia_tea=15.0,
         clia_source="CLIA 2024 Proficiency Limits")

add_test(
    "Total T3", "Thyroid", ["ng/dL", "nmol/L"], "ng/dL", [80, 200],
    cva=4.0, tea=12.1,
    source="Westgard: European Biological Goals (historical)",
    clia_tea=20.0,
    clia_source="CLIA 2024 Proficiency Limits",
    clsi_cva=4.0,
    clsi_tea=12.1,
    clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)"
)

add_test("Anti-TPO", "Thyroid", ["IU/mL"], "IU/mL")

add_test("Anti-Thyroglobulin", "Thyroid", ["IU/mL"], "IU/mL")

add_test("Thyroglobulin", "Thyroid", ["ng/mL", "µg/L"], "ng/mL")

add_test("PTH", "Hormones", ["pg/mL", "ng/L"], "pg/mL")

add_test(
    "Cortisol", "Hormones", ["µg/dL", "nmol/L"], "µg/dL",
    notes="Reference interval depends on collection time."
)

add_test("ACTH", "Hormones", ["pg/mL", "ng/L"], "pg/mL")

add_test(
    "Prolactin", "Hormones", ["ng/mL", "µg/L"], "ng/mL",
    notes="Reference interval depends on sex, pregnancy and method."
)

add_test(
    "FSH", "Hormones", ["mIU/mL", "IU/L"], "mIU/mL",
    notes="Interpretation depends on sex, age and menstrual-cycle phase."
)

add_test(
    "LH", "Hormones", ["mIU/mL", "IU/L"], "mIU/mL",
    notes="Interpretation depends on sex, age and menstrual-cycle phase."
)

add_test(
    "Estradiol", "Hormones", ["pg/mL", "pmol/L"], "pg/mL",
    notes="Reference interval depends on sex and menstrual-cycle phase."
)

add_test("Progesterone", "Hormones", ["ng/mL", "nmol/L"], "ng/mL")

add_test(
    "Testosterone Total", "Hormones", ["ng/dL", "nmol/L"], "ng/dL",
    notes="Reference interval depends on sex, age and method."
)

add_test(
    "Free Testosterone", "Hormones", ["pg/mL", "pmol/L"], "pg/mL",
    notes="Methods and reference intervals vary substantially."
)

add_test("DHEA-S", "Hormones", ["µg/dL", "µmol/L"], "µg/dL")

add_test("SHBG", "Hormones", ["nmol/L"], "nmol/L")

add_test("AMH", "Hormones", ["ng/mL", "pmol/L"], "ng/mL")

add_test(
    "IGF-1", "Hormones", ["ng/mL", "µg/L"], "ng/mL",
    notes="Reference interval depends strongly on age."
)

add_test("Growth Hormone", "Hormones", ["ng/mL", "µg/L"], "ng/mL")

add_test("Aldosterone", "Hormones", ["ng/dL", "pmol/L"], "ng/dL")

add_test(
    "Renin", "Hormones", ["ng/mL/hr", "mIU/L"], "ng/mL/hr",
    notes="Renin activity and direct renin concentration are not interchangeable."
)


# ------------------------------------------------------------------
# TUMOR MARKERS
# ------------------------------------------------------------------

add_test("PSA Total", "Tumor Markers", ["ng/mL", "µg/L"], "ng/mL")

add_test("PSA Free", "Tumor Markers", ["ng/mL", "µg/L"], "ng/mL")

add_test("CEA", "Tumor Markers", ["ng/mL", "µg/L"], "ng/mL")

add_test("AFP", "Tumor Markers", ["ng/mL", "µg/L"], "ng/mL")

add_test("CA 125", "Tumor Markers", ["U/mL"], "U/mL")

add_test("CA 15-3", "Tumor Markers", ["U/mL"], "U/mL")

add_test("CA 19-9", "Tumor Markers", ["U/mL"], "U/mL")

add_test(
    "Beta-hCG", "Hormones and Tumor Markers", ["mIU/mL", "IU/L"], "mIU/mL",
    notes="Interpretation depends on pregnancy status and clinical context."
)


# ------------------------------------------------------------------
# HEMATOLOGY
# ------------------------------------------------------------------

add_test(
    "Hemoglobin", "Hematology", ["g/dL", "g/L"], "g/dL", [12, 17.5],
    critical_low=7.0, critical_high=20.0,
    critical_source="Main Line Health (7.0-20.0 g/dL)",
    clia_tea=7.0,
    clia_source="CLIA 2024 Proficiency Limits",
    clsi_cva=1.43,
    clsi_tea=3.6,
    clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)"
)

add_test(
    "WBC", "Hematology", ["10^3/µL", "10^9/L"], "10^3/µL", [4, 11],
    critical_low=2.5, critical_high=30.0,
    critical_source="Main Line Health (2.5-30.0 x10^3/µL)",
    clia_tea=15.0,
    clia_source="CLIA 2024 Proficiency Limits",
    clsi_cva=5.73,
    clsi_tea=14.3,
    clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)"
)

add_test("RBC", "Hematology", ["10^6/µL", "10^12/L"], "10^6/µL", [4, 6])

add_test(
    "Platelets", "Hematology", ["10^3/µL", "10^9/L"], "10^3/µL", [150, 450],
    critical_low=50, critical_high=1000,
    critical_source="Main Line Health (50-1000 x10^3/µL)",
    clia_tea=25.0,
    clia_source="CLIA 2024 Proficiency Limits",
    clsi_cva=4.6,
    clsi_tea=11.5,
    clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)"
)

add_test("Hematocrit", "Hematology", ["%", "L/L"], "%", [36, 53])

add_test("MCV", "Hematology", ["fL"], "fL", [80, 100])

add_test("MCH", "Hematology", ["pg"], "pg", [27, 33])

add_test("MCHC", "Hematology", ["g/dL", "g/L"], "g/dL", [32, 36])

add_test("RDW-CV", "Hematology", ["%"], "%", [11.5, 14.5])

add_test("Reticulocyte Count", "Hematology", ["%"], "%", [0.5, 2.5])

add_test(
    "Absolute Neutrophils", "Hematology", ["10^3/µL", "10^9/L"],
    "10^3/µL", [1.5, 7.5]
)

add_test(
    "Absolute Lymphocytes", "Hematology", ["10^3/µL", "10^9/L"],
    "10^3/µL", [1.0, 4.0]
)

add_test(
    "Absolute Monocytes", "Hematology", ["10^3/µL", "10^9/L"],
    "10^3/µL", [0.2, 0.8]
)

add_test(
    "Absolute Eosinophils", "Hematology", ["10^3/µL", "10^9/L"],
    "10^3/µL", [0.0, 0.5]
)

add_test(
    "Absolute Basophils", "Hematology", ["10^3/µL", "10^9/L"],
    "10^3/µL", [0.0, 0.2]
)

add_test("ESR", "Hematology", ["mm/hr"], "mm/hr", [0, 20])

add_test(
    "Peripheral Blood Smear", "Hematology", ["Qualitative"], "Qualitative",
    notes="Interpretation is morphology-based, not a numeric reference interval."
)


# ------------------------------------------------------------------
# COAGULATION
# ------------------------------------------------------------------

add_test(
    "PT", "Coagulation", ["seconds"], "seconds",
    critical_high=20.0,
    notes="Use the local reagent and instrument reference interval. Critical high threshold is often defined as INR >= 6.0 or >2x upper limit of normal.",
    critical_source="Main Line Health (INR >= 6.0) / IHSR (PT > 2x ULN)",
    clia_tea=15.0,
    clia_source="CLIA 2024 Proficiency Limits",
    clsi_cva=2.0,
    clsi_tea=5.0,
    clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)"
)

add_test(
    "INR", "Coagulation", ["ratio"], "ratio",
    notes="Therapeutic ranges depend on indication.",
    clia_tea=15.0,
    clia_source="CLIA 2024 Proficiency Limits"
)

add_test("aPTT", "Coagulation", ["seconds"], "seconds",
         clia_tea=15.0,
         clia_source="CLIA 2024 Proficiency Limits")

add_test(
    "Fibrinogen", "Coagulation", ["mg/dL", "g/L"], "mg/dL", [200, 400],
    critical_low=100,
    critical_source="Main Line Health (Low <= 100 mg/dL)",
    clia_tea=20.0,
    clia_source="CLIA 2024 Proficiency Limits",
    clsi_cva=5.4,
    clsi_tea=13.5,
    clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)"
)

add_test(
    "D-Dimer", "Coagulation", ["ng/mL FEU", "µg/L FEU"], "ng/mL FEU",
    notes="FEU and DDU are not interchangeable without the appropriate factor."
)

add_test("Antithrombin Activity", "Coagulation", ["%"], "%", [80, 120])

add_test("Protein C Activity", "Coagulation", ["%"], "%", [70, 140])

add_test("Protein S Activity", "Coagulation", ["%"], "%", [60, 140])


# ------------------------------------------------------------------
# IMMUNOLOGY AND SEROLOGY
# ------------------------------------------------------------------

add_test("IgG", "Immunology", ["mg/dL", "g/L"], "mg/dL", [700, 1600],
         clsi_cva=2.3,
         clsi_tea=5.8,
         clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)")

add_test("IgA", "Immunology", ["mg/dL", "g/L"], "mg/dL", [70, 400],
         clsi_cva=2.7,
         clsi_tea=6.8,
         clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)")

add_test("IgM", "Immunology", ["mg/dL", "g/L"], "mg/dL", [40, 230],
         clsi_cva=3.0,
         clsi_tea=7.5,
         clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)")

add_test("C3", "Immunology", ["mg/dL", "g/L"], "mg/dL", [90, 180],
         clsi_cva=2.6,
         clsi_tea=6.5,
         clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)")

add_test("C4", "Immunology", ["mg/dL", "g/L"], "mg/dL", [10, 40],
         clsi_cva=4.5,
         clsi_tea=11.3,
         clsi_source="CLSI EP21 / Westgard Biological Variation (Desirable)")

add_test("Rheumatoid Factor", "Immunology", ["IU/mL"], "IU/mL")

add_test("Anti-CCP", "Immunology", ["U/mL"], "U/mL")

add_test(
    "ANA", "Immunology", ["Qualitative", "titer"], "Qualitative",
    notes="Report method, titer and pattern when applicable."
)

add_test("Anti-dsDNA", "Immunology", ["IU/mL"], "IU/mL")

add_test("ASO", "Serology", ["IU/mL"], "IU/mL")

add_test(
    "Widal", "Serology", ["titer"], "titer",
    notes="Interpretation depends on local epidemiology and method."
)

add_test("CRP Qualitative", "Serology", ["Qualitative"], "Qualitative")

add_test("HBsAg", "Serology", ["Qualitative", "S/CO"], "Qualitative")

add_test("Anti-HBs", "Serology", ["mIU/mL"], "mIU/mL")

add_test("Anti-HBc Total", "Serology", ["Qualitative", "S/CO"], "Qualitative")

add_test("Anti-HCV", "Serology", ["Qualitative", "S/CO"], "Qualitative")

add_test("HIV Ag/Ab", "Serology", ["Qualitative", "S/CO"], "Qualitative")

add_test("VDRL/RPR", "Serology", ["Qualitative", "titer"], "Qualitative")


# ------------------------------------------------------------------
# URINALYSIS AND STOOL
# ------------------------------------------------------------------

add_test(
    "Urinalysis", "Urinalysis", ["Qualitative"], "Qualitative",
    notes="Includes physical, chemical and microscopic examination."
)

add_test("Urine Specific Gravity", "Urinalysis", ["ratio"], "ratio", [1.005, 1.030])

add_test("Urine pH", "Urinalysis", ["pH"], "pH", [4.5, 8.0])

add_test("Urine Glucose", "Urinalysis", ["Qualitative"], "Qualitative")

add_test("Urine Protein Qualitative", "Urinalysis", ["Qualitative"], "Qualitative")

add_test("Urine Ketones", "Urinalysis", ["Qualitative"], "Qualitative")

add_test("Urine Blood", "Urinalysis", ["Qualitative"], "Qualitative")

add_test("Urine Nitrite", "Urinalysis", ["Qualitative"], "Qualitative")

add_test("Urine Leukocyte Esterase", "Urinalysis", ["Qualitative"], "Qualitative")

add_test("Urine RBC", "Urinalysis", ["cells/HPF"], "cells/HPF", [0, 2])

add_test("Urine WBC", "Urinalysis", ["cells/HPF"], "cells/HPF", [0, 5])

add_test("Stool Occult Blood", "Stool Tests", ["Qualitative"], "Qualitative")

add_test("Stool Ova and Parasites", "Stool Tests", ["Qualitative"], "Qualitative")


# ------------------------------------------------------------------
# MICROBIOLOGY
# ------------------------------------------------------------------

add_test(
    "Urine Culture", "Microbiology", ["Qualitative", "CFU/mL"], "Qualitative",
    notes="Interpret colony count with specimen and clinical context."
)

add_test("Blood Culture", "Microbiology", ["Qualitative"], "Qualitative")

add_test("Throat Culture", "Microbiology", ["Qualitative"], "Qualitative")

add_test("Sputum Culture", "Microbiology", ["Qualitative"], "Qualitative")

add_test(
    "Antibiotic Susceptibility", "Microbiology", ["Qualitative"], "Qualitative",
    notes="Use current organism-specific susceptibility standards."
)


# ------------------------------------------------------------------
# COMPATIBILITY / API FUNCTIONS
# ------------------------------------------------------------------

def get_all_tests():
    return sorted(LAB_TESTS.keys())


def get_test(test_name):
    if test_name in LAB_TESTS:
        return LAB_TESTS[test_name]

    query = str(test_name or "").strip().casefold()

    for name, record in LAB_TESTS.items():
        if name.casefold() == query:
            return record

    return None


def get_test_data(test_name):
    return get_test(test_name)


def search_tests(query):
    query = str(query or "").strip().casefold()

    if not query:
        return get_all_tests()

    results = []

    for name, record in LAB_TESTS.items():
        searchable = " ".join([
            name,
            record.get("category", ""),
            " ".join(record.get("units", [])),
        ]).casefold()

        if query in searchable:
            results.append(name)

    return sorted(results)


def get_reference_range(test_name):
    record = get_test(test_name)
    return record.get("reference_range") if record else None


def check_critical_result(test_name, value):
    record = get_test(test_name)

    if not record:
        return None

    try:
        value = float(value)
    except (ValueError, TypeError):
        return None

    low = record.get("critical_low")
    high = record.get("critical_high")

    if low is not None and value < low:
        return "LOW"

    if high is not None and value > high:
        return "HIGH"

    if low is not None or high is not None:
        return "NORMAL"

    return None


def is_critical(test_name, value):
    """Backward-compatible function used by main.py."""
    return check_critical_result(test_name, value)


def get_categories():
    return sorted({
        record["category"]
        for record in LAB_TESTS.values()
    })


def get_tests_by_category(category):
    return sorted(
        name
        for name, record in LAB_TESTS.items()
        if record.get("category") == category
    )


# ------------------------------------------------------------------
# ADDITIONAL CVa DATA
# Source: Westgard QC, Desirable Biological Variation Database (2014)
# ------------------------------------------------------------------

WESTGARD_CVA_2014 = {
    "HDL Cholesterol": 3.65,
    "LDL Cholesterol": 3.9,
    "Apolipoprotein A1": 3.3,
    "Apolipoprotein B": 3.5,
    "GGT": 6.7,
    "LDH": 4.3,
    "Total Bilirubin": 10.90,
    "Direct Bilirubin": 18.4,
    "Amylase": 4.4,
    "Lipase": 16.1,
    "CK": 11.4,
    "CRP": 21.1,
    "hs-CRP": 24.85,
    "Iron": 13.3,
    "Transferrin": 2.3,
    "Ferritin": 7.1,
    "Lipoprotein(a)": 10.4,
    "Bicarbonate": 2.4,
    "Ionized Calcium": 0.9,
    "Fructosamine": 1.7,
    "Sodium": 0.3,
    "TSH": 9.7,
    "Free T4": 2.9,
    "Free T3": 4.0,
    "Insulin": 10.6,
    "C-Peptide": 8.3,
    "FSH": 5.5,
    "LH": 11.5,
    "Estradiol": 11.25,
    "Prolactin": 11.5,
    "Testosterone Total": 4.63,
    "DHEA-S": 3.188,
    "SHBG": 6.53,
    "IGF-1": 7.3,
    "PSA Total": 9.1,
    "CEA": 6.4,
    "CA 125": 12.4,
    "CA 15-3": 3.1,
    "CA 19-9": 7.98,
    "Hemoglobin": 1.43,
    "WBC": 5.73,
    "RBC": 1.6,
    "Platelets": 4.6,
    "Hematocrit": 1.35,
    "MCV": 0.7,
    "MCH": 0.7,
    "MCHC": 0.53,
    "RDW-CV": 1.8,
    "Reticulocyte Count": 5.5,
    "PT": 2.0,
    "aPTT": 1.4,
    "Fibrinogen": 5.4,
    "IgG": 2.3,
    "IgA": 2.7,
    "IgM": 3.0,
    "C3": 2.6,
    "C4": 4.5,
}


def apply_additional_cva_data():
    source_name = (
        "Westgard QC: Desirable Biological Variation Database (2014)"
    )

    updated_count = 0
    unmatched_tests = []

    for test_name, cva_value in WESTGARD_CVA_2014.items():
        record = LAB_TESTS.get(test_name)

        if record is None:
            unmatched_tests.append(test_name)
            continue

        if record.get("cva") is None:
            record["cva"] = cva_value
            updated_count += 1

        if record.get("westgard_cva") is None:
            record["westgard_cva"] = record["cva"]

        if not record.get("westgard_source"):
            record["westgard_source"] = source_name

        if not record.get("source"):
            record["source"] = source_name

    return {
        "updated": updated_count,
        "unmatched_tests": unmatched_tests,
    }


CVA_UPDATE_REPORT = apply_additional_cva_data()
