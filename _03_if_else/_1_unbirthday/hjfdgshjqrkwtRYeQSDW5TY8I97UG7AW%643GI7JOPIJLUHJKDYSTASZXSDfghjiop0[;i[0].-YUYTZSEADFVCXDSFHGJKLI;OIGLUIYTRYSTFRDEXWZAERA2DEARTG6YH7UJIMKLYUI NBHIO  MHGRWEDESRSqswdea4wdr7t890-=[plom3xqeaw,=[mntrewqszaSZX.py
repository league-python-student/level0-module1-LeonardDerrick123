from tkinter import messagebox, simpledialog, Tk

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    hrfgnrehwnjirfeh = simpledialog.askstring(None,"what is your birthday")
    if hrfgnrehwnjirfeh == "August 21":
        messagebox.showinfo(None,"Happy Birthday")
    else:
        messagebox.showinfo(None,"I wish you a verry merry unbirthday")