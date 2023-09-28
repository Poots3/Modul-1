# Fungsi untuk menghitung nilai akhir mahasiswa
def hitung_nilai_akhir(nama, nilai_tugas, nilai_uts, nilai_uas):
    # Hitung nilai akhir dengan bobot 20% tugas, 40% UTS, dan 40% UAS
    nilai_akhir = (0.2 * nilai_tugas) + (0.4 * nilai_uts) + (0.4 * nilai_uas)
    return (nama, nilai_akhir)

# Fungsi untuk menghitung nilai akhir semua mahasiswa
def hitung_nilai_semua_mahasiswa(daftar_mahasiswa):
    nilai_semua_mahasiswa = []
    for mahasiswa in daftar_mahasiswa:
        nama, nilai_tugas, nilai_uts, nilai_uas = mahasiswa
        nilai_akhir = hitung_nilai_akhir(nama, nilai_tugas, nilai_uts, nilai_uas)
        nilai_semua_mahasiswa.append(nilai_akhir)
    return nilai_semua_mahasiswa

# Contoh data mahasiswa (nama, nilai tugas, nilai UTS, nilai UAS)
daftar_mahasiswa = [
    ("ihza", 80, 81, 90),
    ("hanif", 70, 82, 78),
    ("wilda", 74, 65, 83),
]

# Hitung nilai akhir semua mahasiswa
nilai_semua_mahasiswa = hitung_nilai_semua_mahasiswa(daftar_mahasiswa)

# Tampilkan nilai akhir semua mahasiswa
for nama, nilai_akhir in nilai_semua_mahasiswa:
    print(f"Si {nama}: Final Grade = {nilai_akhir}")
