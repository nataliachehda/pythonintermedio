from .connecciondb import Conneccion

def crear_tabla():
    conn = Conneccion()

    sql= '''
        CREATE TABLE IF NOT EXISTS Razas(
        ID INTEGER NOT NULL,
        Nombre VARCHAR(50),
        PRIMARY KEY (ID AUTOINCREMENT)
        );

        CREATE TABLE IF NOT EXISTS Perros(
        ID INTEGER NOT NULL,
        Nombre VARCHAR(150),
        Altura VARCHAR(4),
        Razas INTEGER,
        PRIMARY KEY (ID AUTOINCREMENT),
        FOREIGN KEY (Razas) REFERENCES Razas(ID)
        );
    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass

class Perros():

    def __init__(self, nombre, altura, razas):
        self.nombre = nombre
        self.altura = altura
        self.razas = razas

    def __str__(self):
        return f'Perro[{self.nombre}, {self.altura}, {self.razas}]'

def guardar_perro(perro):
    conn = Conneccion()

    sql= f'''
        INSERT INTO Perros(Nombre, Altura, Razas)
        VALUES('{perro.nombre}', '{perro.altura}', {perro.razas});
    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass

def listar_perros():
    conn = Conneccion()
    listar_perros = []

    sql= '''
        SELECT * FROM Perros as p
        INNER JOIN Razas as g
        ON p.Razas = g.ID;
    '''
    try:
        conn.cursor.execute(sql)
        listar_perros = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_perros
    except:
        pass

def listar_razas():
    conn = Conneccion()
    listar_razas = []
    sql = '''
        SELECT * FROM Razas;
    '''
    try:
        conn.cursor.execute(sql)
        listar_razas = conn.cursor.fetchall()
    except Exception as e:
        print(f"Error al listar razas: {e}")
    finally:
        conn.cerrar_con()
    return listar_razas if listar_razas else []

def editar_perro(perro, id):
    conn = Conneccion()

    sql= f'''
        UPDATE Perros
        SET Nombre = '{perro.nombre}', Altura = '{perro.altura}', Razas = {perro.razas}
        WHERE ID = {id};
    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass

def borrar_perro(id):
    conn = Conneccion()

    sql= f'''
        DELETE FROM Perros
        WHERE ID = {id};
    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except:
        pass