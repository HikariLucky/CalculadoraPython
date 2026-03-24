import math

class Calculadora:
    def __init__(self):
        self.valores = []
        
    def add_valores(self):
        print("Digite os números(digite 'fim' para finalizar): ")
        
        while True:
            entrada = input('> ')
            if entrada.lower() == 'fim':
                break
            
            try:
                numero = float((entrada))
                self.valores.append(numero)
                
            except ValueError:
                print('Valor inválid. Digite um número válido.')
                
    
    def somar(self):
        if not self.valores:
            return 'Nenhum valor para soma'
        
        return sum(self.valores)
    
    def subtrair(self):
        if len(self.valores) < 2:
            return 'Precisa de pelo menos dois valores.'
        result = self.valores[0]
        for valor in self.valores[1: ]:
            result -= valor
            
        return result
    
    def mult(self):
        if not self.valores:
            return 'Nenhum valor para multiplicar.'
        
        result = 1 
        for valor in self.valores:
            result *= valor
            
        return result
    
    def div(self):
        if len(self.valores) < 2:
            return 'Precisa de pelo menos dois valores.'
        
        result = self.valores[0]
        
        for valor in self.valores[1: ]:
            if valor == 0:
                return 'Erro: Divisão por zero.'
            
            result /= valor
        return result
    
    
    def mostrar(self):
        if self.valores:
            print('Valores digitados', self.valores)
            
        else:
            print('Nenhum valor foi digitado')
            

    def menu(self):
        
        while True:
            print('\n' + '='*40)
            print("1. Adicionar valores")
            print("2. Somar todos")
            print("3. Subtrair todos")
            print("4. Multiplicar todos")
            print("5. Dividir todos")
            print("6. Mostrar valores")
            print("0. Sair")
            print("-"*40)
            
            opcao = input('Escolha uma opcão: ')
            
            if opcao == '1':
                self.add_valores()
                
            elif opcao == '2':
                print('Somar', self.somar())
                
            elif opcao == '3':
                print('substrair', self.subtrair())
            
            elif opcao == '4':
                print('Multiplicação', self.mult())
            
            elif opcao == '5':
                print('Divisão', self.div())
                
            elif opcao == '6':
                self.mostrar()
                
            elif opcao == '0':
                print('Saindo...')
                break
            
            else:
                print("Opção inválida. Tente novamente.")
                
if __name__ == "__main__":
    calc = Calculadora()
    calc.menu()