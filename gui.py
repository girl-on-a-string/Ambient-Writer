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
        menuBar = tk.Menu(self.root) #main menubar that contains all others

        fileMenu = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(menu=fileMenu, label="File")
        fileMenu.add_command(label="New File", accelerator="Ctrl+N")
        fileMenu.add_command(label="Open File", accelerator="Ctrl+O")
        fileMenu.add_command(label="Reload File", accelerator="Ctrl+R")
        fileMenu.add_command(label="New Workspace", accelerator="Ctrl+Shift+N")
        fileMenu.add_separator()
        fileMenu.add_command(label="Save", accelerator="Ctrl+S")
        fileMenu.add_command(label="Save As", accelerator="Ctrl+Shift+S")
        fileMenu.add_command(label="Rename")
        fileMenu.add_command(label="Save All")
        fileMenu.add_separator()
        fileMenu.add_command(label="Print")
        fileMenu.add_command(label="Page Setup", accelerator="Ctrl+P")

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

