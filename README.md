# Laporan Proyek Machine Learning - Muhammad Athar Althariq Irawan

## Project Overview

Rekomendasi film (_movie recommendation_) adalah salah satu aspek yang sangat penting dalam industri hiburan, terutama dalam membantu penonton menemukan film yang sesuai dengan preferensi mereka. Dalam proyek ini, akan digunakan metode _content-based filtering_ untuk memberikan rekomendasi film kepada penonton berdasarkan konten atau karakteristik film yang mereka sukai.

### Contoh Kasus:
Seorang pengguna ingin menerima rekomendasi film berdasarkan film-film yang telah mereka tonton dan sukai sebelumnya. Dengan menganalisis karakteristik film seperti berdasarkan dari ringkasan, sistem dapat memberikan rekomendasi film yang memiliki kesamaan karakteristik dengan film-film yang mereka sukai.

## Business Understanding

### Problem Statements

Masalah latar belakang:

- Bagaimana dapat memberikan rekomendasi film kepada pengguna berdasarkan ringkasan film-film yang mereka sukai?
- Bagaimana dapat mengidentifikasi kesamaan antara film-film yang telah ditonton oleh pengguna dan film-film lainnya berdasarkan karakteristik seperti berdasarkan dari ringkasan?
- Bagaimana mengimplementasikan content-based filtering untuk memberikan rekomendasi yang relevan kepada pengguna?

### Goals

Tujuan dari pernyataan masalah:

- Memberikan rekomendasi film kepada pengguna berdasarkan karakteristik film yang mereka sukai.
- Mengidentifikasi kesamaan antara film-film yang telah ditonton oleh pengguna dan film-film lainnya.
- Mengimplementasikan content-based filtering untuk memberikan rekomendasi yang relevan kepada pengguna.


### Solution statements
- Melakukan analisis data, eksplorasi data film, dan _data preparation_.
- Mengembangkan model content-based filtering berdasarkan ringkasan film.
- Memberikan rekomendasi film kepada pengguna berdasarkan ringkasan film.


## Data Understanding
 Data yang didapat dan digunakan pada proyek ini didapat dari: [TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata?select=tmdb_5000_movies.csv).

- dataset ini berbentuk .zip yang berisi 2 file `.csv`.
- dataset memiliki 4803 baris 
- Terdapat beberapa baris yang kosong (missing value) tapi karena tidak berpengaruh maka dibiarkan saja.

### Penjelasan tiap kolom
- "title": Kolom ini berisi judul atau nama film, yang mengidentifikasi film tersebut.
- "cast": Kolom ini berisi daftar para pemeran atau aktor yang berperan dalam film.
- "crew": Kolom ini berisi informasi mengenai para anggota kru atau staf yang terlibat dalam produksi film, seperti sutradara, produser, sinematografer, dan lainnya.
- "budget": Kolom ini berisi informasi mengenai anggaran (biaya) produksi film.
- "genres": Kolom ini berisi genre-genre film.
- "homepage": Kolom ini berisi tautan ke halaman web resmi film.
- "id": Kolom ini berisi identifikasi unik untuk setiap film dalam dataset.
- "keywords": Kolom ini berisi kata kunci yang berkaitan dengan film.
- "original_language": Kolom ini berisi bahasa asli film.
- "original_title": Kolom ini berisi judul asli film.
- "overview": Kolom ini berisi ringkasan atau deskripsi singkat film.
- "popularity": Kolom ini berisi tingkat popularitas film.
- "production_companies": Kolom ini berisi daftar perusahaan produksi yang terlibat dalam pembuatan film.
- "production_countries": Kolom ini berisi negara-negara tempat film diproduksi.
- "release_date": Kolom ini berisi tanggal rilis film.
- "revenue": Kolom ini berisi pendapatan atau pemasukan film.
- "runtime": Kolom ini berisi durasi atau panjang film dalam menit.
- "spoken_languages": Kolom ini berisi bahasa-bahasa yang digunakan dalam film.
- "status": Kolom ini berisi status produksi film.
- "tagline": Kolom ini berisi slogan atau tagline promosi film, dengan masalah mungkin terkait dengan data yang hilang.
- "title": Kolom ini berisi judul atau nama film.
- "vote_average": Kolom ini berisi rata-rata peringkat yang diberikan oleh penonton atau kritikus.
- "vote_count": Kolom ini berisi jumlah peringkat atau ulasan yang diberikan kepada film.


### Exploratory Data Analysis
- vote_count

