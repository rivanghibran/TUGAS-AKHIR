#code by rivanghibran https://github.com/rivanghibran
from config import connect_db
import psycopg2

def create_tables():
    commands = (
        """
        CREATE TABLE IF NOT EXISTS Pasien (
            id SERIAL PRIMARY KEY,
            nama VARCHAR(255) NOT NULL,
            alamat TEXT NOT NULL,
            tanggal_lahir DATE NOT NULL,
            nomor_telepon VARCHAR(15) NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS Kamar (
            id SERIAL PRIMARY KEY,
            nomor_kamar VARCHAR(10) NOT NULL,
            tipe_kamar VARCHAR(50) NOT NULL
        )
        """,
        """
        CREATE TABLE IF NOT EXISTS RekamMedis (
            id SERIAL PRIMARY KEY,
            id_pasien INT NOT NULL,
            id_kamar INT NOT NULL,
            tanggal_kunjungan DATE NOT NULL,
            diagnosis TEXT NOT NULL,
            pengobatan TEXT NOT NULL,
            FOREIGN KEY (id_pasien)
                REFERENCES Pasien (id)
                ON UPDATE CASCADE ON DELETE CASCADE,
            FOREIGN KEY (id_kamar)
                REFERENCES Kamar (id)
                ON UPDATE CASCADE ON DELETE CASCADE
        )
        """,
        """
        INSERT INTO Kamar (nomor_kamar, tipe_kamar) VALUES
        ('101', 'VIP'),
        ('102', 'VIP'),
        ('103', 'VIP'),
        ('201', 'Kelas 1'),
        ('202', 'Kelas 1'),
        ('203', 'Kelas 1'),
        ('301', 'Kelas 2'),
        ('302', 'Kelas 2'),
        ('304', 'Kelas 2'),
        ('401', 'Kelas 3'),
        ('402', 'Kelas 3'),
        ('403', 'Kelas 3')
        ON CONFLICT DO NOTHING
        """
    )
    conn = connect_db()
    if conn:
        try:
            cur = conn.cursor()
            for command in commands:
                cur.execute(command)
            cur.close()
            conn.commit()
        except Exception as e:
            print(f"Error: {e}")
        finally:
            conn.close()
#code by rivanghibran https://github.com/rivanghibran