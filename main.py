import gi
gi.require_version("Gtk", "3.0")
gi.require_version("Gdk", "3.0")
from gi.repository import Gtk, GLib, Gdk
import threading
import time


class Window(Gtk.Window):
    def __init__(self,*args,**kwargs):
        super(Window, self).__init__(*args, **kwargs)
        self.connect("destroy", Gtk.main_quit)
        self.resize(400, 300)
        self.main_box = Gtk.VBox()
        self.hbox = Gtk.HBox()
        self.button = Gtk.Button(label="Tamam")
        self.button.connect("clicked", self.start_time)
        self.time_entry = Gtk.Entry()
        self.hbox.pack_start(self.time_entry, True, True, 0)
        self.hbox.pack_start(self.button, False, False, 0)
        self.main_box.pack_start(self.hbox, False, False, 0)
        self.count_label = Gtk.Label(label="Kalan süre:")
        self.main_box.pack_start(self.count_label, False, False, 0)
        self.set_resizable(False)
        self.add(self.main_box)
        self.show_all()

    def func(self):
        current_hour = int(time.strftime("%H"))
        current_minute = int(time.strftime("%M"))
        gecen_dakika = (current_hour * 60) + current_minute
        text = self.time_entry.get_text().split(":")
        istenen_saat = text[0]
        istenen_dakika = text[1]
        gecmesi_gereken_dakika = (int(istenen_saat) * 60) + int(istenen_dakika)
        a = gecmesi_gereken_dakika - gecen_dakika
        kalan_saat = int(a / 60)
        kalan_dakika = int(a - kalan_saat * 60)
        self.count_label.set_label("Kalan süre {0} saat {1} dakika".format(kalan_saat, kalan_dakika))
        return True

    def start_time(self, widget):
        a = self.deneme()
        self.set_keep_above(True)
        GLib.timeout_add(10000, self.func)


if __name__ == "__main__":
    pencere = Window()
    Gtk.main()
