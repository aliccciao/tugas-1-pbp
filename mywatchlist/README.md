# Tugas 2: Tugas 3: Pengimplementasian Data Delivery Menggunakan Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

**Nama**  : Alicia Kirana Utomo

**NPM**   : 2106751505

**Kelas** : B

## Perbedaan JSON, XML, dan HTML

HTML dan XML memiliki tampilan yang mirip yaitu menggunakan *opening* dan juga *closing* tags dalam menyimpan informasi atau data. Perbedaan antara keduanya adalah XML biasanya digunakan untuk menyimpan dan mengirim data dan HTML biasanya digunakan untuk memberikan tampilan ke dalam website.

## Mengapa memerlukan *data delivery*

Kita memerlukan *data delivery* untuk mempermudah platform untuk menerima data trhadap perangkat satu ke perangkat lainnya.

## Tahap pengimplementasian

1. Membuat aplikasi baru bernama `mywatchlist`.

2. Menambahkan "mywatchlist" ke dalam list app (`INSTALLED_APPS`) yang berada pada `project_django/settings.py`.

3. Membuat function `main`, `show_watchlist`, `show_xml`, `show_json`, `show_json_by_id`, dan `show_xml_by_id` pada `views.py`. Setiap function memiliki tugas yang berbeda sesuai dengan namanya masing masing.

4. Menambahkan katalog ke dalam list url (`urlpatterns`) pada `project_django/urls.py`.

5. Menambahkan "mywatchlist" ke dalam nama aplikasi (`app_name`) pada `mywatchlist/urls.py`.

6. Menambahkan rute berbagai tampilan ke dalam list url (`urlpatterns`) pada `mywatchlist/urls.py`. Rute tersebut mencakup: main route, html route, xml route, json route, xml by id route, dan json by id route.

7. Membuat file `main.html` dalam templates untuk tampilan awal aplikasi.

8. Membuat file `watchlist.html` dalam templates untuk tampilan HTML aplikasi. Data dari template ini akan diambil dari `views.py`.

9. Agar data pada `katalog/fixtures/initial_wishlist_data.json` dapat di-update, jalankan command di bawah di dalam terminal.

        python manage.py loaddata initial_wishlist_data.json

10. Mengedit `Procfile` menjadi line berikut agar Heroku dapat mengupdate data

    ```
    release: sh -c 'python manage.py migrate && python manage.py migrate --run-syncdb && python manage.py loaddata initial_catalog_data.json && python manage.py loaddata initial_wishlist_data.json'
    web: gunicorn project_django.wsgi --log-file -
    ```
11. Melakukan push pada GitHub dan Heroku app akan otomatis ter-update.

## Screenshot Postman

Tampilan HTML :

![Postman HTML](/resources/html.png)

Tampilan XML :

![Postman XML](/resources/xml.png)

Tampilan JSON :

![Postman JSON](/resources/json.png)

Hasil aplikasi Heroku yang telah dibuat [di sini](https://tugas-1-pbp.herokuapp.com/mywatchlist/).