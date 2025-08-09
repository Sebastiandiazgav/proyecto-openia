import requests
import os

# --- Lista de 37 recursos de élite para el fine-tuning ---
RESOURCES_URLS = {
    # === Artículos Académicos de arXiv ===
    "cs_0105010v1_arch_complexity.pdf": "http://arxiv.org/pdf/cs/0105010v1",
    "2308.09978v2_arch_practice_challenges.pdf": "http://arxiv.org/pdf/2308.09978v2",
    "2505.16697v1_arch_meets_llms.pdf": "http://arxiv.org/pdf/2505.16697v1",
    "2103.07950v2_arch_for_ml.pdf": "http://arxiv.org/pdf/2103.07950v2",
    "2204.11657v1_sustainability_in_arch.pdf": "http://arxiv.org/pdf/2204.11657v1",
    "2301.07516v1_quality_attributes_optimization.pdf": "http://arxiv.org/pdf/2301.07516v1",
    "cs_0105008v1_slicing_architectures.pdf": "http://arxiv.org/pdf/cs/0105008v1",
    "cs_0105009v1_dependence_analysis_arch.pdf": "http://arxiv.org/pdf/cs/0105009v1",
    "1903.11944v1_dui_design_patterns.pdf": "http://arxiv.org/pdf/1903.11944v1",
    "1808.08433v1_ontology_design_patterns.pdf": "http://arxiv.org/pdf/1808.08433v1",
    "1906.01419v1_design_pattern_violations.pdf": "http://arxiv.org/pdf/1906.01419v1",
    "2310.01905v4_domain_driven_design_review.pdf": "http://arxiv.org/pdf/2310.01905v4",
    "2003.02603v1_microservice_decomposition.pdf": "http://arxiv.org/pdf/2003.02603v1",
    "2108.03758v1_consistency_distributed_systems.pdf": "http://arxiv.org/pdf/2108.03758v1",
    "2108.04621v1_refactoring_to_clean_architecture.pdf": "http://arxiv.org/pdf/2108.04621v1",
    "1709.02840_beautiful_code_leading_to_beautiful_software.pdf": "https://arxiv.org/pdf/1709.02840.pdf",
    # === Libros y Guías Prácticas ===
    "RLbook2020_sutton_barto.pdf": "http://incompleteideas.net/book/RLbook2020.pdf",
    "mmds_book_mining_massive_datasets.pdf": "http://infolab.stanford.edu/~ullman/mmds/book.pdf",
    "HOPL2_history_of_programming_languages.pdf": "http://www.dreamsongs.com/Files/HOPL2-Uncut.pdf",
    "isml_intro_to_statistical_learning.pdf": "http://www.cs.cmu.edu/~rwh/isml/book.pdf",
    "designing_event_driven_systems.pdf": "https://assets.confluent.io/m/7a91acf41502a75e/original/20180328-EB-Confluent_Designing_Event_Driven_Systems.pdf",
    "compiler_design_in_c.pdf": "https://holub.com/goodies/compiler/compilerDesignInC.pdf",
    "Algorithms-JeffE.pdf": "https://jeffe.cs.illinois.edu/teaching/algorithms/book/Algorithms-JeffE.pdf",
    "joy_of_cryptography.pdf": "https://joyofcryptography.com/pdf/book.pdf",
    "api_design_ebook.pdf": "https://pages.apigee.com/rs/apigee/images/api-design-ebook-2012-03.pdf",
    "building_secure_and_reliable_systems.pdf": "https://static.googleusercontent.com/media/landing.google.com/en//sre/static/pdf/Building_Secure_and_Reliable_Systems.pdf",
    "daily_design_pattern.pdf": "https://web.archive.org/web/20170930132000/https://www.exceptionnotfound.net/downloads/dailydesignpattern.pdf",
    "oodesign_python_book.pdf": "https://web.archive.org/web/20150824204101/http://buildingskills.itmaybeahack.com/book/oodesign-python-2.2/latex/BuildingSkillsinOODesign.pdf",
    "haskell_school_of_music.pdf": "https://www.cs.yale.edu/homes/hudak/Papers/HSoM.pdf",
    "design_of_approximation_algorithms.pdf": "https://www.designofapproxalgs.com/book.pdf",
    "bishop_pattern_recognition_and_ml.pdf": "https://www.microsoft.com/en-us/research/uploads/prod/2006/01/Bishop-Pattern-Recognition-and-Machine-Learning-2006.pdf",
    "practical_file_system_design.pdf": "https://www.nobius.org/~dbg/practical-file-system-design.pdf",
    "sicp_structure_and_interpretation.pdf": "https://web.mit.edu/6.001/6.037/sicp.pdf",
    "cambridge_object_oriented_programming.pdf": "https://www.cl.cam.ac.uk/teaching/0910/OOProg/OOP.pdf",
    "beautiful_code_renci.pdf": "https://web.archive.org/web/20160411023943/http://www.renci.org/wp-content/pub/tutorials/BeautifulCode.pdf",
    "ingenieria_software_wolnm.pdf": "https://web.archive.org/web/20150824055042/http://www.wolnm.org/apa/articulos/Ingenieria_Software.pdf"
}

# Directorio donde se guardarán los libros
OUTPUT_DIR = "../data/raw_books"

def download_resource(url, file_path):
    """Descarga un archivo desde una URL y lo guarda en la ruta especificada."""
    try:
        if os.path.exists(file_path):
            print(f"✔️ El archivo {os.path.basename(file_path)} ya existe. Omitiendo.")
            return

        print(f"⏬ Descargando {os.path.basename(file_path)}...")
        # Usamos un User-Agent para parecer un navegador normal y evitar bloqueos
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        response = requests.get(url, stream=True, headers=headers, timeout=60)
        response.raise_for_status()  # Lanza un error si la descarga falla (ej. 404)

        with open(file_path, "wb") as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"✅ Descarga completada: {os.path.basename(file_path)}")

    except requests.exceptions.RequestException as e:
        print(f"❌ Error al descargar {url}: {e}")

if __name__ == "__main__":
    # Asegurarse de que el directorio de salida exista
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    print(f"--- Iniciando descarga de {len(RESOURCES_URLS)} recursos de élite ---")
    
    # Descargar todos los recursos de nuestra lista curada
    for filename, url in RESOURCES_URLS.items():
        full_path = os.path.join(OUTPUT_DIR, filename)
        download_resource(url, full_path)
    
    print("\n--- ¡Proceso de descarga finalizado! ---")
    print(f"Revisa la carpeta '{os.path.abspath(OUTPUT_DIR)}' para ver los archivos.")