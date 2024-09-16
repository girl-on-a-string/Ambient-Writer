#imports

import tkinter as tk

class myGUI:
    def __init__(self):
        self.root = tk.Tk();
        self.root.geometry("2000x1000");
        self.root.title("(AmbientWriter)"); #include name of doc or "untitled document" in var before. ex. "title of book (ambientwriter)" later

        self.label = tk.Label(self.root, text="Your message", font=("arial", 18))

        self.root.mainloop();

myGUI();