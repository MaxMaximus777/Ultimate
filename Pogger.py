class Noggers:
    def __init__(self, Vida, Estamina, Força, Sorte, Carisma, Sanidade = 0):
        self.Vida = Vida
        self.Estamina = Estamina
        self.Força = Força
        self.Sorte = Sorte
        self.Carisma = Carisma
        self.Sanidade = Sanidade
    def Tomar_Poção(self, Vida):
        Poção = 5
        if Vida < 0:
            print("Você já está morto")
        else:
            print("Você curou +5 de vida")
            self.Vida += Poção
    def Equipar_Espada_Fodona_Lendária(self, Força):
        if Força < 50:
            print("Ta maluco irmão??")
        else:
            print("Você equipou a Espada")
    def Acender_Fogueira(self, Sanidade):
        if Sanidade < 0:
            print("Você se recusa a acender a fogueira")
        elif Sanidade >= 2 or 1:
            print(f"Você desesperademente acende a fogueira sentindo a pequena chama recuperar sua esperença. Sanidade Atual: {self.Sanidade}")
        else:
            print(f"Você gentilmente acende a tocha e calmamente observa o dançar das labaredas. Sanidade atual: {self.Sanidade}")
    def Descansar(self, Estamina):
        Descanso = 5
        self.Estamina += Descanso
        self.Sanidade += Descanso
        print(f"Você descansou. Status Atuais: {self.Vida, self.Estamina, self.Sanidade}")

def main():
    Vida = int(input("Qual a sua vida inicial?"))
    Estamina = int(input("Qual a sua estamina atual"))
    Força = int(input("Qual a sua força inicial"))
    Sorte = int(input("Qual a sua sorte inicial?"))
    Carisma = int(input("Qual a sua carisma inicial"))
    Sanidade = 10
    print("Sua sanidade é 10.")

    Ficha_Personagem = Noggers(Vida, Estamina, Força, Sorte, Carisma, Sanidade)

    while True:
        print("Após a árdua batalha você se encontra em uma sala agora vazia, Só restando você e uma pilha de corpos. Você respira fundo e olha a sua frente e somente uma espada brilhante chama sua atenção. O que você fará?")
        print("1. Tomar Poção?")
        print("2. Equipar Espada")
        print("3. Ascender uma fogueira")
        print("4. Descansar")

        Escolha = input("Entre sua escolha:")

        if Escolha == "1":
            Ficha_Personagem.Tomar_Poção(Vida)
        elif Escolha == "2":
            Ficha_Personagem.Equipar_Espada_Fodona_Lendária(Força)
        elif Escolha == "3":
            Ficha_Personagem.Acender_Fogueira(Sanidade)
        elif Escolha == "4":
            Ficha_Personagem.Descansar(Estamina)
            break
        else:
            print("Ta chapando, irmão, escolhe direito. SUCUMBA!!!")
            break

if __name__ == "__main__":
    main()