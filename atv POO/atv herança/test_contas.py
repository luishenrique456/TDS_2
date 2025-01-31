import pytest
from contas import ContaCorrente,ContaPoupanca,ContaImposto


#testar class ContaPoupanca herdou da class ContaCorrente
def test_contapopupanca_herda():
    conta1 = ContaPoupanca(1, 123, 1400, 'Luis')
    assert isinstance(conta1,ContaCorrente)

def test_metodo_transferencia():
    conta1 = ContaPoupanca(1, 123, 1400, 'Luis')
    conta2 = ContaPoupanca(90, 456, 90, 'Kallya')

    saldo_inicial_conta1 = conta1.saldo
    saldo_inicial_conta2 = conta2.saldo

    conta1.transferir(conta2,120)

    assert conta1.saldo == saldo_inicial_conta1 - 120

    assert conta2.saldo == saldo_inicial_conta2 + 120



