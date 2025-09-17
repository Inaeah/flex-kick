# FLEX KICK
## Deployment
[Flex Kick](https://inayah-saffanah-flexkick.pbp.cs.ui.ac.id/)

## Pertanyaan Tugas1
### 1. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step
Pertama membuat direktori baru dan virtual environment,lalu instal beberapa dependencies dan buat proyek Djangonya dengan perintah django-admin startproject flex_kick . selanjutnya konfigurasi environment variables dengan PRODUCTIONS=False untuk file .env dan True untuk file .env.prod dan masukkan kredensial database ke .env.prod, lalu daftarkan host local. 

Untuk membuat aplikasi main, jalankan perintah python manage.py startapp main dan mendaftarkannya ke INSTALLED_APPS di settings.py.

Selanjutnya, untuk membuat models, isi file models.py dengan membuat class Product yang mempunyai atribut id, name, price, brand, description, thumbnail, category, dan is_featured. Setiap merubah model, lakukan migrasi dengan mejalankan perintah python manage.py makemigrations dan python manage.py migrate

Untuk membuat fungsi pada views.py, pertama tambah import render agar bisa menampilkan html from django.shortcuts import render. Lalu buat fungsi show_main dengan parameter request sehingga setiap ada permintaan, akan mengembalikan tampilan yang sesuai. Buat dictionary context yang berisi data (nama,npm,kelas) untuk ditampilkan lalu return render untuk merender tampilan main.html. Pada main.html, tambahkan template variables sesuai dengan yang sudah dibuat pada context.

Untuk membuat routing urls.py aplikasi main, buat file urls.py di direktori main terlebih dahulu, lalu import path dari Django.urls untuk mendefinisikan pola URL dan impor show_main dari main.views. Isi list urlpatterns dengan fungsi path. Selanjutnya, buka file urls.py di dalam direktori flex-kick lalu impor fungsi include dari Django.urls dan tambahkan rute URL untuk mengarah tampilan main di urlpatterns.

Lalu saya melakukan deployment ke PWS dengan create new project lalu isi raw editor environment dengan isi .env.prod lalu update all variables. Pada settings.py, tambahkan url deployment PWS di list Allowed_Host. Lalu lakukan git add, commit, dan push pada GitHub dan PWS. 

Terakhir, membuat file readme.md. lalu isi dengan jawaban beberapa pertanyaan dan git add, commit, dan push,

### 2. Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
<img width="1394" height="784" alt="Image" src="https://github.com/user-attachments/assets/7f2bff1e-c8ed-4768-a928-e43713bf34db" />

### 3.Jelaskan peran settings.py dalam proyek Django!
Peran settings.py adalah sebagai pengatur konfigurasi utama proyek. Di settings.py, kita dapat mengatur debug mati atau aktif, menghubungkan database, manajemen aplikasi dan menentukan host yang diizinkan.

### 4. Bagaimana cara kerja migrasi database di Django?
Cara kerja migrasi database di Django pertama membuat migrasi dengan perintah python manage.py makemigrations dan perintah python manage.py migrate untuk menerapkan perubahan ke database. Hal ini perlu dilakukan setiap kali ada perubahan pada model. 

### 5. Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Karena Django mempunyai struktur yang jelas mengikuti pola desain Model View Template (MVT), punya fitur keamanan bawaan, dan memakai Bahasa pemrograman yang mudah, yaitu python.

### 6. Apakah ada feedback untuk asisten dosen tutorial 1 yang telah kamu kerjakan sebelumnya?
Menurut saya, tutorial 1 sudah sangat jelas dan detail sehingga saya mudah mengikutinya.


## Pertanyaan Tugas2
### 1. Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Karena data delivery berfungsi sebagai pengantar informasi antar sistem. Dengan data delivery, data bisa ke tempat lain dengan cepat dan aman, sehingga platform bisa terhubung dengan baik.

### 2. Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Menurut saya, lebih baik JSON. Alasan JSON lebih populer dan lebih baik menurut saya adalah karena JSON lebih mudah dibaca dan dipahami.

### 3. Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Method is_valid() berfungsi untuk mengecek apakah input dari user sudah sesuai dengan aturan. Kita membutuhkan method ini agar data yang masuk sudah lengkap dan sesuai sebelum disimpan, jika tidak ada maka bisa menimbulkan error dalam pengolahan data.

### 4. Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
csrf_token berguna untuk membedakan request asli dengan yang palsu. Jika tidak menambahkan csrf_token, user dapat diserang dengan membuat user yang sedang login tanpa sadar menghapus data, mengganti pasword, atau transfer uang.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
I. Untuk menambahkan 4 fungsi baru, fungsi yang dibutuhkan adalah fungsi untuk melihat XML, XML by id, JSON, dan JSON by id. Pertama fungsinya menerima parameter request dan di dalam fungsinya ada variabel yang menyimpan hasil query dari seluruh data Product. Untuk by id, variabelnya menyimpan hasil query dari id tertentu yang ada di Product. Lalu saya menambahkan return function HttpResponse yang parameternya data hasil query yang sudah diserialisasi dan content type XML atau JSON.

II. Setelahnya, kita perlu routing 4 fungsi sebelumnya di urls.py yang ada di direktori main. Import fungsi yang sudah dibuat sebelumnya, lalu tambahkan path URL ke urlpatterns agar fungsi sebelumnya dapat diakses. 

III. Untuk membuat halaman utama, update kode di main.html yang ada di direktori main/templates. Untuk membuat button "Add" dan "Detail" , kita memerlukan url yang akan redirect jika dipencet. Untuk menampilkan produk, looping product_list lalu tampilkan informasi yang dibuuthkan.

IV. Selanjutnya kita perlu membuat halaman form untuk menambahkann produk. Saya membuat file HTML add_product di main/templates. Pada page ini, kita meminta input kepada user dengan fields yang sudah dibuat pada tugas sebelumnya. 

V. Langkah terakhir, kita perlu membuat page detail produk. Buat button agar user bisa kembali ke landing page lalu masukkan atribut product dibawahnya dengan rapih.

### 6. Apakah ada feedback untuk asdos di tutorial 2 yang sudah kalian kerjakan?
Tidak ada, menurut saya sudah cukup baik.

### Postman
#### XML
![Image](https://github.com/user-attachments/assets/a90b0fe2-0039-46a4-a2ff-b6666594e825)

#### JSON
<img width="1707" height="814" alt="Image" src="https://github.com/user-attachments/assets/374d99d2-4093-49dc-971d-e8d7f52b9dfa" />

#### XML by id
<img width="1713" height="771" alt="Image" src="https://github.com/user-attachments/assets/4266e703-7ca9-4dbe-a28c-e141523064f0" />

#### JSON by id
<img width="1699" height="774" alt="Image" src="https://github.com/user-attachments/assets/bb14180e-1bd5-4318-b4e4-a34c5de649c2" />