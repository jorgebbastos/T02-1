import pytest
from calculadora import calcular_total


def test_total_sem_desconto():
    itens = [(10.0, 2), (5.0, 1)]
    assert calcular_total(itens) == 25.0


def test_total_com_dez_por_cento_de_desconto():
    itens = [(100.0, 2), (50.0, 1)]
    assert calcular_total(itens, desconto_percentual=10) == 225.0


def test_desconto_invalido():
    with pytest.raises(ValueError):
        calcular_total([(100.0, 1)], desconto_percentual=110)


def test_cupom_valido():
    itens = [(100.0, 1)]
    assert calcular_total(itens, cupom="vale10") == 90.0


def test_cupom_vazio():
    itens = [(100.0, 1)]
    assert calcular_total(itens, cupom="") == 100.0


def test_cupom_invalido():
    itens = [(100.0, 1)]
    with pytest.raises(ValueError, match="Cupom inválido."):
        calcular_total(itens, cupom="cupom_invalido")

def test_desconto_excede_cem_por_cento():
    itens = [(100.0, 1)]
    with pytest.raises(ValueError, match="Desconto total maior que 100%"):
        calcular_total(itens, desconto_percentual=95, cupom="vale10")
