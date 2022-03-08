import tkinter as tk
from tkinter import ttk
import tkinter.filedialog
import pandas as pd
import pyautogui as pg

class Application(tkinter.Frame):
    def __init__(self, root=None):
        super().__init__(root,
                     width = 800,
                     height = 600,
                     borderwidth = 5,
                     relief = "groove")
        self.pack()
        self.pack_propagate(0)
        self.csv_pass = tk.StringVar()
        self.root = root
        self.createWidgets()
    
    def createWidgets(self):
        csv_box = ttk.Entry(width=40, textvariable= self.csv_pass)
        csv_box.place(x=30, y=150)
        buttonA = ttk.Button(root, text= "参照", width= 10, command= self.openfile).place(x=600, y=150)
        buttonB = ttk.Button(root, text= "実行", width= 10, command= self.excel_view).place(x=600, y=200)

    def openfile(self):
        f = tkinter.filedialog.askopenfilename(
            title= "ファイル選択（csv）",
            filetypes= [("csv files","*.csv")]
            )
        self.csv_pass.set(f)
    
    def excel_view(self):
        g = self.csv_pass.get()
        print(g)
        df = pd.read_csv(g, encoding="shift-jis")
        print(df)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("タイトル")
    root.geometry("820x620")
    app = Application(root=root)
    app.mainloop()