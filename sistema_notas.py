import json
import os

ARQUIVO_DADOS = 'notas_cadastradas.json'

def carregar_dados():
    """Carrega os dados do arquivo JSON, se ele existir."""
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r', encoding='utf-8') as f:
            return json.load(f)
    return []

def salvar_dados(dados):
    """Salva a lista de notas no arquivo JSON."""
    with open(ARQUIVO_DADOS, 'w', encoding='utf-8') as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def cadastrar_nota():
    """Coleta as informações e cadastra uma nova nota."""
    print("\n--- Cadastro de Nova Nota ---")
    
    empenho = input("Empenho (deixe em branco se não houver): ")
    nf = input("NF (deixe em branco se não houver): ")
    status = input("Status (Paga ou Pendente): ")
    valor = input("Valor (R$): ")
    fundo = input("Fundo para pagamento: ")
    banco = input("Dados bancários da nota: ")

    nota = {
        "empenho": empenho,
        "nf": nf,
        "status": status,
        "valor": valor,
        "fundo": fundo,
        "dados_bancarios": banco
    }

    dados = carregar_dados()
    dados.append(nota)
    salvar_dados(dados)
    
    print("\n✅ Nota cadastrada com sucesso!")

def listar_notas():
    """Exibe todas as notas cadastradas no sistema."""
    dados = carregar_dados()
    print("\n--- Notas Cadastradas ---")
    
    if not dados:
        print("Nenhuma nota cadastrada ainda.")
        return

    for i, nota in enumerate(dados, 1):
        print(f"\nNota {i}:")
        print(f"  Empenho: {nota['empenho'] if nota['empenho'] else 'N/A'}")
        print(f"  NF: {nota['nf'] if nota['nf'] else 'N/A'}")
        print(f"  Status: {nota['status']}")
        print(f"  Valor: R$ {nota['valor']}")
        print(f"  Fundo: {nota['fundo']}")
        print(f"  Dados Bancários: {nota['dados_bancarios']}")
    print("-" * 25)

def menu():
    """Menu principal do sistema."""
    while True:
        print("\n=== Sistema de Controle de Notas ===")
        print("1. Cadastrar nova nota")
        print("2. Listar notas")
        print("3. Sair")
        
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_nota()
        elif opcao == '2':
            listar_notas()
        elif opcao == '3':
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
