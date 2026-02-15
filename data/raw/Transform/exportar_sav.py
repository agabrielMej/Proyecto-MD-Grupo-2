import pyreadstat
import pandas as pd

# el spss nombre 
df, meta = pyreadstat.read_sav("data/raw/2022evaluaciones.sav")


print("Filas:", df.shape[0])
print("Columnas:", df.shape[1])

# SPSS a csv para usar en python 
df.to_csv("data/raw/Transform/evaluaciones_2022.csv", index=False, encoding="utf-8-sig")
print("arrchivo creado ")
