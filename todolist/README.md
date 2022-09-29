# Tugas 4: Pengimplementasian Form dan Autentikasi Menggunakan Django

Pemrograman Berbasis Platform (CSGE602022) - diselenggarakan oleh Fakultas Ilmu Komputer Universitas Indonesia, Semester Ganjil 2022/2023

**Nama**  : Alicia Kirana Utomo

**NPM**   : 2106751505

**Kelas** : B

## Kegunaan `{% csrf_token %}` pada Elemen `<form>`

Penggunaan `{% csrf_token %}` diperlukan agar Django dapat me-render sebuah halaman dan dilakukan cross-check dengan request di dalam server. Jika request tidak memiliki token yang sesuai, maka server tidak akan menjalankan request. Jika tidak menggunakan `{% csrf_token %}`, maka request terhadap server tidak akan dijalankan dan memunculkan error.

## Membuat `<form>` secara Manual

Kita bisa membuat form dengan cara manual di dalam templates HTML. Tetapi di dalam opening tag `<form>`, perlu ditambahkan method yang akan dipakai sehingga menjadi `<form method = "POST">`.

## Proses Alur Data

Ketika sebuah user mengeklik button subit pada form, button tersebut akan mengirimkan sebuah "POST" request ke dalam server. Lalu, membuat object baru menggunakan `Task.objects.create` dengan parameter seluruh fields dari class dengan data diambil dengan method `request.POST.get()`. Setelah itu, untuk menampilkan task berdasarkan user yang log in, diperlukan pengambilan objects dengan filter user, menjadi `Task.objects.filter(user = get_user(request))`. Terakhir, seluruh data akan ditampilkan ke dalam templates menggunakan looping.

## Tahap pengimplementasian

1. Membuat aplikasi baru bernama `todolist`.

2. Menambahkan "todolist" ke dalam list app (`INSTALLED_APPS`) yang berada pada `project_django/settings.py`.

3. Membuat function `register`, `login_user`, `logout_user`, `show_todolist`, `create_task`, `update`, dan `delete` pada `views.py`. Setiap function memiliki tugas yang berbeda sesuai dengan namanya masing masing.

4. Menambahkan todolist ke dalam list url (`urlpatterns`) pada `project_django/urls.py`.

5. Menambahkan "todolist" ke dalam nama aplikasi (`app_name`) pada `todolist/urls.py`.

6. Menambahkan rute berbagai tampilan ke dalam list url (`urlpatterns`) pada `todolist/urls.py`. Rute tersebut mencakup: main route, register, login, logout, membuat task baru, mengupdate task, dan men-delete task.

7. Membuat file `todolist.html`, `register.html`, `login.html`, dan `create_task.html` dalam templates untuk tampilan HTML aplikasi. Data dari template ini akan diambil dari `views.py`.

8. Melakukan push pada GitHub dan Heroku app akan otomatis ter-update.

## Screenshot hasil akhir website

Tampilan page login :

![Tampilan page login](/resources/todolist-login.png)

Tampilan page register :

![Tampilan page register](/resources/todolist-register.png)

Tampilan page todolist :

![Tampilan page todolist](/resources/todolist-main.png)

Tampilan page create task :

![Tampilan page create task](/resources/todolist-create-task.png)

Hasil aplikasi Heroku yang telah dibuat [di sini](https://tugas-1-pbp.herokuapp.com/todolist/).