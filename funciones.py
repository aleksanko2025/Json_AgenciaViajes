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
