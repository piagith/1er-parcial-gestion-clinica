def mostrar_menu () -> str:
    print ('''mostramos menu de opciones:
           1. Cargar pacientes
           2. Mostrar lista de pacientes
           3. Busqueda de pacientes
           4. Ordenamiento de pacientes
           5. Paciente con mayor cantidad de dias de internacion
           6. Paciente con menor cantidad de dias de internacion
           7. cantidad de pacientes con dias de internacion mayor a 5 dias.
           8. Mostrar promedio de dias de internacion.
           9. Salir del sistema.
           ''')
    opcion = input ("seleccione una opcion: ")
    return opcion