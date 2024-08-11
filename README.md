# Panduan Menggunakan Doxing

Panduan ini akan memandu Anda untuk menjalankan skrip Python yang memproses berbagai format file untuk mencari dan menyoroti teks yang relevan. Skrip ini juga akan menganalisis teks untuk entiti seperti nama, nombor telefon, nombor IC, dan alamat.
Prasyarat

Sebelum Anda memulakan, pastikan anda mempunyai:

    Python 3.7 atau lebih tinggi: Pastikan Python sudah dipasang di sistem anda. Anda boleh memuat turun Python dari laman web rasmi Python.

    Pakej-pakej yang diperlukan: Skrip ini memerlukan beberapa pustaka Python yang akan diinstal melalui requirements.txt.

Langkah-Langkah:
Clone repositori GitHub ini ke mesin anda:
1. **Clone repositori:**

   ```bash
   git clone https://github.com/silsicksix/mydox.git
   cd mydox
   ```

2. Buat dan Aktifkan Persekitaran Maya

Disarankan untuk menggunakan persekitaran maya untuk mengelakkan konflik antara pakej-pakej Python:
  ```bash
python -m venv env
source env/bin/activate  # Pada Windows, gunakan `env\Scripts\activate`
 ```

3. Pasang Keperluan

Pasang semua pustaka yang diperlukan menggunakan requirements.txt:
  ```bash
pip install -r requirements.txt
 ```

4. Muat Turun Model spaCy

Skrip ini menggunakan model bahasa spaCy untuk analisis teks. Muat turun model yang diperlukan dengan arahan berikut:
  ```bash
python -m spacy download en_core_web_md
 ```

5. Sediakan Fail-fail Anda

Pastikan anda mempunyai fail yang ingin diproses dalam folder tertentu. Folder ini perlu mengandungi fail-fail dengan format .csv, .xls, .xlsx, .pdf, .docx, dan .txt dan lain-lain.
  ```bash
Ubah nilai folder_path dalam skrip Python anda kepada laluan folder di mana fail-fail tersebut berada. Lihat pada line 
bernombor 241 (/home/kali/Documents/test) ubah kepada lokasi dimana anda letakkan file dan skrip ini.
 ```
6. Jalankan Skrip

Jalankan skrip Python dengan arahan berikut:
  ```bash
python cari.py
 ```

7. Masukkan Nilai Carian dan Bilangan Hasil

Apabila diminta, masukkan nilai yang ingin dicari dalam fail dan bilangan hasil yang ingin dipaparkan. Skrip ini akan memproses setiap fail dalam folder dan memaparkan hasil yang sesuai di terminal.
Contoh Hasil

Skrip ini akan memaparkan hasil yang dipadankan dari fail yang diproses, menyoroti kata kunci, dan memberikan pautan Google untuk carian dan Google Maps untuk alamat.
Masalah yang Mungkin Timbul

Jika anda mengalami masalah seperti kegagalan memuatkan model spaCy atau masalah dengan pemasangan pustaka, pastikan anda telah mengikuti langkah-langkah di atas dengan betul. Semak juga sambungan internet anda dan cuba jalankan semula skrip.
Sokongan

Jika anda memerlukan bantuan tambahan, sila buka isu baru di repositori GitHub ini atau hubungi saya melalui Telegram di [@KanDear].
   ```

Pastikan anda telah menyediakan folder `data` dengan fail yang sesuai untuk diuji.

## Contoh Penggunaan

Skrip ini memerlukan input dari pengguna untuk menentukan kata kunci dan bilangan hasil yang ingin dipaparkan. Contohnya:

Masukkan nama yang ingin dicari: AHMAD BIN SULAIMAN
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

