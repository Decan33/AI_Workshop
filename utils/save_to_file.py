import os
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
]

with MPRester(API_KEY, use_document_model=False) as mpr:
    docs = mpr.summary.search(fields=fields_to_fetch, num_elements=(0, 3))


df = pd.DataFrame(docs)

df = df[df["deprecated"] == False]
df = df.drop(columns=["deprecated"])

df = df.dropna()

df.to_csv("materials.csv")
