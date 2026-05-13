from modelos.servicio import Servicio


class ReservaSala(Servicio):

    def __init__(self, nombre, tarifa_base, capacidad):

        super().__init__(nombre, tarifa_base)

        self.capacidad = capacidad

    def calcular_costo(
        self,
        horas=1,
        descuento=0,
        impuesto=0
    ):

        subtotal = self.tarifa_base * horas

        subtotal -= subtotal * descuento

        subtotal += subtotal * impuesto

        return subtotal

    def descripcion(self):

        return (
            f"Sala con capacidad "
            f"para {self.capacidad} personas"
        )


class AlquilerEquipo(Servicio):

    def __init__(
        self,
        nombre,
        tarifa_base,
        tipo_equipo
    ):

        super().__init__(nombre, tarifa_base)

        self.tipo_equipo = tipo_equipo

    def calcular_costo(
        self,
        dias=1,
        descuento=0
    ):

        subtotal = self.tarifa_base * dias

        subtotal -= subtotal * descuento

        return subtotal

    def descripcion(self):

        return (
            f"Alquiler de equipo: "
            f"{self.tipo_equipo}"
        )


class AsesoriaEspecializada(Servicio):

    def __init__(
        self,
        nombre,
        tarifa_base,
        especialista
    ):

        super().__init__(nombre, tarifa_base)

        self.especialista = especialista

    def calcular_costo(
        self,
        horas=1,
        impuesto=0
    ):

        subtotal = self.tarifa_base * horas

        subtotal += subtotal * impuesto

        return subtotal

    def descripcion(self):

        return (
            f"Asesoría con especialista "
            f"{self.especialista}"
        )
