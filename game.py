import os
import time

os.system('cls' if os.name == 'nt' else 'clear')
player = input(f"\t\tEnter player name: \n\t").title()
os.system('cls' if os.name == 'nt' else 'clear')

def start():
    print(f"{player}, WELCOME TO                             ")
    print("      __________ ________   _____ ____ __________ ")
    print("     /    /    //        | /     /   //         / ")
    print("    /    /    //    /    //     /   //   ______/  ")
    print("   /         //         //         //   /__   /   ")
    print("  /    /    //    /    //   /     //         /    ")
    print(" /____/____//____/____//___/_____//_________/     ")
    print("        _____ _____ ________   _____ ____         ")
    print("       /     /    //        | /     /   /         ")
    print("      /     /    //    /    //     /   /          ")
    print("     /          //         //         /           ")
    print("    /   /  /   //    /    //   /     /            ")
    print("   /___/__/___//____/____//___/_____/  (GoHo2024) ")
    print()
    time.sleep(3)
    os.system('cls' if os.name == 'nt' else 'clear')


def escolher_palavra():
    secret_word = input(f"\t\tEnter a word for the challenge:\n\t")
    os.system('cls' if os.name == 'nt' else 'clear')
    return (secret_word)


def jogar_forca():
    palavra = escolher_palavra()
    tip = input(f"\tEnter a tip: \n\t\t")
    letras_corretas = []
    letras_erradas = []
    tentativas = 6
    
    start()
    
    while True:
        
        #os.system('cls' if os.name == 'nt' else 'clear')
        # Exibir a palavra com letras escondidas
        palavra_oculta = ''.join([letra if letra in letras_corretas else '_' for letra in palavra])
        print("Word: " + palavra_oculta)
        print(f"Tip: {tip}")
        
        # Exibir letras erradas
        if letras_erradas:
            print("Wrong letters:", ' '.join(letras_erradas))
        
        # Verificar se o jogador venceu
        if palavra_oculta == palavra:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(" ___    ____    ____ ____ ____    ____  ____ ____ ____ ")
            print("|   |  /    |  /   //   //    |  /   / /   //   //   / ")
            print("|   | /     | /   //   //     | /   / /   //   //   /  ")
            print("|   |/      |/   //   //      |/   / /___//___//___/   ")
            print("|       /|      //   //   /|      / ____ ____ ____     ")
            print("|      / |     //   //   / |     / /   //   //   /     ")
            print("|_____/  |____//___//___/  |____/ /___//___//___/      ")
            break
        
        # Verificar se o jogador perdeu
        if tentativas == 0:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("You lost! The word was:", palavra.upper())
            print("        _____    _____________________________________________  ")
            print("       /    /   /            |           |          |         | ")
            print("      /    /   /    ____     /  ____     /  ________/  _______/ ")
            print("     /    /   /    /   /    /  /   /    /  /_______   /___      ")
            print("    /    /   /    /   /    /  /   /    /          /      /      ")
            print("   /    /   /    /   /    /  /   /    /_____     /  ____/       ")
            print("  /    /___/__  /___/    /  /___/    /_____/    /  /_______     ")
            print(" /           /          /           /          /           /    ")
            print("/___________/__________/___________/__________/___________/     ")
            break
        
        # Solicitar uma letra ao jogador
        letra = input("Enter a letter: ").lower()
        os.system('cls' if os.name == 'nt' else 'clear')

        
        # Verificar se a letra já foi tentada
        if letra in letras_corretas or letra in letras_erradas:
            print("Have you tried this lyric. Try another one.")
            continue
        
        # Verificar se a letra está na palavra
        if letra in palavra:
            letras_corretas.append(letra)
            print("Correct letter!")
        else:
            letras_erradas.append(letra)
            tentativas -= 1
            print("Wrong letter! You have", tentativas, "attempts remaining.")
            
jogar_forca()