import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import time


from PIL import Image, ImageTk

import numpy as np

import image_processing as im
import stitch_objects as so
import mata_object as mo
import writer as wo


class Gui:

    def __init__(self):
        test = 5
        if test == 5:
            print("gui_window gui.py")

        self.loaded_image = ""
        self.images = []
        self.undo_list = []
        self.undo_function_list = []
        self.temp_images = []
        self.objects = []
        self.hoop_code = int()
        self.section_image_list = []
        self.pro_pop = 0
        self.value = 0

        global og_display
        global cy_display
        global average_pixel_count
        self.root = tk.Tk()
        self.root.title("Pic-to-Stitch")
        self.root.iconbitmap("Pic-to-Stitch_32x32.ico")
        # self.root.iconbitmap("Icon_2.ico")

        # Open in full screen
        self.root.wm_state("zoomed")
        self.screen_width = self.root.winfo_screenwidth()
        self.screen_height = self.root.winfo_screenheight()
        self.centre_width = self.screen_width / 2
        self.centre_height = self.screen_height / 2

        # ** Main Menu **
        menu = Menu(self.root)
        self.root.config(menu=menu)
        sub_menu = Menu(menu)
        menu.add_cascade(label="File", menu=sub_menu)
        sub_menu.add_separator()
        sub_menu.add_command(label="Exit")
        edit_menu = Menu(menu)
        menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Redo", command=redo)

        # Main Frame
        self.main_pane = Frame(self.root)
        self.main_pane.pack(fill=BOTH, expand=1, padx=5)

        # left Frame
        left_pane = tk.Frame(self.main_pane, borderwidth=2, relief="sunken")  # bg="yellow",
        left_pane.pack(fill=BOTH, padx=5, pady=10, expand=1, side=LEFT)

        # Right Frame
        self.right_pane = tk.Frame(self.main_pane, width=30)  # , bg="red")
        self.right_pane.pack(fill=BOTH, expand=False, side=RIGHT)
        self.right_top = tk.Frame(self.right_pane)
        self.right_top.pack()
        self.right_mid = tk.Frame(self.right_pane)
        self.right_mid.pack()
        self.right_display = tk.Frame(self.right_mid)
        self.right_display.pack()
        self.right_bot = tk.Frame(self.right_pane)
        self.right_bot.pack(side=BOTTOM, pady=40)
        # sizing_label_1 = Label(self.right_top, width=50, height=5)  # width = 1/5 of display or minimum 50
        # sizing_label_1.grid(row=0, column=0, columnspan=5)

        title_label = Label(self.right_top, width=10)  # width = 1/5 of display or minimum 50
        title_label.grid(row=2, column=0, pady=5, columnspan=2)

        # self.sizing_label_2 = Label(self.right_top, bg="orange")
        # self.sizing_label_2.grid(row=3, column=0)

        self.info_text = Text(self.right_top, wrap=WORD, width=35, height=16, borderwidth=2,
                              relief="sunken")  # width = 1/5 of display or minimum 50
        instructions = "LOAD IMAGE:\n\nSelect the 'Insert Image' button to begin..."
        self.info_text.insert(1.0, instructions)
        self.info_text.configure(state=DISABLED, font=("Calibri Light", 11, "bold"))
        self.info_text.grid(row=3, column=1, columnspan=3)
        self.info_scroll = Scrollbar(self.right_top)
        self.info_scroll.grid(row=3, column=4, sticky=W + N + S)
        self.info_scroll.config(command=self.info_text.yview)
        self.info_text.config(yscrollcommand=self.info_scroll.set)

        sizing_label_3 = Label(self.right_top, width=50)  # width = 1/5 of display or minimum 50
        sizing_label_3.grid(row=4, column=0, columnspan=5)

        self.right_button_1 = Button(self.right_bot, text="Next", state=DISABLED, width=7,
                                     command=lambda: [do_nothing()])
        self.right_button_1.grid(row=5, column=4, padx=10)
        self.right_button_1.grid_forget()
        self.right_button_2 = Button(self.right_bot, text="Insert Image",
                                     command=lambda: [self.load_image(), self.update_right_pane(1)])
        self.right_button_2.grid(row=5, column=2, padx=10)
        self.right_button_4 = Button(self.right_bot, text="Denoise", width=7, command=lambda: [self.run_denoise()])
        self.right_button_4.grid(row=5, column=3, padx=10)
        self.right_button_4.grid_forget()
        self.right_button_3 = Button(self.right_bot, text="Back", width=7, command=lambda: [self.undo_method()])
        self.right_button_3.grid(row=5, column=1, padx=10)
        self.right_button_3.grid_forget()

        # Scrollbar - Canvas within main frame
        main_canvas = Canvas(left_pane, bg="white")

        # Scrollbar - scroll bar
        scroll_bar_y = tk.Scrollbar(left_pane, orient=VERTICAL, command=main_canvas.yview)
        scroll_bar_y.pack(side=RIGHT, fill=Y)

        scroll_bar_x = tk.Scrollbar(left_pane, orient=HORIZONTAL, command=main_canvas.xview)
        scroll_bar_x.pack(side=BOTTOM, fill=X)
        main_canvas.pack(fill=BOTH, expand=1)
        # Scrollbar - config Canvas
        main_canvas.configure(yscrollcommand=scroll_bar_y.set)
        main_canvas.bind("<Configure>", lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all")))

        main_canvas.configure(xscrollcommand=scroll_bar_x.set)
        main_canvas.bind("<Configure>", lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all")))

        # Scrollbar - frame 2
        self.second_frame = tk.Frame(main_canvas, padx=20, pady=20, bg="white")
        self.second_frame.pack(fill=BOTH)

        # Scrollbar - new window
        main_canvas.update()
        can_w = main_canvas.winfo_width()
        can_h = main_canvas.winfo_height()
        main_canvas.create_window((can_w / 2, can_h / 2), window=self.second_frame, anchor="center")

        self.og_image_frame = tk.Frame(self.second_frame)
        self.og_image_frame.pack(side=LEFT, padx=2, pady=2)
        self.og_label = Label(self.og_image_frame, bg="white")
        self.og_label.pack(fill=BOTH)  # place(relx=0.2, rely=0.2, anchor=CENTER)

        self.cy_image_frame = tk.Frame(self.second_frame)
        self.cy_image_frame.pack(side=RIGHT, padx=2, pady=2, )
        self.cy_label = Label(self.cy_image_frame, bg="white")
        self.cy_label.pack(fill=BOTH)

        # ** Status Bar **
        status = Label(self.root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
        status.pack(side=BOTTOM, fill=X)

        self.root.mainloop()

    def update_right_pane(self, option):
        test = 0
        if test == 5:
            print("update_right_pane - class Gui - gui.py")

        if option == 0:
            # textbox
            instructions = "LOAD IMAGE:\n\nSelect the 'Insert Image' button to begin..."
            self.info_text.configure(state=NORMAL)
            self.info_text.replace(1.0, END, instructions)
            self.info_text.configure(state=DISABLED)

            # right_mid - frame
            self.right_display.destroy()
            self.right_display = tk.Frame(self.right_mid)
            self.right_display.pack()

            # back - button
            self.right_button_3.grid_forget()

            # action - button
            self.right_button_2.configure(text="Insert Image",
                                          command=lambda: [self.load_image(), self.update_right_pane(1)])
            self.right_button_2.grid(row=5, column=2, padx=10)

            # next - button
            self.right_button_1.grid_forget()

        # Size Set
        elif option == 1:
            # textbox
            instructions = "HOOP SIZE:\n\n- Select one form the list of hoop sizes below.\n\n" \
                           "(Optional)\n- Select the 'Custom Size' option for more sizing control"
            self.info_text.configure(state=NORMAL)
            self.info_text.replace(1.0, END, instructions)
            self.info_text.configure(state=DISABLED)

            # Hoop select
            self.right_display.destroy()
            self.right_display = tk.Frame(self.right_mid)
            self.right_display.pack()
            self.hoop_size_select()

            # back - button
            self.right_button_3.configure(command=lambda: [self.undo_method()])
            self.right_button_3.grid(row=5, column=1, padx=10)

            # action - button
            self.right_button_2.grid_forget()

            # next - button
            self.right_button_1.grid(row=5, column=4, padx=10)  # self.update_right_pane(2), im.auto_colour_step(self)
            self.right_button_1.configure(state=NORMAL, text="Next",
                                          command=lambda: [self.sizing_check(hoop_choice.get(), custom.get())])

        # Colour Level
        elif option == 2:
            # textbox
            instructions = "COLOURS:\n\n- Select Maximum amount of colours in you want in the image"
            self.info_text.configure(state=NORMAL)
            self.info_text.replace(1.0, END, instructions)
            self.info_text.configure(state=DISABLED)

            # right_mid - frame
            self.right_display.destroy()
            self.right_display = tk.Frame(self.right_mid)
            self.right_display.pack()

            # back - button - add
            self.right_button_3.configure(command=lambda: [self.undo_method()])

            # action - button
            self.right_button_2.grid_forget()

            # next - button - lock until action - add
            self.right_button_1.configure(text="Next", state=DISABLED,
                                          command=lambda: [self.set_colour_change(floor_choice.get()),
                                                           self.update_right_pane(3), self.stats()])

        # Colour Merge
        elif option == 3:
            # textbox
            instructions = "COLOUR MERGE:\n\n- Select the 'Colour Merge' button until no more changes are made in " \
                           "the image"
            self.info_text.configure(state=NORMAL)
            self.info_text.replace(1.0, END, instructions)
            self.info_text.configure(state=DISABLED)

            # right_mid - frame
            self.right_display.destroy()
            self.right_display = tk.Frame(self.right_mid)
            self.right_display.pack()

            # back - button - update
            self.right_button_3.configure(command=lambda: [self.undo_check(3)])

            # action - button - add
            self.right_button_2.grid(row=5, column=2, padx=10)
            self.right_button_2.configure(text="Colour Merge", command=lambda: [self.run_colour_merge(),
                                                                                self.right_button_1.config(
                                                                                    state=NORMAL)])
            # action button 2
            self.right_button_4.grid_forget()

            # next - button - lock until action -update
            self.right_button_1.configure(state=DISABLED, command=lambda: [self.update_right_pane(4),
                                                                           self.manuel_merge_pop()])

        # Manual Merge
        elif option == 4:
            # textbox
            instructions = "MANUAL MERGE:\n\n- Select the colour you wish to merge.\n\n" \
                           "- Select the drop-down menu and click the Colour ID of the colour you wish to merge it" \
                           " with.\n\n- Select the 'Update Merge' button to merge the colours" \
                           "\n\n- Select the 'Denoise' button to remove small speckled pixels" \
                           "\n\n- Repeat the Merge and Denoise steps until all colours are solid."
            self.info_text.configure(state=NORMAL)
            self.info_text.replace(1.0, END, instructions)
            self.info_text.configure(state=DISABLED)

            self.title_frame = Frame(self.right_display)
            self.title_frame.pack()

            # mid - merge layout
            display_canvas = Canvas(self.right_display, width=300, height=200)
            display_canvas.configure()

            scroll_bar_y = tk.Scrollbar(self.right_display, orient=VERTICAL, command=display_canvas.yview)
            scroll_bar_y.pack(side=RIGHT, fill=Y)
            display_canvas.pack(fill=X, side=RIGHT)

            display_canvas.configure(yscrollcommand=scroll_bar_y.set)
            display_canvas.bind("<Configure>",
                                lambda e: display_canvas.configure(scrollregion=display_canvas.bbox("all")))

            self.display_frame = tk.Frame(display_canvas, padx=10, pady=10)
            can_w = display_canvas.winfo_width()
            can_h = display_canvas.winfo_height()
            display_canvas.create_window((can_w / 2, can_h / 2), window=self.display_frame, anchor="center")

            # back - button - update
            self.right_button_3.configure(command=lambda: [self.undo_check(4)])

            # update - button - update
            self.right_button_2.configure(text="Update Merge",
                                          command=lambda: [self.run_man_merge()])
            self.right_button_2.grid(row=5, column=2, padx=10)

            # next - button - lock until action - update
            self.right_button_1.configure(state=DISABLED, command=lambda: [self.update_right_pane(5),
                                                                           im.janome_colours(self)])

            # action button 2 - button - update
            self.right_button_4.configure()
            self.right_button_4.grid(row=5, column=3, padx=10)

            # next - button - lock until action - update
            self.right_button_1.grid(row=5, column=4, padx=10)
            self.right_button_1.configure(state=DISABLED, command=lambda: [self.update_right_pane(5),
                                                                           im.janome_colours(self)])

        # Create Objects
        elif option == 5:
            # textbox
            instructions = "OBJECT CREATION:\n\n- Select the 'Create Object' button.\n\n"
            self.info_text.configure(state=NORMAL)
            self.info_text.replace(1.0, END, instructions)
            self.info_text.configure(state=DISABLED)

            # right_mid - frame
            self.right_display.destroy()
            self.right_display = tk.Frame(self.right_mid)
            self.right_display.pack()

            # back - button - update
            self.right_button_3.grid(row=5, column=1, padx=10)

            # update - button - update
            self.right_button_4.grid_forget()
            self.right_button_2.configure(text="Create Objects",
                                          command=lambda: [self.run_create_objects()])
            self.right_button_2.grid(row=5, column=2, padx=10)

            # next - button - lock until action - update
            self.right_button_1.grid_forget()
            pass

        # Final - restart
        elif option == 6:
            # textbox
            instructions = "FINISHED:\n\n- Select the 'Insert Image' for another image\n\n" \
                           "- Select the 'Exit' button to close the program"
            self.info_text.configure(state=NORMAL)
            self.info_text.replace(1.0, END, instructions)
            self.info_text.configure(state=DISABLED)

            # back
            self.right_button_3.grid_forget()
            # action
            self.right_button_2.grid(row=5, column=2, padx=10)
            self.right_button_2.configure(text="Insert Image",
                                          command=lambda: [self.load_image(), self.update_right_pane(1)])

            # next
            self.right_button_1.grid(row=5, column=4, padx=10)
            self.right_button_1.configure(state=NORMAL, text="Exit", command=lambda: [self.root.destroy()])

    def run_colour_merge(self):
        test = 0
        if test == 5:
            print("run_colour_merge - class Gui - gui.py")
        self.right_button_1.configure(state=DISABLED)
        self.right_button_2.configure(state=DISABLED)
        self.right_button_3.configure(state=DISABLED)
        im.pix_restrict(self)
        self.right_button_1.configure(state=NORMAL)
        self.right_button_2.configure(state=NORMAL)
        self.right_button_3.configure(state=NORMAL)

    def run_man_merge(self):
        test = 0
        if test == 5:
            print("run_man_merge - class Gui - gui.py")
        self.right_button_1.configure(state=DISABLED)
        self.right_button_2.configure(state=DISABLED)
        self.right_button_3.configure(state=DISABLED)
        self.right_button_4.configure(state=DISABLED)
        self.right_button_4.update()
        im.get_man_merge_vals(self, self.change_list, self.pixel_list)
        self.reset_canvas(), self.manuel_merge_pop()
        self.right_button_1.configure(state=NORMAL)
        self.right_button_2.configure(state=NORMAL)
        self.right_button_3.configure(state=NORMAL)
        self.right_button_4.configure(state=NORMAL)
        self.right_button_4.update()

    def run_denoise(self):
        test = 0
        if test == 5:
            print("bar_denoise - class Gui - gui.py")
        self.right_button_1.configure(state=DISABLED)
        self.right_button_2.configure(state=DISABLED)
        self.right_button_3.configure(state=DISABLED)
        self.right_button_4.configure(state=DISABLED)
        self.right_button_4.update()

        im.pix_change(self)
        self.reset_canvas(), self.manuel_merge_pop()

        self.right_button_1.configure(state=NORMAL)
        self.right_button_2.configure(state=NORMAL)
        self.right_button_3.configure(state=NORMAL)
        self.right_button_4.configure(state=NORMAL)
        self.right_button_4.update()

    def run_create_objects(self):
        test = 0
        if test == 5:
            print("run_create_objects - class Gui - gui.py")
        self.undo_list.append(self.images[1])
        self.undo_function_list.append(5)

        self.right_button_1.configure(state=DISABLED)
        self.right_button_2.configure(state=DISABLED)
        self.right_button_3.configure(state=DISABLED)
        self.right_button_4.configure(state=DISABLED)
        self.right_button_4.update()

        im.create_image_plot(self)
        self.stitch_type_instruction()
        self.stitch_type_pop()

        self.right_button_1.configure(state=NORMAL)
        self.right_button_2.configure(state=NORMAL)
        self.right_button_3.configure(state=NORMAL)
        self.right_button_4.configure(state=NORMAL)
        self.right_button_4.update()

    def stitch_type_instruction(self):
        test = 0
        if test == 5:
            print("stitch_type_instruction - class Gui -  gui.py")

        instructions = "STITCH SETTINGS:\n\n- Select the 'Display' button to highlight the object on the image\n\n" \
                       "- Choose the Stitch Type and Maximum Stitch length for each object\n\n" \
                       "- Remove objects from the final design by selecting the checkbox\n\n" \
                       "- Objects can be reordered by setting the order value and clicking 'Update Order'\n\n" \
                       "- Select 'Save' to export and save the project"
        self.info_text.configure(state=NORMAL)
        self.info_text.replace(1.0, END, instructions)
        self.info_text.configure(state=DISABLED)

        self.right_button_2.grid_forget()
        self.right_button_3.grid_forget()

    def undo_method(self):
        test = 0
        if test == 5:
            print("undo_method - class Gui - gui.py")

        if len(self.undo_function_list) == 1:
            fun = self.undo_function_list.pop(-1)

            if test == 1:
                print("Reset Function: {}".format(fun))

            self.update_right_pane(fun)
            self.images.clear()
            self.display_cy_image()
        elif len(self.undo_function_list) == 2:
            fun = self.undo_function_list.pop(-1)
            self.update_right_pane(fun)
            self.undo_hoop_choice()

        elif len(self.undo_function_list) > 2:
            fun = self.undo_function_list.pop(-1)
            img = self.undo_list.pop(-1)

            if test == 1:
                print("Go to Function: {}".format(fun))

            self.update_right_pane(fun)
            self.images[1] = img
            self.display_cy_image()

    def undo_check(self, c_from):
        test = 0
        if test == 5:
            print("undo_check - class Gui - gui.py")

        print(self.undo_function_list)
        # print(self.undo_function_list[-1])
        if self.undo_function_list[-1] == 2:
            self.undo_method()
            im.auto_colour_step(self)
        elif self.undo_function_list[-1] == 4:
            self.undo_method()
            self.reset_canvas()
            self.manuel_merge_pop()
        elif self.undo_function_list[-1] == 3 and c_from == 4:
            # self.reset_canvas()
            # self.manuel_merge_pop()
            self.undo_method()
            # self.right_button_3.configure(command=lambda: [self.undo_check(3)])
        elif self.undo_function_list[-1] == 3 and c_from == 3:
            self.undo_method()

    def reset_canvas(self):
        test = 0
        if test == 5:
            print("reset_canvas - class Gui - gui.py")

        self.right_display.destroy()
        self.right_display = tk.Frame(self.right_mid)
        self.right_display.pack()

        self.title_frame = Frame(self.right_display)
        self.title_frame.pack()

        display_canvas = Canvas(self.right_display, width=300, height=200)
        display_canvas.configure()

        scroll_bar_y = tk.Scrollbar(self.right_display, orient=VERTICAL, command=display_canvas.yview)
        scroll_bar_y.pack(side=RIGHT, fill=Y)
        display_canvas.pack(fill=BOTH, side=RIGHT, expand=5)

        display_canvas.configure(yscrollcommand=scroll_bar_y.set)
        display_canvas.bind("<Configure>", lambda e: display_canvas.configure(scrollregion=display_canvas.bbox("all")))

        self.display_frame = tk.Frame(display_canvas, padx=10, pady=10)
        can_w = display_canvas.winfo_width()
        can_h = display_canvas.winfo_height()
        display_canvas.create_window((can_w / 2, can_h / 2), window=self.display_frame, anchor="center")

    # Load Image from file function
    def load_image(self):
        test = 4
        if test == 5:
            print("load_image - class Gui - gui.py")

        self.images = []
        self.temp_images = []
        self.objects = []
        self.hoop_code = int()
        self.section_image_list = []
        self.undo_list.clear()
        self.undo_function_list.clear()
        self.value = 0

        file_path = filedialog.askopenfilename(defaultextension=".png", filetypes=(("All Files", "*.*"),
                                                                                   ("JPEG", "*.jpg"), ("PNG", "*.png")))
        if test == 1:
            print("file_path: {}".format(file_path))
        if file_path == "":  # askopenfilename return "" if dialog closed with "cancel".
            return

        og_img = Image.open(file_path)
        cy_img = og_img

        self.loaded_image = og_img
        self.undo_list.append(og_img)
        self.undo_function_list.append(0)
        length = len(self.images)

        if test == 4:
            print("0 - Functions so far: {}".format(self.undo_function_list))

        if length == 0:
            self.images.append(og_img)
            self.images.append(cy_img)
        else:
            self.images[0] = og_img
            self.images[1] = cy_img

        self.display_og_image()
        self.display_cy_image()

    def display_cy_image(self):
        test = 0
        if test == 5:
            print("display_cy_image - class Gui - gui.py")

        global cy_display
        global cy_label
        if self.images:
            cy_display = ImageTk.PhotoImage(self.images[1])
            self.cy_label.config(image=cy_display)
            if test == 1:
                print("Display cy image")
        else:
            self.og_image_frame.destroy()
            self.cy_image_frame.destroy()
            self.og_image_frame = tk.Frame(self.second_frame)
            self.og_image_frame.pack(side=LEFT, padx=2, pady=2)
            self.og_label = Label(self.og_image_frame, bg="white")
            self.og_label.pack(fill=BOTH)  # place(relx=0.2, rely=0.2, anchor=CENTER)

            self.cy_image_frame = tk.Frame(self.second_frame)
            self.cy_image_frame.pack(side=RIGHT, padx=2, pady=2, )
            self.cy_label = Label(self.cy_image_frame, bg="white")
            self.cy_label.pack(fill=BOTH)

    def display_og_image(self):
        test = 0
        if test == 5:
            print("display_og_image - class Gui - gui.py")

        global og_display
        global og_label
        og_display = ImageTk.PhotoImage(self.images[0])
        self.og_label.config(image=og_display)
        if test == 1:
            print("Display og image")

    def display_image(self, image):
        test = 0
        if test == 5:
            print("display_image - class Gui - gui.py")

        global img
        img = ImageTk.PhotoImage(image)
        self.cy_label.config(image=img)
        if test == 1:
            print("Display image")

    def hoop_size_select(self):
        test = 0
        if test == 5:
            print("hoop_size_select - class Gui - gui.py")

        global pop
        global hoop_choice
        global lock
        global custom
        hoop_choice = IntVar()
        lock = IntVar()
        custom = IntVar()

        pop_frame1 = Frame(self.right_display)
        pop_frame1.pack()
        pop_label_1 = Label(pop_frame1, text='Select a Hoop Size:')
        pop_label_1.grid(row=0, column=0, padx=20, pady=10)
        pop_label_2 = Label(pop_frame1, text='2"x2" Hoop (50x50mm)')
        pop_label_2.grid(row=1, column=0)
        pop_label_3 = Label(pop_frame1, text='4"x4" Hoop (110x110mm)')
        pop_label_3.grid(row=2, column=0)
        pop_label_4 = Label(pop_frame1, text='5"x4" Hoop (127x110mm)')
        pop_label_4.grid(row=3, column=0)
        pop_label_3 = Label(pop_frame1, text='5.5"x8" Hoop (140x200mm)')
        pop_label_3.grid(row=4, column=0)
        pop_label_4 = Label(pop_frame1, text='8"x8" Hoop (200x200mm)')
        pop_label_4.grid(row=5, column=0)
        r_button_1 = Radiobutton(pop_frame1, variable=hoop_choice, value=1)
        r_button_1.grid(row=1, column=1)
        r_button_2 = Radiobutton(pop_frame1, variable=hoop_choice, value=2)
        r_button_2.grid(row=2, column=1)
        r_button_3 = Radiobutton(pop_frame1, variable=hoop_choice, value=3)
        r_button_3.grid(row=3, column=1)
        r_button_1 = Radiobutton(pop_frame1, variable=hoop_choice, value=4)
        r_button_1.grid(row=4, column=1)
        r_button_2 = Radiobutton(pop_frame1, variable=hoop_choice, value=5)
        r_button_2.grid(row=5, column=1)

        custom = IntVar()
        custom_check = Checkbutton(pop_frame1, variable=custom, command=self.custom_option)
        custom_check.grid(row=6, column=1)
        pop_label_7 = Label(pop_frame1, text="Custom size:")
        pop_label_7.grid(row=6, column=0)

        global pop_frame2
        pop_frame2 = Frame(self.right_display)
        pop_frame2.pack()

        global pop_frame3
        pop_frame3 = Frame(self.right_display)
        pop_frame3.pack()

    def pop_geometry(self, width, height):
        test = 0
        if test == 5:
            print("pop_geometry - class Gui - gui.py")

        pop_width = width
        pop_height = height
        pop_x = self.centre_width - (pop_width / 2)
        pop_y = self.centre_height - (pop_height / 2)
        pop.geometry(f'{pop_width}x{pop_height}+{int(pop_x)}+{int(pop_y)}')
        pop.update()

    def pop_geometry_progress(self, width, height):
        test = 0
        if test == 5:
            print("pop_geometry_progress - class Gui - gui.py")

        pop_width = width
        pop_height = height
        win_height = self.centre_height / 4
        win_height += self.centre_height
        pop_x = self.centre_width - (pop_width / 2)
        pop_y = win_height - (pop_height / 2)
        pop.geometry(f'{pop_width}x{pop_height}+{int(pop_x)}+{int(pop_y)}')
        pop.update()

    def custom_option(self):
        test = 0
        if test == 5:
            print("custom_option - class Gui - gui.py")

        checked = custom.get()
        if checked == 1:
            global enter_width
            global enter_height
            global pop_label_5
            global pop_label_6
            global aspect_lock
            global pop_label_8
            enter_width = Entry(pop_frame2, width=5)
            enter_width.grid(row=5, column=1)
            enter_height = Entry(pop_frame2, width=5)
            enter_height.grid(row=6, column=1)
            pop_label_5 = Label(pop_frame2, text='Width (mm):')
            pop_label_5.grid(row=5, column=0)
            pop_label_6 = Label(pop_frame2, text='Height (mm):')
            pop_label_6.grid(row=6, column=0)
            aspect_lock = Checkbutton(pop_frame2, variable=lock)
            aspect_lock.grid(row=7, column=1)
            pop_label_8 = Label(pop_frame2, text="Lock Aspect Ratio:")
            pop_label_8.grid(row=7, column=0)
            pop_frame2.config()
            # self.pop_geometry(300, 320)

        elif checked == 0:
            if test == 1:
                print("No Custom")

            enter_width.destroy()
            enter_height.destroy()
            pop_label_5.destroy()
            pop_label_6.destroy()
            aspect_lock.destroy()
            pop_label_8.destroy()
            pop_frame2.config()
            pop_frame3.config()
        else:
            print("Error: Custom Size Checkbox Value")

    def bar(self, title, message, max, mode):
        test = 0
        if test == 5:
            print("bar - class Gui - gui.py")
        self.pro_pop = ProgressPop(self, title, message, max, mode)

    def bar_update_progress(self, count, secs, mode):
        test = 0
        if test == 5:
            print("bar_update_progress - class Gui - gui.py")

        if mode == 1:
            self.pro_pop.progress_update_progress_d(count, secs)
        else:
            self.pro_pop.progress_update_progress_ind(count, secs)

    def bar_update_message(self, message):
        test = 0
        if test == 5:
            print("bar_update_message - class Gui - gui.py")
        self.pro_pop.progress_update_message(message)

    def bar_update_object(self, object):
        test = 0
        if test == 5:
            print("bar_update_object - class Gui - gui.py")
        self.pro_pop.progress_update_object(object)

    def bar_reset(self, message, pro_val, max, mode):
        test = 0
        if test == 5:
            print("bar_reset - class Gui - gui.py")
        self.pro_pop.progress_reset(message, pro_val, max, mode)

    def bar_des(self):
        test = 0
        if test == 5:
            print("bar_des - class Gui - gui.py")
        self.pro_pop.destroy()

    def error_message(self, message):
        test = 0
        if test == 5:
            print("error_message - class Gui - gui.py")

        error_message = Toplevel(self.second_frame)
        error_message.title("Error")
        error_message.iconbitmap("Pic-to-Stitch_32x32.ico")
        error_width = 300
        error_height = 100
        error_x = self.centre_width - (error_width / 2)
        error_y = self.centre_height - (error_height / 2)
        error_message.geometry(f'{error_width}x{error_height}+{int(error_x)}+{int(error_y)}')
        error_label = Label(error_message, text="Error: " + message)
        error_label.pack(pady=20)
        error_button = Button(error_message, text="OK", width=10,  command=lambda:[error_message.destroy()])
        error_button.pack(pady=10)

    def warn_message(self, message, hoop, option, width, height):
        test = 0
        if test == 5:
            print("warn_message - class Gui - gui.py")

        hp = hoop
        op = option
        w = width
        h = height
        warn_message = Toplevel(self.second_frame)
        warn_message.title("Warning")
        warn_message.iconbitmap("Pic-to-Stitch_32x32.ico")
        warn_width = 280
        warn_height = 100
        warn_x = self.centre_width - (warn_width / 2)
        warn_y = self.centre_height - (warn_height / 2)
        warn_message.geometry(f'{warn_width}x{warn_height}+{int(warn_x)}+{int(warn_y)}')
        warn_label = Label(warn_message, text="Warning: " + message)
        warn_label.grid(row=0, column=0, columnspan=3, pady=15, padx=35)
        warn_button_back = Button(warn_message, text="Back", width=10, command=lambda: [warn_message.destroy()])
        warn_button_back.grid(row=1, column=0, pady=10, sticky=E)
        warn_button_ok = Button(warn_message, text="OK", width=10,
                                command=lambda: [self.run_image_resize(hp, op, w, h), warn_message.destroy(),
                                                 pop.destroy()])
        warn_button_ok.grid(row=1, column=2, pady=10, sticky=W)

    def sizing_check(self, hoopchoice, customcheck):
        test = 0
        if test == 5:
            print("sizing_check - class Gui - gui.py")

        hoop_width = IntVar()
        hoop_height = IntVar()
        img_w, img_h = self.images[0].size
        self.hoop_code

        go = int()
        try:
            if hoopchoice == 1:
                hoop_width = 50
                hoop_height = 50

            elif hoopchoice == 2:
                hoop_width = 110
                hoop_height = 110

            elif hoopchoice == 3:
                hoop_width = 127
                hoop_height = 110

            elif hoopchoice == 4:
                hoop_width = 140
                hoop_height = 200

            elif hoopchoice == 5:
                hoop_width = 200
                hoop_height = 200

            else:
                raise ValueError1
        except ValueError1:

            self.error_message("Select a Hoop SIze")

        if hoopchoice > 0 and customcheck == 1:     # custom size option
            try:
                img_w = enter_width.get()
                img_h = enter_height.get()
                if bool(img_w) == True and bool(img_h) == True:     # Height, Width Sizing
                    img_w = int(enter_width.get())
                    img_h = int(enter_height.get())
                    go = 1

                    # console testing comment
                    if test == 1:
                        print("option 1")

                elif bool(img_w) == False and bool(img_h) == True:  # Height sizing
                    img_w = 0
                    img_h = int(enter_height.get())
                    go = 1
                    if test == 1:
                        print("option 2")
                elif bool(img_h) == False and bool(img_w) == True:  # Width Sizing
                    img_h = 0
                    img_w = int(enter_width.get())
                    go = 1
                    if test == 1:
                        print("option 3")

                else:                                               # Error option
                    go = 0
                    raise ValueError3

            except ValueError3:
                self.error_message("Width and Height fields left blank")

            checked = int(lock.get())

            if go > 0:
                if img_h > 0 and img_w > 0:
                    if checked == 1:
                        try:
                            if img_w > hoop_width:
                                raise ValueError1
                            else:
                                self.run_image_resize(hoopchoice, 3, img_w, img_h)
                                if test == 1:
                                    print("C1 W1 H1 A1 - Custom size to Width")
                        except ValueError1:
                            self.error_message("Custom width is larger than Hoop Width")
                    elif checked == 0:
                        self.warn_message("Image may be unevenly sized", hoopchoice, 2, img_w, img_h)
                    else:
                        if test == 1:
                            print("Error: Lock Aspect Ratio Checkbox Value ")
                elif img_h > 0:
                    try:
                        if checked == 1:
                            try:
                                if img_h > hoop_height:
                                    raise ValueError1
                                else:
                                    self.run_image_resize(hoopchoice, 4, img_w, img_h)
                                    if test == 1:
                                        print("C1 W0 H1 A1 - Custom ratio size to only Height")
                            except ValueError1:
                                self.error_message("Custom Height is larger than Hoop Height")
                        elif checked == 0:
                            raise ValueError2
                        else:
                            if test == 1:
                                print("Error: Lock Aspect Ratio Checkbox Value ")
                    except ValueError2:
                        self.error_message("Complete Width or Select 'Lock Aspect Ratio'")
                elif img_w > 0:
                    try:
                        if checked == 1:
                            try:
                                if img_w > hoop_width:
                                    raise ValueError1
                                else:
                                    self.run_image_resize(hoopchoice, 3, img_w, img_h)
                                    if test == 1:
                                        print("C1 W1 H0 A1 - Custom ratio size to only Width")

                            except ValueError1:
                                self.error_message("Custom Width is larger than Hoop Width")
                        elif checked == 0:
                            raise ValueError2
                        else:
                            if test == 1:
                                print("Error: Lock Aspect Ratio Checkbox Value ")
                    except ValueError2:
                        self.error_message("Complete Height or Select 'Lock Aspect Ratio'")
                else:
                    if test == 1:
                        print("Error: Custom Height/Width Values")

        elif hoopchoice > 0 and customcheck == 0:
            self.run_image_resize(hoopchoice, 1, img_w, img_h)
            if test == 1:
                print("C0 W0 H0 A0 - Auto Sizing to Hoop")

    def run_image_resize(self, hoop_select, option, img_w, img_h):
        test = 4
        if test == 5:
            print("run_image_resize - class Gui - gui.py")

        image = self.images[1]

        image = im.image_resize(self, image, hoop_select, option, img_w, img_h)

        self.undo_list.append(self.images[1])
        self.undo_function_list.append(1)

        if test == 4:
            print("1 - Functions so far: {}".format(self.undo_function_list))

        self.images[0] = image
        self.images[1] = image

        self.display_og_image()
        self.display_cy_image()
        self.update_right_pane(2)
        self.right_button_3.configure(state=DISABLED)
        im.auto_colour_step(self)
        self.right_button_3.configure(state=NORMAL)

    def undo_hoop_choice(self):
        test = 0
        if test == 5:
            print("undo_hoop_choice - class Gui - gui.py")

        length = len(self.images)
        if length > 0:
            img = self.undo_list.pop(-1)
            self.images[0] = img
            self.images[1] = img
            self.display_cy_image()
            self.display_og_image()
        else:
            if test == 1:
                print("no image selected")

    def stitch_type_pop(self):
        test = 0
        if test == 5:
            print("stitch_type_pop - class Gui - gui.py")

        global pop
        stitch_drop_list = []
        len_drop_list = []
        order_drop_list = []
        checkbox_list = []

        # set lists
        for i in range(len(self.objects)):
            s_stitch = StringVar()
            s_stitch.set("Stitch Outline")
            stitch_drop_list.append(s_stitch)
            l_stitch = StringVar()
            l_stitch.set("0.3mm")
            len_drop_list.append(l_stitch)
            ord = IntVar()
            ord.set(i + 1)
            order_drop_list.append(ord)
            che = IntVar()
            che.set(0)
            checkbox_list.append(che)

        length = len(self.objects)
        pop = Toplevel(self.second_frame)
        pop.title("Set Stitches")
        pop.iconbitmap("Pic-to-Stitch_32x32.ico")
        if length - 1 <= 0:
            ob_len = 0
        else:
            ob_len = 30 * length
        self.pop_geometry(700, 30 + 30 + 50 + ob_len)
        count_list = []
        pop_frame1 = Frame(pop)
        pop_frame1.pack()
        pop_frame2 = Frame(pop)
        pop_frame2.pack()
        pop_frame3 = Frame(pop)
        pop_frame3.pack()
        count = 1

        pop_label_1 = Label(pop_frame1, width=6, text='Object ID')
        pop_label_1.grid(row=0, column=0, pady=5)
        pop_label_1 = Label(pop_frame1, width=7, text='Colour')
        pop_label_1.grid(row=0, column=1, padx=10)
        pop_label_1 = Label(pop_frame1, width=15, text='Stitch Type')
        pop_label_1.grid(row=0, column=2, padx=5)
        pop_label_1 = Label(pop_frame1, width=15, text='Max Stitch Length')
        pop_label_1.grid(row=0, column=3, padx=5)
        pop_label_1 = Label(pop_frame1, width=8, text='Order')
        pop_label_1.grid(row=0, column=4, padx=5)
        pop_label_1 = Label(pop_frame1, width=14, text='Remove Object')
        pop_label_1.grid(row=0, column=5, padx=10)
        pop_label_1 = Label(pop_frame1, width=8, text='Highlight')
        pop_label_1.grid(row=0, column=6)
        pop_label_1 = Label(pop_frame1, width=3)
        pop_label_1.grid(row=0, column=7)
        len_count = 0

        for i in range(length + 1):
            count_list.append(len_count)
            len_count += 1

        self.frame2(self.objects, stitch_drop_list, len_drop_list, order_drop_list, checkbox_list, pop_frame2, length)

        pop_button = Button(pop_frame3, text="Save",
                            command=lambda: [pop.destroy(), process_stitch_choices(self, self.objects,
                                                                                   self.section_image_list,
                                                                                   stitch_drop_list,
                                                                                   len_drop_list,
                                                                                   order_drop_list,
                                                                                   checkbox_list),
                                             mo.create_mata_object(so.create_stitch_objects(self.objects),
                                                                   self.hoop_code),
                                             save_file(mo.mata_file),
                                             self.update_right_pane(6)])

        pop_button.grid(row=1, column=4, pady=10, columnspan=2, padx=10)
        pop_button = Button(pop_frame3, text="Update Order", command=lambda: [self.reorder_list(self.objects,
                                                                                                self.section_image_list,
                                                                                                stitch_drop_list,
                                                                                                len_drop_list,
                                                                                                order_drop_list,
                                                                                                checkbox_list,
                                                                                                pop_frame2, len_count)])
        pop_button.grid(row=1, column=3, pady=10, padx=5)
        pop_button = Button(pop_frame3, text="Back", command=lambda: [self.undo_method(), pop.destroy()])
        pop_button.grid(row=1, column=1, pady=10, columnspan=2, padx=10)

    def reorder_list(self, objects, section_image, stitch_type, stitch_len, order, del_list, pop_frame2, len_count):
        test = 0
        if test == 5:
            print("reorder_list - class Gui - gui.py")

        for i, val in enumerate(order):
            val = val.get()
            if i + 1 != val:
                if test == 2:
                    print("Not E: {}, {}".format(i + 1, val))
                ob_copy = objects[i]
                del objects[i]
                objects.insert(val - 1, ob_copy)

                sec_copy = section_image[i]
                del section_image[i]
                section_image.insert(val - 1, sec_copy)

                typ_copy = stitch_type[i]
                del stitch_type[i]
                stitch_type.insert(val - 1, typ_copy)
                if test == 1:
                    print(typ_copy)
                len_copy = stitch_len[i]
                del stitch_len[i]
                stitch_len.insert(val - 1, len_copy)

                del_copy = del_list[i]
                del del_list[i]
                del_list.insert(val - 1, del_copy)

            else:
                if test == 2:
                    print("Equal: {}, {}".format(i + 1, val))
        if test == 2:
            print_lists(stitch_type, stitch_len, order, del_list)
        self.frame2(objects, stitch_type, stitch_len, order, del_list, pop_frame2, len_count)
        if test == 2:
            print_lists(stitch_type, stitch_len, order, del_list)

    def frame2(self, ob_list, stitch_drop_list, len_drop_list, order_drop_list, checkbox_list, pop_frame2, len_count):
        test = 0
        if test == 5:
            print("frame2 - class Gui - gui.py")

        count = 1
        if test == 2:
            print_lists(stitch_drop_list, len_drop_list, order_drop_list, checkbox_list)

        # mid - merge layout
        self.top_display = tk.Frame(pop_frame2, pady=10)
        self.top_display.pack()
        self.bottom_display = tk.Frame(pop_frame2)
        self.bottom_display.pack()

        height = self.root.winfo_screenheight()
        max_height = height * 0.9

        if 31 * len_count > max_height:
            set_h = height
        else:
            set_h = 31 * len_count

        stitch_canvas = Canvas(self.bottom_display, width=610, height=set_h)
        stitch_canvas.configure()

        scroll_bar_y = tk.Scrollbar(self.bottom_display, orient=VERTICAL, command=stitch_canvas.yview)
        scroll_bar_y.pack(side=RIGHT, fill=Y)
        stitch_canvas.pack(fill=X, side=RIGHT)

        stitch_canvas.configure(yscrollcommand=scroll_bar_y.set)
        stitch_canvas.bind("<Configure>",
                           lambda e: stitch_canvas.configure(scrollregion=stitch_canvas.bbox("all")))

        self.stitch_frame = tk.Frame(stitch_canvas)
        can_w = stitch_canvas.winfo_width()
        can_h = stitch_canvas.winfo_height()
        stitch_canvas.create_window((can_w / 2, can_h / 2), window=self.stitch_frame, anchor="center")

        for ob in ob_list:

            # object ID = if not set then set, then display
            ob_id = ob.ob_id
            pop_label_1 = Label(self.stitch_frame, width=6, text=ob_id)
            pop_label_1.grid(row=count, column=0, padx=5)

            # object colour = get then display
            col = ob.colour
            hex_col = rgb_to_hex(col)
            pop_label_1 = Label(self.stitch_frame, width=5, bg=hex_col, borderwidth=1, relief="solid")
            pop_label_1.grid(row=count, column=1, padx=5, pady=5)

            # stitch type drop down = create
            select = StringVar()
            de = stitch_drop_list[count - 1]
            select.set(de.get())
            stitch_drop = OptionMenu(self.stitch_frame, select, "Stitch Outline", "Running Stitch Fill", "Fill Stitch")
            stitch_drop.config(width=15)
            stitch_drop.grid(row=count, column=2, padx=5)
            stitch_drop_list[count - 1] = select

            # max stitch len dropdown = create
            lengths = ["0.3mm", "0.5mm", "1.0mm", "1.2mm", "1.5mm", "2.0mm", "2.5mm", "3.0mm", "3.5mm", "4.0mm",
                       "4.5mm", "5.0mm"]
            stitch_len = StringVar()
            de = len_drop_list[count - 1]
            stitch_len.set(de.get())
            len_drop = OptionMenu(self.stitch_frame, stitch_len, *lengths)
            len_drop.config(width=5)
            len_drop.grid(row=count, column=3, padx=15)
            len_drop_list[count - 1] = stitch_len

            # stitch order  = set then display
            object_count = []
            for i in enumerate(self.objects):
                object_count.append(i[0] + 1)

            order = IntVar()
            de = order_drop_list[count - 1]
            order.set(count)
            order_drop = OptionMenu(self.stitch_frame, order, *object_count)
            order_drop.config(width=5)
            order_drop.grid(row=count, column=4, padx=5)
            order_drop_list[count - 1] = order

            # remove
            checked = IntVar()
            de = checkbox_list[count - 1]
            checked.set(de.get())
            checkbox = Checkbutton(self.stitch_frame, variable=checked)
            checkbox.grid(row=count, column=5, padx=5)
            checkbox.config(width=12)
            checkbox_list[count - 1] = checked

            # display section image
            self.section_image_list.append(ob.section_image)

            val = count - 1
            pop_button = Button(self.stitch_frame, text='Display',
                                command=lambda val=val: [self.display_section_image(val)])
            pop_button.grid(row=count, column=6, padx=5)

            count += 1
        pop_frame2.config()

    def colour_select_pop(self):
        test = 0
        if test == 5:
            print("colour_select_pop - class Gui - gui.py")

        global pop
        global floor_choice
        global lock
        global custom
        floor_choice = IntVar()
        lock = IntVar()
        custom = IntVar()

        # pop = Toplevel(self.second_frame)
        # pop.title("Colour Sample")
        # self.pop_geometry(300, 220)

        pop_frame1 = Frame(self.right_display)
        pop_frame1.pack()
        pop_label_1 = Label(pop_frame1, text='Number of Colours:')
        pop_label_1.grid(row=0, column=0, columnspan=4, sticky=W)
        pop_label_2 = Label(pop_frame1, text='1331')
        pop_label_2.grid(row=1, column=0)
        pop_label_3 = Label(pop_frame1, text='1000')
        pop_label_3.grid(row=2, column=0)
        pop_label_4 = Label(pop_frame1, text='729')
        pop_label_4.grid(row=3, column=0)
        pop_label_5 = Label(pop_frame1, text='512')
        pop_label_5.grid(row=4, column=0)
        pop_label_6 = Label(pop_frame1, text='343')
        pop_label_6.grid(row=5, column=0)
        pop_label_7 = Label(pop_frame1, text='216')
        pop_label_7.grid(row=1, column=3)
        pop_label_8 = Label(pop_frame1, text='125')
        pop_label_8.grid(row=2, column=3)
        pop_label_9 = Label(pop_frame1, text='64')
        pop_label_9.grid(row=3, column=3)
        pop_label_10 = Label(pop_frame1, text='27')
        pop_label_10.grid(row=4, column=3)
        pop_label_11 = Label(pop_frame1, text='8')
        pop_label_11.grid(row=5, column=3)

        pop_label_12 = Label(pop_frame1, width=5)
        pop_label_12.grid(row=1, column=2)
        pop_label_12 = Label(pop_frame1, width=5)
        pop_label_12.grid(row=2, column=2)
        pop_label_12 = Label(pop_frame1, width=5)
        pop_label_12.grid(row=3, column=2)
        pop_label_12 = Label(pop_frame1, width=5)
        pop_label_12.grid(row=4, column=2)
        pop_label_12 = Label(pop_frame1, width=5)
        pop_label_12.grid(row=5, column=2)

        # ** Pre-run alg before pop-up **
        # ** Colour button must run auto_colour_step()
        # ** - Runs colour_display(floor_choice)
        r_button_1 = Radiobutton(pop_frame1, variable=floor_choice, value=1,
                                 command=lambda: [self.colour_display(floor_choice),
                                                  self.right_button_1.configure(state=NORMAL)])
        r_button_1.grid(row=1, column=1, padx=10)
        r_button_2 = Radiobutton(pop_frame1, variable=floor_choice, value=2,
                                 command=lambda: [self.colour_display(floor_choice),
                                                  self.right_button_1.configure(state=NORMAL)])
        r_button_2.grid(row=2, column=1)
        r_button_3 = Radiobutton(pop_frame1, variable=floor_choice, value=3,
                                 command=lambda: [self.colour_display(floor_choice),
                                                  self.right_button_1.configure(state=NORMAL)])
        r_button_3.grid(row=3, column=1)
        r_button_4 = Radiobutton(pop_frame1, variable=floor_choice, value=4,
                                 command=lambda: [self.colour_display(floor_choice),
                                                  self.right_button_1.configure(state=NORMAL)])
        r_button_4.grid(row=4, column=1)
        r_button_5 = Radiobutton(pop_frame1, variable=floor_choice, value=5,
                                 command=lambda: [self.colour_display(floor_choice),
                                                  self.right_button_1.configure(state=NORMAL)])
        r_button_5.grid(row=5, column=1)
        r_button_6 = Radiobutton(pop_frame1, variable=floor_choice, value=6,
                                 command=lambda: [self.colour_display(floor_choice),
                                                  self.right_button_1.configure(state=NORMAL)])
        r_button_6.grid(row=1, column=4)
        r_button_7 = Radiobutton(pop_frame1, variable=floor_choice, value=7,
                                 command=lambda: [self.colour_display(floor_choice),
                                                  self.right_button_1.configure(state=NORMAL)])
        r_button_7.grid(row=2, column=4)
        r_button_8 = Radiobutton(pop_frame1, variable=floor_choice, value=8,
                                 command=lambda: [self.colour_display(floor_choice),
                                                  self.right_button_1.configure(state=NORMAL)])
        r_button_8.grid(row=3, column=4)
        r_button_9 = Radiobutton(pop_frame1, variable=floor_choice, value=9,
                                 command=lambda: [self.colour_display(floor_choice),
                                                  self.right_button_1.configure(state=NORMAL)])
        r_button_9.grid(row=4, column=4)
        r_button_10 = Radiobutton(pop_frame1, variable=floor_choice, value=10,
                                  command=lambda: [self.colour_display(floor_choice),
                                                   self.right_button_1.configure(state=NORMAL)])
        r_button_10.grid(row=5, column=4)
        # self.right_button_1.configure(state=NORMAL)
        # pop_button = Button(pop_frame1, text="OK", command=lambda: [self.set_colour_change(floor_choice.get()), self.stats()])  # pop.destory
        # pop_button.grid(row=8, column=3, pady=10)
        # pop_button = Button(pop_frame1, text="Back", command=lambda: [pop.destroy()])
        # pop_button.grid(row=8, column=0, pady=10)
        # self.right_top.config()

    def colour_display(self, option):  # gui
        test = 0
        if test == 5:
            print("colour_display gui.py")

        if 0 < option.get() < 11:
            img = self.temp_images[option.get() - 1]
            self.display_image(img)
        else:
            if test == 1:
                print("Error: Colour Display function")

    def set_colour_change(self, option):  # gui
        test = 4
        if test == 5:
            print("set_colour_change gui.py")

        self.undo_list.append(self.images[1])
        self.undo_function_list.append(2)
        if test == 4:
            print("2 - Functions so far: {}".format(self.undo_function_list))

        self.images[1] = self.temp_images[option - 1]
        self.display_cy_image()

    def stats(self):
        test = 0
        if test == 5 or test == 1:
            print("stats - class Gui - gui.py")

        image = self.images[1]
        pixel_matrix = np.array(image)
        pixel_list = []
        colour_count = []
        av_count = 0
        combine_count = []
        total_pix = len(pixel_matrix) * len(pixel_matrix[0])

        pixel_list, colour_count, combine_count = im.count_colour(pixel_matrix)

        im.sort_algorithm(pixel_list, combine_count, colour_count)
        avg = total_pix / len(colour_count)

        for x in colour_count:
            if x > avg:
                av_count += 1

        if test == 1:
            e = 1
            for x in pixel_list:
                comb = combine_count[e - 1]
                num = colour_count[e - 1]
                per_part = num / total_pix
                per = per_part * 100
                per = '%.2f' % per
                str_e = str(e)
                str_x = str(x)
                str_comb = str(comb)
                str_num = str(num)
                str_per = str(per)
                str_per += "%"

                while len(str_e) != 3:
                    str_e += " "

                while len(str_x) != 16:
                    str_x += " "

                while len(str_comb) != 4:
                    str_comb += " "

                while len(str_num) != len(str(total_pix)) + 1:
                    str_num += " "

                while len(str_per) != 8:
                    str_per = " " + str_per

                print("Colour {}  Value: {}  Comb Val: {}  Amount: {}  Percentage: {}".format(str_e, str_x, str_comb, str_num, str_per))
                e += 1

            print("Total Pixel Count: ", total_pix)
            print("Total Height: ", len(pixel_matrix), "\nTotal Length: ", len(pixel_matrix[0]))
            print("Number of colours > Average Pixel count: ", av_count, " Average: ", av_count)

    def manuel_merge_pop(self):
        test = 0
        if test == 5:
            print("manuel_merge_pop - class Gui - gui.py")

        global pop
        image = self.images[1]
        pixel_matrix = np.array(image)
        y_len = len(pixel_matrix)
        x_len = len(pixel_matrix[0])
        total_pix = y_len * x_len

        self.change_list = []

        self.pixel_list, colour_count, combine_count = im.count_colour(pixel_matrix)
        length = len(self.pixel_list)

        # pop = Toplevel(self.second_frame)
        # pop.title("Colour Sample")
        # self.pop_geometry(300, 50 + 35 * length)

        count_list = []
        pop_frame1 = Frame(self.title_frame)
        pop_frame1.pack()
        pop_frame2 = Frame(self.display_frame)
        pop_frame2.pack()
        count = 1
        op_list = []

        pop_label_1 = Label(pop_frame1, text='Colour ID', width=8)
        pop_label_1.grid(row=0, column=0)
        pop_label_1 = Label(pop_frame1)
        pop_label_1.grid(row=0, column=1, padx=5)
        pop_label_1 = Label(pop_frame1, text='Colour', width=5)
        pop_label_1.grid(row=0, column=2, padx=10)
        pop_label_1 = Label(pop_frame1, text='% of Image:', width=8)
        pop_label_1.grid(row=0, column=3, padx=6)
        pop_label_1 = Label(pop_frame1, text='Merge', width=8)
        pop_label_1.grid(row=0, column=4)
        pop_label_1 = Label(pop_frame1)
        pop_label_1.grid(row=0, column=5, padx=5)
        len_count = 1

        for i in range(length):
            count_list.append(len_count)
            len_count += 1

        for pixel in self.pixel_list:

            ind = self.pixel_list.index(pixel)

            hex_colour = rgb_to_hex(pixel)
            colour_text = "#" + str(count)
            pop_label = Label(pop_frame2, text=colour_text, width=8)
            pop_label.grid(row=count, column=0, padx=5)

            colour_label = Label(pop_frame2, width=5, bg=hex_colour, borderwidth=1, relief="solid")
            colour_label.grid(row=count, column=1, padx=20)

            pix_count = colour_count[ind]

            per = pix_count / total_pix
            per = per * 100
            per_text = "{:.1f}%".format(per)
            per_label = Label(pop_frame2, text=per_text, width=8)
            per_label.grid(row=count, column=2, padx=5)

            for i in enumerate(self.pixel_list):
                op_list.append(i[0] + 1)

            change = IntVar()
            change.set(0)
            drop = OptionMenu(pop_frame2, change, *count_list)
            drop.grid(row=count, column=3, padx=5)
            self.change_list.append(change)

            count += 1

        # # update - button - update
        # self.right_button_2.configure(text="Update Merge",
        #                               command=lambda: [im.get_man_merge_vals(self, self.change_list, self.pixel_list),
        #                                                self.reset_canvas(), self.manuel_merge_pop(),
        #                                                self.right_button_1.config(state=NORMAL)])
        # # next - button - lock until action - update
        # self.right_button_1.configure(state=DISABLED, command=lambda: [self.update_right_pane(5),
        #                                                                im.janome_colours(self)])
        # pop_button = Button(pop_frame1, text="OK",
        #                     command=lambda: [im.get_man_merge_vals(self, change_list, self.pixel_list)])
        # pop_button.grid(row=count + 1, column=2, pady=10, columnspan=2)
        # pop_button = Button(pop_frame1, text="Back")
        # pop_button.grid(row=count + 1, column=0, pady=10, columnspan=2)

    def display_section_image(self, val):
        test = 0
        if test == 5:
            print("display_section_image - Gui - gui.py")

        image = self.section_image_list[val]
        self.images[1] = image
        self.display_cy_image()


class ProgressPop:

    def __init__(self, main, title, message, max, mode):
        test = 0
        if test == 5:
            print("class ProgressPop - gui.py")
        global pop
        self.max = max
        self.object = ""

        pop = Toplevel(main.second_frame)
        pop.title(title)
        pop.iconbitmap("Pic-to-Stitch_32x32.ico")
        main.pop_geometry_progress(400, 100)
        self.pop_frame1 = Frame(pop)
        self.pop_frame1.pack()

        label = Label(self.pop_frame1)
        label.grid(row=0, column=1, pady=3, padx=5, sticky=W)

        self.bar_label = Label(self.pop_frame1, text=message)
        self.bar_label.grid(row=1, column=1, pady=1, sticky=W)

        if mode == 1:
            set_mode = 'determinate'
        else:
            set_mode = 'indeterminate'

        self.progress_bar = ttk.Progressbar(self.pop_frame1, orient=HORIZONTAL, length=300, mode=set_mode)
        self.progress_bar.grid(row=2, column=1)

        if mode != 1:
            self.progress_bar.step()

    def progress_update_progress_d(self, count, secs):
        test = 0
        if test == 5:
            print("progress_update_progress_d - class ProgressPop - gui.py")
        if count != 0:
            one_per = count / self.max
            cur_pro = one_per * 100
            self.progress_bar['value'] = cur_pro
        self.progress_bar.update()
        time.sleep(secs)

    def progress_update_progress_ind(self, count, secs):
        test = 0
        if test == 5:
            print("progress_update_progress_ind - class ProgressPop - gui.py")
        self.progress_bar['value'] += count + 9
        self.progress_bar.update()
        time.sleep(secs)

    def progress_update_message(self, message):
        test = 0
        if test == 5:
            print("progress_update_message - class ProgressPop - gui.py")
        text = self.object + message
        self.bar_label.config(text=text)
        self.progress_bar.update()

    def progress_update_object(self, object):
        test = 0
        if test == 5:
            print("progress_update_object - class ProgressPop - gui.py")
        self.object = object
        self.progress_bar.update()

    def progress_reset(self, message, pro_val, max, mode):
        test = 0
        if test == 5:
            print("progress_reset - class ProgressPop - gui.py")
        self.max = max
        self.bar_label.config(text=message)
        self.progress_bar['value'] = pro_val
        if mode == 1:
            set_mode = 'determinate'
        else:
            set_mode = 'indeterminate'
        self.progress_bar.config(mode=set_mode)

    def destroy(self):
        test = 0
        if test == 5:
            print("destroy - class ProgressPop - gui.py")
        pop.destroy()


def temp_folder():
    test = 5
    if test == 5:
        print("temp_folder gui.py")
    print("check for or create temp folder to store temp files")


def save_folder():
    test = 5
    if test == 5:
        print("save_folder gui.py")
    print("check for or create save folder to save project images")


def do_nothing():
    print("C1 W1 H1 A0 - Custom size Squish")


def open_project():
    pass


def new_project():
    print("Ooooh a new project? Whats this one for?")


def exit_option():
    print("You can't go yet")


def redo():
    print("Shall I say that again?")


class ValueError1(ValueError):
    pass


class ValueError2(ValueError):
    pass


class ValueError3(ValueError):
    pass


# not used ?
def print_plot(plot):
    test = 5
    if test == 5:
        print("print_plot gui.py")

    for y in plot:
        print(y)


def print_pixel_plot(plot):
    test = 5
    if test == 5:
        print("print_pixel_plot gui.py")

    for y, row in enumerate(plot):
        p_row = ""
        for x, point in enumerate(row):
            p_row = p_row + str(point) + " "

        print(p_row)


# new
def plot_check(plot):
    test = 5
    if test == 5:
        print("plot_check gui.py")

    for y in plot:
        for x in y:

            if x == 0:
                return True
    return False


def process_stitch_choices(main, objects, section_images, stitch_type, stitch_len, order, del_list):
    test = 0
    if test == 5:
        print("process_stitch_choices gui.py")

    for i, item in enumerate(del_list):
        del_list[i] = item.get()

    ext = 0
    while ext != 1:  # check for del in list

        if 1 in del_list:  # if del in list then remove
            ind = del_list.index(1)
            del del_list[ind]
            del objects[ind]
            del stitch_len[ind]
            del stitch_type[ind]
            del order[ind]
            del section_images[ind]
        else:  # else break
            ext = 1

    # progress bar creation
    message = "Creating Stitch Objects..."
    main.bar("Stitch Objects", message, len(objects), 1)
    main.bar_update_progress(0, 0.3, 1)
    msg_count = 1
    # end

    for i, ob in enumerate(objects):

        # progress bar update
        msg = "Processing..."
        text_object = "Object " + str(msg_count) + " : "
        main.bar_update_object(text_object)
        main.bar_update_message(msg)
        main.bar_update_progress(msg_count, 0.1, 1)
        # end

        stitch = stitch_type[i]
        stitch = stitch.get()
        if test == 1:
            print(stitch)

        if stitch == "Stitch Outline":
            if test == 1:
                print("Objects {} set with Outline Running Stitch".format(i + 1))
            ob.outline_running_stitch()
            ob.set_stitch_type("Outline Running Stitch")

        elif stitch == "Running Stitch Fill":
            if test == 1:
                print("Objects {} set with Running Stitch Fill".format(i + 1))
            ob.running_stitch_fill(main)
            ob.set_stitch_type("Running Stitch Fill")

        elif stitch == "Fill Stitch":
            if test == 1:
                print("Objects {} set with Fill Stitch".format(i + 1))
            ob.fill_stitch_fill(main)
            ob.set_stitch_type("Fill Stitch")

        stitch_len_int = [3, 6, 9, 12, 15, 21, 24, 30, 36, 39, 45, 51]
        stitch_len_str = ["0.3mm", "0.5mm", "1.0mm", "1.2mm", "1.5mm", "2.0mm", "2.5mm", "3.0mm", "3.5mm", "4.0mm",
                          "4.5mm", "5.0mm"]

        max_len = stitch_len[i]
        ind = stitch_len_str.index(max_len.get())
        val = stitch_len_int[ind]

        ob.set_stitch_len(val)

        msg_count += 1

    # progress bar destroy
    main.bar_des()
    # end

    if test == 1:
        print("Object Set Finished")


def save_file(mata_file):
    test = 0
    if test == 5:
        print("save_file - gui.py")
    f = filedialog.asksaveasfilename(defaultextension=".jef", filetypes=(("Janome (*.jef)", ".jef"),))
    if f == "":  # asksaveasfile return `None` if dialog closed with "cancel".
        return
    else:
        wo.write_to_file(mata_file, f)


def print_lists(a, b, c, d):
    test = 5
    if test == 5:
        print("print_lists gui.py")

    a_str = ""
    b_str = ""
    c_str = ""
    d_str = ""
    for i in a:
        a_str = a_str + " " + str(i.get())

    for i in b:
        b_str = b_str + " " + str(i.get())

    for i in c:
        c_str = c_str + " " + str(i.get())

    for i in d:
        d_str = d_str + " " + str(i.get())

    print("Stitch Type")
    print(a_str)
    print("Stitch Length")
    print(b_str)
    print("Order Change")
    print(c_str)
    print("Delete Y/N")
    print(d_str)


def rgb_to_hex(pixel):
    test = 0
    if test == 5:
        print("rgb_to_hex gui.py")

    hex_r = hex(pixel[0])
    n_hex_r = hex_r.replace("0x", "")
    if len(n_hex_r) == 1:
        n_hex_r = "0" + n_hex_r

    hex_g = hex(pixel[1])
    n_hex_g = hex_g.replace("0x", "")
    if len(n_hex_g) == 1:
        n_hex_g = "0" + n_hex_g

    hex_b = hex(pixel[2])
    n_hex_b = hex_b.replace("0x", "")
    if len(n_hex_b) == 1:
        n_hex_b = "0" + n_hex_b

    hex_colour = "#" + n_hex_r + n_hex_g + n_hex_b
    if test == 1:
        print("New colour hex: ", hex_colour, " RGB Hex: ", hex_r, hex_g, hex_b, " Change RGB Hex: ", n_hex_r, n_hex_g,
              n_hex_b)

    return hex_colour


if __name__ == '__main__':
    global main_window
    main_window = Gui()
