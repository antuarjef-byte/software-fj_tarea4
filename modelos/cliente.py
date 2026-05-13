from modelos.entidad import Entidad
from excepciones.excepciones import ClienteInvalidoError


class Cliente(Entidad):

    def __init__(self, id_entidad, nombre, correo):

        super().__init__(id_entidad)

        if not nombre.strip():
            raise ClienteInvalidoError(
                "El nombre no puede estar vacío"
            )

        if "@" not in correo:
            raise ClienteInvalidoError(
                "Correo inválido"
            )

        self.__nombre = nombre
        self.__correo = correo

    @property
    def nombre(self):
        return self.__nombre

    @property
    def correo(self):
        return self.__correo

    def mostrar_info(self):

        return (
            f"Cliente: {self.__nombre} "
            f"- {self.__correo}"
        )
