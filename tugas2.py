# Inisialisasi data campuran
data_campuran = [115, 2.2, "Hello", 377, "python", 1.7 , "World", 400, 4.3, "AI"]

# Inisialisasi struktur data untuk menyimpan hasil
int_values = {"satuan": [], "puluhan": [], "ratusan": []}
float_values = ()
string_values = []

# Memisahkan data sesuai tipe
for item in data_campuran:
    if isinstance(item, int):
        if item < 10:
            int_values["satuan"].append(item)
        elif item < 100:
            int_values["puluhan"].append(item)
        else:
            int_values["ratusan"].append(item)
    elif isinstance(item, float):
        float_values += (item,)
    elif isinstance(item, str):
        string_values.append(item)

# Menampilkan hasil pemisahan
print("Data Integer:")
print("Satuan:", int_values["satuan"])
print("Puluhan:", int_values["puluhan"])
print("Ratusan:", int_values["ratusan"])

print("\nData Float:")
print("Tuple Float:", float_values)

print("\nData String:")
print("List String:", string_values)
