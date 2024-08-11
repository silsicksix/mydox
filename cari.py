import subprocess
import sys

def install_requirements():
    """Install requirements from requirements.txt if not already installed."""
    try:
        import pandas
        import spacy
        import os
        from tabulate import tabulate
        from colorama import Fore, Style, init
        from pyfiglet import Figlet
        from PyPDF2 import PdfReader
        import docx
        import re
        import webbrowser
    except ImportError as e:
        print(f"Missing module: {e.name}. Installing...")
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

# Call the function to ensure all requirements are installed
install_requirements()

# Import modules after ensuring they are installed
import spacy
import pandas as pd
import os
from tabulate import tabulate
from colorama import Fore, Style, init
from pyfiglet import Figlet
from PyPDF2 import PdfReader
import docx
import re
import webbrowser

# Muatkan model bahasa
nlp = spacy.load("en_core_web_lg")

# Contoh teks
text = "This is a sample sentence."
doc = nlp(text)

# Paparkan hasil analisis
for token in doc:
    print(f"{token.text}: {token.pos_}, {token.dep_}")

# Inisialisasi colorama
init(autoreset=True)

# Paparkan perkataan DOXING dengan gaya ASCII
def print_doxing_header():
    figlet = Figlet(font='big')
    doxing_text = figlet.renderText('DOXING')
    print(Fore.CYAN + Style.BRIGHT + doxing_text)
    print(Style.RESET_ALL)

# Install spacy dan model bahasa yang dibutuhkan
subprocess.check_call(["pip", "install", "spacy"])
subprocess.check_call(["python", "-m", "spacy", "download", "en_core_web_lg"])

# Load model bahasa spacy
nlp = spacy.load("en_core_web_lg")

# Kemaskini pandas jika perlu
subprocess.check_call(["pip", "install", "--upgrade", "pandas"])

# Paparkan perkataan DOXING sebelum memulakan pemprosesan
print_doxing_header()

def highlight_keyword(text, keyword):
    """Highlight keyword dalam teks"""
    if keyword.lower() in text.lower():
        start = text.lower().find(keyword.lower())
        end = start + len(keyword)
        return (text[:start] + Fore.YELLOW + Style.BRIGHT + text[start:end] + Style.RESET_ALL + text[end:])
    return text

def process_csv(file_path, search_value):
    """Proses fail CSV dan kembalikan data yang sesuai"""
    df = pd.read_csv(file_path, encoding='ISO-8859-1', on_bad_lines='skip', low_memory=False)
    return filter_dataframe(df, search_value)

def process_excel(file_path, search_value):
    """Proses fail Excel dan kembalikan data yang sesuai"""
    df = pd.read_excel(file_path)
    return filter_dataframe(df, search_value)

def process_pdf(file_path, search_value):
    """Proses fail PDF dan kembalikan teks yang sesuai"""
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return filter_text(text, search_value)

def process_docx(file_path, search_value):
    """Proses fail DOCX dan kembalikan teks yang sesuai"""
    doc = docx.Document(file_path)
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text + "\n"
    return filter_text(text, search_value)

def process_txt(file_path, search_value):
    """Proses fail TXT dan kembalikan teks yang sesuai"""
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    return filter_text(text, search_value)

def filter_dataframe(df, search_value):
    """Cari nilai dalam DataFrame dan kembalikan baris yang sesuai"""
    filtered_df = pd.DataFrame()
    for column in df.columns:
        if df[column].dtype == 'object':
            matched_rows = df[df[column].astype(str).str.contains(search_value, case=False, na=False)]
            if not matched_rows.empty:
                filtered_df = pd.concat([filtered_df, matched_rows], axis=0)
    return filtered_df.drop_duplicates()

def filter_text(text, search_value):
    """Cari nilai dalam teks dan kembalikan baris yang sesuai"""
    lines = text.splitlines()
    return [line for line in lines if search_value.lower() in line.lower()]

def generate_google_link(query):
    """Buat link Google search berdasarkan query"""
    google_search_query = f"https://www.google.com/search?q={'+'.join(query.split())}"
    return google_search_query

def generate_map_link(address):
    """Buat link Google Maps berdasarkan alamat"""
    google_map_query = f"https://www.google.com/maps/search/{'+'.join(address.split())}"
    return google_map_query

def analyze_text_with_spacy(text):
    """Analisa teks untuk mengenal pasti entiti seperti Nama, No Telefon, No IC, dan Alamat"""
    doc = nlp(text)
    entities = {'Name': [], 'Phone': [], 'IC': [], 'Address': []}

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            entities['Name'].append(ent.text)
        elif ent.label_ == "GPE" or ent.label_ == "LOC":
            entities['Address'].append(ent.text)
        elif re.match(r'\b\d{10,}\b', ent.text):  # Pencocokan sederhana untuk no telefon/IC
            entities['Phone'].append(ent.text)
        elif re.match(r'\b\d{12}\b', ent.text):  # Pencocokan sederhana untuk no IC
            entities['IC'].append(ent.text)
    
    return entities

