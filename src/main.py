import math

import gi
gi.require_version("Gtk", "4.0")
from gi.repository import GLib, Gtk

outline_r = 0
outline_g = 0
outline_b = 0
outline_a = 0

txt_r = 0
txt_g = 0
txt_b = 0
txt_a = 0

bg_r = 0
bg_g = 0
bg_b = 0
bg_a = 0

outline_thickness_v = 5
outline_roundness_v = 5

class RiceTool(Gtk.Application):
    def __init__(self) -> None:
        super().__init__(application_id="io.scripterblox.rice_tool")
        GLib.set_application_name("Hyprland Ricing Tool")

    def applyf(abc1, abc2):
        waybar_file = """
@define-color txt_main rgba("""+str(txt_r)+""", """+str(txt_g)+""", """+str(txt_b)+""", """+str(txt_a)+""");
@define-color outline rgba("""+str(math.ceil(outline_r))+""", """+str(math.ceil(outline_g))+""", """+str(math.ceil(outline_b))+""", """+str(outline_a)+""");
        @define-color bg rgba("""+str(math.ceil(bg_r))+""", """+str(math.ceil(bg_g))+""", """+str(math.ceil(bg_b))+""", """+str(bg_a)+""");

#battery,
#window,
#workspaces,
#clock,
#custom-weather,
#temperature,
#memory,
#cpu,
#pulseaudio,
#network,
#tray,
#custom-power { 
  border: """+str(outline_thickness_v)+"""px solid @outline;
}
"""

        with open("/home/scripterblox/.config/waybar/cols.css", "w") as file:
            file.write(waybar_file)


