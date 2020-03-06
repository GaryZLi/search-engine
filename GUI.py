import tkinter
from tkinter import StringVar

def search():
    print(searchText.get())

master = tkinter.Tk()
master.minsize(500, 500)
master.wm_title("Search Engine")

# master.columnconfigure(0, weight=1)
master.configure(background='black') #delete

searchContainer = tkinter.Frame(master, width=master.winfo_width(), background='black')
searchContainer.pack(padx=20, pady=20)
resultsContainer = tkinter.Frame(master)

searchContainer.grid(row=0, sticky='ew')
resultsContainer.grid(row=1, sticky='ew')

searchContainer.grid_rowconfigure(0, weight=1)
searchContainer.grid_columnconfigure(1, weight=1)

searchText = StringVar()
searchInput = tkinter.Entry(searchContainer, textvariable=searchText, width=95)
searchButton = tkinter.Button(searchContainer, text='Search', width=20, command=search)

searchInput.grid(row=0, column=0)
# searchButton.grid(row=0, column=1)


master.mainloop()