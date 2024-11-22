from abc import ABC, abstractmethod

# Classe abstrata Veiculo
# Representa um veículo genérico com atributos e métodos abstratos
class Veiculo(ABC):
    def __init__(self, marca, modelo, velocidade=0):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade
 
    @abstractmethod
    def acelerar(self):
        pass
 
    @abstractmethod
    def frear(self):
        pass
 
    @abstractmethod
    def mostrar_velocidade(self):
        pass

# Classe Carro que herda de Veiculo
# Adiciona o atributo tipo_combustivel e implementa os métodos abstratos
class Carro(Veiculo):
    def __init__(self, marca, modelo, velocidade=0, tipo_combustivel="Diesel"):
        super().__init__(marca, modelo, velocidade)
        self.tipo_combustivel = tipo_combustivel
 
    def acelerar(self):
        self.velocidade += 10
        return "O carro está acelerando..."
 
    def frear(self):
        self.velocidade = max(0, self.velocidade - 10)
        return "O carro freou."
 
    def mostrar_velocidade(self):
        return f"Velocidade atual do carro: {self.velocidade} km/h"
 
# Classe Moto que herda de Veiculo
# Adiciona o atributo tipo_combustivel e implementa os métodos abstratos
class Moto(Veiculo):
    def __init__(self, marca, modelo, velocidade=0, tipo_combustivel="Gasolina"):
        super().__init__(marca, modelo, velocidade)
        self.tipo_combustivel = tipo_combustivel
 
    def acelerar(self):
        self.velocidade += 15
        return "A moto está acelerando..."
 
    def frear(self):
        self.velocidade = max(0, self.velocidade - 15)
        return "A moto freou."
 
    def mostrar_velocidade(self):
        return f"Velocidade atual da moto: {self.velocidade} km/h"

# Função que testa qualquer objeto que herde de Veiculo
# Mostra o comportamento dos métodos acelerar, frear e mostrar_velocidade
def teste_veiculo(veiculo):
    print(veiculo.acelerar())
    print(veiculo.acelerar())
    print(veiculo.mostrar_velocidade())
    print(veiculo.frear())
    print(veiculo.mostrar_velocidade())
 
# Teste do polimorfismo com Carro e Moto
print("Testando um carro:\n")
carro1 = Carro("Toyota", "Corolla")
teste_veiculo(carro1)
 
print("\nTestando uma moto:\n")
moto1 = Moto("Honda", "Titan 160")
teste_veiculo(moto1)


 