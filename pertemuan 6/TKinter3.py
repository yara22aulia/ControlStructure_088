import tkinter as tk

# Fungsi prediksi prodi
def prediksi_prodi():
    hasil_label.config(text="Prediksi Prodi: Teknologi Informasi")

# Membuat jendela utama
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")
root.geometry("500x600")
root.configure(bg="#f0f4f7")

# Judul aplikasi
judul = tk.Label(
    root,
    text="Aplikasi Prediksi Prodi Pilihan",
    font=("Helvetica", 16, "bold"),
    bg="#f0f4f7",
    fg="#333333"
)
judul.pack(pady=20)

# Frame untuk input
input_frame = tk.Frame(root, bg="#f0f4f7")
input_frame.pack(pady=10)

# Label dan entry untuk 10 nilai pelajaran
entries = []

for i in range(10):
    data_pelajaran = tk.Label(
        input_frame,
        text=f"Nilai Mata Pelajaran {i+1}:",
        font=("Helvetica", 12),
        bg="#f0f4f7"
    )
    data_pelajaran.grid(row=i, column=0, sticky="w", pady=5, padx=10)

    entry = tk.Entry(input_frame, width=20)
    entry.grid(row=i, column=1, pady=5, padx=10)
    entries.append(entry)

# Tombol hasil prediksi
prediksi_button = tk.Button(
    root,
    text="Hasil Prediksi",
    command=prediksi_prodi,
    font=("Helvetica", 12, "bold"),
    bg="#3333cc",
    fg="white"
)
prediksi_button.pack(pady=20)

# Label hasil prediksi
hasil_label = tk.Label(
    root,
    text="Hasil Prediksi: -",
    font=("Helvetica", 14, "italic"),
    bg="#f0f4f7",
    fg="blue"
)
hasil_label.pack(pady=10)

# Menjalankan aplikasi
root.mainloop()