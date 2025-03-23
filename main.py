from funciones import *

bandera = False

while bandera != True:
    menu()
    opciones = [1, 2, 3, 4, 5, 6]
    opcion = int(input("Indique la opción para elegir: "))

    if opcion == 1:
        listar_paquetes()
        continuar = input("\n Presiones 'Enter' para continuar ")
    if opcion == 2:
        opiniones_puntuacion()
        continuar = input("\n Presiones 'Enter' para continuar ")
    if opcion == 3:
        buscar_valoraciones()
        continuar = input("\n Presiones 'Enter' para continuar ")
    if opcion == 4:
        presupuesto_destino()
        continuar = input("\n Presiones 'Enter' para continuar ")
    if opcion == 5:
        destino_top()
        continuar = input("\n Presiones 'Enter' para continuar ")
    if opcion not in opciones:
        print("Opción no existe, pruebe de nuevo.")
        continuar = input("\n Presiones 'Enter' para continuar ")
    if opcion == 6:
        bandera = True

print("Programa terminado")