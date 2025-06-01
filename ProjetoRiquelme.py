import random
import os
import json
import time
from colorama import init, Fore, Style

# Inicializa colorama
init(autoreset=True)

# Caminho do arquivo de banco JSON
ARQUIVO_DB = "banco_dados.json"

# Função para limpar tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# Função para esperar o ENTER
def esperar_enter():
    input(Fore.YELLOW + "\nPressione ENTER para continuar...")

# Cabeçalho bonito
def cabecalho(texto):
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)
    print(Fore.CYAN + Style.BRIGHT + f"{texto.center(50)}")
    print(Fore.CYAN + Style.BRIGHT + "=" * 50)

# Carregar banco de dados JSON
def carregar_db():
    if not os.path.exists(ARQUIVO_DB):
        return {"usuarios": []}
    with open(ARQUIVO_DB, "r", encoding="utf-8") as f:
        return json.load(f)

# Salvar banco de dados JSON
def salvar_db(db):
    with open(ARQUIVO_DB, "w", encoding="utf-8") as f:
        json.dump(db, f, indent=4)

# Procurar usuário por nome
def achar_usuario(db, nome):
    for u in db["usuarios"]:
        if u["nome"] == nome:
            return u
    return None

# Cadastro de usuário
def cadastrar(db):
    limpar_tela()
    cabecalho("CADASTRO")
    nome = input(Fore.YELLOW + "Digite seu nome: ").strip()
    if achar_usuario(db, nome):
        print(Fore.RED + "Nome já cadastrado! Tente outro.")
        esperar_enter()
        return None
    senha = input(Fore.YELLOW + "Digite sua senha: ").strip()
    usuario = {
        "nome": nome,
        "senha": senha,
        "conquistas": [],
        "estatisticas": {
            "adivinha_jogadas": 0,
            "adivinha_vitorias": 0,
            "jokenpo_jogadas": 0,
            "jokenpo_vitorias": 0,
            "jokenpo_derrotas": 0,
            "jokenpo_empates": 0,
            "calculadora_uso": 0,
            "pythonzinho_perguntas": 0,
            "pythonzinho_respostas": 0
        }
    }
    db["usuarios"].append(usuario)
    salvar_db(db)
    print(Fore.GREEN + f"Usuário '{nome}' cadastrado com sucesso!")
    esperar_enter()
    return usuario

# Login de usuário
def login(db):
    limpar_tela()
    cabecalho("LOGIN")
    nome = input(Fore.YELLOW + "Nome: ").strip()
    senha = input(Fore.YELLOW + "Senha: ").strip()
    usuario = achar_usuario(db, nome)
    if usuario and usuario["senha"] == senha:
        print(Fore.GREEN + f"Bem vindo(a) {nome}!")
        esperar_enter()
        return usuario
    print(Fore.RED + "Usuário ou senha incorretos!")
    esperar_enter()
    return None

# Mostrar perfil e conquistas
def mostrar_perfil(usuario):
    limpar_tela()
    cabecalho(f"PERFIL DE {usuario['nome'].upper()}")
    est = usuario["estatisticas"]

    print(Fore.MAGENTA + Style.BRIGHT + "Estatísticas de Jogos:")
    print(f"  Jogo da Adivinhação:")
    print(f"    - Jogadas: {est['adivinha_jogadas']}")
    print(f"    - Vitórias: {est['adivinha_vitorias']}")
    print(f"\n  Jokenpô:")
    print(f"    - Jogadas: {est['jokenpo_jogadas']}")
    print(f"    - Vitórias: {est['jokenpo_vitorias']}")
    print(f"    - Derrotas: {est['jokenpo_derrotas']}")
    print(f"    - Empates: {est['jokenpo_empates']}")
    print(f"\n  Calculadora:")
    print(f"    - Uso: {est['calculadora_uso']}")
    print(f"\n  Pythonzinho (bot):")
    print(f"    - Perguntas feitas: {est['pythonzinho_perguntas']}")
    print(f"    - Respostas dadas: {est['pythonzinho_respostas']}")

    print("\n" + Fore.MAGENTA + Style.BRIGHT + "Conquistas desbloqueadas:")
    if usuario["conquistas"]:
        for c in usuario["conquistas"]:
            print(Fore.GREEN + f" - {c}")
    else:
        print(Fore.RED + " Nenhuma conquista desbloqueada ainda.")
    esperar_enter()

# Função para desbloquear conquista e mostrar mensagem
def desbloquear_conquista(nome_conquista, usuario):
    if nome_conquista not in usuario["conquistas"]:
        print(Fore.MAGENTA + Style.BRIGHT + f"\n🎉 Conquista desbloqueada: {nome_conquista} 🎉\n")
        usuario["conquistas"].append(nome_conquista)
        time.sleep(1.5)

