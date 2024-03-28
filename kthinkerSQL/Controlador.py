from tkinter import messagebox
import sqlite3
import bcrypt

class Controlador:
    
    def conexion(self):
        try:
            conex=sqlite3.connect("/Users/Admin/Documents/GitHub/195POO/kthinkerSQL/tbUsuarios.db")
            print("Conectado")
            return conex
        except sqlite3.OperationalError:
            print("No se pudo conectar")
            
    def encriptapass(self,cont):
        passPlana=cont
        passPlana= passPlana.encode()
        sal= bcrypt.gensalt()
        passHash= bcrypt.hashpw(passPlana, sal)
        
        return passHash
    
    def insertUsuario(self,nom,corr,cont):
        
        conexion= self.conexion()
        
        if( nom==""or corr=="" or cont==""):
            messagebox.showwarning("cuidado","inputs vacios menso!")
            conexion.close()
            
        else:
            cursor = conexion.cursor()
            conH= self.encriptapass(cont)
            datos=(nom,corr,conH)
            sqlInsert="insert into tbUsuarios(nombre,correo,contra)values(?,?,?)"
            
            cursor.execute(sqlInsert,datos)
            conexion.commit()
            conexion.close()
            messagebox.showinfo("exito tilin","eso tilin")
            
    def buscarUsuario(self, id):
        conexion = self.conexion()
        if(id==""):
            messagebox.showwarning("cuidado","input vacio")
            conexion.close()
        else:
            try:
                cursor = conexion.cursor()
                sqlSelect="SELECT * FROM tbUsuarios WHERE id="+id
                cursor.execute(sqlSelect)
                usuario = cursor.fetchall()
                conexion.close()
                return usuario
            except sqlite3.OperationalError:
                print("no se pudo ejecutar la busqueda")
                
    def consultarTodosUsuarios(self):
        conexion = self.conexion()
        try:
            cursor = conexion.cursor()
            sqlSelect = "SELECT * FROM tbUsuarios"
            cursor.execute(sqlSelect)
            usuarios = cursor.fetchall()
            conexion.close()
            return usuarios
        except sqlite3.OperationalError:
            print("no se ejecuto la operacion")
            