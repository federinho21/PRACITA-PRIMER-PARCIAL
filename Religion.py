class Religion:
    def __init__(self, nombre, deidad=None, anio_origen=None, lugar_origen=None, fundador=None, creencias=None,
                 libros_sagrados=None, descripcion=None):
        self.nombre = nombre
        self.deidad = deidad
        self.anio_origen = anio_origen
        self.lugar_origen = lugar_origen
        self.descripcion = descripcion
        self.fundador = fundador
        self.creencias = creencias if creencias is not None else []
        self.libros_sagrados = libros_sagrados if libros_sagrados is not None else []


    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not isinstance(value, str):
            raise ValueError("El nombre debe ser una cadena de texto.")
        self._nombre = value.strip()  # Eliminar espacios en blanco al inicio y al final

    @property
    def anio_origen(self):
        return self._anio_origen

    @anio_origen.setter
    def anio_origen(self, value):
        if value is not None:
            if type(value) is not int or value == 0:
                raise ValueError("El año debe ser un entero distinto de cero.")
        self._anio_origen = value

    @property
    def deidad(self):
        return self._deidad

    @deidad.setter
    def deidad(self, value):
        if value is not None:
            if not isinstance(value, str) or not value.strip():
                raise ValueError("La deidad debe ser una cadena de texto no vacío.")
            value = value.strip()
        self._deidad = value

    @property
    def lugar_origen(self):
        return self._lugar_origen

    @lugar_origen.setter
    def lugar_origen(self, value):
        if value is not None:
            if not isinstance(value, str) or not value.strip():
                raise ValueError("El lugar de origen debe ser un texto no vacío.")
            value = value.strip()
        self._lugar_origen = value