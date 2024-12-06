def pacientes_con_menos_dias(pacientes: list) -> None:
    if not pacientes:
        print("no hay pacientes registrados.")
        return
    
    paciente_menor_dias = pacientes[0]

    for paciente in pacientes:
        if paciente [3] < paciente_menor_dias[3]:
            paciente_menor_dias = paciente
        print(f"paciente con menos dias de internacion: historia clinica: {paciente_menor_dias[0]}, nombre: {paciente_menor_dias[1]}, edad: {paciente_menor_dias[2]}, dias de internacion: {paciente_menor_dias[3]}, diagnostico: {paciente_menor_dias[4]}.")
