def buscar_paciente(pacientes: list) -> None:
    if not pacientes:
        print("no hay pacientes registrados.")
        return
    
    historia_clinica = int(input("ingrese el numero de historia clinica: "))

    for paciente in pacientes:
        if paciente[0] == historia_clinica:
            print(f"paciente encontrado: historia clinica: {paciente[0]}, nombre: {paciente[1]}, edad: {paciente[2]}, dias de internacion: {paciente[3]}, diagnostico: {paciente[4]}")
            return
        
    print("paciente no encontrado.")