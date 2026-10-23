# -*- coding: utf-8 -*-
"""MEHR LAB - Analyte-aware and general-purpose unit converter."""

GENERAL_FACTORS = {
    # Concentration
    ("g/dL", "g/L"): 10.0,
    ("g/L", "g/dL"): 0.1,
    ("mg/L", "mg/dL"): 0.1,
    ("mg/dL", "mg/L"): 10.0,
    ("µg/mL", "mg/L"): 1.0,
    ("mg/L", "µg/mL"): 1.0,
    ("ng/mL", "µg/L"): 1.0,
    ("µg/L", "ng/mL"): 1.0,
    ("pg/mL", "ng/L"): 1.0,
    ("ng/L", "pg/mL"): 1.0,
    ("ng/mL", "ng/L"): 1000.0,
    ("ng/L", "ng/mL"): 0.001,
    ("µIU/mL", "mIU/L"): 1.0,
    ("mIU/L", "µIU/mL"): 1.0,
    ("IU/L", "mIU/mL"): 1.0,
    ("mIU/mL", "IU/L"): 1.0,
    ("10^3/µL", "10^9/L"): 1.0,
    ("10^9/L", "10^3/µL"): 1.0,
    ("10^6/µL", "10^12/L"): 1.0,
    ("10^12/L", "10^6/µL"): 1.0,
    ("%", "L/L"): 0.01,
    ("L/L", "%"): 100.0,
    ("pg/mL", "µg/L"): 0.001,
    ("µg/L", "pg/mL"): 1000.0,
    ("mg/dL", "g/L"): 0.01,
    ("g/L", "mg/dL"): 100.0,
    ("pg/mL", "ng/mL"): 0.001,
    ("ng/mL", "pg/mL"): 1000.0,

    # Volume
    ("mL", "L"): 0.001,
    ("L", "mL"): 1000.0,
    ("µL", "mL"): 0.001,
    ("mL", "µL"): 1000.0,
    ("µL", "L"): 0.000001,
    ("L", "µL"): 1000000.0,

    # Mass
    ("mg", "g"): 0.001,
    ("g", "mg"): 1000.0,
    ("µg", "mg"): 0.001,
    ("mg", "µg"): 1000.0,
    ("ng", "µg"): 0.001,
    ("µg", "ng"): 1000.0,
    ("ng", "mg"): 0.000001,
    ("mg", "ng"): 1000000.0,
    ("µg", "g"): 0.000001,
    ("g", "µg"): 1000000.0,
}

