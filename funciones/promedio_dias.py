def promedio_dias_internacion (pacientes : list) -> None:
    if not pacientes:
        print ("no hay pacientes registrados.")
        return

    total_dias = 0

    for paciente in pacientes:
        total_dias += paciente[3]

    promedio = total_dias / len(pacientes)
    print (f"el promedio de dias de internacion es: {promedio:.2f}")

'''
otra forma de hacerlo: 

total_dias = 0
for paciente in pacientes:
    total_dias += paciente[2]

promedio =  total_dias /len(pacientes)
return promedio
'''