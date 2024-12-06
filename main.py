from funciones.mostrar_menu import mostrar_menu
from funciones.cargar_pacientes import cargar_pacientes
from funciones.mostrar_paciente import mostrar_pacientes
from funciones.buscar_paciente import buscar_paciente
from funciones.ordenar_pacientes import ordenar_pacientes
from funciones.paciente_mayor_dias import paciente_con_mayor_dias
from funciones.paciente_menor_dias import pacientes_con_menos_dias
from funciones.internacion_mayor_5_dias import internacion_5_dias
from funciones.promedio_dias import promedio_dias_internacion
from funciones.salir import salir

def main():
    """
    funcion principal que coordina la ejecucion del programa.
    """
    print ("bienvenidos al sistema de gestion de pacientes de la clinica 'la fuerza'")

    # lista inicial de pacientes
    pacientes = []

    while True:
        opcion = mostrar_menu()

        if opcion == "1":
                #Carga pacientes
                cargar_pacientes (pacientes)
        elif opcion == "2":

                mostrar_pacientes(pacientes)
        elif opcion == "3":
                # busqueda de pacientes
                buscar_paciente(pacientes)
        elif opcion == "4":
                if pacientes:
                       ordenar_pacientes(pacientes)
                else:
                       print("no hay pacientes registrados para ordenar.")
            
        elif opcion == "5":
                if pacientes:
                    paciente_con_mayor_dias(pacientes)
                else: 
                       print("no hay pacientes registrados.")
        elif opcion == "6":
            if pacientes:
                   pacientes_con_menos_dias(pacientes)
            else:
                   
                   print("no hay pacientes registrados.")
        elif opcion == "7":
                # cantidad paciente con dias mayor a 5
                internacion_5_dias(pacientes)
        elif opcion == "8":
                #promedio de dias
                promedio_dias_internacion(pacientes)
        elif opcion == "9":
                # sale del sistema
                salir()
        else:
            print("opcion invalida. Seleccione una opcion del menu: ")


if __name__ == "__main__":
       main()