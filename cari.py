
import subprocess
import pandas as pd
import os
from tabulate import tabulate
from colorama import Fore, Style, init
from pyfiglet import Figlet

# Inisialisasi colorama
init(autoreset=True)

# Paparkan perkataan DOXING dengan gaya ASCII
def print_doxing_header():
    """Print perkataan DOXING dengan gaya ASCII"""
    figlet = Figlet(font='big')  # Anda boleh memilih font yang berbeza untuk kesan yang berbeza
    doxing_text = figlet.renderText('DOXING')
    print(Fore.CYAN + Style.BRIGHT + doxing_text)
    print(Style.RESET_ALL)

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

# Folder yang mengandungi fail CSV
folder_path = '/home/kali/Downloads'  # Gantikan dengan laluan sebenar folder anda

# Dapatkan senarai semua fail CSV dalam folder
csv_files = [f for f in os.listdir(folder_path) if f.endswith('.csv')]

# Terima input dari pengguna untuk pencarian
search_value = input("Masukkan nilai yang ingin dicari: ").strip()

# Tanya pengguna berapa banyak hasil yang ingin dipaparkan
try:
    max_results = int(input("Masukkan bilangan hasil yang ingin dipaparkan: ").strip())
except ValueError:
    print("Sila masukkan nombor yang sah.")
    exit()

# Proses setiap fail CSV
for file in csv_files:
    file_path = os.path.join(folder_path, file)
    print(f"\nMemproses fail: {file}\n")

    try:
        # Baca fail CSV menggunakan pandas dengan parameter encoding dan low_memory
        df = pd.read_csv(file_path, encoding='ISO-8859-1', on_bad_lines='skip', low_memory=False)

        # Cari maklumat yang spesifik dalam semua lajur
        filtered_df = pd.DataFrame()
        for column in df.columns:
            if df[column].dtype == 'object':  # Hanya cari dalam lajur dengan jenis data object (string)
                matched_rows = df[df[column].astype(str).str.contains(search_value, case=False, na=False)]
                if not matched_rows.empty:
                    # Highlight keyword dalam matched_rows
                    matched_rows[column] = matched_rows[column].astype(str).apply(lambda x: highlight_keyword(x, search_value))
                    filtered_df = pd.concat([filtered_df, matched_rows], axis=0)

        # Hadkan bilangan hasil yang dipaparkan
        filtered_df = filtered_df.head(max_results)

        if filtered_df.empty:
            print(f"Tidak terdapat sebarang hasil untuk '{search_value}' dalam fail '{file}'.")
        else:
            # Paparkan data dengan format yang baik menggunakan tabulate
            print(tabulate(filtered_df, headers='keys', tablefmt='grid', showindex=False))

    except pd.errors.ParserError as e:
        print(f"Ralat pemprosesan fail: {e}")
    except UnicodeDecodeError as e:
        print(f"Ralat pengkodan fail: {e}")

    print("\n" + "="*40 + "\n")
