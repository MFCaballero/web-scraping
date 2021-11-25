import sqlite3

#BASE DE DATOS SUAC
class ConnectionDB:

    def DBSuac(self):
        conexion = self.abrir()
        try:
            conexion.execute("""create table dbsuac (
                              sticker text,
                              inicio text,
                              tipo text,
                              subtipo text,
                              reparticion text,
                              asunto text,
                              folios text,
                              cuerpos text,
                              origen text,
                              iniciador text,
                              calle text,
                              altura text,
                              barrio text,
                              departamento text,
                              localidad text,
                              provincia text
                            )""")
            print("se creo la tabla dbsuac")                        
        except sqlite3.OperationalError: 
            print("La tabla dbsuac ya existe") 
    
    def abrir(self):
        conexion = sqlite3.connect("BaseDeDatos.db")
        return conexion 


    def carga_info(self, datos):
        cone = self.abrir() 
        cursor = cone.cursor() 
        sql = "insert into dbsuac(sticker, inicio, tipo, subtipo, reparticion, asunto, folios, cuerpos, origen, iniciador, calle, altura, barrio, departamento, localidad, provincia) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)" 
        cursor.execute(sql, datos) 
        cone.commit() 
        cone.close() 



    
#BASE DE DATOS PRESTAMOS
class ConnectionDB2:

    def DBHojadeRuta(self):
        conexion = self.abrir()
        try:
            conexion.execute("""create table hojaderuta (
                              sticker text,
                              unidad text,
                              ingreso text,
                              egreso text,
                              folios text,
                              cuerpos text
                            )""")
            print("se creo la tabla hojaderuta")                        
        except sqlite3.OperationalError: 
            print("La tabla hojaderuta ya existe") 
    
    
    def abrir(self):
        conexion = sqlite3.connect("BaseDeDatos2.db")
        return conexion 

    def carga_hdr(self, datos):
        cone = self.abrir() 
        cursor = cone.cursor() 
        sql = "insert into hojaderuta(sticker, unidad, ingreso, egreso, folios, cuerpos) values (?,?,?,?,?,?)" 
        cursor.execute(sql, datos) 
        cone.commit() 
        cone.close() 

    def consulta(self, datos):
        try:
            cone = self.abrir()
            cursor = cone.cursor()
            sql = "select unidad, ingreso, egreso, folios, cuerpos from hojaderuta where sticker=?"
            cursor.execute(sql, datos)
            return cursor.fetchall() 
        finally: 
            cone.close()

    
class ConnectionDB3:

    def DBSuac2(self):
        conexion = self.abrir()
        try:
            conexion.execute("""create table dbsuac2 (
                              sticker text,
                              inicio text,
                              tipo text,
                              subtipo text,
                              reparticion text,
                              asunto text,
                              folios text,
                              cuerpos text,
                              origen text,
                              iniciador text,
                              documento text,
                              sexo text,
                              calle text,
                              altura text,
                              barrio text,
                              departamento text,
                              localidad text,
                              provincia text
                            )""")
            print("se creo la tabla dbsuac2")                        
        except sqlite3.OperationalError: 
            print("La tabla dbsuac2 ya existe") 
    
    def abrir(self):
        conexion = sqlite3.connect("BaseDeDatos3.db")
        return conexion 


    def carga_info(self, datos):
        cone = self.abrir() 
        cursor = cone.cursor() 
        sql = "insert into dbsuac2(sticker, inicio, tipo, subtipo, reparticion, asunto, folios, cuerpos, origen, iniciador, documento, sexo, calle, altura, barrio, departamento, localidad, provincia) values (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)" 
        cursor.execute(sql, datos) 
        cone.commit() 
        cone.close() 

