#!/usr/bin/env python3
import gi, subprocess, json, os, math, time
import socket, threading

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, Gdk

RECENTS_FILE = os.path.expanduser("~/.cache/emoji_recents.json")

EMOJIS = [
    "😀","😁","😂","🤣","😃","😄","😅","😆","😉","😊","😍","😘",
    "😎","🤩","😏","😢","😭","😡","🤔","😴","👍","👎","🙏","🔥",
    "💯","🎉","✨","❤️","💀","😇","🥳","🤯","🤖","👀","😺","😻"
]

ICON_SIZE = 48
COLS = 8
PADDING = 20
TOP_BAR_HEIGHT = 40

#SKIN_TONES = ["🏻","🏼","🏽","🏾","🏿"]

def load_recents():
    if os.path.exists(RECENTS_FILE):
        with open(RECENTS_FILE, "r") as f:
            return json.load(f)
    return []

def save_recents(recents):
    os.makedirs(os.path.dirname(RECENTS_FILE), exist_ok=True)
    with open(RECENTS_FILE, "w") as f:
        json.dump(recents[:20], f)



class EmojiWindow(Gtk.Window):
    def __init__(self):
        try:
            print(
                subprocess.check_output(
                    ["xdotool", "getwindowfocus", "getwindowname"]
                ).decode().strip()
            )
            self.previous_window = subprocess.check_output(
                ["xdotool", "getwindowfocus"]
            ).decode().strip()
        except Exception:
            self.previous_window = None
        
        super().__init__(title="Emoji Panel")
        #self.set_default_size(100, 100)
        self.set_size_request(ICON_SIZE * COLS , -1)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_keep_above(True)

        self.recents = load_recents()

        vbox = Gtk.VBox(spacing=6)
        self.add(vbox)

        #self.entry = Gtk.Entry()
        #self.entry.set_placeholder_text("Search emojis...")
        #self.entry.connect("changed", self.filter_emojis)
        #vbox.pack_start(self.entry, False, False, 5)

        self.grid = Gtk.FlowBox()
        self.grid.set_valign(Gtk.Align.START)
        self.grid.set_halign(Gtk.Align.START)
        self.grid.set_column_spacing(0)
        self.grid.set_row_spacing(0)
        self.grid.set_homogeneous(True)
        self.grid.set_max_children_per_line(COLS)
        self.grid.set_selection_mode(Gtk.SelectionMode.NONE)
        vbox.pack_start(self.grid, False, False, 0)

        self.populate(self.recents + EMOJIS)
        self.hide()

        ## SERVICE LISTENER!
        threading.Thread(target=self.listen, daemon=True).start()
        
    
    def show_panel(self):
        self.present()

    def populate(self, emojis):
        for child in self.grid.get_children():
            self.grid.remove(child)

        for e in emojis:
            btn = Gtk.Button(label=e)
            btn.set_size_request(ICON_SIZE, ICON_SIZE)
            btn.set_hexpand(False)
            btn.set_vexpand(False)
            btn.set_halign(Gtk.Align.CENTER)
            btn.set_valign(Gtk.Align.CENTER)
            btn.connect("clicked", self.on_click, e)
            self.grid.add(btn)
        self.show_all()

    def on_hover(self, widget, event):
        widget.set_name("hover")

    def on_click(self, widget, emoji):
        self.hide()
        while Gtk.events_pending():
            Gtk.main_iteration()

        time.sleep(0.2)
        self.type_emoji(emoji, self.previous_window)

        if emoji in self.recents:
            self.recents.remove(emoji)
        self.recents.insert(0, emoji)
        save_recents(self.recents)
        self.hide()

    def filter_emojis(self, entry):
        text = entry.get_text().lower()
        if not text:
            self.populate(self.recents + EMOJIS)
            return

        filtered = [e for e in EMOJIS if text in e]
        self.populate(filtered)
    
    def type_emoji(self, emoji, target_window):
        if target_window:
            subprocess.run(
                ["xdotool", "windowactivate", "--sync", target_window]
            )
        
        subprocess.run(
            ["xdotool", "type", "--delay", "50", "--clearmodifiers", emoji]
        )

    ## listener voor de service op te roepen
    def listen(self):
        sock_path = "/tmp/emoji.sock"

            try:
                os.remove(sock_path)
            except FileNotFoundError:
                pass

            s = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
            s.bind(sock_path)

            while True:
                data = s.recv(1024)
                msg = data.decode().strip()

                if msg == "show":
                    self.show_panel()


if __name__ == "__main__":
    win = EmojiWindow()
    #win.show_panel()
    Gtk.main()
    
