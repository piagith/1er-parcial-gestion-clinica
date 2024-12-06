def internacion_5_dias (pacientes: list) -> None:
    if not pacientes:
        print("no hay pacientes registrados.")
        return
    
    pacientes_mas_5_dias = [paciente for paciente in pacientes if paciente[3] > 5]
    print(f"la cantidad de pacientes con dias de internacion mayor a 5 dias es: {len(pacientes_mas_5_dias)}")
