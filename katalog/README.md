# Tugas 2: Pengenalan Aplikasi Django dan Models View Template (MVT) pada Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

**Nama**  : Alicia Kirana Utomo

**NPM**   : 2106751505

**Kelas** : E

## Django Flow Diagram

![Django Flow Diagram](/resources/tugas-2-diagram.png)

Client akan memberikan request kepada url (`url.py`) yang lalu akan memanggil function pada view (`views.py`). Di sini, view terhubung dengan 2 file yang memiliki tugasnya masing masing. Template (`katalog.html`) memberikan tampilan/sisi Front-End dari aplikasi, sedangkan model (`models.py`) memberikan akses terhadap database (`initial_catalog_data.json`) yang akan ditampilkan.

## Mengapa menggunakan *virtual enviroment*?

Kita perlu menggunakan *virtual enviroment* untuk memastikan bahwa semua *developer* yang berkontribusi pada *project* sedang menggunakan *dependencies* yang sama. Hal ini akan mengurangi kemungkinan dari seorang *developer* yang memiliki *requirements* yang berbeda dan akan menimbulkan *error*.

## Apakah dapat membuat Django *project* tanpa *virtual enviroment*?

Bisa, tetapi seperti yang telah dijelaskan sebelumnya *project* memiliki kemungkinan lebih besar untuk menimbulkan *error*. Ini dikarenakan setiap *developer* tidak memiliki *requirements* yang sama dalam mengerjakan *project*.

## Tahap pengimplementasian

1. Menambahkan "katalog" ke dalam list app (`INSTALLED_APPS`) yang berada pada `project_django/settings.py`.

2. Membuat function `show_katalog` pada `views.py` yang berisi render file template (`katalog.html`) dan data yang akan dimasukan di dalam template tersebut.

3. Menambahkan katalog ke dalam list url (`urlpatterns`) pada `project_django/urls.py`.

4. Menambahkan "katalog" ke dalam nama aplikasi (`app_name`) pada `katalog/urls.py`.

5. Menggunakan data dari `views.py` dan mengimplementasikan data-data tersebut agar dapat di-*render* oleh html. Tahap ini dapat dilakukan dengan mengganti beberapa line program pada `katalog/templates/katalog.html`.

6. Agar data pada `katalog/fixtures/initial_catalog_data.json` dapat di-update, jalankan command di bawah di dalam terminal.

        python manage.py loaddata initial_catalog_data.json

7. Deploy project ke dalam Heroku:

    1. Membuat app baru pada Heroku
    
    2. Mengambil API Key yang terdapat pada akun Heroku

    3. Membuka repositori GitHub:

        - Menuju `Settings > Secrets > Actions`
        - Membuat 2 secret baru dengan nama `HEROKU_API_KEY` dengan value API key yang tadi telah didapatkan dan juga `HEROKU_APP_NAME` dengan value nama app yang baru saja dibuat di Heroku
        - Melakukan push terhadap project
        - Menuju bagian `Actions` pada repositori GitHub dan lakukan run atau re-run
        - Project telah selesai di-deploy ke Heroku

Hasil aplikasi Heroku yang telah dibuat [di sini](https://tugas-1-pbp.herokuapp.com/katalog/).