from datetime import date

from Modelo.Pedido import Pedido

p = Pedido('Bruno', '1234')


def test_novo_pedido():
    assert p.nome == 'Bruno'


def test_modificar():
    p.modificar('Mario', 'Em andamento')
    assert p.nome == 'Mario'


def test_data_abertura():
    assert p.data_abertura.day == date.today().day
