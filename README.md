# Dokumentasi Proyek Prediksi Penyakit Batu Ginjal

## Pendahuluan
Proyek ini bertujuan untuk membangun sistem prediksi penyakit batu ginjal menggunakan algoritma machine learning berbasis **Decision Tree Classifier**. Sistem ini dirancang untuk membantu tenaga kesehatan, terutama di daerah pedalaman, dalam melakukan deteksi dini penyakit batu ginjal berdasarkan data kesehatan pasien.

---

## Fitur Utama
1. **Prediksi Penyakit**
   - Memprediksi kemungkinan pasien menderita penyakit batu ginjal berdasarkan data kesehatan yang dimasukkan.
2. **Visualisasi Hasil**
   - **Confusion Matrix**: Menunjukkan tingkat kesalahan dan keberhasilan prediksi.
   - **Decision Tree Plot**: Memberikan transparansi pada proses pengambilan keputusan model.
3. **Antarmuka Web**
   - Dibangun menggunakan framework **Streamlit** yang mudah digunakan.

---

## Struktur Proyek
- **`web_functions.py`**: Mengelola fungsi utama seperti pemrosesan data, pelatihan model, dan prediksi.
- **`predict.py`**: Mengatur antarmuka Streamlit untuk menerima input pengguna dan menampilkan hasil prediksi.
- **Dataset**: File CSV berisi data kesehatan pasien.

---

## Cara Menggunakan

### Prasyarat
- Python 3.8 atau lebih baru.
- Pustaka yang diperlukan:
  ```bash
  pip install streamlit pandas scikit-learn
  ```

### Menjalankan Aplikasi
1. Clone repositori ini:
   ```bash
   git clone https://github.com/username/kidney-stone-prediction.git
   ```
2. Pindah ke direktori proyek:
   ```bash
   cd kidney-stone-prediction
   ```
3. Jalankan aplikasi Streamlit:
   ```bash
   streamlit run predict.py
   ```
4. Akses aplikasi melalui browser di `http://localhost:8501`.

---

## Penjelasan Dataset
Dataset `kidney-disease.csv` terdiri dari beberapa atribut utama:
- **Tekanan Darah (bp)**: Angka tekanan darah pasien.
- **Kadar Hemoglobin (hemo)**: Tingkat hemoglobin dalam darah.
- **Albumin Urin (al)**: Tingkat albumin dalam urin.
- **Klasifikasi (classification)**: Label target (0 = tidak terkena batu ginjal, 1 = terkena batu ginjal).

---

## Akurasi Model
Model prediksi menggunakan algoritma **Decision Tree Classifier** dengan tingkat akurasi **75%** berdasarkan pengujian awal menggunakan data pelatihan.

---

## Kontribusi
1. Fork repositori ini.
2. Buat branch fitur baru:
   ```bash
   git checkout -b fitur-anda
   ```
3. Lakukan perubahan dan commit:
   ```bash
   git commit -m "Menambahkan fitur baru"
   ```
4. Push ke branch Anda:
   ```bash
   git push origin fitur-anda
   ```
5. Kirim Pull Request.

---


