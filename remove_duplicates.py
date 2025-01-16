def remover_duplicados_arquivo(input_file, output_file):
    try:
        with open(input_file, 'r', encoding='utf-8') as file:
            domains = file.readlines()
        
        see = set()
        duplicates = set()
        unique_domains = []
        for domain in domains:
            domain = domain.strip()
            if domain not in see:
                see.add(domain)
                unique_domains.append(domain)
            else:
                duplicates.add(domain)
        
        with open(output_file, 'w', encoding='utf-8') as file:
            for domain in unique_domains:
                file.write(f"{domain}\n")

        for duplicate in duplicates:
            print(f"Duplicate: {duplicate}")
        
        print(f"Lista de dominios sem duplicados salva em: {output_file}")
    
    except FileNotFoundError:
        print(f"File {input_file} not found.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")


input_file = 'domains'
output_file = 'Websites_for_block'
remover_duplicados_arquivo(input_file, output_file)