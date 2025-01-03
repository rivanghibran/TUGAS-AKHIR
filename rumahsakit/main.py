#code by rivanghibran https://github.com/rivanghibran
import moduls

class MenuScreen(moduls.Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = moduls.BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(moduls.Button(text='Tambah Data Pasien', on_press=self.go_to_tambah, size_hint=(1, 0.2)))
        layout.add_widget(moduls.Button(text='Hapus Data Pasien', on_press=self.go_to_hapus, size_hint=(1, 0.2)))
        layout.add_widget(moduls.Button(text='Lihat Data Pasien', on_press=self.go_to_lihat, size_hint=(1, 0.2)))
        layout.add_widget(moduls.Button(text='Update Data Pasien', on_press=self.go_to_update, size_hint=(1, 0.2)))
        layout.add_widget(moduls.Button(text='Cari Rekam Medis', on_press=self.go_to_cari_rekam_medis, size_hint=(1, 0.2)))
        layout.add_widget(moduls.Button(text='Input Rekam Medis', on_press=self.go_to_input_rekam_medis, size_hint=(1, 0.2)))
        layout.add_widget(moduls.Button(text='Ekspor ke Excel', on_press=self.export, size_hint=(1, 0.2)))
        self.add_widget(layout)

    def go_to_tambah(self, instance):
        self.manager.current = 'tambah'

    def go_to_hapus(self, instance):
        self.manager.current = 'hapus'

    def go_to_lihat(self, instance):
        self.manager.current = 'lihat'

    def go_to_update(self, instance):
        self.manager.current = 'update'

    def go_to_cari_rekam_medis(self, instance):
        self.manager.current = 'cari_rekam_medis'

    def go_to_input_rekam_medis(self, instance):
        self.manager.current = 'input_rekam_medis'

    def export(self, instance):
        moduls.ekspor_ke_excel('data_pasien.xlsx')
        popup = moduls.Popup(title='Ekspor Selesai', content=moduls.Label(text='Data berhasil diekspor ke data_pasien.xlsx'), size_hint=(0.6, 0.4))
        popup.open()

class TambahPasien(moduls.Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = moduls.BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(moduls.Label(text='Nama Pasien'))
        self.nama_input = moduls.TextInput()
        layout.add_widget(self.nama_input)
        layout.add_widget(moduls.Label(text='Alamat'))
        self.alamat_input = moduls.TextInput()
        layout.add_widget(self.alamat_input)
        layout.add_widget(moduls.Label(text='Tanggal Lahir (DD/MM/YYYY)'))
        self.tanggal_lahir_input = moduls.TextInput()
        layout.add_widget(self.tanggal_lahir_input)
        layout.add_widget(moduls.Label(text='Nomor Telepon'))
        self.nomor_telepon_input = moduls.TextInput()
        layout.add_widget(self.nomor_telepon_input)
        self.submit_button = moduls.Button(text='Submit', on_press=self.submit, size_hint=(1, 1))
        layout.add_widget(self.submit_button)
        self.output_label = moduls.Label(text='')
        layout.add_widget(self.output_label)
        self.back_button = moduls.Button(text='Back', on_press=self.go_back, size_hint=(1, 1))
        layout.add_widget(self.back_button)
        self.add_widget(layout)

    def submit(self, instance):
        nama = self.nama_input.text
        alamat = self.alamat_input.text
        tanggal_lahir = self.tanggal_lahir_input.text
        nomor_telepon = self.nomor_telepon_input.text
        moduls.tambah_pasien(nama, alamat, tanggal_lahir, nomor_telepon)
        self.output_label.text = 'Data pasien berhasil disimpan'
        self.nama_input.text = ''
        self.alamat_input.text = ''
        self.tanggal_lahir_input.text = ''
        self.nomor_telepon_input.text = ''

    def go_back(self, instance):
        self.manager.current = 'menu'

class HapusPasien(moduls.Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = moduls.BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(moduls.Label(text='ID Pasien'))
        self.id_input = moduls.TextInput()
        layout.add_widget(self.id_input)
        self.delete_button = moduls.Button(text='Hapus', on_press=self.delete, size_hint=(1,0.5))
        layout.add_widget(self.delete_button)
        self.output_label = moduls.Label(text='')
        layout.add_widget(self.output_label)
        self.back_button = moduls.Button(text='Back', on_press=self.go_back, size_hint=(1,0.5))
        layout.add_widget(self.back_button)
        self.add_widget(layout)

    def delete(self, instance):
        id_pasien = self.id_input.text
        moduls.hapus_pasien(id_pasien)
        self.output_label.text = 'Data pasien berhasil dihapus'
        self.id_input.text = ''

    def go_back(self, instance):
        self.manager.current = 'menu'

class LihatPasien(moduls.Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = moduls.BoxLayout(orientation='vertical', padding=10, spacing=10)
        self.table_layout = moduls.GridLayout(
            cols=5,
            size_hint_y=None,
            spacing=[5, 5]
        )
        self.table_layout.bind(minimum_height=self.table_layout.setter('height'))
        layout.add_widget(self.table_layout)
        self.refresh_button = moduls.Button(text='Refresh', on_press=self.refresh, size_hint=(1, 1))
        layout.add_widget(self.refresh_button)
        self.back_button = moduls.Button(text='Back', on_press=self.go_back, size_hint=(1, 1))
        layout.add_widget(self.back_button)
        self.add_widget(layout)

    def refresh(self, instance):
        self.table_layout.clear_widgets()
        moduls.lihat_pasien(self.table_layout)
        
    def go_back(self, instance):
        self.manager.current = 'menu'

class UpdatePasien(moduls.Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = moduls.BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(moduls.Label(text='ID Pasien'))
        self.id_input = moduls.TextInput()
        layout.add_widget(self.id_input)
        layout.add_widget(moduls.Label(text='Nama Pasien'))
        self.nama_input = moduls.TextInput()
        layout.add_widget(self.nama_input)
        layout.add_widget(moduls.Label(text='Alamat'))
        self.alamat_input = moduls.TextInput()
        layout.add_widget(self.alamat_input)
        layout.add_widget(moduls.Label(text='Tanggal Lahir (DD/MM/YYYY)'))
        self.tanggal_lahir_input = moduls.TextInput()
        layout.add_widget(self.tanggal_lahir_input)
        layout.add_widget(moduls.Label(text='Nomor Telepon'))
        self.nomor_telepon_input = moduls.TextInput()
        layout.add_widget(self.nomor_telepon_input)
        self.update_button = moduls.Button(text='Update', on_press=self.update, size_hint=(1, 1.5))
        layout.add_widget(self.update_button)
        self.output_label = moduls.Label(text='')
        layout.add_widget(self.output_label)
        self.back_button = moduls.Button(text='Back', on_press=self.go_back, size_hint=(1, 1.5))
        layout.add_widget(self.back_button)
        self.add_widget(layout)

    def update(self, instance):
        id_pasien = self.id_input.text
        nama = self.nama_input.text
        alamat = self.alamat_input.text
        tanggal_lahir = self.tanggal_lahir_input.text
        nomor_telepon = self.nomor_telepon_input.text
        moduls.update_pasien(id_pasien, nama, alamat, tanggal_lahir, nomor_telepon)
        self.output_label.text = 'Data pasien berhasil diupdate'
        self.id_input.text = ''
        self.nama_input.text = ''
        self.alamat_input.text = ''
        self.tanggal_lahir_input.text = ''
        self.nomor_telepon_input.text = ''

    def go_back(self, instance):
        self.manager.current = 'menu'

class CariRekamMedisScreen(moduls.Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = moduls.BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(moduls.Label(text='Cari Berdasarkan ID atau Nama Pasien'))
        self.search_input = moduls.TextInput()
        layout.add_widget(self.search_input)
        self.search_button = moduls.Button(text='Cari', on_press=self.search, size_hint=(1, 0.2))
        layout.add_widget(self.search_button)
        
        # Create a GridLayout for the table
        self.table_layout = moduls.GridLayout(cols=10, size_hint_y=None)
        self.table_layout.bind(minimum_height=self.table_layout.setter('height'))
        layout.add_widget(self.table_layout)
        
        self.back_button = moduls.Button(text='Back', on_press=self.go_back, size_hint=(1, 0.2))
        layout.add_widget(self.back_button)
        self.add_widget(layout)

    def search(self, instance):
        search_term = self.search_input.text
        self.table_layout.clear_widgets()
        moduls.search_rekam_medis(search_term, self.search_input, self.table_layout)

    def go_back(self, instance):
        self.manager.current = 'menu'

class InputRekamMedisScreen(moduls.Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = moduls.BoxLayout(orientation='vertical', padding=10, spacing=10)
        layout.add_widget(moduls.Label(text='ID Pasien'))
        self.id_pasien_input = moduls.TextInput()
        layout.add_widget(self.id_pasien_input)
        layout.add_widget(moduls.Label(text='ID Kamar'))
        self.id_kamar_input = moduls.TextInput()
        layout.add_widget(self.id_kamar_input)
        layout.add_widget(moduls.Label(text='Tanggal Kunjungan (DD/MM/YYYY)'))
        self.tanggal_kunjungan_input = moduls.TextInput()
        layout.add_widget(self.tanggal_kunjungan_input)
        layout.add_widget(moduls.Label(text='Diagnosis'))
        self.diagnosis_input = moduls.TextInput()
        layout.add_widget(self.diagnosis_input)
        layout.add_widget(moduls.Label(text='Pengobatan'))
        self.pengobatan_input = moduls.TextInput()
        layout.add_widget(self.pengobatan_input)
        self.submit_button = moduls.Button(text='Submit', on_press=self.submit, size_hint=(1, 1))
        layout.add_widget(self.submit_button)
        self.output_label = moduls.Label(text='')
        layout.add_widget(self.output_label)
        self.back_button = moduls.Button(text='Back', on_press=self.go_back, size_hint=(1, 1))
        layout.add_widget(self.back_button)
        self.add_widget(layout)

    def submit(self, instance):
        id_pasien = self.id_pasien_input.text
        id_kamar = self.id_kamar_input.text
        tanggal_kunjungan = self.tanggal_kunjungan_input.text
        diagnosis = self.diagnosis_input.text
        pengobatan = self.pengobatan_input.text
        result = moduls.tambah_rekam_medis(id_pasien, id_kamar, tanggal_kunjungan, diagnosis, pengobatan)
        self.output_label.text = result
        self.id_pasien_input.text = ''
        self.id_kamar_input.text = ''
        self.tanggal_kunjungan_input.text = ''
        self.diagnosis_input.text = ''
        self.pengobatan_input.text = ''

    def go_back(self, instance):
        self.manager.current = 'menu'

class PasienApp(moduls.App):
    def build(self):
        moduls.create_tables()
        sm = moduls.ScreenManager()
        sm.add_widget(MenuScreen(name='menu'))
        sm.add_widget(TambahPasien(name='tambah'))
        sm.add_widget(HapusPasien(name='hapus'))
        sm.add_widget(LihatPasien(name='lihat'))
        sm.add_widget(UpdatePasien(name='update'))
        sm.add_widget(CariRekamMedisScreen(name='cari_rekam_medis'))
        sm.add_widget(InputRekamMedisScreen(name='input_rekam_medis'))
        return sm

if __name__ == '__main__':
    PasienApp().run()
#code by rivanghibran https://github.com/rivanghibran