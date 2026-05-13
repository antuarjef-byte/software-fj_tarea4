from modelos.cliente import Cliente

from modelos.servicios_especializados import (
    ReservaSala,
    AlquilerEquipo,
    AsesoriaEspecializada
)

from modelos.reserva import Reserva

from excepciones.excepciones import (
    ClienteInvalidoError,
    ReservaError
)

from utilidades.logger import registrar_log


clientes = []
reservas = []


print("\n===== SOFTWARE FJ =====\n")


# OPERACIÓN 1
try:

    cliente1 = Cliente(
        1,
        "Luis",
        "luis@gmail.com"
    )

    clientes.append(cliente1)

    print(cliente1.mostrar_info())

except ClienteInvalidoError as e:

    registrar_log(str(e))

    print(e)


# OPERACIÓN 2
try:

    cliente2 = Cliente(
        2,
        "",
        "correo_invalido"
    )

    clientes.append(cliente2)

except ClienteInvalidoError as e:

    registrar_log(str(e))

    print(e)


# OPERACIÓN 3
try:

    sala = ReservaSala(
        "Sala Ejecutiva",
        100,
        20
    )

    print(sala.descripcion())

except Exception as e:

    registrar_log(str(e))


# OPERACIÓN 4
try:

    equipo = AlquilerEquipo(
        "Laptop Gamer",
        80,
        "Laptop"
    )

    print(equipo.descripcion())

except Exception as e:

    registrar_log(str(e))


# OPERACIÓN 5
try:

    asesoria = AsesoriaEspecializada(
        "Asesoría Python",
        150,
        "Carlos Pérez"
    )

    print(asesoria.descripcion())

except Exception as e:

    registrar_log(str(e))


# OPERACIÓN 6
try:

    reserva1 = Reserva(
        cliente1,
        sala,
        3
    )

    reserva1.procesar()

    reservas.append(reserva1)

    print(
        "Reserva confirmada:",
        reserva1.estado
    )

except ReservaError as e:

    registrar_log(str(e))

    print(e)


# OPERACIÓN 7
try:

    reserva2 = Reserva(
        cliente1,
        equipo,
        -2
    )

    reserva2.procesar()

except ReservaError as e:

    registrar_log(str(e))

    print(e)


# OPERACIÓN 8
try:

    costo = sala.calcular_costo(
        horas=5,
        descuento=0.10,
        impuesto=0.19
    )

    print("Costo sala:", costo)

except Exception as e:

    registrar_log(str(e))


# OPERACIÓN 9
try:

    costo_equipo = equipo.calcular_costo(
        dias=4,
        descuento=0.05
    )

    print(
        "Costo equipo:",
        costo_equipo
    )

except Exception as e:

    registrar_log(str(e))


# OPERACIÓN 10
try:

    costo_asesoria = asesoria.calcular_costo(
        horas=2,
        impuesto=0.19
    )

    print(
        "Costo asesoría:",
        costo_asesoria
    )

except Exception as e:

    registrar_log(str(e))

finally:

    print("\nSistema finalizado correctamente")
