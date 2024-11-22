## Criando a classe

class ContaBancaria:
  def __init__(self, numero_conta, titular, saldo = 0):
    ## Atributos privadod
    self.__numero_conta = numero_conta
    self.__titular = titular
    self.__saldo = saldo
 
## Função para consultar o saldo
  def consultar_saldo(self):
    return f"Seu saldo atual é de: R${self.__saldo}"
 
## Função para depositar
  def depositar(self, valor):
    ## Permitir que apenas valores acima de 0 seja possível depositar
    if valor > 0:
      self.__saldo += valor
      return f"Valor de R${valor} foi depositado com sucesso.\n{self.consultar_saldo()}"
    ## Caso digite 0 ou valor negativos
    else:
      return "Não foi possível depositar, valor informado inválido!"
 
## Função para sacar
  def sacar(self, valor):
    ## Verificar se o número é maior que 0
    if valor > 0:
      ## Verifica se o valor digitado é menor ou igual o saldo, se sim decrementa
      if valor <= self.__saldo:
        self.__saldo -= valor
        return f"Valor de R${valor} foi sacado com sucesso.\n{self.consultar_saldo()}"
      ## Se não, ocorre erro
      else:
        return "Saldo insuficiente para o saque!"
    ## Erro caso o valor digitado seja negativo ou 0
    else:
      return "Valor negativo ou 0 digitado, digite um valor válido!"
 
###### TESTES ######
 
pessoa1 = ContaBancaria(numero_conta = 101547, titular = "Roberto", saldo = 0)
 
## Consulta o saldo inicial | 0
print(pessoa1.consultar_saldo())
print("")
## Deposita R$8 na conta
print(pessoa1.depositar(8))
print("")
## Saca R$3 da conta
print(pessoa1.sacar(3))
print("")
 
## TESTE DE ERRO ##
## Tenta sacar mais do que tem na conta
print(pessoa1.sacar(10))
print("")
## Tenta depositar e sacar valores negativos
print(pessoa1.depositar(-10))
print("")
print(pessoa1.sacar(-10))
