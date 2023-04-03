from persona import Persona

class Familia:
    __miembros : list
    
    def __init__(self) -> None:
        self.__miembros = []
        
    @property
    def miembros(self):
        return self.__miembros

    @miembros.setter
    def miembros(self, value:list):
        self.miembros = value.copy()
    
    def agregar_miemrbro(self, miembro : Persona) -> None:
        self.miembros.append(miembro)
    
    def listar_miembros(self) -> None:
        for miembro in self.miembros:
            print(f"{miembro.nombre} {miembro.apellidos} con {miembro.edad} años pertenece a la familia.")