def format_entities_for_output(entities):
    """Format entiti menjadi teks yang siap untuk dipaparkan di terminal dengan link Google"""
    output_lines = []
    for category, items in entities.items():
        for item in items:
            link = generate_google_link(item) if category != 'Address' else generate_map_link(item)
            output_lines.append(f"{category}: {highlight_keyword(item, item)} | Link: {link}")
    return output_lines

# Folder yang mengandungi fail
folder_path = '/home/kali/Documents/test'  # Gantikan dengan laluan sebenar folder anda

# Dapatkan senarai semua fail dalam folder
files = os.listdir(folder_path)

# Terima input dari pengguna untuk pencarian
search_value = input("Masukkan nilai yang ingin dicari: ").strip()

# Tanya pengguna berapa banyak hasil yang ingin dipaparkan
try:
    max_results = int(input("Masukkan bilangan hasil yang ingin dipaparkan: ").strip())
except ValueError:
    print("Sila masukkan nombor yang sah.")
    exit()

# Proses setiap fail
for file in files:
    file_path = os.path.join(folder_path, file)
    print(f"\nMemproses fail: {file}\n")

    try:
        if file.endswith('.csv'):
            # Proses CSV
            filtered_df = process_csv(file_path, search_value)
            if not filtered_df.empty:
                # Highlighting keywords dalam CSV
                for col in filtered_df.columns:
                    if filtered_df[col].dtype == 'object':
                        filtered_df[col] = filtered_df[col].apply(lambda x: highlight_keyword(str(x), search_value))
                table = tabulate(filtered_df.head(max_results), headers='keys', tablefmt='grid', showindex=False)
                print(table)
                for _, row in filtered_df.iterrows():
                    combined_text = ' '.join(str(val) for val in row)
                    entities = analyze_text_with_spacy(combined_text)
                    output_lines = format_entities_for_output(entities)
                    for line in output_lines:
                        print(line)
            else:
                print(f"Tidak terdapat sebarang hasil untuk '{search_value}' dalam fail '{file}'.")

        elif file.endswith('.xls') or file.endswith('.xlsx'):
            # Proses Excel
            filtered_df = process_excel(file_path, search_value)
            if not filtered_df.empty:
                table = tabulate(filtered_df.head(max_results), headers='keys', tablefmt='grid', showindex=False)
                print(table)
                for _, row in filtered_df.iterrows():
                    combined_text = ' '.join(str(val) for val in row)
                    entities = analyze_text_with_spacy(combined_text)
                    output_lines = format_entities_for_output(entities)
                    for line in output_lines:
                        print(line)
            else:
                print(f"Tidak terdapat sebarang hasil untuk '{search_value}' dalam fail '{file}'.")

        elif file.endswith('.pdf'):
            # Proses PDF
            filtered_text = process_pdf(file_path, search_value)
            if filtered_text:
                for line in filtered_text[:max_results]:
                    highlighted_line = highlight_keyword(line, search_value)
                    print(highlighted_line)
                    entities = analyze_text_with_spacy(highlighted_line)
                    output_lines = format_entities_for_output(entities)
                    for line in output_lines:
                        print(line)
            else:
                print(f"Tidak terdapat sebarang hasil untuk '{search_value}' dalam fail '{file}'.")

        elif file.endswith('.doc') or file.endswith('.docx'):
            # Proses DOCX
            filtered_text = process_docx
            # Proses DOCX
            filtered_text = process_docx(file_path, search_value)
            if filtered_text:
                for line in filtered_text[:max_results]:
                    highlighted_line = highlight_keyword(line, search_value)
                    print(highlighted_line)
                    entities = analyze_text_with_spacy(line)
                    output_lines = format_entities_for_output(entities)
                    for line in output_lines:
                        print(line)
            else:
                print(f"Tidak terdapat sebarang hasil untuk '{search_value}' dalam fail '{file}'.")

        elif file.endswith('.txt'):
            # Proses TXT
            filtered_text = process_txt(file_path, search_value)
            if filtered_text:
                for line in filtered_text[:max_results]:
                    highlighted_line = highlight_keyword(line, search_value)
                    print(highlighted_line)
                    entities = analyze_text_with_spacy(line)
                    output_lines = format_entities_for_output(entities)
                    for line in output_lines:
                        print(line)
            else:
                print(f"Tidak terdapat sebarang hasil untuk '{search_value}' dalam fail '{file}'.")

        else:
            print(f"Format fail '{file}' tidak disokong.")

    except Exception as e:
        print(f"Ralat pemprosesan fail: {e}")

    print("\n" + "="*40 + "\n")
