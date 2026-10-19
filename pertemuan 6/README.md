
1. Mengimpor Tkinter
import tkinter as tk
Digunakan untuk membuat tampilan aplikasi, seperti jendela, tombol, teks, dan kolom input.

2. Fungsi prediksi prodi
def prediksi_prodi():
    hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")
Fungsi ini menampilkan hasil prediksi program studi Teknologi Informasi ketika tombol diklik.

3. Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x600")
Membuat jendela aplikasi, mengatur judul, dan menentukan ukuran jendela sebesar 500 × 600 piksel.

4.Membuat jendela utama
judul = tk.Label(...)
judul.pack(pady=20)
Menampilkan judul aplikasi dengan ukuran dan gaya tulisan tertentu. pady=20 memberikan jarak vertikal.

5. Membuat tempat input
input_frame = tk.Frame(root, bg="#f0f4f7")
input_frame.pack(pady=10)
Membuat wadah untuk menempatkan label dan kolom input nilai pelajaran.

6. Membuat 10 kolom nilai
entries = []
for i in range(10):
Perulangan ini membuat 10 kolom input nilai pelajaran. entries digunakan untuk menyimpan setiap kolom input agar bisa diakses kembali.

7. Membuat kolom input
entry = tk.Entry(input_frame, width=20)
entry.grid(row=i, column=1, pady=5, padx=10)
entries.append(entry)
Entry digunakan untuk memasukkan nilai, grid() mengatur posisi kolom, sedangkan append() menyimpan kolom tersebut ke dalam list.

8. Membuat tombol prediksi
prediksi_button = tk.Button(
    root,
    text="Hasil Prediksi",
    command=prediksi_prodi
)
Membuat tombol yang akan menjalankan fungsi prediksi_prodi() ketika ditekan.

9. Menampilkan hasil prediksi
hasil_label = tk.Label(
    root,
    text="Hasil Prediksi: -"
)
Membuat label untuk menampilkan hasil. Awalnya bertuliskan tanda -, kemudian berubah setelah tombol diklik.

10. Menjalankan aplikasi
root.mainloop()
Menjalankan aplikasi dan membuat jendela tetap aktif sampai ditutup.


Aplikasi ini memungkinkan pengguna memasukkan 10 nilai mata pelajaran dan menekan tombol untuk melihat hasil prediksi. Namun, kode saat ini belum membaca atau menghitung nilai yang dimasukkan, sehingga hasilnya selalu Teknologi Informasi.