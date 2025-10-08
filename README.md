# FLEX KICK
## Deployment
[Flex Kick](https://inayah-saffanah-flexkick.pbp.cs.ui.ac.id/)

## Pertanyaan Tugas 2
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


## Pertanyaan Tugas 3
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


## Pertanyaan Tugas 4
### 1. Apa itu Django AuthenticationForm? Jelaskan juga kelebihan dan kekurangannya.
Django AuthenticationForm adalah form dari Django untuk proses login. Form ini otomatis menyediakan field username dan password. Kelebihannya adalah mudah digunakan dan sudah aman. Kekurangannya adalah kurang fleksibel jika ingin login bukan dengan username dan password.

### 2. Apa perbedaan antara autentikasi dan otorisasi? Bagaiamana Django mengimplementasikan kedua konsep tersebut?
Autentikasi adalah proses verifikasi identitas user sedangkan otorisasi adalah hak akses pengguna. Autentikasi diimplementasikan menggunakan AuthenticationForm (memasukkan username dan password) sedangkan otorisasi diimplementasikan seperti decorators login_required.

### 3. Apa saja kelebihan dan kekurangan session dan cookies dalam konteks menyimpan state di aplikasi web?
Session : Data disimpan di server sehingga lebih aman dan user tidak bisa langsung mengubah/melihat, tapi butuh resource server lebih banyak.
Cookies : Data disimpan di browser sehingga lebih ringan, tapi rentan terhadap serangan keamananan

### 4. Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai? Bagaimana Django menangani hal tersebut?
Ada risiko yang harus diwaspadai karena Cookies bisa terkena XSS. Django menangani hal ini dengan menggunakan CSRF token untuk memastikan bahwa request benar-benar berasal dari user yang memakai aplikasi kita. 

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama membuat form registrasi dengan impor formulir bawaan lalu menambahkan fungsi register di views.py untuk menghasilkan form register dan menghasilkan akun pengguna lalu buat templatenya dan tambahkan path url. Selanjutnya membuat fungsi login dengan fungsi bawaan Django lalu buat template dan path urlnya. Terakhir membuat fungsi logout dengan import logout, buat fungsi dengan menghapus sesi pengguna yg sedang masuk dan arahkan ke halaman login lalu buat template dan path url. 

Membuat dua akun dilakukan dengan register dua akun dan login. Lalu menambahkan tiga produk pada masing-masing akun dengan add product dan memasukkan data.

Untuk menghubungkan model Product dengan User, kita harus mengubah models.py dengan import User. Setelahnya, tambahkan variabel user untuk menghubungkan satu product dengan user. Lalu lakukan migrasi. Setelahnya ubah views dengan menyimpan user setiap menambahkan produk.Terakhir, tampilkan user yang membuat produk dengan menambahkannya di product_detail.html.

Gunakan request.user.username untuk mengambil username user yang sedang login. Untuk membuat last_login, pertama import HttpResponseRedirect, reverse, dan datetime di views.py lalu simpan cookie last_login yang berisi timestamp terakhir login. Ubah fungsi logout untuk menghapus cookie saat logout. Terakhir menampilkan last_login dengan request.COOKIES.get('last_login', 'Never').

## Pertanyaan Tugas 5
### 1. Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
Jika ada beberapa CSS selector, prioritas paling tinggi adalah inline style. Inline style ini langsung ditulisa di elemen dengan atribut style=...Prioritas kedua adalah ID selector. ID selector menggunakan id pada tag sebagai selectornya. Prioritas selanjutnya adalah Class selector. Class selector ini mengelompokkan elemen dengan karakteristik yg sama. Selanjutnya ada Element Selector. Element Selector mengubah elemen HTML berdasarkan nama tagnya.


### 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design, serta jelaskan mengapa!
Contoh yang sudah menerapkan responsive adalah Scele karena saat dibuka di tab atau HP, layoutnya menyesuaikan. Contoh yang tidak menerapkan responsive design adalah SIAK-NG karena layoutnya tidak menyesuaikan saat dibuka di hp.
Responsive design sangat penting karena tidak semua user mengakses web dengan komputer, banyak yang memakai hp karena lebih mudah dibawa. Web yang tidak menerapkan responsive design membuat user kesulitan dan tidak nyaman. Hal ini menurunkan pengalaman pengguna. 

### 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
Margin adalah jarak kosong di sekitar border.
Border adalah garis ujung yang mengelilingi konten dan padding jika ada.
Padding adalah jarak kosong antara konten dengan border.

Contoh implementasi ketiganya:
.kotak {
  margin: 20px;         
  padding: 20px;            
  border: 2px black;   
}

### 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!
Flex box digunakan untuk mengatur elemen 1 dimensi (baris atau kolom) sehingga elemen bisa menyesuaikan posisi dan ukuran. Flex box cocok digunakan untuk navbar.
Grid Layout digunakan untuk mengatur elemen 2 dimensi (baris dan kolom). Grid Layout cocok digunakan untuk galeri foto.

### 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

I. Pertama menambahkan fungsi edit_product dan delete_product di views.py. Lalu tambahkan routing url keduanya. Selanjutnya buat template html edit_product.html untuk mengedit. delete_product tidak perlu dibuat template karena user akan tetap di main.

II. Selain itu, untuk memastikan tampilan menarik dan konsisten, gunakan Tailwind pada template dasar (base) sehingga semua halaman mewarisi gaya yang sama. Di base juga tambahkan meta viewport agar browser pada perangkat mobile dapat menyesuaikan lebar viewport saat merender halaman, serta mendefinisikan CSS global untuk menyamakan tampilan form (input, textarea, select, checkbox), sehingga tampilannya lebih rapi, konsisten, dan responsif.

III. Lalu ubah template html login, register, add_product, edit_product, detail_product dengan mengganti bg, tombol, dan teks semenarik mungkin. Styling dibuat menggunakan utilitas Tailwind agar mudah diubah kemudian.

IV. Jika belum ada product, siapkan gambar di folder static/image untuk ditampilkan saat belum ada product. Tambahkan button add product dibawahnya. Jika sudah ada product, buat card untuk menampilkan tiap product dengan atribut yang sudah ada. 

V. Cek dulu apakah user yang sekarang login adalah pemilik produknya. Jika iya maka tampilkan button untuk mengedit dan menghapus. Tombol dibuat dengan menyisipkan link edit atau hapus.

VI. Buat 2 navbar, untuk mobile dan desktop agar web menjadi responsive. Navbar berisi nama aplikasi, home, add product, informasi pengguna yg login, dan tombol logout. Untuk navbar versi desktop, fitur-fiturnya ada secara horizontal. Sedangkkan navbar mobile secara vertikal.

## Pertanyaan Tugas 6
### 1. Apa perbedaan antara synchronous request dan asynchronous request?
Synchronus request dieksekusi secara berurutan, sehingga tugas sebelumnya harus sudah selesai sebelum tugas selanjutnya dieksekusi.
Asynchronus request dieksekusi secara bersamaan, sehingga dapat lanjut ke tugas selanjutnya tanpa menunggu respons tugas sebelumnya.
s

### 2. Bagaimana AJAX bekerja di Django (alur request–response)?
Pengguna melakukan aksi di web, JavaScript mengirim request AJAX ke server Django tanpa reload halaman, Django menerima request dan memproses di views.py, views mengirim respons ke JavaScript, terakhir JavaScript menerima dan menampilkan tampilan terbaru secara dinamis.

### 3. Apa keuntungan menggunakan AJAX dibandingkan render biasa di Django?
Halaman web bisa memperbarui data secara dinamis tanpa reload seluruh halaman, sehingga membuat aplikasi lebih cepat, interaktif, dan efisien dibandingkan render biasa di Django.

### 4. Bagaimana cara memastikan keamanan saat menggunakan AJAX untuk fitur Login dan Register di Django?
Menggunakan CSRF token untuk mencegah Cross-Site Request Forgery, validasi data di server agar input berbahaya tidak masuk, dan menggunakan sistem autentikasi Django.

### 5. Bagaimana AJAX mempengaruhi pengalaman pengguna (User Experience) pada website?
Dengan AJAX, pengguna tidak perlu reload page untuk mendapatkan data terbaru karena pembaruan dilakukan secara asynchronus. Hal ini membuat pengguna dapat menggunakan website dengan lebih cepat dan lancar.