from calendar import c
from cmath import pi
from doctest import OutputChecker
from flask import Flask, request
import csv
import json

app = Flask(__name__)

@app.route('/listado_estudiantes')
def listado_estudiantes():
    with open('datos\estudiante.csv') as archivo:
        reader = csv.reader(archivo)
        next(reader)
        listado_estudiante = []
        for fila in reader:
            listado_estudiante.append({'cedula': fila[0],'primer_apellido': fila[1],'segundo_apellido': fila[2],'primer_nombre': fila[3],'segundo_nombre': fila[4]})
    return json.dumps(sorted(listado_estudiante, key=lambda a: a['primer_nombre']))

@app.route('/registro_asistencia_del_estudiante', methods=['POST'])
def registro_asistencia_del_estudiante():
    
    with open('datos\datos_asistencia.csv', 'a' , newline='') as archivo:
        escritor = csv.writer(archivo,delimiter=',')
        escritor.writerow([request.json['cedula'],request.json['materia'],request.json['fecha_anio'],request.json['fecha_mes'],request.json['fecha_dia']])
    return 'creado'

@app.route('/eliminar_asistencia_por_cedula/<cedula>', methods=['DELETE'])
def eliminar_asistencia_por_cedula(cedula):
    with open('datos\datos_asistencia.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        listado_estudiante = []
        for columna in reader:
            if columna[0] != cedula:
                listado_estudiante.append(columna)
    with open('datos\datos_asistencia.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(listado_estudiante)
    return 'asistencias eliminada'

if __name__ == '__main__':
    app.run(debug=True)