#imports

import palettes
import tkinter as tk

# class startGUI:
#     def __init__(self):
#         #create window

#         self.root = tk.Tk()
#         self.root.geometry("2000x1000")
#         self.root.title("AmbientWriter")

#         #create frame

#         frame = tk.Frame(self.root);
#         frame.pack()

#         #create widgets

#         welcome = tk.Label(frame, text="Welcome to AmbientWriter", font=75)
#         welcome.pack()

#         openRecentBtn = tk.Button(frame, text="Open recent document")
#         openRecentBtn.pack()

#         createNewBtn = tk.Button(frame, text="Create new document")
#         createNewBtn.pack()

#         recentsList = tk.Label(frame, text="Recent documents...")
#         recentsList.pack();

#         #create window

#         self.root.mainloop()

class docGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("2000x1000")
        self.root.title("(AmbientWriter)"); #include name of doc or "untitled document" in var before. ex. "title of book (ambientwriter)" later

        self.textbox = tk.Text(self.root, height=5, font=("Arial", 10))
        self.textbox.pack(padx=10, pady=10)

        #make menu

        self.root.option_add("*tearoff", False)

        menuBar = tk.Menu(self.root) #main menubar that contains all others


        fileMenu = tk.Menu(menuBar)
        menuBar.add_cascade(menu=fileMenu, label="File")

        editMenu = tk.Menu(menuBar)
        menuBar.add_cascade(menu=editMenu, label="Edit")

        formatMenu = tk.Menu(menuBar)
        menuBar.add_cascade(menu=formatMenu, label="Format")

        toolsMenu = tk.Menu(menuBar)
        menuBar.add_cascade(menu=toolsMenu, label="Tools")

        settingsMenu = tk.Menu(menuBar)
        menuBar.add_cascade(menu=settingsMenu, label="Settings")

        helpMenu = tk.Menu(menuBar)
        menuBar.add_cascade(menu=helpMenu, label="Help")

        #init

        self.root.config(menu=menuBar)
        self.root.mainloop()

docGUI()

# startGUI()

