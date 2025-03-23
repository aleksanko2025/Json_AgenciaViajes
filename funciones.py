import json
with open("agencia_viajes.json") as fichero: #Abrimos el fichero json
    datos = json.load(fichero)

def menu():
    print("""""")

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

def destino_top():
    datos_reserva = [] #Aquí se guardará la información de destino y número de personas por cada reserva en una lista independiente

    for reserva in datos["clientes_con_reserva"]:
        info = [] #En esta lista vamos almacenar el destino y número de personas por cada reserva
        destino = reserva["paquete_reservado"]
        info.append(destino)
        personas = reserva["número_personas"] 
        info.append(personas)
        datos_reserva.append(info) #Insertamos la lista con información en los datos_reserva
    
    ck_destinos = [] #Creamos esta lista para quedarnos con los nombres de destinos reservados sin repetir
    
    for reserva in datos_reserva: #Recorremos la lista datos_reserva para quedarnos con destinos sin repetir
        destino = reserva[0]
        if destino not in ck_destinos: #En el caso de que el nombre de destino no este en la lista lo agregamos
            ck_destinos.append(destino)
    
    cont_reserva = [] 

    for campo in ck_destinos: #Guardamos la cantidad de reservas por destino 
        cont = 0
        for lista in datos_reserva:
            if campo == lista[0]:
                cont += 1
        cont_reserva.append(cont)
    
    cont_personas = [] 

    for campo in ck_destinos: #Guardamos la cantidad de viajeros por destino
        cont = 0
        for lista in datos_reserva:
            if campo == lista[0]:
                cont += lista[1]
        cont_personas.append(cont)
    
    #Para averiguar el destino con más reservas, lo haremos averiguando la posición del número más alto de la lista cont_reservas

    reserva_top = max(cont_reserva) #Averiguamos el numero de reserva más alto
    posicion = cont_reserva.index(reserva_top) #Averiguamos la posicion del número que va a coincidir con los demás datos

    print(f"El destino {ck_destinos[posicion]} es el más reservado: con {cont_reserva[posicion]} reservas y {cont_personas[posicion]} viajeros en total.")