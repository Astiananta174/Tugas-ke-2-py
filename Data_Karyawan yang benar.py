karyawan_1 = ("Riski Karlina", "CEO", 20, "Kopang ")
karyawan_2 = ("Siti Aminah", "Admin Keuangan", 30, "praya")
karyawan_3 = ("Iqbal Ramadhan", "Staff", 25, "Bandung")

daftar_karyawan = (karyawan_1, karyawan_2, karyawan_3)

def tampilkan_data_karyawan():
    print("Data Karyawan:")
    print("========================")
    for karyawan in daftar_karyawan:
        print(f"Nama: {karyawan[0]}")
        print(f"Jabatan: {karyawan[1]}")
        print(f"Umur: {karyawan[2]}")
        print(f"Kota: {karyawan[3]}")
        print("------------------------")
        
tampilkan_data_karyawan()
