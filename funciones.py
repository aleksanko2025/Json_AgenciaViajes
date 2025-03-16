import json
with open("agencia_viajes.json") as fichero: #Abrimos el fichero json
    datos = json.load(fichero)

def listar_paquetes():
    contador = 0
    for paquete in datos["paquetes_viaje"]:
        contador += 1
        ciudad = paquete["destino"]["ciudad"]
        pais = paquete["destino"]["país"]
        duracion = paquete["duración"]
        print(f"""
Paquete {contador}
Ciudad --> {ciudad}
Pais --> {pais}
Duración --> {duracion}""")

def opiniones_puntuacion():
    opiniones = []
    for paquete in datos["paquetes_viaje"]:
        for opinion in paquete["opiniones"]:
            if opinion["puntuación"] < 4:
                opiniones.append(opinion)
    print(f"Opiniones con puntación por debajo del 4 --> Hay {len(opiniones)} opiniones")
    for elemento in opiniones:
        nombre = elemento["nombre"]
        comentario = elemento["comentario"]
        puntuacion = elemento["puntuación"]
        print(f"Nombre: {nombre}, Comentario: {comentario} Puntuación: {puntuacion}")