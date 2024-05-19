import os
from mp_api.client import MPRester
import pandas as pd

API_KEY = os.getenv("API_KEY")

fields_to_fetch = [
    "formula_pretty",
    "material_id",
    "nelements",
    "efermi",
    "energy_per_atom",
    "formation_energy_per_atom",
    "formation_energy",
    "energy_above_hull",
    "is_magnetic",
    "ordering",
    "total_magnetization",
    "total_magnetization_normalized_vol",
    "spacegroup_number",
    "spacegroup_symbol",
    "magnetic_ordering",
    "band_gap",
]

with MPRester(API_KEY, use_document_model=False) as mpr:
    docs = mpr.materials.summary.search(fields=fields_to_fetch, num_elements=(0, 3))

df = pd.DataFrame(docs)

df.to_csv("materials.csv")
