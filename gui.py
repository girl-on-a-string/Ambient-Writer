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
        frame.pack()

        #create widgets

        label = tk.Label(frame, text="Welcome to AmbientWriter", font=75)
        label.pack()

        openRecentBtn = tk.Button(frame, text="Open recent document")

        createNewBtn = tk.Button(frame, text="Create new document")

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

