import gi
gi.require_version("Gtk", "4.0")
from gi.repository import GLib, Gtk

class RiceTool(Gtk.Application):
    def __init__(self) -> None:
        super().__init__(application_id="io.scripterblox.rice_tool")
        GLib.set_application_name("Hyprland Ricing Tool")

    def do_activate(self):
        win = Gtk.ApplicationWindow(application=self, title="Hello World")
        win.present()

def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    btn = Gtk.Button(label="Hello, World!")
    btn.connect('clicked',
                lambda x:
                    win.close()
                )
    win.set_child(btn)
    win.present()

app = RiceTool()
app.connect('activate', on_activate)
app.run()
