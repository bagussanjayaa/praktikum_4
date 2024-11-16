def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

data_mahasiswa = []

while True:
    nama = input("Nama: ")
    nim = input("NIM: ")
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))
    
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    data_mahasiswa.append({
        "nama": nama,
        "nim": nim,
        "tugas": tugas,
        "uts": uts,
        "uas": uas,
        "nilai_akhir": nilai_akhir
    })
    
    tambah_data = input("Tambah data lagi? (y/t): ")
    if tambah_data.lower() == 't':
        break

print("-----------------------------------------------------------------------------------------")
print("| No | Nama                 | NIM           | Tugas    | UTS      | UAS      | Akhir    |")
print("-----------------------------------------------------------------------------------------")

for i, mahasiswa in enumerate(data_mahasiswa, start=1):
    print(f"| {i:<2} | {mahasiswa['nama']:<20} | {mahasiswa['nim']:<13} | {mahasiswa['tugas']:<8.2f} | {mahasiswa['uts']:<8.2f} | {mahasiswa['uas']:<8.2f} | {mahasiswa['nilai_akhir']:<8.2f} |")

print("-----------------------------------------------------------------------------------------")
