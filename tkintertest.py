from tkinter import *

# #Use this root for sections 1-8
# root = Tk()

# #1 Labels(text)
# label1 = Label(root, text='lots of word')
# label1.pack()

# #2 Frames
# topFrame = Frame(root)
# topFrame.pack()
# bottomFrame = Frame(root)
# bottomFrame.pack(side=BOTTOM)


# #3 Buttons
# button1 = Button(topFrame, text='Hello', fg='blue', bg='red')
# button2 = Button(topFrame, text='whats', fg='red')
# button3 = Button(bottomFrame, text='your', fg='yellow')
# button4 = Button(bottomFrame, text='Name', fg='green')
# button1.pack(side=LEFT)
# button2.pack()
# button3.pack(side=RIGHT)
# button4.pack()


# #4 Placement of Widgets
# one = Label(root, text='One', bg='red', fg='white')
# one.pack()
# two = Label(root, text='Two', bg='green', fg='black')
# two.pack(fill=X)
# three = Label(root, text='Three', bg='blue', fg='yellow')
# three.pack(side=LEFT, fill=Y)


# #5 Grid layout
# label1 = Label(root, text='Name')
# label2 = Label(root, text='Password')
# entry1 = Entry(root)
# entry2 = Entry(root)
# label1.grid(row=0, sticky=E)
# label2.grid(row=1, sticky=E)
# entry1.grid(row=0, column=1)
# entry2.grid(row=1, column=1)
# checkbox = Checkbutton(root, text='Keep me Logged in')
# checkbox.grid(columnspan=2)


# #6 Binding buttons to functions 1
# def printName():
#    print('Hello my name is Joshua')
# button_1 = Button(root, text="Print My Name", command=printName)
# button_1.pack()


# #7 Binding buttons to functions 2
# def printName(event):
#    print('Hello my name is Joshua')
# button_1 = Button(root, text="Print My Name")
# button_1.bind('<Button-1>', printName)
# button_1.pack()


# #8 Binding Multi-function to one widget
# def leftClick(event):
#    print('Left')
# def middleClick(event):
#    print('Middle')
# def rightClick(event):
#    print('Right')
# frame = Frame(root, width=300, height=250)
# frame.bind('<Button-1>', leftClick)
# frame.bind('<Button-2>', middleClick)
# frame.bind('<Button-3>', rightClick)
# frame.pack()


# #9 Classes
# class ButtonB:
#    def __init__(self, master):
#        frame = Frame(master)
#        frame.pack()
#        self.printButton = Button(frame, text='Print Message', command=self.printMessage)
#        self.printButton.pack(side=LEFT)
#        self.quitButton = Button(frame, text='Quit', command=frame.quit)
#        self.quitButton.pack(side=LEFT)
#    def printMessage(self):
#        print('wow this actually worked')
# root=Tk()
# b = ButtonB(root)


# #10, 11, 12  Main Menu | Toolbar | Status Bar
# def doNothing():
#    print("Ok ok I won't!")
# root=Tk()
# # ** Main Menu **
# menu = Menu(root)
# root.config(menu=menu)
# subMenu = Menu(menu)
# menu.add_cascade(label="File", menu=subMenu)
# subMenu.add_command(label="New Project...", command=doNothing)
# subMenu.add_command(label="Open Project...", command=doNothing)
# subMenu.add_separator()
# subMenu.add_command(label="Exit", command=doNothing)
# editMenu = Menu(menu)
# menu.add_cascade(label="Edit", menu=editMenu)
# editMenu.add_command(label="Redo", command=doNothing)
# # ** Toolbar **
# toolbar = Frame(root, bg="blue")
# insertButton = Button(toolbar, text="Insert Image", command=doNothing)
# insertButton.pack(side=LEFT, padx=2, pady=2)
# printButton = Button(toolbar, text="Print", command=doNothing)
# printButton.pack(side=LEFT, padx=2, pady=2)
# toolbar.pack(side=TOP, fill=X)
# # ** Status Bar **
# status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
# status.pack(side=BOTTOM, fill=X)


##13 Message Boxes
# import tkinter.messagebox
# root = Tk()
# tkinter.messagebox.showinfo("Window Title", "More words that give info, not to be confused with the 'Window Title'")
# answer = tkinter.messagebox.askquestion("Question 1", "Is the moon made of cheese?")
# if answer == "yes":
#     print(" You are incorret ")


##14 Draw and Delete
# root = Tk()
# canvas = Canvas(root, width=200, height=100)
# canvas.pack()
# blackLine = canvas.create_line(0, 0, 200, 50)
# redLine = canvas.create_line(0, 100, 200, 50, fill="red")
# greenBox = canvas.create_rectangle(25, 25, 130, 60, fill="green")
# canvas.delete(redLine)
# canvas.delete(ALL)


root = Tk()

photo = PhotoImage(file="Fluffy.jpg")
label = Label(root, image=photo)
label.pack()

root.mainloop()