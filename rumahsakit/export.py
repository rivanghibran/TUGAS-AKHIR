#code by rivanghibran https://github.com/rivanghibran
import pandas as pd
from config import connect_db

def ekspor_ke_excel(nama_file):
    if not nama_file.endswith(".xlsx"):
        print("Error: Nama file harus memiliki ekstensi .xlsx")
        return
    
    conn = connect_db()
    if conn:
        try:
            with conn.cursor() as cur:
                cur.execute("""
                    SELECT 
                        Pasien.id, 
                        Pasien.nama, 
                        Pasien.alamat, 
                        Pasien.tanggal_lahir, 
                        Pasien.nomor_telepon, 
                        RekamMedis.diagnosis, 
                        RekamMedis.tanggal_kunjungan, 
                        RekamMedis.pengobatan, 
                        Kamar.nomor_kamar, 
                        Kamar.tipe_kamar 
                    FROM 
                        Pasien 
                    JOIN 
                        RekamMedis ON Pasien.id = RekamMedis.id_pasien 
                    JOIN 
                        Kamar ON RekamMedis.id_kamar = Kamar.id
                """)
                rows = cur.fetchall()
                data = [
                    {
                        'ID Pasien': row[0],
                        'Nama': row[1],
                        'Alamat': row[2],
                        'Tanggal Lahir': row[3],
                        'Nomor Telepon': row[4],
                        'Diagnosis': row[5],
                        'Tanggal Kunjungan': row[6],
                        'Pengobatan': row[7],
                        'Nomor Kamar': row[8],
                        'Tipe Kamar': row[9]
                    }
                    for row in rows
                ]
                df = pd.DataFrame(data)
                df.to_excel(nama_file, index=False)
                print(f"Data berhasil diekspor ke file: {nama_file}")
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")
        finally:
            conn.close()
    else:
        print("Error: Tidak dapat terhubung ke database.")
#code by rivanghibran https://github.com/rivanghibran