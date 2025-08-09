import arxiv

# Temas que queremos buscar
SEARCH_QUERIES = [
    '"software architecture"',
    '"design patterns"',
    '"domain driven design"',
    '"clean architecture"'
]

# Número máximo de resultados por búsqueda
MAX_RESULTS = 20

print("Buscando artículos académicos en arXiv...")

try:
    all_papers = {} # Usamos un diccionario para evitar duplicados por ID

    for query in SEARCH_QUERIES:
        print(f"\n--- Buscando sobre: {query} ---")
        search = arxiv.Search(
            query = query,
            max_results = MAX_RESULTS,
            sort_by = arxiv.SortCriterion.Relevance
        )

        for result in search.results():
            # Guardamos el título y el enlace al PDF
            all_papers[result.entry_id] = {
                "title": result.title,
                "pdf_url": result.pdf_url
            }

    print(f"\n\n--- Total de {len(all_papers)} artículos únicos encontrados ---")
    for paper_id, details in all_papers.items():
        print(f"Título: {details['title']}")
        print(f"URL: {details['pdf_url']}\n")


except Exception as e:
    print(f"Ocurrió un error: {e}")