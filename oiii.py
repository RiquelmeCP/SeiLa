import random  # Importa a biblioteca 'random', usada para gerar números ou escolhas aleatórias

# Função que exibe o menu inicial com uma mensagem de boas-vindas
def menu_inicial():
    print("=" * 50)  # Imprime 50 sinais de igual para formar uma linha decorativa
    print("       BEM-VINDO AO MEGA PROJETO")
    print("    JOGOS | CALCULADORA | PYTHONZINHO")
    print("=" * 50)
    input("Pressione ENTER para continuar...")  # Aguarda o usuário apertar ENTER

# Função do jogo pedra, papel e tesoura (Jokenpo)
def pedra_papel_tesoura():
    vitorias_jogador = 0
    vitorias_computador = 0
    empates = 0

    while True:
        print("\n--- Jokenpo ---")
        opcoes = ['pedra', 'papel', 'tesoura']
        jogador = input("Escolha pedra, papel ou tesoura: ").lower()  
        # .lower() transforma todo o texto digitado pelo usuário em minúsculo
        # Isso evita erro se o usuário digitar "Pedra" ou "PEDRA", pois tudo vira "pedra"

        if jogador not in opcoes:
            print("Opção inválida. Tente novamente.")
            continue

        computador = random.choice(opcoes)
        print(f"Computador escolheu: {computador}")

        if jogador == computador:
            print("Empate.")
            empates += 1
        elif (jogador == 'pedra' and computador == 'tesoura') or \
             (jogador == 'papel' and computador == 'pedra') or \
             (jogador == 'tesoura' and computador == 'papel'):
            print("Você venceu.")
            vitorias_jogador += 1
        else:
            print("Você perdeu.")
            vitorias_computador += 1

        print(f"\nPlacar Atual:")
        print(f"Você: {vitorias_jogador} | Computador: {vitorias_computador} | Empates: {empates}")

        jogar_novamente = input("\nQuer jogar novamente? (s/n): ").lower()
        # .lower() aqui garante que qualquer entrada como "S", "s", "Sim" fique minúscula e seja comparável
        if jogar_novamente != 's':
            print("Voltando ao menu de jogos...")
            break

# Função do jogo de adivinhar o número
def adivinhar_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    print("\n--- Jogo: Adivinha ---")

    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
            # try: Tenta executar esse bloco
            # Se o usuário digitar algo que não seja número, dá erro e vai para o except
            tentativas += 1
        except ValueError:
            # except: Executado se acontecer um erro no bloco try
            # ValueError: tipo de erro que acontece quando tenta converter algo inválido para número
            print("Por favor, digite um número inteiro válido.")
            continue

        if palpite < numero_secreto:
            print("Mais alto!")
        elif palpite > numero_secreto:
            print("Mais baixo!")
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
            break

# Função da calculadora
def calculadora():
    while True:
        print("\n--- CALCULADORA ---")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Potência")
        print("6. Tabuada")
        print("0. Voltar ao menu principal")

        opcao = input("Digite o número da sua opção: ")

        if opcao == '0':
            break

        elif opcao in ['1', '2', '3', '4', '5']:
            try:
                n1 = float(input("Digite o primeiro número: "))
                n2 = float(input("Digite o segundo número: "))
                # Novamente usamos try-except para capturar erro se o usuário digitar letras ou símbolos
            except ValueError:
                print("Entrada inválida. Use apenas números.")
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
                    print("Não é possível dividir por zero.")
            elif opcao == '5':
                print(f"Resultado: {n1 ** n2}")  # Potência (ex: 2 ** 3 = 8)

        elif opcao == '6':
            try:
                numero = int(input("Digite o número da tabuada: "))
            except ValueError:
                print("Entrada inválida. Use um número inteiro.")
                continue

            print(f"\nTabuada do {numero}")
            for i in range(1, 11):
                # range(1, 11) gera os números de 1 até 10
                # Usado para fazer a tabuada
                print(f"{numero} x {i} = {numero * i}")
        else:
            print("Opção inválida. Tente novamente.")

# Função do Pythonzinho (assistente virtual)
def falar_com_pythonzinho():
    respostas = {
        "qual seu nome?": "Eu sou o Pythonzinho, seu assistente virtual.",
        "quantos anos você tem?": "Eu não tenho idade, pois sou um programa de computador.",
        "tudo bem com você?": "Estou sempre bem, obrigado por perguntar!",
        "o que você gosta de fazer?": "Eu adoro ajudar você com jogos, cálculos e aprender coisas novas.",
        "você gosta de python?": "Sim, Python é minha linguagem favorita!",
        "qual é seu jogo preferido?": "Eu gosto muito de jogar Jokenpo e Adivinha aqui no Mega Projeto.",
        "você pode me ajudar?": "Claro! Estou aqui para ajudar no que você precisar.",
        "como está o tempo aí?": "Eu não sei, pois não tenho acesso a informações externas ainda.",
        "você gosta de música?": "Adoro música! Mas ainda não consigo ouvir.",
    }

    print("\n--- Fale com o Pythonzinho (digite 'sair' para voltar ao menu) ---")
    print("Você pode perguntar coisas como:")
    for pergunta in respostas.keys():
        print(f"- {pergunta.capitalize()}")
    print()

    while True:
        entrada = input("Você: ").lower().strip()
        # .lower() transforma em minúsculas para facilitar comparação
        # .strip() remove espaços no início e fim da frase
        # Ex: "   Olá  " vira "olá"

        if entrada == 'sair':
            break

        resposta = respostas.get(entrada, "Ainda estou aprendendo a responder isso.")
        # .get() procura a resposta no dicionário. Se não encontrar, mostra a mensagem padrão
        print(f"Pythonzinho: {resposta}")

# Menu dos jogos
def menu_jogos():
    while True:
        print("\n" + "="*40)
        print("            MENU JOGOS")
        print("="*40)
        print("1 - Jokenpo")
        print("2 - Adivinha")
        print("0 - Voltar ao menu principal")
        print("="*40)

        escolha = input("Digite o número da sua opção: ")

        if escolha == '1':
            pedra_papel_tesoura()
        elif escolha == '2':
            adivinhar_numero()
        elif escolha == '0':
            break
        else:
            print("Opção inválida. Tente novamente.")

# Menu principal
def menu_principal():
    while True:
        print("\n" + "="*50)
        print("                 MENU PRINCIPAL")
        print("="*50)
        print("1 - Jogos")
        print("2 - Calculadora")
        print("3 - Falar com Pythonzinho")
        print("0 - Sair")
        print("="*50)

        escolha = input("Digite o número da sua opção: ")

        if escolha == '1':
            menu_jogos()
        elif escolha == '2':
            calculadora()
        elif escolha == '3':
            falar_com_pythonzinho()
        elif escolha == '0':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Início do programa
menu_inicial()
menu_principal()
