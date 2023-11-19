from pathlib import Path
from os import listdir
from importlib import import_module


path_parent = Path("./app/rutas")

for modulo in listdir(path_parent):
    if "ruta" in modulo:
        import_module(f"app.rutas.{modulo[:-3]}")