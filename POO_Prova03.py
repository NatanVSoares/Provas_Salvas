#[PYIA-A13] Crie uma classe chamada ContaBancaria que tenha dois atributos privados, 
# _saldo e _titular. O atributo _saldo deve armazenar o saldo da conta, 
# enquanto o atributo _titular deve armazenar o nome do titular da conta. 
# Para interagir com esses atributos, implemente métodos públicos que permitam realizar operações bancárias. 
# Crie um método depositar que permita adicionar um valor ao saldo, 
# um método sacar que permita retirar um valor do saldo (caso haja saldo suficiente), 
# e um método exibir_saldo que exiba o saldo atual da conta. Utilize métodos para encapsular o acesso ao saldo, 
# garantindo que ele só possa ser alterado de maneira controlada pelos métodos de depósito e saque.


class ContaBancaria:
    def __init__(self,nome):
        self._nome = nome
        self._saldo = 0

    def depositar(self,valor):
        if valor > 0:
            self._saldo += valor 
            print(f'Valor De R${valor}, seu novo saldo é R$ {self._saldo}')
        else:
            print('Necessario saldo de valor positivo')

    def sacar(self,valor):
        if 0 < valor <= self._saldo :
            self._saldo -= valor
            print(f'Valor sacado R$ {valor} , Novo saldo R${self._saldo}')
        else:
            print('Valor de saldo inválido')

    def exibir_saldo(self):
        print(f'Saldo atual:{self._saldo}')

nova_conta = ContaBancaria('Irineu')


nova_conta.exibir_saldo()
print('-'*60)

nova_conta.depositar(1000)
print('-'*60)

nova_conta.exibir_saldo()
print('-'*60)

nova_conta.sacar(150)
print('-'*60)

nova_conta.exibir_saldo()
print('-'*60)

nova_conta.sacar(2000)




