from flask import Flask, jsonify
app = Flask(__name__)

import mysql.connector

conexion = mysql.connector.connect(
    user="adrian",
    password="12345",
    database="casas"
)

cursor = conexion.cursor()

@app.route("/api/v1/casas/")
def hello():
    query = "SELECT bienraiz.id, titulo, precio, m2, rooms, baths, cars, " \
    "descripcion, colonia.nombre, municipio.nombre FROM bienraiz " \
    "LEFT JOIN colonia ON bienraiz.id_colonia = colonia.id " \
    "LEFT JOIN municipio ON municipio.id = colonia.id_municipio ORDER BY precio DESC"

    q_imagenes = "SELECT ubicacion FROM imagen WHERE id_bienraiz=%s"

    cursor.execute(query)
    casas = cursor.fetchall()
    lista_casas = []
    for casa in casas:
        cursor.execute(q_imagenes, (casa[0], ))
        imagenes = cursor.fetchall()
        c = {
            "id": casa[0],
            "titulo": casa[1],
            "precio": casa[2],
            "m2": casa[3],
            "rooms": casa[4],
            "baths": casa[5],
            "cars": casa[6],
            "descripcion": casa[7],
            "colonia": casa[8],
            "imagenes": imagenes,
            "municipio": casa[9]
        }
        lista_casas.append(c)
    return jsonify(lista_casas)



app.run()


#@app.route("/")
#def prueba():
    #return "Hello world2"