import os
import re
import argparse

def find_pdf_links_in_repo(repo_path):
    """
    Analiza un repositorio local de archivos Markdown en busca de enlaces a PDFs.
    """
    pdf_links = set()
    url_pattern = re.compile(r'https?://[^\s()]+')

    print(f"Analizando archivos en: {repo_path}")

    if not os.path.isdir(repo_path):
        print(f"Error: La ruta '{repo_path}' no es un directorio válido.")
        return

    # Recorremos cada carpeta y archivo en el repositorio
    for root, _, files in os.walk(repo_path):
        for file in files:
            # Solo nos interesan los archivos Markdown
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Encontramos todas las URLs en el archivo
                        potential_urls = url_pattern.findall(content)
                        for url in potential_urls:
                            # Filtramos para quedarnos solo con las que terminan en .pdf
                            if url.lower().endswith(".pdf"):
                                pdf_links.add(url)
                except Exception as e:
                    print(f"No se pudo leer el archivo {file_path}: {e}")

    return sorted(list(pdf_links))

if __name__ == "__main__":
    # Hacemos el script más flexible para que puedas decirle dónde está el repositorio
    parser = argparse.ArgumentParser(description="Encuentra enlaces a PDF en un repositorio local de libros.")
    parser.add_argument("repo_path", help="La ruta a la carpeta del repositorio 'free-programming-books' clonado.")
    
    args = parser.parse_args()

    links = find_pdf_links_in_repo(args.repo_path)

    if links:
        print(f"\n--- ¡Éxito! Se encontraron {len(links)} enlaces a PDF únicos ---")
        for link in links:
            print(link)
        print("\nAhora puedes copiar estos enlaces a tu script 'collect_books.py'")
    else:
        print("\nNo se encontraron enlaces a PDF en la ruta especificada.")