# Mass-to-molar conversion factors depend on the analyte's molecular mass.
ANALYTE_FACTORS = {
    "glucose": {
        ("mg/dL", "mmol/L"): 1 / 18.0182,
        ("mmol/L", "mg/dL"): 18.0182,
    },
    "urea": {
        ("mg/dL", "mmol/L"): 1 / 6.006,
        ("mmol/L", "mg/dL"): 6.006,
    },
    "bun": {
        ("mg/dL", "mmol/L"): 1 / 2.801,
        ("mmol/L", "mg/dL"): 2.801,
    },
    "creatinine": {
        ("mg/dL", "µmol/L"): 88.4,
        ("µmol/L", "mg/dL"): 1 / 88.4,
    },
    "uric acid": {
        ("mg/dL", "µmol/L"): 59.48,
        ("µmol/L", "mg/dL"): 1 / 59.48,
    },
    "total cholesterol": {
        ("mg/dL", "mmol/L"): 1 / 38.67,
        ("mmol/L", "mg/dL"): 38.67,
    },
    "cholesterol": {
        ("mg/dL", "mmol/L"): 1 / 38.67,
        ("mmol/L", "mg/dL"): 38.67,
    },
    "hdl cholesterol": {
        ("mg/dL", "mmol/L"): 1 / 38.67,
        ("mmol/L", "mg/dL"): 38.67,
    },
    "ldl cholesterol": {
        ("mg/dL", "mmol/L"): 1 / 38.67,
        ("mmol/L", "mg/dL"): 38.67,
    },
    "non-hdl cholesterol": {
        ("mg/dL", "mmol/L"): 1 / 38.67,
        ("mmol/L", "mg/dL"): 38.67,
    },
    "triglycerides": {
        ("mg/dL", "mmol/L"): 1 / 88.57,
        ("mmol/L", "mg/dL"): 88.57,
    },
    "calcium": {
        ("mg/dL", "mmol/L"): 1 / 4.008,
        ("mmol/L", "mg/dL"): 4.008,
    },
    "magnesium": {
        ("mg/dL", "mmol/L"): 1 / 2.4305,
        ("mmol/L", "mg/dL"): 2.4305,
    },
    "phosphorus": {
        ("mg/dL", "mmol/L"): 1 / 3.097,
        ("mmol/L", "mg/dL"): 3.097,
    },
    "total bilirubin": {
        ("mg/dL", "µmol/L"): 17.104,
        ("µmol/L", "mg/dL"): 1 / 17.104,
    },
    "direct bilirubin": {
        ("mg/dL", "µmol/L"): 17.104,
        ("µmol/L", "mg/dL"): 1 / 17.104,
    },
    "indirect bilirubin": {
        ("mg/dL", "µmol/L"): 17.104,
        ("µmol/L", "mg/dL"): 1 / 17.104,
    },
    "albumin": {
        ("g/dL", "g/L"): 10.0,
        ("g/L", "g/dL"): 0.1,
    },
    "total protein": {
        ("g/dL", "g/L"): 10.0,
        ("g/L", "g/dL"): 0.1,
    },
    "globulin": {
        ("g/dL", "g/L"): 10.0,
        ("g/L", "g/dL"): 0.1,
    },
    "free t4": {
        ("ng/dL", "pmol/L"): 12.87,
        ("pmol/L", "ng/dL"): 1 / 12.87,
    },
    "total t4": {
        ("µg/dL", "nmol/L"): 12.87,
        ("nmol/L", "µg/dL"): 1 / 12.87,
    },
    "free t3": {
        ("pg/mL", "pmol/L"): 1.536,
        ("pmol/L", "pg/mL"): 1 / 1.536,
    },
    "total t3": {
        ("ng/dL", "nmol/L"): 0.01536,
        ("nmol/L", "ng/dL"): 1 / 0.01536,
    },
    "iron": {
        ("µg/dL", "µmol/L"): 0.1791,
        ("µmol/L", "µg/dL"): 1 / 0.1791,
    },
    "tibc": {
        ("µg/dL", "µmol/L"): 0.1791,
        ("µmol/L", "µg/dL"): 1 / 0.1791,
    },
    "lactate": {
        ("mmol/L", "mg/dL"): 9.008,
        ("mg/dL", "mmol/L"): 1 / 9.008,
    },
    "lactate dehydrogenase": {},
}

TEMPERATURE_PAIRS = {("°C", "°F"), ("°F", "°C")}

GENERAL_UNITS = [
    "L", "mL", "µL", "g", "mg", "µg", "ng",
    "g/dL", "g/L", "mg/dL", "mg/L",
    "µg/mL", "µg/L", "ng/mL", "ng/L", "pg/mL",
    "mIU/L", "µIU/mL", "IU/L", "mIU/mL",
    "10^3/µL", "10^9/L", "10^6/µL", "10^12/L",
    "%", "L/L", "°C", "°F",
]

