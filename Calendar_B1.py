# Imports
import calendar as cl
import tkinter as tk
import datetime
from tkinter import messagebox

# Setting up current date in order to get current month and year
now = datetime.datetime.now()

# Functions required
def search(m):
    im = now.month
    for i in range(12):
        if Months[i].lower() == m.lower():
            im = i + 1
    return im


def CalPrint():
    m, y = months.get(), Year_Entry.get()
    im, iy = now.month, now.year
    if y.isdigit():
        if y != iy and len(y) != 4:
            messagebox.showwarning("Warning","Invalid Year Input: \n Please provide a valid year input.")
            y = now.year
        iy = int(y)
    if m != im:
        im = search(m)
    cal = cl.month(iy,im)
    textfield.delete(0.0,tk.END)
    textfield.insert(tk.INSERT,cal)

# main()
if __name__ == '__main__':

    # List of Months
    Months = ['January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December']

    # Designing of GUI
    win = tk.Tk()  # master
    win.title("Calendar")
    win.geometry('450x300')
    months = tk.StringVar(win)

    # Uncomment For Debugging function:
    # print(r_calendar(now.month,now.year))

    # labels
    label_month = tk.Label(win, text='Enter Month')
    label_year = tk.Label(win, text='Enter Year')
    label_month.grid(row=0, column=0)
    label_year.grid(row=0, column=4)
    textfield = tk.Text(win, height=7.5, width=21,foreground='#FF0000')



    # Entry widgets
    months.set(Months[int(now.month) - 1])  # The default value
    dropdown = tk.OptionMenu(win, months,
                 'January', 'February', 'March', 'April', 'May', 'June',
                 'July', 'August', 'September', 'October', 'November', 'December')

    #Year_Entry = tk.Entry(win, bd=6)
    year_curr = tk.StringVar(win)
    year_curr.set(now.year)
    Year_Entry = tk.Spinbox(win,from_=1600,to=2100,width=10,textvariable=year_curr)
    Year_Entry.grid(row=0, column=5)

    # Packing buttons and Entry widget
    tk.Button(win, text='Quit', command=win.quit).grid(row=5, column=0, pady=4)
    tk.Button(win, text='Show', command=CalPrint).grid(row=5, column=1, pady=4)
    dropdown.grid(row=0, column=1)
    textfield.grid(row=6,columnspan=3)

    # Running it
    win.mainloop()
