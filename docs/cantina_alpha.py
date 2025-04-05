estoque = {}

def cadastrar():
    id = input("ID: ")
    nome = input("Nome: ")
    quantidade = int(input("Qtd inicial: "))
    validade = input("Validade (dd/mm/aaaa): ")
    estoque[id] = {"nome": nome, "quantidade": quantidade, "validade": validade}
    print("Produto cadastrado.\n")

def entrada():
    id = input("ID do produto: ")
    if id in estoque:
        qtd = int(input("Qtd entrada: "))
        estoque[id]["quantidade"] += qtd
        print("Entrada registrada.\n")
    else:
        print("Produto não encontrado.\n")

def saida():
    id = input("ID do produto: ")
    if id in estoque:
        qtd = int(input("Qtd saída: "))
        estoque[id]["quantidade"] -= qtd
        print("Saída registrada.\n")
    else:
        print("Produto não encontrado.\n")

def saldo():
    print("\n--- SALDO ---")
    for id, dados in estoque.items():
        print(f"{id} - {dados['nome']}: {dados['quantidade']} unidades")
    print()

def validade():
    from datetime import datetime
    hoje = datetime.now()
    print("\n--- ALERTA DE VALIDADE ---")
    for id, dados in estoque.items():
        d = datetime.strptime(dados["validade"], "%d/%m/%Y")
        dias = (d - hoje).days
        if 0 <= dias <= 5:
            print(f"{dados['nome']} vence em {dias} dias ({dados['validade']})")
    print()

def menu():
    while True:
        print("1. Cadastrar\n2. Entrada\n3. Saída\n4. Saldo\n5. Validade\n0. Sair")
        op = input("Opção: ")
        if op == "1": cadastrar()
        elif op == "2": entrada()
        elif op == "3": saida()
        elif op == "4": saldo()
        elif op == "5": validade()
        elif op == "0": break
        else: print("Inválido.\n")

menu()
