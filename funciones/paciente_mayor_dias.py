def paciente_con_mayor_dias(pacientes: list) -> int:
    if not pacientes:
        print("no hay pacientes registrados.")
        return
    
    mayor = pacientes[0]
    for paciente in pacientes:
        if paciente[3] > mayor[3]:
            mayor = paciente
    
    print(f"paciente con mas dias de internacion: historia clinica {mayor[0]}, nombre: {mayor[1]}, edad: {mayor[2]}, dias de internacion: {mayor[3]}, diagnostico: {mayor[4]} ")
