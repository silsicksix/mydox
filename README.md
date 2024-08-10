# Doxing

Skrip ini memproses fail dalam pelbagai format (.csv, .xlsx, .pdf, .docx, .txt) untuk mencari dan memaparkan data berdasarkan kata kunci yang diberikan. Hasil carian ditampilkan dalam bentuk jadual berformat dan termasuk pautan yang boleh diklik untuk carian Google dan peta Google.

## Prasyarat

Pastikan anda mempunyai Python 3.6 atau yang lebih baru dipasang pada sistem anda. Anda juga perlu memasang beberapa pustaka Python yang diperlukan oleh skrip ini. Anda boleh memasangnya dengan menggunakan `requirements.txt`.

## Arahan Pemasangan

1. **Clone repositori:**

   ```bash
   git clone https://github.com/silsicksix/mydox.git
   cd repository-name
   ```

2. **Muat turun dan pasang keperluan:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Download model spaCy:**

   ```bash
   python -m spacy download en_core_web_sm
   ```

4. **Jalankan skrip:**

   ```bash
   python src/cari.py
   ```

Pastikan anda telah menyediakan folder `data` dengan fail yang sesuai untuk diuji.

## Contoh Penggunaan

Skrip ini memerlukan input dari pengguna untuk menentukan kata kunci dan bilangan hasil yang ingin dipaparkan. Contohnya:

Masukkan nilai yang ingin dicari: AHMAD BIN SULAIMAN
Masukkan bilangan hasil yang ingin dipaparkan: 5
Hasil carian akan dipaparkan dalam terminal dengan pautan yang boleh diklik untuk carian Google dan peta Google jika ada alamatnya.

## Kredit

Skrip ini menggunakan beberapa pustaka dan model berikut:
- [spaCy](https://spacy.io/)
- [transformers](https://huggingface.co/transformers/)
- [tabulate](https://pypi.org/project/tabulate/)


# Python bytecode files
*.pyc
__pycache__/

# Jupyter Notebook checkpoints
.ipynb_checkpoints/

# Environment
.env

# Virtual environment
venv/

