import numpy as np

# Constants (example values; adjust based on real conditions)
FARADAY_CONSTANT = 96485  # Faraday constant (C/mol e-)
CATALYST_EFFICIENCIES = {
    "CO": 0.8,
    "HCOO-": 0.7,
    "CH3OH": 0.6,
    "CH4": 0.4,
    "H2": 0.5,
    "H2O": 0.3,
    "O2": 0.3,
    "HCHO": 0.2,
    "C2H4": 0.1,
    "C2H5OH": 0.1,
    "CO3^2-": 0.1,
}

# Define the reactions and their stoichiometries
REACTIONS = {
    "CO": {"e-": 2, "H+": 2, "products": {"CO": 1, "H2O": 1}},
    "HCOO-": {"e-": 2, "H+": 2, "products": {"HCOO-": 1}},
    "CH3OH": {"e-": 6, "H+": 6, "products": {"CH3OH": 1, "H2O": 1}},
    "CH4": {"e-": 8, "H+": 8, "products": {"CH4": 1, "H2O": 2}},
    "H2": {"e-": 2, "H+": 2, "products": {"H2": 1}},
    "H2O": {"e-": 1, "H+": 1, "products": {"H2": 0.5, "OH-": 1}},
    "O2": {"e-": 4, "H2O": 2, "products": {"O2": 1, "H+": 4}},
    "HCHO": {"e-": 4, "H+": 4, "products": {"HCHO": 1, "H2O": 1}},
    "C2H4": {"e-": 12, "H+": 12, "products": {"C2H4": 1, "H2O": 4}},
    "C2H5OH": {"e-": 12, "H+": 12, "products": {"C2H5OH": 1, "H2O": 3}},
    "CO3^2-": {"e-": 0, "H+": 0, "products": {"HCO3-": 1, "CO3^2-": 1}},
}


def simulate_reactions(current, time, catalyst):
    """
    Simulates the reactions occurring during the experiment.

    Parameters:
    - current (float): Applied current in amperes.
    - time (float): Duration of the experiment in seconds.
    - catalyst (str): Catalyst type (e.g., 'Cu', 'Ag', 'Sn').

    Returns:
    - results (dict): Reaction product distributions and rates.
    """
    total_charge = current * time  # Total charge passed (C)
    total_moles_electrons = total_charge / FARADAY_CONSTANT

    results = {}
    for reaction, data in REACTIONS.items():
        e_moles = data["e-"]
        if e_moles == 0:
            continue

        max_moles = total_moles_electrons / e_moles
        efficiency = CATALYST_EFFICIENCIES.get(reaction, 0.1)
        catalyst_factor = efficiency if catalyst in ["Cu", "Au", "Sn"] else 0.1
        actual_moles = max_moles * catalyst_factor

        results[reaction] = {
            "moles": actual_moles,
            "products": {k: v * actual_moles for k, v in data["products"].items()},
        }

    return results