# Jogo Adivinhação
def jogo_adivinha(usuario, db):
    limpar_tela()
    cabecalho("JOGO DA ADIVINHAÇÃO")
    numero_secreto = random.randint(1, 100)
    tentativas = 0
    usuario["estatisticas"]["adivinha_jogadas"] += 1
    salvar_db(db)

    while True:
        try:
            palpite = int(input(Fore.YELLOW + "Digite seu palpite (1 a 100): "))
            if palpite < 1 or palpite > 100:
                print(Fore.RED + "Por favor, digite um número entre 1 e 100.")
                continue
        except ValueError:
            print(Fore.RED + "Entrada inválida! Digite um número inteiro.")
            continue

        tentativas += 1

        if palpite == numero_secreto:
            print(Fore.GREEN + f"\nParabéns! Você acertou o número em {tentativas} tentativas!")
            usuario["estatisticas"]["adivinha_vitorias"] += 1
            # Conquistas criativas para adivinhação
            conquistas_possiveis = {
                1: "🎯 Mestre da Sorte (Acertou de primeira!)",
                3: "🏆 Caçador de Números (Acerte em até 3 tentativas)",
                5: "🎖️ Persistente (Acerte em até 5 tentativas)",
                10: "👍 Dedicado (Acerte em até 10 tentativas)",
                15: "🔍 Detetive (Acerte em até 15 tentativas)",
                30: "🚀 Explorador (Acerte em até 30 tentativas)"
            }
            for k, v in conquistas_possiveis.items():
                if tentativas <= k:
                    desbloquear_conquista(v, usuario)
                    break
            salvar_db(db)
            break
        elif palpite < numero_secreto:
            print(Fore.BLUE + "Tente um número maior.")
        else:
            print(Fore.BLUE + "Tente um número menor.")
    esperar_enter()

# Jokenpô
def jogo_jokenpo(usuario, db):
    limpar_tela()
    cabecalho("JOKENPÔ")
    escolhas = ['pedra', 'papel', 'tesoura']
    usuario["estatisticas"]["jokenpo_jogadas"] += 1
    salvar_db(db)

    while True:
        escolha_usuario = input(Fore.YELLOW + "Escolha (pedra, papel, tesoura) ou 'sair' para voltar: ").lower()
        if escolha_usuario == "sair":
            break
        if escolha_usuario not in escolhas:
            print(Fore.RED + "Escolha inválida! Tente novamente.")
            continue

        escolha_pc = random.choice(escolhas)
        print(Fore.CYAN + f"Computador escolheu: {escolha_pc}")

        if escolha_usuario == escolha_pc:
            print(Fore.YELLOW + "Empate!")
            usuario["estatisticas"]["jokenpo_empates"] += 1
        elif (escolha_usuario == 'pedra' and escolha_pc == 'tesoura') or \
             (escolha_usuario == 'papel' and escolha_pc == 'pedra') or \
             (escolha_usuario == 'tesoura' and escolha_pc == 'papel'):
            print(Fore.GREEN + "Você venceu!")
            usuario["estatisticas"]["jokenpo_vitorias"] += 1
        else:
            print(Fore.RED + "Você perdeu!")
            usuario["estatisticas"]["jokenpo_derrotas"] += 1
        salvar_db(db)
    esperar_enter()

# Calculadora com tabuada
def calculadora(usuario, db):
    limpar_tela()
    cabecalho("CALCULADORA")
    usuario["estatisticas"]["calculadora_uso"] += 1
    salvar_db(db)

    while True:
        print(Fore.GREEN + "\n1 - Somar")
        print("2 - Subtrair")
        print("3 - Multiplicar")
        print("4 - Dividir")
        print("5 - Tabuada")
        print("6 - Voltar")
        opcao = input(Fore.YELLOW + "Escolha a operação: ")
        if opcao == "6":
            break

        if opcao not in ['1','2','3','4','5']:
            print(Fore.RED + "Opção inválida!")
            continue

        if opcao == '5':
            try:
                num = int(input(Fore.YELLOW + "Digite o número para tabuada: "))
                limpar_tela()
                cabecalho(f"Tabuada do {num}")
                for i in range(1, 11):
                    print(Fore.CYAN + f"{num} x {i} = {num * i}")
            except ValueError:
                print(Fore.RED + "Número inválido!")
            esperar_enter()
            continue

        try:
            num1 = float(input(Fore.YELLOW + "Digite o primeiro número: "))
            num2 = float(input(Fore.YELLOW + "Digite o segundo número: "))
        except ValueError:
            print(Fore.RED + "Número inválido!")
            continue

        if opcao == '1':
            resultado = num1 + num2
            print(Fore.GREEN + f"Resultado: {resultado}")
        elif opcao == '2':
            resultado = num1 - num2
            print(Fore.GREEN + f"Resultado: {resultado}")
        elif opcao == '3':
            resultado = num1 * num2
            print(Fore.GREEN + f"Resultado: {resultado}")
        elif opcao == '4':
            if num2 == 0:
                print(Fore.RED + "Erro: divisão por zero não é permitida.")
            else:
                resultado = num1 / num2
                print(Fore.GREEN + f"Resultado: {resultado}")
        esperar_enter()

