## VEÍCULO ##
 
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