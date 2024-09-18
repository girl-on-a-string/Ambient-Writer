#imports

import palettes
import tkinter as tk

class startGUI:
    def __init__(self):
        #create window

        self.root = tk.Tk()
        self.root.geometry("2000x1000")
        self.root.title("AmbientWriter")

        #create frame

        frame = tk.Frame(self.root);

        #define grid

        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=1)
        self.root.columnconfigure(2, weight=1)
        self.root.columnconfigure(3, weight=1)
        self.root.columnconfigure(4, weight=1)
        self.root.columnconfigure(5, weight=1)
        self.root.columnconfigure(6, weight=1)
        self.root.columnconfigure(7, weight=1)

        #place widgets



        #create window

        self.root.mainloop()

# class docGUI:
#     def __init__(self):
#         self.root = tk.Tk()
#         self.root.geometry("2000x1000")
#         self.root.title("(AmbientWriter)"); #include name of doc or "untitled document" in var before. ex. "title of book (ambientwriter)" later

#         self.textbox = tk.Text(self.root, height=5, font=("Arial", 16))
#         self.textbox.pack(padx=10, pady=10)

#         #make menu

#         menu = tk.Menu(self.root);

#         self.root.mainloop()

startGUI()

