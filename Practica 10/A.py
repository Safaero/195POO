class User:
    
    def _init_(self,nomb,corr,cont,id,apep,apem);
        self._nombre = nomb
        self._correo = corr
        self._contra = cont
        self._id = id
        self._apellidoP = apep
        self._apellidoM = apem
        
    #getters & setters
    def getnombre(self):
        return self._nombre
    def getcorreo(self):
        return self._correo
    def getcontra(self):
        return self._contra
    def getid(self):
        return self._id
    def getapep(self):
        return self._apellidoP
    def getapem (self):
        return self._apellidoM
    
    