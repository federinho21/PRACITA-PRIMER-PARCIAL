class Religion:
    def __init__(self, nombre,deidad,anio_origen=none,lugar_origen=none):
        self.nombre = nombre
        self.deidad = deidad
        self.anio_origen = anio_origen
        self.lugar_origen = lugar_origen


    @property
    def nombre(self):
        return self._nombre  


    @nombre.setter
    def nombre(self, value):
        if not isinstance(value, str):
            raise ValueError("El nombre debe ser una cadena de texto.")
        self._nombre = value   


    @property
    def anio_origen(self):
        return self._anio_origen

    @anio_origen.setter
    def anio_origen(self, value):
        if value is not None and not isinstance(value, int):
            raise ValueError("El año de origen debe ser un número entero.")
        self._anio_origen = value    
   