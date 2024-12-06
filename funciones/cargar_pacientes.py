def cargar_pacientes (pacientes: list) -> None:
    try:
        cantidad = int(input("ingrese la cantidad de pacientes que desea ingresar: "))
        if cantidad <= 0:
            print ("la cantidad debe ser mayor que 0.")
            return
    except ValueError:
        print("por favor ingrese un numero valido para la cantidad de pacientes.")
        return

    for i in range(cantidad):
        historia_clinica = int(input("ingrese el numero de historia clinica: "))
        nombre = input ("ingrese el nombre: ")

        while True: 
            try:
                edad = int(input("ingrese la edad del paciente: "))
                dias_internacion = int(input("ingrese los dias de internacion: "))
                if edad <= 0 or dias_internacion <0:
                    print("debe ser mayor que 0")
                    continue
                break
            except ValueError:
                print("por favor ingrese valores validos para edad y dias de internacion.")

        diagnostico = input("ingrese el diagnostico: ")
        
        
        pacientes.append([historia_clinica, nombre, edad, dias_internacion, diagnostico])

        print(f"paciente {i + 1} cargado: historial clinica: {historia_clinica}, nombre: {nombre}, edad: {edad}, diagnostico: {diagnostico}")
