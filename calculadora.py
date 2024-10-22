class Calculadora:
    def __init__(self):
        self.Nome = input("Digite seu nome: ")
    
    def Menu(self):
        numeros = []
        adicoes = 0
        resad = []
        subtracoes = 0
        ressub = []
        multiplicacoes = 0
        resmult = []
        divisoes = 0
        resdiv = []
        totOp = 0
        op = ""
        while op != '0':
            op = input("Qual operação aritmética deseja realizar? (Digite '0' para sair) ")
            
            if op == '0':
                print("Encerrando o programa.")
                break  # Sai do loop imediatamente

            n1 = float(input("Digite o primeiro número: "))
            n2 = float(input("Digite o segundo número: "))
            
            numeros.append(n1)
            numeros.append(n2)

            if op == "+":
                print(self.__Ad(n1, n2))
                adicoes+=1
                totOp+=1
                resad.append(f"{n1} + {n2} = {n1+n2}")
            elif op == "-":
                print(self.__Sub(n1, n2))
                subtracoes+=1
                totOp+=1
                ressub.append(f"{n1} - {n2} = {n1-n2}")
            elif op == "*":
                print(self.__Mult(n1, n2))
                multiplicacoes+=1
                totOp+=1
                resmult.append(f"{n1} * {n2} = {n1*n2}")
            elif op == "/":
                print(self.__Div(n1, n2))
                divisoes+=1
                totOp+=1
                resdiv.append(f"{n1} / {n2} = {n1/n2}")
            else:
                print("Operação inválida.")
        print(f"Total de operações realizadas: {totOp}\nAdições: {adicoes} - {resad}")
        print(f"Subtrações: {subtracoes} - {ressub}")
        print(f"Multiplicações: {multiplicacoes} - {resmult}")
        print(f"Subtrações: {divisoes} - {resdiv}")

    
    def __Ad(self, n1, n2):
        return n1 + n2
    
    def __Sub(self, n1, n2):
        return n1 - n2
    
    def __Mult(self, n1, n2):
        return n1 * n2
    
    def __Div(self, n1, n2):
        return n1 / n2

calculadora = Calculadora()
calculadora.Menu()
