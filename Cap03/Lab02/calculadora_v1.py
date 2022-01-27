# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3.
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

class Calculadora():
    def __init__(self,marca:str) -> None:
        self.marca = marca

    def soma(self,numero1:float, numero2:float):
        print(f"Calculadora {self.marca} somou:")
        return numero1+numero2

    def subtracao(self,numero1:float, numero2:float):
        print(f"Calculadora {self.marca} somou:")
        return numero1-numero2
    
    def multiplicacao(self,numero1:float, numero2:float):
        print(f"Calculadora {self.marca} somou:")
        return numero1*numero2


if __name__ == "__main__":
    calculadora_habibs = Calculadora(marca="HP")
    resulado = calculadora_habibs.soma(numero1=1,numero2=9)
    print(resulado)
    calculadora_saulo = Calculadora(marca="Cassio")
    resulado2 = calculadora_saulo.soma(numero1=12,numero2=4)
    print(resulado2)