ANALYTE_UNITS = {
    "Glucose": ["mg/dL", "mmol/L"],
    "Urea": ["mg/dL", "mmol/L"],
    "BUN": ["mg/dL", "mmol/L"],
    "Creatinine": ["mg/dL", "µmol/L"],
    "Uric Acid": ["mg/dL", "µmol/L"],
    "Total Cholesterol": ["mg/dL", "mmol/L"],
    "Cholesterol": ["mg/dL", "mmol/L"],
    "HDL Cholesterol": ["mg/dL", "mmol/L"],
    "LDL Cholesterol": ["mg/dL", "mmol/L"],
    "Non-HDL Cholesterol": ["mg/dL", "mmol/L"],
    "Triglycerides": ["mg/dL", "mmol/L"],
    "Calcium": ["mg/dL", "mmol/L"],
    "Magnesium": ["mg/dL", "mmol/L"],
    "Phosphorus": ["mg/dL", "mmol/L"],
    "Total Bilirubin": ["mg/dL", "µmol/L"],
    "Direct Bilirubin": ["mg/dL", "µmol/L"],
    "Indirect Bilirubin": ["mg/dL", "µmol/L"],
    "Albumin": ["g/dL", "g/L"],
    "Total Protein": ["g/dL", "g/L"],
    "Globulin": ["g/dL", "g/L"],
    "Free T4": ["ng/dL", "pmol/L"],
    "Total T4": ["µg/dL", "nmol/L"],
    "Free T3": ["pg/mL", "pmol/L"],
    "Total T3": ["ng/dL", "nmol/L"],
    "Iron": ["µg/dL", "µmol/L"],
    "TIBC": ["µg/dL", "µmol/L"],
    "Lactate": ["mmol/L", "mg/dL"],
    "Hemoglobin": ["g/dL", "g/L"],
    "MCHC": ["g/dL", "g/L"],
    "Transferrin": ["mg/dL", "g/L"],
    "Ferritin": ["ng/mL", "µg/L"],
    "Vitamin B12": ["pg/mL", "pmol/L"],
    "Folate": ["ng/mL", "nmol/L"],
    "25-OH Vitamin D": ["ng/mL", "nmol/L"],
    "TSH": ["mIU/L", "µIU/mL"],
    "Prolactin": ["ng/mL", "µg/L"],
    "PSA Total": ["ng/mL", "µg/L"],
    "PSA Free": ["ng/mL", "µg/L"],
    "CEA": ["ng/mL", "µg/L"],
    "AFP": ["ng/mL", "µg/L"],
    "Beta-hCG": ["mIU/mL", "IU/L"],
    "WBC": ["10^3/µL", "10^9/L"],
    "RBC": ["10^6/µL", "10^12/L"],
    "Platelets": ["10^3/µL", "10^9/L"],
    "Hematocrit": ["%", "L/L"],
    "IgG": ["mg/dL", "g/L"],
    "IgA": ["mg/dL", "g/L"],
    "IgM": ["mg/dL", "g/L"],
    "C3": ["mg/dL", "g/L"],
    "C4": ["mg/dL", "g/L"],
    "Lipoprotein(a)": ["mg/dL", "nmol/L"],
    "HbA1c": ["%", "mmol/mol"],
}

ALIASES = {
    "fbs": "glucose",
    "fasting blood glucose": "glucose",
    "fasting glucose": "glucose",
    "tg": "triglycerides",
    "triglyceride": "triglycerides",
    "creat": "creatinine",
    "urate": "uric acid",
    "chol": "total cholesterol",
    "tchol": "total cholesterol",
    "ca": "calcium",
    "phosphate": "phosphorus",
    "tbil": "total bilirubin",
    "dbil": "direct bilirubin",
    "ibil": "indirect bilirubin",
    "ft4": "free t4",
    "tt4": "total t4",
    "ft3": "free t3",
    "tt3": "total t3",
    "hba1c": "hba1c",
}


def normalize_analyte(analyte):
    name = str(analyte or "").strip().casefold()
    return ALIASES.get(name, name)


def list_analytes():
    return sorted(ANALYTE_UNITS.keys())


def units_for_analyte(analyte):
    """Return only the explicitly configured units for an analyte."""
    name = str(analyte or "").strip()
    return list(ANALYTE_UNITS.get(name, []))


def list_general_units():
    """Units available in analyte-independent conversion mode."""
    return list(GENERAL_UNITS)


def list_conversions():
    pairs = set(GENERAL_FACTORS)
    for factors in ANALYTE_FACTORS.values():
        pairs.update(factors)
    pairs.update(TEMPERATURE_PAIRS)
    pairs.update({("%", "mmol/mol"), ("mmol/mol", "%")})
    return sorted(pairs)


def convert(value, source_unit, target_unit, analyte=None):
    try:
        value = float(value)
    except (ValueError, TypeError):
        return None

    source_unit = str(source_unit or "").strip()
    target_unit = str(target_unit or "").strip()

    if not source_unit or not target_unit:
        return None

    if source_unit == target_unit:
        return value

    pair = (source_unit, target_unit)

    if pair == ("°C", "°F"):
        return value * 9 / 5 + 32

    if pair == ("°F", "°C"):
        return (value - 32) * 5 / 9

    name = normalize_analyte(analyte)

    # NGSP (%) = 0.09148 * IFCC (mmol/mol) + 2.152
    if name == "hba1c":
        if pair == ("%", "mmol/mol"):
            return (value - 2.152) / 0.09148
        if pair == ("mmol/mol", "%"):
            return 0.09148 * value + 2.152

    # General conversion is allowed without choosing a test.
    if pair in GENERAL_FACTORS:
        return value * GENERAL_FACTORS[pair]

    # Molecular-weight-dependent conversions require a matching analyte.
    factors = ANALYTE_FACTORS.get(name)
    if not factors:
        return None

    factor = factors.get(pair)
    if factor is None:
        return None

    return value * factor
