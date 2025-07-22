import carregador_dados
import algoritmos
from tabela_hash import TabelaHash

def imprimir_resultados(resultados):
    if resultados:
        if not isinstance(resultados, list): resultados = [resultados]
        print(f"\n--- {len(resultados)} resultado(s) encontrado(s) ---")
        for item in resultados: print(item)
    else:
        print("\n>> Nenhum resultado encontrado.")

def main():

    catalogo_materias, catalogo_professores = carregador_dados.carregar_dados()
    lista_codigos_ordenada = sorted(catalogo_materias.todas_as_chaves())

    while True:
        print("\n======= 🧠 EduPlanner - Menu Principal =======")
        print("1. Buscar Matéria por Código (Busca Binária)")
        print("2. Buscar Matérias por Professor (Busca Sequencial)")
        print("3. Buscar na Ementa por Palavra-Chave (Rabin-Karp)")
        print("4. Comparar Funções de Hash")
        print("5. Demonstrção de Huffman")
        print("6. Sair")

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
            print("\n--- Comparando a Distribuição de Chaves com Funções de Hash ---")
            chaves_teste = catalogo_materias.todas_as_chaves()
            tamanho_tabela_teste = 97

            print(f"\nUsando {len(chaves_teste)} chaves carregadas.")
            print(f"Tabela de tamanho: {tamanho_tabela_teste}\n")

            print("--- Hash por Enlaçamento Deslocado ---")
            tabela_enl = TabelaHash(tamanho=tamanho_tabela_teste, funcao_hash='enlacamento')
            for chave in chaves_teste:
                tabela_enl.inserir(chave, None)
            print(tabela_enl)

            print("--- Hash por Extração ---")
            tabela_ext = TabelaHash(tamanho=tamanho_tabela_teste, funcao_hash='extracao')
            for chave in chaves_teste:
                tabela_ext.inserir(chave, None)
            print(tabela_ext)

        elif escolha == '5':
            plano_simulado = "BSI0101;BSI0201;BSI0202;MAT0030;BSI0301"
            
            print(f"\n--- Demonstração do Ciclo de Compressão Huffman ---\n")
            print(f"1. Texto Original: '{plano_simulado}'")
            
            comprimido, arvore = algoritmos.comprimir_huffman(plano_simulado)
            
            tamanho_original_bits = len(plano_simulado.encode('utf-8')) * 8
            tamanho_comprimido_bits = len(comprimido)

            print(f"\n2. Resultados da Compressão:")
            print(f"   -> Texto Comprimido (bits): {comprimido}")
            print(f"   -> Tamanho Original: {tamanho_original_bits} bits")
            print(f"   -> Tamanho Comprimido: {tamanho_comprimido_bits} bits")

            descomprimido = algoritmos.descomprimir_huffman(comprimido, arvore)
            print(f"\n3. Resultado da Descompressão:")
            print(f"   -> Texto Descomprimido: '{descomprimido}'")

            print("\n4. Verificação de Integridade:")
            if plano_simulado == descomprimido:
                print("   -> SUCESSO! O texto original e o descomprimido são idênticos.")
            else:
                print("   -> ERRO! O texto descomprimido é diferente do original.")

        elif escolha == '6':
            print(">> Saindo do EduPlanner. Até logo!")
            break

        else:
            print(">> Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()