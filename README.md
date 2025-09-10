Tautan PWS : inayah-saffanah-flexkick.pbp.cs.ui.ac.id

1. Pertama membuat direktori baru dan virtual environment,lalu instal beberapa dependencies dan buat proyek Djangonya dengan perintah django-admin startproject flex_kick . selanjutnya konfigurasi environment variables dengan PRODUCTIONS=False untuk file .env dan True untuk file .env.prod dan masukkan kredensial database ke .env.prod, lalu daftarkan host local. 

    Untuk membuat aplikasi main, jalankan perintah python manage.py startapp main dan mendaftarkannya ke INSTALLED_APPS di settings.py.

    Selanjutnya, untuk membuat models, isi file models.py dengan membuat class Product yang mempunyai atribut id, name, price, brand, description, thumbnail, category, dan is_featured. Setiap merubah model, lakukan migrasi dengan mejalankan perintah python manage.py makemigrations dan python manage.py migrate

    Untuk membuat fungsi pada views.py, pertama tambah import render agar bisa menampilkan html from django.shortcuts import render. Lalu buat fungsi show_main dengan parameter request sehingga setiap ada permintaan, akan mengembalikan tampilan yang sesuai. Buat dictionary context yang berisi data (nama,npm,kelas) untuk ditampilkan lalu return render untuk merender tampilan main.html. Pada main.html, tambahkan template variables sesuai dengan yang sudah dibuat pada context.

    Untuk membuat routing urls.py aplikasi main, buat file urls.py di direktori main terlebih dahulu, lalu import path dari Django.urls untuk mendefinisikan pola URL dan impor show_main dari main.views. Isi list urlpatterns dengan fungsi path. Selanjutnya, buka file urls.py di dalam direktori flex-kick lalu impor fungsi include dari Django.urls dan tambahkan rute URL untuk mengarah tampilan main di urlpatterns.

    Lalu saya melakukan deployment ke PWS dengan create new project lalu isi raw editor environment dengan isi .env.prod lalu update all variables. Pada settings.py, tambahkan url deployment PWS di list Allowed_Host. Lalu lakukan git add, commit, dan push pada GitHub dan PWS. 

    Terakhir, membuat file readme.md. lalu isi dengan jawaban beberapa pertanyaan dan git add, commit, dan push,

2. bagan

3. Peran settings.py adalah sebagai pengatur konfigurasi utama proyek. Di settings.py, kita dapat mengatur debug mati atau aktif, menghubungkan database, manajemen aplikasi dan menentukan host yang diizinkan.

4. Cara kerja migrasi database di Django pertama membuat migrasi dengan perintah python manage.py makemigrations dan perintah python manage.py migrate untuk menerapkan perubahan ke database. Hal ini perlu dilakukan setiap kali ada perubahan pada model. 

5. Karena Django mempunyai struktur yang jelas mengikuti pola desain Model View Template (MVT), punya fitur keamanan bawaan, dan memakai Bahasa pemrograman yang mudah, yaitu python.

6. Menurut saya, tutorial 1 sudah sangat jelas dan detail sehingga saya mudah mengikutinya.
