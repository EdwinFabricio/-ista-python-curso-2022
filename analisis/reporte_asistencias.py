import pandas as pd
import matplotlib.pyplot as plt
import csv

datosestudiante = pd.read_csv('datos\estudiante.csv')

print('ESTUDIANTES')
print(datosestudiante)

datosestu1 = pd.read_csv('datos\datos_asistencia.csv')

print('ASISTENCIAS')
print(datosestu1)

estudent = pd.merge(datosestudiante,datosestu1, how='right')
print(estudent)

print('ESTUDIANTES POR CEDULA = 1123457897')
print(estudent[estudent.cedula == 1123457897])

estudent[estudent.cedula == 1123457897].to_csv('datos\datos_reporte_1123457897.csv', index=True)

estudent[estudent.cedula == 1123457897]['fecha_dia'].value_counts().plot(kind='bar')

plt.show()

