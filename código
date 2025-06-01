import random
import time
import os

# Cores ANSI
VERDE = '\033[92m'
VERMELHO = '\033[91m'
AZUL = '\033[94m'
AMARELO = '\033[93m'
RESET = '\033[0m'

# Limpar tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Sistema de conquistas
conquistas = {
    "Jokenpo": {
        "Venceu o bot 3 vezes seguidas": False,
        "Perdeu 3 vezes seguidas": False
    },
    "Adivinha": {
        "Acertou em até 15 tentativas": False,
        "Acertou em até 5 tentativas": False,
        "Acertou em até 3 tentativas": False
    },
    "Mega Projeto": {
        "Iniciou o Mega Projeto": False
    }
}

# Desbloqueio
def desbloquear_conquista(categoria, nome):
    if not conquistas[categoria][nome]:
        conquistas[categoria][nome] = True
        print(f"{VERDE}✅ Conquista desbloqueada: {nome}{RESET}")
        time.sleep(1)

# Mega Projeto intro
def mega_projeto():
    limpar_tela()
    print(f"{AMARELO}========================{RESET}")
    print(f"{AMARELO}========================{RESET}")
    print(f"{AMARELO}       MEGA PROJETO      {RESET}")
    print(f"{AMARELO}========================{RESET}")
    print(f"{AMARELO}========================{RESET}")
    desbloquear_conquista("Mega Projeto", "Iniciou o Mega Projeto")
    input("\nPressione ENTER para continuar...")
    limpar_tela()

# Menu
def menu():
    while True:
        print(f"{AZUL}=== MENU PRINCIPAL ==={RESET}")
        print("1 - Jogos")
        print("2 - Calculadora")
        print("3 - Falar com Pythonzinho")
        print("4 - Conquistas")
        print("0 - Sair")
        
        escolha = input("Escolha: ")

        if escolha == '1':
            menu_jogos()
        elif escolha == '2':
            calculadora()
        elif escolha == '3':
            falar_com_pythonzinho()
        elif escolha == '4':
            mostrar_conquistas()
        elif escolha == '0':
            print(f"{VERMELHO}Saindo... Até logo!{RESET}")
            break
        else:
            print(f"{VERMELHO}Opção inválida!{RESET}")
            input("ENTER pra continuar...")

# Menu de jogos
def menu_jogos():
    while True:
        limpar_tela()
        print(f"{AZUL}=== MENU JOGOS ==={RESET}")
        print("1 - Jokenpo")
        print("2 - Adivinha")
        print("0 - Voltar")
        
        escolha = input("Escolha: ")

        if escolha == '1':
            pedra_papel_tesoura()
        elif escolha == '2':
            adivinhar_numero()
        elif escolha == '0':
            break
        else:
            print(f"{VERMELHO}Opção inválida!{RESET}")
            input("ENTER pra continuar...")

# Jokenpo
def pedra_papel_tesoura():
    vitorias_seguidas = 0
    derrotas_seguidas = 0
    limpar_tela()
    
    while True:
        print(f"{AZUL}--- JOKENPO ---{RESET}")
        opcoes = ['pedra', 'papel', 'tesoura']
        jogador = input("Escolha pedra, papel ou tesoura: ").lower()

        if jogador not in opcoes:
            print(f"{VERMELHO}Opção inválida!{RESET}")
            continue

        computador = random.choice(opcoes)
        print(f"Computador escolheu: {computador}")
        time.sleep(0.5)

        if jogador == computador:
            print(f"{AMARELO}Empate!{RESET}")
            vitorias_seguidas = 0
            derrotas_seguidas = 0
        elif (jogador == 'pedra' and computador == 'tesoura') or \
             (jogador == 'papel' and computador == 'pedra') or \
             (jogador == 'tesoura' and computador == 'papel'):
            print(f"{VERDE}Você venceu!{RESET}")
            vitorias_seguidas += 1
            derrotas_seguidas = 0
            if vitorias_seguidas == 3:
                desbloquear_conquista("Jokenpo", "Venceu o bot 3 vezes seguidas")
        else:
            print(f"{VERMELHO}Você perdeu!{RESET}")
            vitorias_seguidas = 0
            derrotas_seguidas += 1
            if derrotas_seguidas == 3:
                desbloquear_conquista("Jokenpo", "Perdeu 3 vezes seguidas")

        jogar = input("Jogar de novo? (s/n): ").lower()
        if jogar != 's':
            break
        limpar_tela()

