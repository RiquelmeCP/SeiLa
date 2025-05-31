import os
import random

# Função para limpar a tela com confirmação
def limpar_tela():
    input("\nPressione ENTER para continuar...")
    os.system('cls' if os.name == 'nt' else 'clear')

# Perfil do usuário
perfil_usuario = {
    'nome': '',
    'vitorias_jokenpo': 0,
    'jogadas_jokenpo': 0,
    'jogadas_adivinha': 0,
    'interacoes_pythonzinho': 0,
    'usos_calculadora': 0,
    'conquistas': []
}

# Função para checar conquistas
def checar_conquistas():
    if perfil_usuario['jogadas_jokenpo'] >= 10 and "Viciado em Jokenpo" not in perfil_usuario['conquistas']:
        perfil_usuario['conquistas'].append("Viciado em Jokenpo")
        print("🏆 Conquista desbloqueada: Viciado em Jokenpo!")

    if perfil_usuario['jogadas_adivinha'] >= 5 and "Mestre da Adivinhação" not in perfil_usuario['conquistas']:
        perfil_usuario['conquistas'].append("Mestre da Adivinhação")
        print("🏆 Conquista desbloqueada: Mestre da Adivinhação!")

    if perfil_usuario['interacoes_pythonzinho'] >= 20 and "Amigo do Pythonzinho" not in perfil_usuario['conquistas']:
        perfil_usuario['conquistas'].append("Amigo do Pythonzinho")
        print("🏆 Conquista desbloqueada: Amigo do Pythonzinho!")

    if perfil_usuario['usos_calculadora'] >= 50 and "Calculista Profissional" not in perfil_usuario['conquistas']:
        perfil_usuario['conquistas'].append("Calculista Profissional")
        print("🏆 Conquista desbloqueada: Calculista Profissional!")

# Função para ver perfil
def ver_perfil():
    limpar_tela()
    print("=== SEU PERFIL ===")
    for k, v in perfil_usuario.items():
        if k != 'conquistas':
            print(f"{k}: {v}")
    print("\n=== Conquistas Desbloqueadas ===")
    for conquista in perfil_usuario['conquistas']:
        print(f"- {conquista}")
    if not perfil_usuario['conquistas']:
        print("Nenhuma conquista ainda.")
    limpar_tela()

# Menu inicial
def menu_inicial():
    limpar_tela()
    perfil_usuario['nome'] = input("Digite seu nome: ")
    print("=" * 50)
    print(f"   BEM-VINDO AO MEGA PROJETO, {perfil_usuario['nome']}!")
    print("    JOGOS | CALCULADORA | PYTHONZINHO")
    print("=" * 50)
    limpar_tela()

# Jokenpo
def pedra_papel_tesoura():
    vitorias_jogador = 0
    vitorias_computador = 0
    empates = 0

    while True:
        limpar_tela()
        print("\n--- Jokenpo ---")
        opcoes = ['pedra', 'papel', 'tesoura']
        jogador = input("Escolha pedra, papel ou tesoura: ").lower()

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
            perfil_usuario['vitorias_jokenpo'] += 1
        else:
            print("Você perdeu.")
            vitorias_computador += 1

        perfil_usuario['jogadas_jokenpo'] += 1
        checar_conquistas()

        print(f"\nPlacar Atual:")
        print(f"Você: {vitorias_jogador} | Computador: {vitorias_computador} | Empates: {empates}")

        jogar_novamente = input("\nQuer jogar novamente? (s/n): ").lower()
        if jogar_novamente != 's':
            print("Voltando ao menu de jogos...")
            limpar_tela()
            break

# Adivinha
def adivinhar_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    limpar_tela()
    print("\n--- Jogo: Adivinha ---")

    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
            tentativas += 1
        except ValueError:
            print("Por favor, digite um número inteiro válido.")
            continue

        if palpite < numero_secreto:
            print("Mais alto!")
        elif palpite > numero_secreto:
            print("Mais baixo!")
        else:
            print(f"Parabéns! Você acertou o número em {tentativas} tentativas.")
            perfil_usuario['jogadas_adivinha'] += 1
            checar_conquistas()
            limpar_tela()
            break

# Calculadora
def calculadora():
    while True:
        limpar_tela()
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

        perfil_usuario['usos_calculadora'] += 1
        checar_conquistas()

        if opcao in ['1', '2', '3', '4', '5']:
            try:
                n1 = float(input("Digite o primeiro número: "))
                n2 = float(input("Digite o segundo número: "))
            except ValueError:
                print("Entrada inválida. Use apenas números.")
                limpar_tela()
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
                print(f"Resultado: {n1 ** n2}")

            limpar_tela()

        elif opcao == '6':
            try:
                numero = int(input("Digite o número da tabuada: "))
            except ValueError:
                print("Entrada inválida. Use um número inteiro.")
                limpar_tela()
                continue

            print(f"\nTabuada do {numero}")
            for i in range(1, 11):
                print(f"{numero} x {i} = {numero * i}")
            limpar_tela()

        else:
            print("Opção inválida. Tente novamente.")
            limpar_tela()

# Falar com Pythonzinho
def falar_com_pythonzinho():
    limpar_tela()
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
        if entrada == 'sair':
            break

        perfil_usuario['interacoes_pythonzinho'] += 1
        checar_conquistas()

        resposta = respostas.get(entrada, "Ainda estou aprendendo a responder isso.")
        print(f"Pythonzinho: {resposta}")

# Menu jogos
def menu_jogos():
    while True:
        limpar_tela()
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
            limpar_tela()

# Menu principal
def menu_principal():
    while True:
        limpar_tela()
        print("\n" + "="*50)
        print("                 MENU PRINCIPAL")
        print("="*50)
        print("1 - Jogos")
        print("2 - Calculadora")
        print("3 - Falar com Pythonzinho")
        print("4 - Ver meu perfil e conquistas")
        print("0 - Sair")
        print("="*50)

        escolha = input("Digite o número da sua opção: ")

        if escolha == '1':
            menu_jogos()
        elif escolha == '2':
            calculadora()
        elif escolha == '3':
            falar_com_pythonzinho()
        elif escolha == '4':
            ver_perfil()
        elif escolha == '0':
            print("Saindo... Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.")
            limpar_tela()

# Início
menu_inicial()
menu_principal()