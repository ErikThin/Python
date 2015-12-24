import tkinter

class Example(tkinter.Frame):
    def __init__(self, parent):
        tkinter.Frame.__init__(self, parent, background="green")

        self.parent = parent
        self.initUI()
        self.centerWindow()

    def initUI(self):
        self.parent.title("Simple")
        self.pack(fill=tkinter.BOTH, expand = 1)

    def centerWindow(self):
        w = 290
        h = 150
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()

        x = (sw - w)/2
        y = (sh - h)/2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))


root = tkinter.Tk()
app = Example(root)
root.mainloop()
