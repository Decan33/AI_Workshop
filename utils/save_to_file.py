import os
import numpy as np
from mp_api.client import MPRester
import pandas as pd

API_KEY = os.getenv("API_KEY")

fields_to_fetch = [
    "formula_pretty",
    "material_id",
    "nelements",
    "efermi",
    "spacegroup_number",
    "spacegroup_symbol",
    "energy_per_atom",
    "formation_energy_per_atom",
    "formation_energy",
    "energy_above_hull",
    "is_magnetic",
    "ordering",
    "total_magnetization",
    "total_magnetization_normalized_vol",
    "band_gap",
    "volume",
    "density",
    "density_atomic",
    "deprecated",
    "uncorrected_energy_per_atom",
    "formation_energy_per_atom",
    "is_metal",
    "is_gap_direct",
    "num_magnetic_sites",
    "uncorrected_energy_per_atom",
    "structure",
]

with MPRester(API_KEY, use_document_model=False) as mpr:
    docs = mpr.summary.search(fields=fields_to_fetch, num_elements=(0, 3))

additional_data = []
for doc in docs:
    structure = doc["structure"]
    atomic_numbers = [site.specie.number for site in structure.sites]
    lattice = structure.lattice
    distance_matrix = structure.distance_matrix

    additional_data.append(
        {
            "material_id": doc["material_id"],
            "mean_atomic_numbers": np.mean(atomic_numbers),
            "max_atomic_numbers": np.max(atomic_numbers),
            "min_atomic_numbers": np.min(atomic_numbers),
            "std_atomic_numbers": np.std(atomic_numbers),
            "a_parameters": lattice.a,
            "b_parameters": lattice.b,
            "c_parameters": lattice.c,
            "alpha_parameters": lattice.alpha,
            "beta_parameters": lattice.beta,
            "gamma_parameters": lattice.gamma,
            "mean_distance_matrix": np.mean(distance_matrix),
            "max_distance_matrix": np.max(distance_matrix),
            "min_distance_matrix": np.min(distance_matrix),
            "std_distance_matrix": np.std(distance_matrix),
        }
    )

additional_df = pd.DataFrame(additional_data)

df = pd.DataFrame(docs)

df = df[df["deprecated"] == False]
df = df.drop(columns=["deprecated"])
df = df.drop(columns=["structure"])

df = df.dropna()

df = df.merge(additional_df, on="material_id")

df.to_csv("materials.csv")
