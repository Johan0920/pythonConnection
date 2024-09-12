import psycopg2

connection=psycopg2.connect(
    host="localhost",
    port=5432,
    database="TestDB",
    user="postgres",
    password="secret"
 )

class ServicioPersona:
    def __init__(self) -> None:
        self.connection=connection
        
    def obtenerNumeroPersonas(self):
       cursor=self.connection.cursor()
       sql="SELECT * FROM Persona"
       cursor.execute(sql)
       filas=cursor.fetchall()
       cant=len(filas)
       print(f"Cantidad de resgistros consultados son: {cant}")
       for fila in filas:
           print(".")
       cursor.close()
       connection.close()
       
    def insertarPersona(self):
        cursor=self.connection.cursor()
        sql="INSERT INTO Persona (nombre,apellido,estadocivil) VALUES ('Juan Sebastian','Mendez', 'CASADO');"
        cursor.execute(sql)
        connection.commit()
        print("Adición realizada con exito")
        cursor.close()
        connection.close()
        
    def actualizarPersona(self):
        cursor=self.connection.cursor()
        sql="UPDATE Persona SET estadocivil='SOLTERO', apellido='Botero' WHERE id=6"
        cursor.execute(sql)
        connection.commit()
        print("Actualización realizada con exito")
        cursor.close()
        connection.close()
        
    def eliminarPersona(self):
        cursor=self.connection.cursor()
        sql="DELETE FROM Persona WHERE id=6"
        cursor.execute(sql)
        connection.commit()
        print("Eliminación realizada de forma exitosa")
        cursor.close()
        connection.close()
        
    def insertarPersonaConValores(self):
        cursor=self.connection.cursor()
        nombre=input("Digite el nombre de la persona: ")
        apellido=input("Digite el apellido de la persona: ")
        estadoCivil=input("Digite el estado civil de la persona: ")
        sql="INSERT INTO Persona (nombre,apellido,estadocivil) VALUES (%s,%s,%s)"
        cursor.execute(sql,(nombre,apellido,estadoCivil))
        connection.commit()
        print("EL registro fue insertado de forma correcta")
        cursor.close()
        connection.close()
        
    def actualizarPersonaConValores(self,nombre,apellido,estadoCivil,id):
        cursor=self.connection.cursor()
        sql="UPDATE Persona SET nombre=%s, apellido=%s, estadocivil=%s WHERE id=%s;"
        campos=(nombre,apellido,estadoCivil,id)
        cursor.execute(sql,campos)
        connection.commit()
        print("Regitro actualizado de forma exitosa")
        cursor.close()
        connection.close()
        
    def eliminarPersonaConValores(self):
        cursor=self.connection.cursor()
        id=input("Digite el id de la persona a eliminar: ")
        sql="DELETE FROM Persona WHERE id=%s"
        cursor.execute(sql,(id))
        connection.commit()
        print("El registro se eliminó de forma exitosa")
        cursor.close()
        connection.close()
        
    def obtenerPersonasConValores(self):
        cursor=self.connection.cursor()
        sql="SELECT * FROM Persona"
        cursor.execute(sql)
        filas=cursor.fetchall()
        for fila in filas:
            print("ID: ", fila[0])
            print("Nombre: ", fila[1])
            print("Apellido: ", fila[2])
            print("Estado Civil: ", fila[3])
            print("\n")
        cursor.close()
        connection.close()
    