def on_activate(app):
    win = Gtk.Window(application=app)
    win.set_modal(True)
    win.present()

    outline_col_label = Gtk.Label(label="Hyprland/Waybar outline color")
    outline_col_r_label = Gtk.Label(label="R")
    outline_col_g_label = Gtk.Label(label="G")
    outline_col_b_label = Gtk.Label(label="B")
    outline_col_a_label = Gtk.Label(label="A")
    outline_col_r_scale = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 0, 255, 1)
    outline_col_r_scale.set_hexpand(True)
    outline_col_r_scale.connect("value-changed", lambda x: globals().__setitem__("outline_r", x.get_value()))
    outline_col_g_scale = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 0, 255, 1)
    outline_col_r_scale.set_hexpand(True)
    outline_col_g_scale.connect("value-changed", lambda x: globals().__setitem__("outline_g", x.get_value()))
    outline_col_b_scale = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 0, 255, 1)
    outline_col_r_scale.set_hexpand(True)
    outline_col_b_scale.connect("value-changed", lambda x: globals().__setitem__("outline_b", x.get_value()))
    outline_col_a_scale = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 0, 1, 0.05)
    outline_col_a_scale.set_hexpand(True)
    outline_col_a_scale.connect("value-changed", lambda x: globals().__setitem__("outline_a", x.get_value()))
    
    outline_col_box = Gtk.Grid()
    outline_col_box.attach(outline_col_label, 0, 0, 2, 1)
    outline_col_box.attach(outline_col_r_label, 0, 1, 1, 1)
    outline_col_box.attach(outline_col_g_label, 0, 2, 1, 1)
    outline_col_box.attach(outline_col_b_label, 0, 3, 1, 1)
    outline_col_box.attach(outline_col_a_label, 0, 4, 1, 1)

    outline_col_box.attach(outline_col_r_scale, 1, 1, 1, 1)
    outline_col_box.attach(outline_col_g_scale, 1, 2, 1, 1)
    outline_col_box.attach(outline_col_b_scale, 1, 3, 1, 1)
    outline_col_box.attach(outline_col_a_scale, 1, 4, 1, 1)

    colors_bar = Gtk.Grid()
    colors_bar.attach(outline_col_box, 0, 0, 1, 1)


    waybar_col_label = Gtk.Label(label="Waybar text color")
    waybar_col_r_label = Gtk.Label(label="R")
    waybar_col_g_label = Gtk.Label(label="G")
    waybar_col_b_label = Gtk.Label(label="B")
    waybar_col_a_label = Gtk.Label(label="A")
    waybar_col_r_scale = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 0, 255, 1)
    waybar_col_r_scale.set_hexpand(True)
    waybar_col_r_scale.connect("value-changed", lambda x: globals().__setitem__("txt_r", x.get_value()))
    waybar_col_g_scale = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 0, 255, 1)
    waybar_col_r_scale.set_hexpand(True)
    waybar_col_g_scale.connect("value-changed", lambda x: globals().__setitem__("txt_g", x.get_value()))
    waybar_col_b_scale = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 0, 255, 1)
    waybar_col_r_scale.set_hexpand(True)
    waybar_col_b_scale.connect("value-changed", lambda x: globals().__setitem__("txt_b", x.get_value()))
    waybar_col_a_scale = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 0, 1, 0.05)
    waybar_col_a_scale.set_hexpand(True)
    waybar_col_a_scale.connect("value-changed", lambda x: globals().__setitem__("txt_a", x.get_value()))
    
    waybar_col_box = Gtk.Grid()
    waybar_col_box.attach(waybar_col_label, 0, 0, 2, 1)
    waybar_col_box.attach(waybar_col_r_label, 0, 1, 1, 1)
    waybar_col_box.attach(waybar_col_g_label, 0, 2, 1, 1)
    waybar_col_box.attach(waybar_col_b_label, 0, 3, 1, 1)
    waybar_col_box.attach(waybar_col_a_label, 0, 4, 1, 1)

    waybar_col_box.attach(waybar_col_r_scale, 1, 1, 1, 1)
    waybar_col_box.attach(waybar_col_g_scale, 1, 2, 1, 1)
    waybar_col_box.attach(waybar_col_b_scale, 1, 3, 1, 1)
    waybar_col_box.attach(waybar_col_a_scale, 1, 4, 1, 1)


    waybar_background_label = Gtk.Label(label="Waybar background color")
    waybar_background_r_label = Gtk.Label(label="R")
    waybar_background_g_label = Gtk.Label(label="G")
    waybar_background_b_label = Gtk.Label(label="B")
    waybar_background_a_label = Gtk.Label(label="A")
    waybar_background_r_scale = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 0, 255, 1)
    waybar_background_r_scale.set_hexpand(True)
    waybar_background_r_scale.connect("value-changed", lambda x: globals().__setitem__("bg_r", x.get_value()))
    waybar_background_g_scale = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 0, 255, 1)
    waybar_background_g_scale.set_hexpand(True)
    waybar_background_g_scale.connect("value-changed", lambda x: globals().__setitem__("bg_g", x.get_value()))
    waybar_background_b_scale = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 0, 255, 1)
    waybar_background_b_scale.set_hexpand(True)
    waybar_background_b_scale.connect("value-changed", lambda x: globals().__setitem__("bg_b", x.get_value()))
    waybar_background_a_scale = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 0, 1, 0.05)
    waybar_background_a_scale.set_hexpand(True)
    waybar_background_a_scale.connect("value-changed", lambda x: globals().__setitem__("bg_a", x.get_value()))
    
    waybar_background_box = Gtk.Grid()
    waybar_background_box.attach(waybar_background_label, 0, 0, 2, 1)
    waybar_background_box.attach(waybar_background_r_label, 0, 1, 1, 1)
    waybar_background_box.attach(waybar_background_g_label, 0, 2, 1, 1)
    waybar_background_box.attach(waybar_background_b_label, 0, 3, 1, 1)
    waybar_background_box.attach(waybar_background_a_label, 0, 4, 1, 1)

    waybar_background_box.attach(waybar_background_r_scale, 1, 1, 1, 1)
    waybar_background_box.attach(waybar_background_g_scale, 1, 2, 1, 1)
    waybar_background_box.attach(waybar_background_b_scale, 1, 3, 1, 1)
    waybar_background_box.attach(waybar_background_a_scale, 1, 4, 1, 1)

    
    colors_bar = Gtk.Grid()
    colors_bar.attach(outline_col_box, 0, 0, 1, 1)
    colors_bar.attach(waybar_col_box, 0, 1, 1, 1)
    colors_bar.attach(waybar_background_box, 0, 2, 1, 1)
    
    outline_thickness_label = Gtk.Label(label="Outline Thickness")
    outline_thickness_selector = Gtk.SpinButton()
    outline_thickness_selector.props.adjustment = Gtk.Adjustment(upper=50, step_increment=1)
    outline_thickness_selector.connect("value-changed", lambda x: globals().__setitem__("outline_thickness_v", x.get_value()))

    outline_thickness = Gtk.Grid()
    outline_thickness.attach(outline_thickness_label, 0, 0, 1, 1)
    outline_thickness.attach(outline_thickness_selector, 0, 1, 1, 1)


    outline_roundness_label = Gtk.Label(label="Outline Roundness")
    outline_roundness_selector = Gtk.SpinButton()
    outline_roundness_selector.props.adjustment = Gtk.Adjustment(upper=50, step_increment=1)
    outline_roundness_selector.connect("value-changed", lambda x: globals().__setitem__("outline_roundness_v", x.get_value()))
    
    outline_roundness = Gtk.Grid()
    outline_roundness.attach(outline_roundness_label, 0, 0, 1, 1)
    outline_roundness.attach(outline_roundness_selector, 0, 1, 1, 1)


    values = Gtk.Grid()
    values.attach(outline_thickness, 0, 0, 1, 1)
    values.attach(outline_roundness, 0, 1, 1, 1)


    apply = Gtk.Button.new_with_label("Apply")
    apply.connect("clicked", app.applyf)


    grid = Gtk.Grid()
    grid.attach(colors_bar, 0, 0, 1, 3)
    grid.attach(values, 1, 0, 1, 3)
    grid.attach(apply, 1, 3, 1, 1)
    
    win.set_child(grid)
    win.set_default_size(500, 200)


app = RiceTool()
app.set_application_id("dialog")
app.connect('activate', on_activate)
app.run()
