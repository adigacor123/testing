import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Fungsi untuk menghitung kebutuhan material
def calculate_materials():
    # Mendapatkan input berat beton dan jenis beton
    berat_beton = berat_entry.get()
    jenis_beton = jenis_combobox.get()

    # Memvalidasi input
    if not berat_beton:
        messagebox.showerror("Error", "Masukkan berat beton terlebih dahulu.")
        return
    if not jenis_beton:
        messagebox.showerror("Error", "Pilih jenis beton terlebih dahulu.")
        return

    try:
        berat_beton = float(berat_beton)
    except ValueError:
        messagebox.showerror("Error", "Input berat beton tidak valid.")
        return

    # Rasio bahan untuk setiap jenis beton (sesuaikan sesuai kebutuhan)
    beton_ratios = {
        "Beton Ringan": {"semen": 0.12, "pasir": 0.25, "air": 0.18, "kerikil": 0.45},
        "Beton Normal": {"semen": 0.14, "pasir": 0.26, "air": 0.16, "kerikil": 0.44},
        "Beton Berat": {"semen": 0.16, "pasir": 0.27, "air": 0.14, "kerikil": 0.43}
}

    # Mendapatkan rasio bahan sesuai jenis beton
    rasio_bahan = beton_ratios[jenis_beton]

    # Menghitung kebutuhan material
    semen_kebutuhan = berat_beton * rasio_bahan["semen"]
    pasir_kebutuhan = berat_beton * rasio_bahan["pasir"]
    air_kebutuhan = berat_beton * rasio_bahan["air"]
    kerikil_kebutuhan = berat_beton * rasio_bahan["kerikil"]

    # Menampilkan hasil di display
    result_text = f"Untuk {berat_beton} kg {jenis_beton}, dibutuhkan:\n\n"
    result_text += f"Semen: {semen_kebutuhan:.2f} kg\n"
    result_text += f"Pasir: {pasir_kebutuhan:.2f} kg\n"
    result_text += f"Air: {air_kebutuhan:.2f} kg\n"
    result_text += f"Kerikil: {kerikil_kebutuhan:.2f} kg"
    display_result.config(text=result_text)

# Fungsi untuk mereset input dan hasil perhitungan
def reset_fields():
    berat_entry.delete(0, tk.END)
    jenis_combobox.set("")
    display_result.config(text="")

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Pembuatan Material Beton")
root.geometry("600x600")  # Mengatur ukuran jendela
root.configure(bg="#2C3E50")  # Memberi warna latar belakang

# Membuat style untuk ttk
style = ttk.Style()
style.theme_use("clam")

style.configure("TLabel", background="#2C3E50", foreground="white", font=("Helvetica", 12))
style.configure("TFrame", background="#2C3E50")
style.configure("TButton", background="#4CAF50", foreground="white", font=("Helvetica", 12), borderwidth=0)
style.map("TButton", background=[("active", "#45A049")])

# Membuat frame utama
main_frame = ttk.Frame(root)
main_frame.pack(expand=True, padx=20, pady=20)

# Membuat frame untuk display
display_frame = ttk.Frame(main_frame)
display_frame.grid(row=0, column=0, columnspan=2, pady=(10, 20), sticky="ew")

# Membuat label untuk menampilkan hasil perhitungan
display_result = ttk.Label(display_frame, font=("Helvetica", 14), anchor="center", justify="center", relief="solid", padding=10)
display_result.pack(fill="both")

# Membuat frame untuk input berat beton dan jenis beton
input_frame = ttk.Frame(main_frame)
input_frame.grid(row=1, column=0, columnspan=2, pady=(10, 20), sticky="ew")

# Membuat label dan entry untuk input berat beton
berat_label = ttk.Label(input_frame, text="Berat Beton (kg):")
berat_label.grid(row=0, column=0, padx=(10, 5), pady=10, sticky="e")

berat_entry = ttk.Entry(input_frame, font=("Helvetica", 12))
berat_entry.grid(row=0, column=1, padx=(0, 10), pady=10, sticky="ew")

# Membuat label dan combobox untuk memilih jenis beton
jenis_label = ttk.Label(input_frame, text="Jenis Beton:")
jenis_label.grid(row=1, column=0, padx=(10, 5), pady=10, sticky="e")

jenis_combobox = ttk.Combobox(input_frame, values=["Beton Ringan", "Beton Normal", "Beton Berat"], state="readonly", font=("Helvetica", 12))
jenis_combobox.grid(row=1, column=1, padx=(0, 10), pady=10, sticky="ew")

# Membuat tombol untuk menghitung kebutuhan material
calculate_button = ttk.Button(main_frame, text="Hitung Kebutuhan Material", command=calculate_materials)
calculate_button.grid(row=2, column=0, columnspan=2, pady=20, sticky="ew")

# Membuat tombol untuk mereset input dan hasil perhitungan
reset_button = ttk.Button(main_frame, text="Reset", command=reset_fields)
reset_button.grid(row=3, column=0, columnspan=2, pady=10, sticky="ew")

# Fokuskan entry berat ketika jendela utama diluncurkan
berat_entry.focus_set()

# Menjalankan loop utama
root.mainloop()