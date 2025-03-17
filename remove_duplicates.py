#!/usr/bin/env python3

# Função para remover domínios duplicados de um arquivo e salvar em outro
def remover_duplicados_arquivo(input_file, output_file):
    try:
        print("🔍 Lendo o arquivo de entrada...")

        # Abre o arquivo de entrada para leitura (modo 'r') com codificação UTF-8
        with open(input_file, 'r', encoding='utf-8') as file:
            domains = file.readlines()  # Lê todas as linhas e armazena na lista 'domains'

        if not domains:  # Se o arquivo estiver vazio
            print("⚠️  Aviso: O arquivo de entrada está vazio.")
            return

        # Conjuntos para armazenar domínios únicos e duplicados
        see = set()         # Armazena domínios únicos
        duplicates = set()  # Armazena domínios que aparecem mais de uma vez
        unique_domains = [] # Lista para manter a ordem original dos domínios únicos
        
        print("🔄 Removendo duplicatas...")

        # Itera sobre cada domínio no arquivo
        for domain in domains:
            domain = domain.strip()  # Remove espaços extras no início e fim da linha

            # Se o domínio ainda não foi visto, adiciona aos únicos
            if domain not in see:
                see.add(domain)         # Adiciona ao conjunto de domínios únicos
                unique_domains.append(domain)  # Mantém a ordem na lista
            else:
                duplicates.add(domain)  # Se já foi visto, adiciona ao conjunto de duplicados

        # Abre o arquivo de saída para escrita (modo 'w'), sobrescrevendo o conteúdo anterior
        with open(output_file, 'w', encoding='utf-8') as file:
            for domain in unique_domains:
                file.write(f"{domain}\n")  # Escreve cada domínio único no arquivo de saída

        # Exibe os domínios duplicados no console
        if duplicates:
            print("⚠️  Domínios duplicados encontrados:")
            for duplicate in duplicates:
                print(f"   ❌ {duplicate}")

        # Mensagem de sucesso
        print(f"✅ Lista de domínios sem duplicados salva em: {output_file}")

    # Tratamento de erro se o arquivo de entrada não for encontrado
    except FileNotFoundError:
        print(f"❌ Erro: O arquivo '{input_file}' não foi encontrado.")

    # Tratamento genérico para outros erros inesperados
    except Exception as e:
        print(f"❌ Ocorreu um erro inesperado: {e}")

# Definição dos arquivos de entrada e saída
input_file = 'domains'              # Nome do arquivo de entrada contendo os domínios
output_file = 'Websites_for_block'  # Nome do arquivo de saída para salvar os domínios únicos

# Chamada da função para remover duplicatas
remover_duplicados_arquivo(input_file, output_file)
