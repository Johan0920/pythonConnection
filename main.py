from ServicioPersona import ServicioPersona


if __name__=="__main__":
    servicio=ServicioPersona()
    #servicio.obtenerNumeroPersonas()
    #servicio.insertarPersona()
    #ervicio.actualizarPersona()
    #servicio.eliminarPersona()
    #servicio.insertarPersonaConValores()
    """nombre=input("Digite el nuevo nombre de la persona: ")
    apellido=input("Digite el nuevo apellido de la persona: ")
    estadoCivil=input("Digite el nuevo estado civil de la persona: ")
    id=input("Digite el ID de la persona que se va a modificar: ")
    servicio.actualizarPersonaConValores(nombre,apellido,estadoCivil,id)"""
    #servicio.eliminarPersonaConValores()
    servicio.obtenerPersonasConValores()