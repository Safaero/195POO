class Personaje:
    
    #atributos de personaje ja
    #poner un guion bajo en el nombre de un atributo lo vuelve privado
    #declaracion del consttructor para crear los objetos
    def __init__(self,esp,nom,alt):
        self.__especie= esp
        self.__nombre= nom
        self.__altura= alt
    
    #metodos del personaje
    def correr(self, estado):
        if(estado): 
            print("el personaje"+ self.nombre +"esta corriendo")
        else: 
            print ("el personaje" + self.nombre + "esta muerto")
            
    def lanzarGranada(self):
        print(self.nombre +"pego una granada")
        
    