# Pythonzinho (bot simples)
import random

def pythonzinho(usuario, db):
    limpar_tela()
    cabecalho("PYTHONZINHO BOT")
    perguntas = {
        "Qual a capital do Brasil?": "Brasília",
        "Qual a cor do céu em um dia limpo?": "azul",
        "Quem escreveu 'Dom Quixote'?": "Miguel de Cervantes",
        "Qual a fórmula da água?": "H2O",
        "Qual o maior planeta do sistema solar?": "Júpiter"
    }
    usuario["estatisticas"]["pythonzinho_perguntas"] += len(perguntas)
    salvar_db(db)

    # Transformar dicionário em lista e embaralhar
    lista_perguntas = list(perguntas.items())
    random.shuffle(lista_perguntas)

    for pergunta, resposta in lista_perguntas:
        print(Fore.YELLOW + f"\nPergunta: {pergunta}")
        resp = input(Fore.CYAN + "Sua resposta: ").strip().lower()
        if resp == resposta.lower():
            print(Fore.GREEN + "Resposta correta!")
            usuario["estatisticas"]["pythonzinho_respostas"] += 1
        else:
            print(Fore.RED + f"Resposta incorreta! A resposta correta é: {resposta}")
        salvar_db(db)
    esperar_enter()

# Menu de jogos
def menu_jogos(usuario, db):
    while True:
        limpar_tela()
        cabecalho("MENU DE JOGOS")
        print(Fore.GREEN + "1 - Adivinha (O Desafio dos Números)")
        print("2 - Jokenpô (Pedra, Papel e Tesoura)")
        print("3 - Voltar")
        escolha = input(Fore.YELLOW + "Escolha uma opção: ")

        if escolha == "1":
            jogo_adivinha(usuario, db)
        elif escolha == "2":
            jogo_jokenpo(usuario, db)
        elif escolha == "3":
            break
        else:
            print(Fore.RED + "Opção inválida!")
            time.sleep(1)

# Limpar cadastros com senha especial
def limpar_cadastros(db, usuario_atual):
    limpar_tela()
    cabecalho("LIMPAR CADASTROS")
    senha_admin = "r3lat2025"
    senha = input(Fore.YELLOW + "Digite a senha para acessar esta opção: ")
    if senha != senha_admin:
        print(Fore.RED + "Senha incorreta! Acesso negado.")
        esperar_enter()
        return
    confirm = input(Fore.RED + "Tem certeza que quer apagar todos os cadastros? (s/n): ").lower()
    if confirm == 's':
        db["usuarios"] = []
        salvar_db(db)
        print(Fore.GREEN + "Todos os cadastros foram apagados com sucesso!")
        esperar_enter()
    else:
        print(Fore.YELLOW + "Operação cancelada.")
        esperar_enter()

# Menu principal
def menu_principal(usuario, db):
    while True:
        limpar_tela()
        cabecalho(f"SEJA BEM-VINDO(A), {usuario['nome'].upper()}!")
        print(Fore.GREEN + "1 - Perfil")
        print("2 - Jogar")
        print("3 - Calculadora")
        print("4 - Pythonzinho Bot")
        print("5 - Limpar Cadastros (Admin)")
        print("6 - Sair")
        escolha = input(Fore.YELLOW + "Escolha uma opção: ")

        if escolha == "1":
            mostrar_perfil(usuario)
        elif escolha == "2":
            menu_jogos(usuario, db)
        elif escolha == "3":
            calculadora(usuario, db)
        elif escolha == "4":
            pythonzinho(usuario, db)
        elif escolha == "5":
            limpar_cadastros(db, usuario)
        elif escolha == "6":
            print(Fore.CYAN + "Saindo... Até a próxima!")
            time.sleep(1)
            break
        else:
            print(Fore.RED + "Opção inválida!")
            time.sleep(1)

# Programa principal
def main():
    db = carregar_db()
    usuario_logado = None
    while True:
        limpar_tela()
        cabecalho("BEM-VINDO AO MENU PRINCIPAL")
        print(Fore.GREEN + "1 - Login")
        print("2 - Cadastrar")
        print("3 - Sair")
        escolha = input(Fore.YELLOW + "Escolha uma opção: ")

        if escolha == "1":
            usuario_logado = login(db)
            if usuario_logado:
                menu_principal(usuario_logado, db)
        elif escolha == "2":
            usuario_logado = cadastrar(db)
            if usuario_logado:
                menu_principal(usuario_logado, db)
        elif escolha == "3":
            print(Fore.CYAN + "Saindo do programa... Até logo!")
            time.sleep(1)
            break
        else:
            print(Fore.RED + "Opção inválida!")
            time.sleep(1)

if __name__ == "__main__":
    main()
