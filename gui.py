#imports

import tkinter as tk

class docGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("2000x1000")
        self.root.title("(AmbientWriter)"); #include name of doc or "untitled document" in var before. ex. "title of book (ambientwriter)" later

        self.textbox = tk.Text(self.root, height=5, font=("Arial", 10))
        self.textbox.pack(padx=10, pady=10)

        #make menus
        menuBar = tk.Menu(self.root) #main menubar that contains all others

        fileMenu = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(menu=fileMenu, label="File")
        fileMenu.add_command(label="New File", accelerator="Ctrl+N")
        fileMenu.add_command(label="Open File", accelerator="Ctrl+O")
        fileMenu.add_command(label="Reload File", accelerator="Ctrl+R")
        fileMenu.add_command(label="New Window", accelerator="Ctrl+Shift+N")
        fileMenu.add_separator()
        fileMenu.add_command(label="Save", accelerator="Ctrl+S")
        fileMenu.add_command(label="Save As", accelerator="Ctrl+Shift+S")
        fileMenu.add_command(label="Rename")
        fileMenu.add_separator()
        fileMenu.add_command(label="Export")
        fileMenu.add_command(label="Print")
        fileMenu.add_command(label="Page Setup", accelerator="Ctrl+P")

        editMenu = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(menu=editMenu, label="Edit")
        editMenu.add_command(label="Undo", accelerator="Ctrl+Z")
        editMenu.add_command(label="Redo", accelerator="Ctrl+Y")
        editMenu.add_separator()
        editMenu.add_command(label="Cut", accelerator="Ctrl+X")
        editMenu.add_command(label="Copy", accelerator="Ctrl+C")
        editMenu.add_command(label="Paste", accelerator="Ctrl+Z")
        editMenu.add_command(label="Select All", accelerator="Ctrl+A")
        editMenu.add_separator()
        editMenu.add_command(label="Find", accelerator="Ctrl+F")
        editMenu.add_command(label="Replace", accelerator="Ctrl+H")

        formatMenu = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(menu=formatMenu, label="Format")
        headingSubMenu = tk.Menu(formatMenu, tearoff=0)
        formatMenu.add_cascade(menu=headingSubMenu, label="Heading")
        headingSubMenu.add_radiobutton(label="Normal")
        headingSubMenu.add_radiobutton(label="Heading 1")
        headingSubMenu.add_radiobutton(label="Heading 2")
        headingSubMenu.add_radiobutton(label="Heading 3")
        headingSubMenu.add_radiobutton(label="Heading 4")
        headingSubMenu.add_radiobutton(label="Heading 5")
        headingSubMenu.add_radiobutton(label="Heading 6")
        formatMenu.add_checkbutton(label="Italics", accelerator="Ctrl+I")
        formatMenu.add_checkbutton(label="Bold", accelerator="Ctrl+B")
        formatMenu.add_checkbutton(label="Underline", accelerator="Ctrl+U")
        formatMenu.add_checkbutton(label="Highlight")
        formatMenu.add_checkbutton(label="Strikethrough", accelerator="Ctrl+K")
        formatMenu.add_checkbutton(label="Superscript", accelerator="Ctrl+^")
        formatMenu.add_checkbutton(label="Subscript", accelerator="Ctrl+_")
        formatMenu.add_separator()
        formatMenu.add_command(label="Align Text Left", accelerator="Ctrl+{")
        formatMenu.add_command(label="Align Text Center", accelerator="Ctrl+|")
        formatMenu.add_command(label="Align Text Right", accelerator="Ctrl+}")

        toolsMenu = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(menu=toolsMenu, label="Tools")
        toolsMenu.add_command(label="Word Count...")
        toolsMenu.add_command(label="Daily Goals...")

        settingsMenu = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(menu=settingsMenu, label="Settings")
        settingsMenu.add_command(label="Themes")
        settingsMenu.add_command(label="Preferences")

        helpMenu = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(menu=helpMenu, label="Help")
        helpMenu.add_command(label="About AmbientWriter")

        #init

        self.root.config(menu=menuBar)
        self.root.mainloop()

docGUI()

# startGUI()