# Adivinha número
def adivinhar_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    limpar_tela()

    print(f"{AZUL}--- JOGO: ADIVINHA ---{RESET}")

    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1
        except ValueError:
            print(f"{VERMELHO}Digite um número válido!{RESET}")
            continue

        if palpite < numero_secreto:
            print(f"{AMARELO}O número é maior que {palpite}{RESET}")
        elif palpite > numero_secreto:
            print(f"{AMARELO}O número é menor que {palpite}{RESET}")
        else:
            print(f"{VERDE}Parabéns! Acertou com {tentativas} tentativas!{RESET}")

            if tentativas <= 15:
                desbloquear_conquista("Adivinha", "Acertou em até 15 tentativas")
            if tentativas <= 5:
                desbloquear_conquista("Adivinha", "Acertou em até 5 tentativas")
            if tentativas <= 3:
                desbloquear_conquista("Adivinha", "Acertou em até 3 tentativas")

            input("ENTER pra voltar...")
            break

# Calculadora
def calculadora():
    while True:
        limpar_tela()
        print(f"{AZUL}--- CALCULADORA ---{RESET}")
        print("1 - Adição")
        print("2 - Subtração")
        print("3 - Multiplicação")
        print("4 - Divisão")
        print("5 - Potência")
        print("6 - Tabuada")
        print("0 - Voltar")

        opcao = input("Escolha: ")

        if opcao == '0':
            break
        elif opcao in ['1','2','3','4','5']:
            try:
                n1 = float(input("Primeiro número: "))
                n2 = float(input("Segundo número: "))
            except ValueError:
                print(f"{VERMELHO}Entrada inválida!{RESET}")
                input("ENTER pra continuar...")
                continue

            if opcao == '1':
                print(f"Resultado: {n1 + n2}")
            elif opcao == '2':
                print(f"Resultado: {n1 - n2}")
            elif opcao == '3':
                print(f"Resultado: {n1 * n2}")
            elif opcao == '4':
                if n2 != 0:
                    print(f"Resultado: {n1 / n2}")
                else:
                    print(f"{VERMELHO}Não divide por zero!{RESET}")
            elif opcao == '5':
                print(f"Resultado: {n1 ** n2}")

        elif opcao == '6':
            try:
                numero = int(input("Número da tabuada: "))
            except ValueError:
                print(f"{VERMELHO}Entrada inválida!{RESET}")
                continue

            for i in range(1,11):
                print(f"{numero} x {i} = {numero * i}")

        else:
            print(f"{VERMELHO}Opção inválida!{RESET}")
        input("ENTER pra continuar...")

# Conversa com Pythonzinho
def falar_com_pythonzinho():
    respostas = {
        "qual seu nome?": "Eu sou o Pythonzinho, seu assistente virtual.",
        "quantos anos você tem?": "Eu não tenho idade, sou código!",
        "tudo bem com você?": "Sempre bem, valeu!",
        "o que você gosta de fazer?": "Gosto de rodar programas e ajudar.",
        "você gosta de python?": "Lógico! Python é minha vida!",
        "qual é seu jogo preferido?": "Adoro Jokenpo e Adivinha.",
        "você pode me ajudar?": "Claro! Só perguntar.",
        "como está o tempo aí?": "Não sei, ainda não tenho acesso à internet.",
        "você gosta de música?": "Adoro! Pena que não posso ouvir."
    }

    print(f"{AZUL}--- Fale com Pythonzinho ---{RESET}")
    print("Perguntas que ele entende:")
    for pergunta in respostas:
        print(f"- {pergunta}")

    while True:
        entrada = input("\nVocê: ").lower().strip()
        if entrada == 'sair':
            break
        resposta = respostas.get(entrada, "Ainda estou aprendendo a responder isso.")
        print(f"Pythonzinho: {resposta}")

# Mostrar conquistas
def mostrar_conquistas():
    limpar_tela()
    print(f"{AZUL}=== CONQUISTAS ==={RESET}")
    for categoria, conquistas_categoria in conquistas.items():
        print(f"\n{categoria}:")
        for nome, desbloqueada in conquistas_categoria.items():
            status = "✅" if desbloqueada else "🔒"
            print(f"{status} {nome}")
    input("\nENTER pra voltar...")

# --- Iniciar programa ---
mega_projeto()
menu()