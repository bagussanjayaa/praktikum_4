# praktikum_4

Nama: Bagus Sanjaya

NIM: 312410505

Kelas: TI.24.A.5

## Ini adalah penjelasan dari program yang saya buat

![gambar](screenshot4/data1.png)

Fungsi ini menghitung nilai akhir berdasarkan nilai tugas, UTS, dan UAS dengan bobot masing-masing:

- Tugas: 30%

- UTS: 35%

- UAS: 35%

STRUKTUR UTAMA PROGRAM

Program ini mengumpulkan data mahasiswa, menghitung nilai akhir mereka, dan menampilkan hasil dalam bentuk tabel. Berikut adalah langkah-langkah utamanya:

1. Inisialisasi list data_mahasiswa:

![gambar](screenshot4/data2.png)

List kosong ini akan menyimpan data semua mahasiswa.

2. Pengumpulan data dengan while true: loop ini akan terus meminta iput dari pengguna hingga pengguna memilih untuk berhenti.

![gambar](screenshot4/data3.png)

- Input data: Mengambil input dari pengguna untuk nama, nim, tugas, uts, dan uas.

- Menghitung nilai akhir: Menggunakan fungsi hitung_nilai_akhir untuk menghitung nilai akhir.

- Menyimpan data: Menyimpan semua data ke dalam dictionary dan menambahkannya ke list data_mahasiswa.

- Kontrol loop: Menanyakan pengguna apakah ingin menambahkan data lagi. Jika pengguna menjawab 't', loop akan berhenti.

3. Mencetak tabel data mahasiswa:

- Header tabel:

![gambar](screenshot4/data4.png)

Mencetak header tabel dengan format yang diatur.

- Isi tabel:

![gambar](screenshot4/data5.png)

![gambar](screenshot4/data6.png)

Loop ini akan mencetak setiap data mahasiswa dalam bentuk tabel. enumerate digunakan untuk mendapatkan indeks mulai dari 1. 

- Footer tabel:

![gambar](screenshot4/data7.png)

Mencetak garis penutup tabel.

## Ini adalah Output dari program yang saya buat

![gambar](screenshot4/hsl.png)

## Ini adalah penjelasan dari flowchart yang saya buat

1. 

![gambar](screenshot4/datafw1.png)

Memulai flowchart menggunakan simbol oval.

2. 

![gambar](screenshot4/datafw2.png)

Inisialisasi list data_mahasiswa tersebut kosong.

3. 

![gambar](screenshot4/datafw3.png)

Memasukan Nama, NIM, Nilai_tugas, Nilai_UTS, Nilai_UAS.

4. 

![gambar](screenshot4/datafw4.png)

Menghitung nilai akhir dengan program yang tadi sudah saya buat.

hitung_nilai_akhir(tugas, uts, uas):

(tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

5. 

![gambar](screenshot4/datafw5.png)

Simpan semua data mahasiswa tersebut ke data_mahasiswa, yang dimana data mahasiswa tersebut mencangkup Nama, NIM, Nilai_tugas, Nilai_UTS, Nilai_UAS, dan Nilai_akhir.

6. 

![gambar](screenshot4/datafw6.png)

Apakah pengguna ingin menambah data lagi?

- Jika y, maka program akan kembali ke no3.

- Jika t, maka program akan melanjutkan ke langkah berikutnya.

7. 

![gambar](screenshot4/datafw7.png)

Mencetak header tabel yang sudah saya buat pada program sebelumnya.

8. 

![gambar](screenshot4/datafw8.png)

Menampilkan data mahasiswa yang telah diinputkan berbentuk tabel.

9. 

![gambar](screenshot4/datafw9.png)

Mencetak footer tabel yang sudah saya buat pada program sebelumnya.

10. 

![gambar](screenshot4/datafw10.png)

Program selesai ditutup dengan simbol oval.

## Dan ini adalah flowchartnya

![gambar](screenshot4/fwdata1.png)

![gambar](screenshot4/fwdata2.png)
