#imports

# import guiFunct
import tkinter as tk

#class

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
        btnNewFile = fileMenu.add_command(label="New File", accelerator="Ctrl+N")
        btnOpenFile = fileMenu.add_command(label="Open File", accelerator="Ctrl+O")
        btnReloadFile = fileMenu.add_command(label="Reload File", accelerator="Ctrl+R")
        btnNewWindow = fileMenu.add_command(label="New Window", accelerator="Ctrl+Shift+N")
        fileMenu.add_separator()
        btnSave = fileMenu.add_command(label="Save", accelerator="Ctrl+S")
        btnSaveAs = fileMenu.add_command(label="Save As", accelerator="Ctrl+Shift+S")
        btnRename = fileMenu.add_command(label="Rename")
        fileMenu.add_separator()
        btnExport = fileMenu.add_command(label="Export")
        btnPrint = fileMenu.add_command(label="Print")
        btnPageSetup = fileMenu.add_command(label="Page Setup", accelerator="Ctrl+P")

        editMenu = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(menu=editMenu, label="Edit")
        btnUndo = editMenu.add_command(label="Undo", accelerator="Ctrl+Z")
        btnRedo = editMenu.add_command(label="Redo", accelerator="Ctrl+Y")
        editMenu.add_separator()
        btnCut = editMenu.add_command(label="Cut", accelerator="Ctrl+X")
        btnCopy = editMenu.add_command(label="Copy", accelerator="Ctrl+C")
        btnPaste = editMenu.add_command(label="Paste", accelerator="Ctrl+Z")
        btnSelectAll = editMenu.add_command(label="Select All", accelerator="Ctrl+A")
        editMenu.add_separator()
        btnFind = editMenu.add_command(label="Find", accelerator="Ctrl+F")
        btnReplace = editMenu.add_command(label="Replace", accelerator="Ctrl+H")

        formatMenu = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(menu=formatMenu, label="Format")
        headingSubMenu = tk.Menu(formatMenu, tearoff=0)
        formatMenu.add_cascade(menu=headingSubMenu, label="Heading")
        btnHeadNorm = headingSubMenu.add_radiobutton(label="Normal")
        btnHeadOne = headingSubMenu.add_radiobutton(label="Heading 1")
        btnHeadTwo = headingSubMenu.add_radiobutton(label="Heading 2")
        btnHeadThree = headingSubMenu.add_radiobutton(label="Heading 3")
        btnHeadFour = headingSubMenu.add_radiobutton(label="Heading 4")
        btnHeadFive = headingSubMenu.add_radiobutton(label="Heading 5")
        btnHeadSix = headingSubMenu.add_radiobutton(label="Heading 6")
        btnFormatItalics = formatMenu.add_checkbutton(label="Italics", accelerator="Ctrl+I")
        btnFormatBold = formatMenu.add_checkbutton(label="Bold", accelerator="Ctrl+B")
        btnFormatUnderline = formatMenu.add_checkbutton(label="Underline", accelerator="Ctrl+U")
        btnFormatHighlight = formatMenu.add_checkbutton(label="Highlight")
        btnFormatStrike = formatMenu.add_checkbutton(label="Strikethrough", accelerator="Ctrl+K")
        btnFormatSuper = formatMenu.add_checkbutton(label="Superscript", accelerator="Ctrl+^")
        btnFormatSub = formatMenu.add_checkbutton(label="Subscript", accelerator="Ctrl+_")
        formatMenu.add_separator()
        btnAlignLeft = formatMenu.add_command(label="Align Text Left", accelerator="Ctrl+{")
        btnAlignCenter = formatMenu.add_command(label="Align Text Center", accelerator="Ctrl+|")
        btnAlignRight = formatMenu.add_command(label="Align Text Right", accelerator="Ctrl+}")

        toolsMenu = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(menu=toolsMenu, label="Tools")
        btnWordCount = toolsMenu.add_command(label="Word Count...")
        btnDailyGoals = toolsMenu.add_command(label="Daily Goals...")

        settingsMenu = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(menu=settingsMenu, label="Settings")
        btnThemes = settingsMenu.add_command(label="Themes")
        btnPref = settingsMenu.add_command(label="Preferences")

        helpMenu = tk.Menu(menuBar, tearoff=0)
        menuBar.add_cascade(menu=helpMenu, label="Help")
        btnAbtAW = helpMenu.add_command(label="About AmbientWriter")

        #create bottom frame

        # bottomBarFrame = tk.Frame(self.root)
        # bottomBarFrame.pack()

        # wordCount = ""
        # wordCountMeter = tk.Label(bottomBarFrame, text=f"Word Count: {wordCount}")
        # wordCountMeter.pack(bottomBarFrame)

        # dailyProg = ""
        # dailyProgMeter = tk.Label(bottomBarFrame, text=f"Daily Goal: {dailyProg}")
        # dailyProgMeter.pack(bottomBarFrame)

        #init

        self.root.config(menu=menuBar)
        self.root.mainloop()

docGUI()

