import carregador_dados
import algoritmos

def imprimir_resultados(resultados):
    if resultados:
        if not isinstance(resultados, list): resultados = [resultados]
        print(f"\n--- {len(resultados)} resultado(s) encontrado(s) ---")
        for item in resultados: print(item)
    else:
        print("\n>> Nenhum resultado encontrado.")

def main():

    catalogo_materias, catalogo_professores = carregador_dados.carregar_dados()
    
    lista_codigos_ordenada = sorted(catalogo_materias.keys())

    while True:
        print("\n======= 🧠 EduPlanner - Menu de Buscas =======")
        print("1. Buscar Matéria por Código (Busca Binária)")
        print("2. Buscar Matérias por Professor (Busca Sequencial)")
        print("3. Buscar na Ementa por Palavra-Chave (Rabin-Karp)")
        print("4. Sair")
        
        escolha = input(">> Escolha uma opção: ")

        if escolha == '1':
            codigo = input("Digite o código da matéria (ex: BSI0201): ").upper()
            resultado = algoritmos.busca_binaria_por_codigo(codigo, lista_codigos_ordenada, catalogo_materias)
            imprimir_resultados(resultado)

        elif escolha == '2':
            nome_prof = input("Digite o nome do professor: ")
            resultados = algoritmos.busca_sequencial_por_professor(nome_prof, catalogo_professores, catalogo_materias)
            imprimir_resultados(resultados)

        elif escolha == '3':
            palavra = input("Digite a palavra-chave para buscar na ementa: ")
            resultados = algoritmos.busca_por_palavra_chave_na_ementa(palavra, catalogo_materias)
            imprimir_resultados(resultados)

        elif escolha == '4':
            print(">> Saindo do EduPlanner. Até logo!")
            break
        else:
            print(">> Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()