![image](https://github.com/athar3/MovieRecommendation/assets/72434013/cdcce5f7-1367-4bac-9399-08e538fcf224)

Berisi list film dengan nilai vote terbanyak

- popularity
  
![image](https://github.com/athar3/MovieRecommendation/assets/72434013/48f1d89b-51f0-471d-8354-5a9666c19c27)

Berisi list film paling populer.

- runtime
  
![image](https://github.com/athar3/MovieRecommendation/assets/72434013/c323a424-3038-4275-8768-467e7d2c0e8b)

berisi list film dengan runtime terlama.

- vote_count

![image](https://github.com/athar3/MovieRecommendation/assets/72434013/cdcce5f7-1367-4bac-9399-08e538fcf224)

berisi list film dengan nilai vote terbanyak.

- budget

![image](https://github.com/athar3/MovieRecommendation/assets/72434013/f6fb8e8d-7bdb-4079-bb3f-8fe2b972e452)

berisi list film dengan budget tertinggi.

- revenue

![image](https://github.com/athar3/MovieRecommendation/assets/72434013/e56f2c22-e5e7-44d1-b5a1-bcf7270331ed)

berisi list film dengan pendapatan tertinggi.



## Data Preparation
Teknik yang digunakan dalam Data Preparation yaitu:
- Menghapus fitur yang tidak diperlukan: akan dilakukan drop kolom dikarenakan kebanyakan kolom pada dataset tidak digunakan dalam proses menganalisa kredit, maka sebagian akan dihapus.
- _Merge Dataset_ : Akan dilakukan penggabungan 2 dataset `.csv` menjadi 1. Ini digunakan untuk memudahkan proses pembuatan _movie recommender_.


## Modeling
### Content Based Filtering
Content-based filtering adalah salah satu metode dalam sistem rekomendasi yang mengandalkan informasi tentang item yang disukai oleh pengguna untuk memberikan rekomendasi. Rumus dasar untuk content-based filtering adalah menghitung sejauh mana item-item dalam dataset cocok dengan preferensi pengguna berdasarkan atribut-atribut tertentu. Rumusnya dapat dijelaskan sebagai berikut:

$Precision@K = \frac{\ of\ recommended\ items\ that\ are\ relevant}{\ of\ recommended\ items}$


#### Representasi Pengguna (User Profile):
Pertama, perlu menghitung profil preferensi pengguna terhadap atribut-atribut yang relevan. Ini bisa dilakukan dengan cara menjumlahkan atau menghitung bobot dari atribut-atribut yang dimiliki oleh item-item yang disukai oleh pengguna. Jika pengguna memberikan peringkat pada item, bobot bisa berdasarkan peringkat. Contohnya, jika pengguna suka film-film komedi dengan peringkat tinggi, maka bobot komedi dalam profil pengguna akan tinggi.

Sebagai contoh, jika memiliki pengguna U dan atribut-atribut A1, A2, ..., An, maka profil pengguna U terhadap atribut A dapat dihitung sebagai berikut:

$Profil(U, A) = \sum_{i=1}^{n} w_i \cdot A_i$
di mana:
- Profil(U, A) adalah profil preferensi pengguna U terhadap atribut A.
- w_i adalah bobot yang mengindikasikan sejauh mana pengguna U menyukai atribut A_i.
- A_i adalah nilai atribut dari item yang disukai oleh pengguna U.

#### Rekomendasi:
Setelah profil preferensi pengguna dihitung, dapat menghitung sejauh mana setiap item dalam dataset cocok dengan profil pengguna. Salah satu metode yang umum digunakan adalah menghitung kesamaan kosinus (cosine similarity) antara profil pengguna dan atribut-atribut item. Item dengan kesamaan kosinus yang lebih tinggi akan dianggap sebagai rekomendasi yang lebih sesuai. Rumus untuk menghitung kesamaan kosinus adalah sebagai berikut:

$Cosine\_Similarity(U, I) = \frac{Profil(U) \cdot Profil(I)}{||Profil(U)|| \cdot ||Profil(I)||}$
di mana:
- U adalah pengguna.
- I adalah item yang akan dinilai kemungkinan disukai oleh pengguna U.
- Profil(U) adalah profil preferensi pengguna U terhadap atribut-atribut.
- Profil(I) adalah profil atribut item I.
- |Profil(U)| dan |Profil(I)| adalah norma Euclidean dari masing-masing profil.

Item dengan nilai Cosine_Similarity yang lebih tinggi akan menjadi rekomendasi yang lebih potensial untuk pengguna tersebut.


##### Kelebihan
- Tidak memerlukan data apapun terhadap pengguna
- Dapat merekomendasikan item khusus

##### Kekurangan
- Membutuhkan banyak pengetahuan suatu domain
- Membuat rekomendasi berdasarkan minat pengguna yang ada saja

#### Hasil
<img width="265" alt="image" src="https://github.com/athar3/MovieRecommendation/assets/72434013/e38010fc-863f-4814-88bc-094ccb07369a">

**Output**

|  |      |
|------|-----------------------|
| 3604 |     Apollo 18        |
| 2130 |    The American      |
|  634 |     The Matrix       |
| 1341 | The Inhabited Island |
|  529 |  Tears of the Sun    |
| 1610 |        Hanna          |
|  311 | The Adventures of Pluto Nash |
|  847 |       Semi-Pro        |
|  775 |      Supernova       |
| 2628 | Blood and Chocolate  |


Terlihat bahwa rekomendasi dari film Avatar keseluruhannya adalah film-film bertema petualangan. Ini dikarenakan deskripsi film avatar merupakan film petualangan dan film-film yang direkomendasikan juga merupakan film petualangan berdasarkan deskripsi.

## Evaluation
Untuk evaluasi dari sistem rekomendasi dengan pendekatan *content based filtering* dapat menggunakan salah satu metric yaitu *precision@K*. Yaitu *Precision* adalah perbandingan antara *True Positive (TP)* dengan banyaknya data yang diprediksi positif. Atau juga bisa ditulis secara matematis sebagai berikut :

*precision = TP / (TP + FP)*

dimana :
TP = *True Positive* atau positif yang sebenarnya
FP = *False Positive* atau positif yang salah dari hasil prediksi

Namun pada sistem rekomendasi tidak akan menggunakan *True positive* atau *False Positive* melainkan *overview* yang diberikan pada film untuk menentukan buku yang direkomendasikan relevan atau tidak. Dengan rumus sebagai berikut :

$Precision@K = \frac{\ of\ recommended\ items\ that\ are\ relevant}{\ of\ recommended\ items}$

Evaluasi dengan precision@K memberikan gambaran tentang seberapa baik sistem rekomendasi dalam menghadirkan item yang sesuai di antara K rekomendasi pertama yang diberikan kepada pengguna. Semakin tinggi nilai precision@K, semakin baik sistem dalam menghadirkan item yang relevan ke pengguna dalam K rekomendasi pertama.

Dalam konteks Content-Based Filtering, sistem menggunakan atribut atau konten item, seperti deskripsi atau overview pada film, untuk membuat rekomendasi. Penggunaan precision@K membantu mengukur sejauh mana metode ini berhasil dalam mencocokkan atribut atribut pengguna dengan atribut item dan menghasilkan rekomendasi yang sesuai. Nilai precision@K yang tinggi menunjukkan bahwa sistem dapat mengidentifikasi dengan baik item-item yang sesuai dengan preferensi pengguna berdasarkan atribut kontennya.


<img width="406" alt="image" src="https://github.com/athar3/MovieRecommendation/assets/72434013/61bb4574-8adc-4891-a891-5bc770b6127e">

|   title                         |   genres                                                      |
|---------------------------------|---------------------------------------------------------------|
|   Apollo 18                    |   [{"id": 27, "name": "Horror"}, {"id": 53, "name": ...     |
|   The American                  |   [{"id": 80, "name": "Crime"}, {"id": 18, "name": ...     |
|   The Matrix                  |   [{"id": 28, "name": "Action"}, {"id": 878, "na...       |
|   The Inhabited Island   |   [{"id": 28, "name": "Action"}, {"id": 14, "nam...       |
|   Tears of the Sun           |   [{"id": 28, "name": "Action"}, {"id": 18, "nam...       |
|   Hanna                           |   [{"id": 28, "name": "Action"}, {"id": 53, "nam...       |
|   The Adventures of Pluto Nash |   [{"id": 28, "name": "Action"}, {"id": 35, "nam...       |
|   Semi-Pro                       |   [{"id": 35, "name": "Comedy"}]                             |
|   Supernova                    |   [{"id": 27, "name": "Horror"}, {"id": 878, "na...       |
|   Blood and Chocolate    |   [{"id": 18, "name": "Drama"}, {"id": 14, "name...       |

Maka hasil evaluasi adalah:

Precision = #of recommendation that are relevant/#of item we recommend.

Pada contoh rekomendasi film di atas:

Precission = 5/10.

Jadi presisinya = 50%

## Rujukan
- [Implementasi Algoritma Cosine Similarity Dan Metode TF-IDF Berbasis PHP Untuk Menghasilkan Rekomendasi Seminar](https://publikasi.mercubuana.ac.id/index.php/fasilkom/article/view/8830/3555) 
