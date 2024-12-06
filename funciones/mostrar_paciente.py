def mostrar_pacientes(pacientes: list) -> None:
      
      if not pacientes:
            print("no hay pacientes registrados.")
            return
      
      print("lista de pacientes: ")
      for paciente in pacientes:
            print(f"historia clinica: {paciente[0]}, nombre: {paciente[1]}, edad: {paciente[2]} dias de internacion: {paciente[3]}, diagnostico: {paciente[4]}")
            
