#code by rivanghibran https://github.com/rivanghibran
from config import connect_db
import moduls

def tambah_pasien(nama, alamat, tanggal_lahir, nomor_telepon):
    conn = connect_db()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO Pasien (nama, alamat, tanggal_lahir, nomor_telepon) VALUES (%s, %s, %s, %s)",
                        (nama, alamat, tanggal_lahir, nomor_telepon))
            conn.commit()
            cur.close()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            conn.close()

def lihat_pasien(table_layout):
    conn = connect_db()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("SELECT * FROM Pasien")
            rows = cur.fetchall() 
            cur.close()
            if rows:
                headers = ['ID', 'Nama', 'Alamat', 'Tanggal Lahir', 'Nomor Telepon']
                for header in headers:
                    table_layout.add_widget(moduls.Label(text=header, bold=True))
                for row in rows:
                    for cell in row:
                        table_layout.add_widget(moduls.Label(text=str(cell),size_hint_y=None,))
            else:
                table_layout.add_widget(moduls.Label(text='Data pasien tidak ditemukan'))
        except Exception as e:
            table_layout.add_widget(moduls.Label(text=f"Error: {e}"))
        finally:
            conn.close()

def update_pasien(id, nama=None, alamat=None, tanggal_lahir=None, nomor_telepon=None):
    conn = connect_db()
    if conn:
        try:
            cur = conn.cursor()
            if nama:
                cur.execute("UPDATE Pasien SET nama = %s WHERE id = %s", (nama, id))
            if alamat:
                cur.execute("UPDATE Pasien SET alamat = %s WHERE id = %s", (alamat, id))
            if tanggal_lahir:
                cur.execute("UPDATE Pasien SET tanggal_lahir = %s WHERE id = %s", (tanggal_lahir, id))
            if nomor_telepon:
                cur.execute("UPDATE Pasien SET nomor_telepon = %s WHERE id = %s", (nomor_telepon, id))
            conn.commit()
            cur.close()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            conn.close()

def hapus_pasien(id):
    conn = connect_db()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("DELETE FROM RekamMedis WHERE id = %s", (id,))
            cur.execute("DELETE FROM Pasien WHERE id = %s", (id,))
            conn.commit()
            cur.close()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            conn.close()

def tambah_rekam_medis(id_pasien, id_kamar, tanggal_kunjungan, diagnosis, pengobatan):
    conn = connect_db()
    if conn:
        try:
            cur = conn.cursor()
            cur.execute("INSERT INTO RekamMedis (id_pasien, id_kamar, tanggal_kunjungan, diagnosis, pengobatan) VALUES (%s, %s, %s, %s, %s)",
                        (id_pasien, id_kamar, tanggal_kunjungan, diagnosis, pengobatan))
            conn.commit()
            cur.close()
            return 'Rekam medis berhasil disimpan'
        except Exception as e:
            return f"Error: {e}"
        finally:
            conn.close()
    return 'Koneksi ke database gagal'

def search_rekam_medis(search_term, search_input, table_layout):
    conn = connect_db()
    if conn:
        try:
            cur = conn.cursor()
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
                    Kamar.nomor_kamar AS nomor_kamar, 
                    Kamar.tipe_kamar AS tipe_kamar 
                FROM 
                    Pasien 
                JOIN 
                    RekamMedis ON Pasien.id = RekamMedis.id_pasien 
                JOIN 
                    Kamar ON RekamMedis.id_kamar = Kamar.id
                WHERE 
                    Pasien.id = %s
            """, (search_term,))
            rows = cur.fetchall()
            if rows:
                headers = ['ID Pasien', 'Nama', 'Alamat', 'Tanggal Lahir', 'Nomor Telepon',
                           'Diagnosis', 'Tanggal Kunjungan', 'Pengobatan', 'Nomor Kamar', 'Tipe Kamar']
                for header in headers:
                    table_layout.add_widget(moduls.Label(text=header, bold=True))
                for row in rows:
                    for cell in row:
                        table_layout.add_widget(moduls.Label(text=str(cell)))
            else:
                table_layout.add_widget(moduls.Label(text='Rekam medis tidak ditemukan'))
            cur.close()
        except Exception as e:
            table_layout.add_widget(moduls.Label(text=f"Error: {e}"))
        finally:
            conn.close()
#code by rivanghibran https://github.com/rivanghibran

