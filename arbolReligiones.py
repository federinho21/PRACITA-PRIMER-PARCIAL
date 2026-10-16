from Religion import Religion
class arbolReligiones:
    def __init__(self):
        self._religiones = []


    def buscar(self,nombre):
        for religion in self._religiones:
            if religion.nombre.lower() == nombre.strip().lower():
                return religion   
        return None



    def agregar_religion(self, religion):
        if not isinstance(religion, Religion):
            raise ValueError("El objeto debe ser una instancia de la clase Religion.")


        if self.buscar(religion.nombre) is not None:
            raise ValueError(f"La religión '{religion.nombre}' ya existe en el árbol.")

        self._religiones.append(religion)


    def listar_religiones(self):
        for religion in self._religiones:
            print(religion.nombre)