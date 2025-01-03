#code by rivanghibran https://github.com/rivanghibran
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.uix.popup import Popup
from functions import tambah_pasien, lihat_pasien, update_pasien, hapus_pasien, tambah_rekam_medis, search_rekam_medis
from export import ekspor_ke_excel
from models import create_tables
from config import connect_db
#code by rivanghibran https://github.com/rivanghibran
