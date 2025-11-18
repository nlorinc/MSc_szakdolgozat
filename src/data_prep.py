# src/data_prep.py
import pandas as pd
import re
from pathlib import Path

def split_author_ids(cell):
    if pd.isna(cell):
        return []
    parts = re.split(r"\s*\|\s*", str(cell).strip())
    return [p.strip() for p in parts if p.strip()]



def detect_header_index(path: str) -> int:
    """Az első olyan sor indexét adja vissza, ahol az első cella 'Title'."""
    tmp = pd.read_excel(path, header=None)
    for i in range(len(tmp)):
        if str(tmp.iloc[i, 0]).strip() == "Title":
            return i
    raise ValueError(f"Nincs 'Title' az első oszlopban ebben a fájlban: {path}")