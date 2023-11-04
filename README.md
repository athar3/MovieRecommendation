# Laporan Proyek Machine Learning - Muhammad Athar Althariq Irawan

## Domain Proyek

Rekomendasi film (_movie recommendation_) adalah salah satu aspek yang sangat penting dalam industri hiburan, terutama dalam membantu penonton menemukan film yang sesuai dengan preferensi mereka. Dalam proyek ini, akan digunakan metode _content-based filtering_ untuk memberikan rekomendasi film kepada penonton berdasarkan konten atau karakteristik film yang mereka sukai.

### Contoh Kasus:
Seorang pengguna ingin menerima rekomendasi film berdasarkan film-film yang telah mereka tonton dan sukai sebelumnya. Dengan menganalisis karakteristik film seperti berdasarkan dari ringkasan, sistem dapat memberikan rekomendasi film yang memiliki kesamaan karakteristik dengan film-film yang mereka sukai.


Format Referensi: [Credit risk assessment mechanism of personal auto loan based on PSO-XGBoost Model](https://doi.org/10.1007/s40747-022-00854-y) 

## Business Understanding

### Problem Statements

Masalah latar belakang:

- Bagaimana dapat memberikan rekomendasi film kepada pengguna berdasarkan film-film yang mereka sukai?
- Bagaimana dapat mengidentifikasi kesamaan antara film-film yang telah ditonton oleh pengguna dan film-film lainnya berdasarkan karakteristik seperti genre, sutradara, pemain, dan peringkat?
- Bagaimana mengimplementasikan content-based filtering untuk memberikan rekomendasi yang relevan kepada pengguna?

### Goals

Tujuan dari pernyataan masalah:

- Memberikan rekomendasi film kepada pengguna berdasarkan karakteristik film yang mereka sukai.
- Mengidentifikasi kesamaan antara film-film yang telah ditonton oleh pengguna dan film-film lainnya.
- Mengimplementasikan content-based filtering untuk memberikan rekomendasi yang relevan kepada pengguna.


### Solution statements
- Melakukan analisis data, eksplorasi data film, dan persiapan data.
- Mengembangkan model content-based filtering berdasarkan karakteristik film.
- Memberikan rekomendasi film kepada pengguna berdasarkan ringkasan film.
MASIH PERLU DIPERBAIKI


## Data Understanding
 Data yang didapat dan digunakan pada proyek ini didapat dari: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv).

- dataset ini berbentuk .zip yang berisi 2 file `.csv`.
- dataset memiliki 4803 baris 
- Terdapat beberapa baris yang kosong (missing value) tapi karena tidak berpengaruh maka dibiarkan saja. 

### Exploratory Data Analysis
- Grade
![Grade](gambar\image-2.png)
merupakan resiko peminjaman yang dibuat oleh perusahaan, dari A-G dimana G merupakan resiko peminjaman paling besar.

## Data Preparation
Teknik yang digunakan dalam Data Preparation yaitu:
- Menghapus fitur yang tidak diperlukan: akan dilakukan drop kolom dikarenakan kebanyakan kolom pada dataset tidak digunakan dalam proses menganalisa kredit, maka sebagian akan dihapus.
- _Merge Dataset_ : Akan dilakukan penggabungan 2 dataset `.csv` menjadi 1. Ini digunakan untuk memudahkan proses pembuatan _movie recommender_.


## Modeling
Model yang digunakan proyek kali ini yaitu XGBoost (eXtreme Gradient Boosting). extreme gradien merupakan algoritma Machine Learning yang mencoba memprediksi variabel target secara akurat dengan menggabungkan gabungan perkiraan dari serangkaian model yang lebih sederhana. Algoritma XGBoost berkinerja baik dalam machine learning karena penanganannya yang kuat untuk berbagai jenis data, hubungan, distribusi, dan variasi hyperparameter yang dapat disesuaikan.

Sebuah fungsi evaluate_model digunakan untuk mengevaluasi kinerja model dengan menggunakan metrik tertentu (dalam hal ini, F1-score).

Fungsi robust_evaluate_model digunakan untuk menangani kesalahan dan peringatan yang mungkin muncul selama evaluasi.

Fungsi evaluate_models digunakan untuk mengevaluasi semua model yang telah didefinisikan sebelumnya.

Fungsi summarize_results digunakan untuk mencetak ringkasan hasil evaluasi model.

## Evaluation
di proyek ini, model yang dibuat merupakan kasus klasifikasi dan menggunakan beberapa metriks seperti:
- akurasi: Akurasi merupakan kalkulasi presentase jumlah ketepatan prediksi dari jumlah seluruh data yang diprediksi.
Dinyatakan dalam persentase, akurasi = (Jumlah prediksi benar) / (Jumlah total data).
pada model ini mendapatkan hasil:

|Train Score   |0.8864233625971649   |
|---|---|
|Test Score   |0.8926334625708321   |

Hasil penerapan akurasi pada proyek ini:

|Train Score   |0.8864233625971649   |

yang berarti pada data pelatihan model berhasil memprediksi dengan benar sekitar 88.64% dari semua sampel.

|Test Score   |0.8926334625708321   | 

yang berarti pada data pengujian model berhasil memprediksi dengan benar sekitar 89.26% dari semua sampel.


- f1 score: nilai Harmonic Mean (Rata-rata Harmonik) dari Precision dan Recall.
Precision adalah sejauh mana prediksi positif model adalah benar. Precision dihitung sebagai (True Positives) / (True Positives + False Positives).
Recall adalah sejauh mana model dapat mendeteksi semua instance yang benar. Recall dihitung sebagai (True Positives) / (True Positives + False Negatives).
F1-score memberikan keseluruhan pengukuran performa model yang mempertimbangkan trade-off antara Precision dan Recall.

|   |  f1-score |
|---|---|
|  0_good_loan |  0.99 |
|  1_bad_loan |  0.89 |

Hasil penerapan F1-score pada proyek ini:

F1-score untuk kelas pertama: 0.99 (dapat diinterpretasikan sebagai sangat baik)
F1-score untuk kelas kedua: 0.89 (dapat diinterpretasikan sebagai baik)
