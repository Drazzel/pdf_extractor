import tkinter
from tkinter import *
from tkinter import filedialog
import tabula
from pathlib import Path


def center_window(width=300, height=200):
    # get screen width and height
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    root.geometry('%dx%d+%d+%d' % (width, height, x, y))

root = Tk()
root.title('PDF Converter')
center_window(300,300)


def open():
    global pdf
    # once settled - maybe add the internet link options - a decision on local brings up the file dialog
    # choose network allows for an address field that gets connected to the files downstream
    # in fact its more likely that i would essential be creating an if statement at the top
    # that creates two paths downstream
    root.filename = filedialog.askopenfilename(initialdir="/",
                                               title="Choose a pdf file",
                                               filetypes=[("pdf", "*.pdf")])
    pdf = root.filename
    file_label = Label(root, text="You have selected: " + Path(pdf).name).pack()
    # print the file name shorter with just the name of the pdf


my_button = Button(root, text="Choose a PDF", command=open).pack()

# redefine this entry field - maybe as a popup page picker on the pdf
f = Entry(root, width=3)
f.pack()


# # add lattice or stream checkbox
# status = tkinter.IntVar()
# state_l = []
#
# def check_checkbox ():
#     if status.get() ==1:
#         state_l = True
#     else: state_l = False
#
#
# g = tkinter.Checkbutton(root, text='Table Type:',
#                         variable=status,
#                         onvalue=1,
#                         offvalue=0,
#                         command = check_checkbox)
# g.pack()


# unsure if checkbox is passing the correct status to encode
# 11/28/2021 19:32 - confirmed that checkbox is not working as intended
# using gars_2021.pdf page 34 as an example,
# lattice should return 0 tables, stream should return 1,
# independent of status of checkbox, v2 returns 1 table suggesting it does not recognize checkbox state

def encode():
    pdf = tabula.read_pdf(root.filename, encoding='latin-1',
                          pages=int(f.get()),
                          stream= True)
    for df in pdf:
        print(df.size)
        print(df)
    my_label = Label(root, text="Found " + str(len(pdf)) + " tables.")
    my_label.pack()
    df.to_csv(filedialog.asksaveasfilename())

button = Button(root, text="Process PDF to CSV", command=encode).pack()
# display csv immediately

root.mainloop()
