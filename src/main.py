import gi
gi.require_version("Gtk", "4.0")
from gi.repository import GLib, Gtk

class RiceTool(Gtk.Application):
    def __init__(self) -> None:
        super().__init__(application_id="io.scripterblox.rice_tool")
        GLib.set_application_name("Hyprland Ricing Tool")

def on_activate(app):
    win = Gtk.Window(application=app)
    win.set_modal(True)
    win.present()

    outline_col_label = Gtk.Label(label="Hyprland/Waybar outline color")
    outline_col_r_label = Gtk.Label(label="R")
    outline_col_g_label = Gtk.Label(label="G")
    outline_col_b_label = Gtk.Label(label="B")
    outline_col_r_scale = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 0, 255, 1)
    outline_col_r_scale.set_hexpand(True)
    outline_col_g_scale = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 0, 255, 1)
    outline_col_r_scale.set_hexpand(True)
    outline_col_b_scale = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 0, 255, 1)
    outline_col_r_scale.set_hexpand(True)
    
    outline_col_box = Gtk.Grid()
    outline_col_box.attach(outline_col_label, 0, 0, 2, 1)
    outline_col_box.attach(outline_col_r_label, 0, 1, 1, 1)
    outline_col_box.attach(outline_col_g_label, 0, 2, 1, 1)
    outline_col_box.attach(outline_col_b_label, 0, 3, 1, 1)

    outline_col_box.attach(outline_col_r_scale, 1, 1, 1, 1)
    outline_col_box.attach(outline_col_g_scale, 1, 2, 1, 1)
    outline_col_box.attach(outline_col_b_scale, 1, 3, 1, 1)

    colors_bar = Gtk.Grid()
    colors_bar.attach(outline_col_box, 0, 0, 1, 1)

    
    outline_thickness_label = Gtk.Label(label="Outline Thickness")
    outline_thickness_selector = Gtk.SpinButton()

    outline_thickness = Gtk.Grid()
    outline_thickness.attach(outline_thickness_label, 0, 0, 1, 1)
    outline_thickness.attach(outline_thickness_selector, 0, 1, 1, 1)

    outline_roundness_label = Gtk.Label(label="Outline Roundness")
    outline_roundness_selector = Gtk.SpinButton()
    
    outline_roundness = Gtk.Grid()
    outline_roundness.attach(outline_roundness_label, 0, 0, 1, 1)
    outline_roundness.attach(outline_roundness_selector, 0, 1, 1, 1)

    values = Gtk.Grid()
    values.attach(outline_thickness, 0, 0, 1, 1)
    values.attach(outline_roundness, 0, 1, 1, 1)


    grid = Gtk.Grid()
    grid.attach(colors_bar, 0, 0, 1, 3)
    grid.attach(values, 1, 0, 1, 2)
    
    win.set_child(grid)
    win.set_default_size(500, 200)

    """box = Gtk.Box()
    win.set_child(box)

    button1 = Gtk.Button(label="Test")
    button1.connect("clicked", lambda x: print("Test"))
    box.append(button1)"""


app = RiceTool()
app.set_application_id("dialog")
app.connect('activate', on_activate)
app.run()
