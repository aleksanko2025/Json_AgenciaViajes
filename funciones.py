import json
with open("agencia_viajes.json") as fichero: #Abrimos el fichero json
    datos = json.load(fichero)

def listar_paquetes():
    contador = 0
    print("Podemos ofrecer los siguientes viajes: ")
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

def buscar_valoraciones():
    valoraciones = []
    bandera = False
    while bandera == False:
        quest = input("Indique destino Ciudad/País (Para saber los destinos indique 1): ")
        for paquete in datos["paquetes_viaje"]:
            if quest == "1":                     #Para consultar destinos
                ciudad = paquete["destino"]["ciudad"]
                pais = paquete["destino"]["país"]
                print(f"Ciudad: {ciudad} País: {pais}")
            elif paquete["destino"]["ciudad"] == quest or paquete["destino"]["país"] == quest:
                for comentario in paquete["opiniones"]:
                    valoraciones.append(comentario)
                    bandera = True
    for elemento in valoraciones:                #Reciclamos el código de la función anterior.
        nombre = elemento["nombre"]
        comentario = elemento["comentario"]
        puntuacion = elemento["puntuación"]
        print(f"Nombre: {nombre}, Comentario: {comentario} Puntuación: {puntuacion}")

def presupuesto_destino():
    destino = []
    presupuesto = int(input("Indique su presupuesto para viajar: "))
    for paquete in datos["paquetes_viaje"]:
        if paquete["precio"] <= presupuesto:
            destino.append(paquete["destino"])
    if len(destino) > 0:   #En el caso de que la lista no esté vacía se muestran los resultados, en caso contrario se muestra un mensaje.
        print("Opciones que se ajustan a su presupuesto: ")
        for elemento in destino:
            ciudad = elemento["ciudad"]
            pais = elemento["país"]
            print(f"{ciudad}, {pais}")
    else:               
        print("No hay ningún destino que se ajuste a su presupuesto.")