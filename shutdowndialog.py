#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  shutdowndialog.py
#  
#  Copyright 2013 Azis Ws aka mijortsa<azis.astrojim@surabaya.di.blankon.in>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  

import pygtk
import subprocess
pygtk.require("2.0")
import gtk
import os
import sys

class ShutDownDialog:

    def __init__(self):
		
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.set_title("")
        self.window.set_size_request(430,150)
        self.window.set_position(gtk.WIN_POS_CENTER) 
        self.window.set_deletable(False)
        self.window.set_resizable(False)
        self.window.set_skip_taskbar_hint(True)
        self.window.set_decorated(True)
        self.window.show()

        # Create packing boxes. Outer level is vertical containing
        # Label upper, then horizontal box lower.
        self.box0 = gtk.VBox(False, 15)
        self.box1 = gtk.HBox(False, 0)
        

        # Add the veritcal box to the window
        self.window.add(self.box0)
    
        # hook up delete callback to event
        #self.window.connect("delete_event", self.delete_event)
    
        # hook up destroy callback to event
        #self.window.connect("destroy", self.destroy)
    
        # Sets the border width of the window.
        self.window.set_border_width(10)
       
        # Label for message
        self.label = gtk.Label()
        self.label.set_line_wrap(False)
        self.label.set_use_markup(True)
        self.label.set_markup("<span>Save and close all programs and select one action or cancel</span>")
        
        # Add the vertical elementals
        self.box0.pack_start(self.label, False, False, 0)
        self.box0.pack_start(self.box1, False, False, 0)
        
        # Creates Shutdown buttons        
        image1 = gtk.Image()
        image1.set_from_file("/usr/share/shutdowndialog/image/shutdown.png")
        image1.show()
        self.shutdown_button = gtk.Button()
        self.shutdown_button.set_size_request(96, 96)
        self.shutdown_button.add(image1)
        self.shutdown_button.show()
        
        # Creates Reboot buttons
        image2 = gtk.Image()
        image2.set_from_file("/usr/share/shutdowndialog/image/reboot.png")
        image2.show()
        self.reboot_button = gtk.Button()
        self.reboot_button.set_size_request(96, 96)
        self.reboot_button.add(image2)
        self.reboot_button.show()
        
        # Creates Hibernate buttons
        image3 = gtk.Image()
        image3.set_from_file("/usr/share/shutdowndialog/image/hibernate.png")
        image3.show()
        self.hibernate_button = gtk.Button()
        self.hibernate_button.set_size_request(96, 96)
        self.hibernate_button.add(image3)
        self.hibernate_button.show()
        
        # Creates Cancel buttons
        image4 = gtk.Image()
        image4.set_from_file("/usr/share/shutdowndialog/image/cancel.png")
        image4.show()
        self.cancel_button = gtk.Button()
        self.cancel_button.set_size_request(96, 96)
        self.cancel_button.add(image4)
        self.cancel_button.show()
    
        # Hook up enable button to callback on click event
        self.shutdown_button.connect("clicked", self.shutdown)
        self.reboot_button.connect("clicked", self.reboot)
        self.hibernate_button.connect("clicked", self.hibernate)
    
        # Hook up the cancel button to destroy callback on click event
        self.cancel_button.connect_object("clicked", gtk.Widget.destroy, self.window)
    
        # This packs the buttons into the horizontal box (container).
        self.box1.pack_start(self.cancel_button, True, True, 5)
        self.cancel_button.show()

        self.box1.pack_start(self.hibernate_button, True, True, 5)
        self.hibernate_button.show()
        
        self.box1.pack_start(self.reboot_button, True, True, 5)
        self.reboot_button.show()

        self.box1.pack_start(self.shutdown_button, True, True, 5)
        self.shutdown_button.show()

        # Make the items visible...
        self.label.show()
        self.box1.show()
        self.box0.show()
    
        # Make the window visible...
        self.window.show()
    
    def main(self):
        # All PyGTK applications must have a gtk.main(). Control ends here
        # and waits for an event to occur (like a key press or mouse event).
        gtk.main()      
 
    def shutdown(self, widget = None, data = None):
        os.system("dbus-send --system --print-reply --dest=org.freedesktop.ConsoleKit /org/freedesktop/ConsoleKit/Manager org.freedesktop.ConsoleKit.Manager.Stop &")
        gtk.main_quit()
     
    def reboot(self, widget = None, data = None):
        os.system("dbus-send --system --print-reply --dest=org.freedesktop.ConsoleKit /org/freedesktop/ConsoleKit/Manager org.freedesktop.ConsoleKit.Manager.Restart &")
        gtk.main_quit()
    
    def hibernate(self, widget = None, data = None):
        os.system("dbus-send --print-reply --system --dest=org.freedesktop.UPower /org/freedesktop/UPower org.freedesktop.UPower.Hibernate &")
        gtk.main_quit()

# If the program is run directly or passed as an argument to the python
# interpreter then create a HelloWorld instance and show it
if __name__ == "__main__":
    launcher = ShutDownDialog()
    launcher.main()