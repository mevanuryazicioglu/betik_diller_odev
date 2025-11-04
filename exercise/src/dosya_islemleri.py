from pathlib import Path
from .dekorator import timer
import csv, json

@timer
def read_csv(path):
    with Path(path).open("r", encoding="utf-8", newline="") as f:
        rows = list(csv.DictReader(f))
        return rows

@timer
def write_json(path, obj):
    with Path(path).open("w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=4)

@timer
def write_text(path, text):
    Path(path).write_text(text, encoding="utf-8")
