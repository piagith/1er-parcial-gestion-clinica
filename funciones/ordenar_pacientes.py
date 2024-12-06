def ordenar_pacientes(pacientes: list) -> None:
    if not pacientes:
        print("no hay pacientes registrados.")
        return
    
    pacientes.sort(key=lambda paciente: paciente[0])
    print("pacientes ordenados por numero de historia clinica.")