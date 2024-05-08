class Banco:
    def __init__(self, id_conta, nome_conta, initial_balance= 0.0):
        self.id_conta = id_conta
        self.nome_conta = nome_conta
        self.balance = initial_balance



    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Você depositou ${amount}. Você tem agora: ${self.balance}")
        else:
            print("Inválido use uma quantidade positiva")

    def sacar(self, amount):

        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Você tirou ${amount}. Seu total agora é ${self.balance}")
        
        elif amount > self.balance:
            print("Fundos insuficientes, retirada cancelada")
        else:
            print("Quantidade invalida, por favor retire uma quantidade positiva")


    def check_extrato(self):
        print(f"{self.nome_conta} você tem ${self.balance}")



def main():
    id_conta = int(input("Entre o seu ID: "))
    nome_conta = input("Entre o seu nome: ")
    initial_balance = float(input("Entre o seu dinheiro inicial:"))

    conta = Banco(id_conta, nome_conta, initial_balance)

    while True:
        print("Escolha a operação:")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Checar o Extrato")
        print("4. Exit")

        choice = input("Entre sua escolha:")

        if choice == "1":
            amount = float(input("Entre a quantidade que você quer depositar:  "))
            conta.deposit(amount)
        elif choice == "2":
            amount = float(input("Entre a quantidade que você quer sacar:  "))
            conta.sacar(amount)
        elif choice == "3":
            conta.check_extrato()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Escolha invalida, tente outra vez")


if __name__ == "__main__":
    main()