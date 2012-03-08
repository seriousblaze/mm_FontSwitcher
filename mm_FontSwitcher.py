#!/usr/bin/env python

from gi.repository import Gtk, Gdk
from subprocess import *
 
class aStatusIcon:
    def __init__ (self):
        self.statusicon = Gtk.StatusIcon()
        self.statusicon.set_from_stock(Gtk.STOCK_SELECT_FONT)
        self.statusicon.connect("activate", self.click_event)

        self.zgy_layout = "[us,mm\tzawgyi]"
        self.uni_layout = "[us,mm\tmm3]"

    def get_layout (self):
        out_file = Popen("gconftool-2 --get '/desktop/gnome/peripherals/keyboard/kbd/layouts'", shell=True, stdout=PIPE).stdout
        out = out_file.read().strip ()
        out_file.close ()
        return out
            
        #    def click_event(self, icon, button, time):
    def click_event( self,  statusicon):

        self.menu = Gtk.Menu()

        unicode_item = Gtk.MenuItem()
        unicode_item.set_label("Unicode")
        zgy_item = Gtk.MenuItem()
        zgy_item.set_label("Zawgyi-One")
        quit_item = Gtk.MenuItem()
        quit_item.set_label("Quit")

        def layout_toggle (toggle):
            layout = self.get_layout ()
            if layout == self.zgy_layout:
                Popen("gconftool-2 --set --type list --list-type string '/desktop/gnome/peripherals/keyboard/kbd/layouts' '[us,mm\tmm3]'", shell=True)
                Popen("sed -i 's/TharLon/zawgyi-one/g' ~/.fonts.conf", shell=True)
                zgy_item.set_label("Changed")
            else:
                Popen("gconftool-2 --set --type list --list-type string '/desktop/gnome/peripherals/keyboard/kbd/layouts' '[us,mm\tzawgyi]'", shell=True)
                Popen("sed -i 's/zawgyi-one/TharLon/g' ~/.fonts.conf", shell=True)

        unicode_item.connect("activate", layout_toggle)
        zgy_item.connect("activate", layout_toggle)
        quit_item.connect("activate", Gtk.main_quit)

        out = self.get_layout()
        if out == self.uni_layout:
            self.menu.append(unicode_item)
        else:
            self.menu.append(zgy_item)
        
        self.menu.append(quit_item)

        self.menu.show_all()

        def pos(menu, icon):
            return (Gtk.StatusIcon.position_menu(menu, icon))

        self.menu.popup(None, None, pos, self.statusicon, 0, Gdk.CURRENT_TIME)

aStatusIcon()
Gtk.main()
