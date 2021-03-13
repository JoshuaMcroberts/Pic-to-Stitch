import tkinter as tk
from tkinter import filedialog
from tkinter import *
# from tkinter.ttk import *
from PIL import Image, ImageTk, ImageFilter, ImageOps
import tkinter.messagebox
import numpy as np
from prompt_toolkit import selection

import plot_objects as po
import stitch_objects as so

# list
# from PIL.ImageTk import PhotoImage
loaded_image = ""
images = []
undo = []
temp_images = []
objects = []
# filepath
# og_img
global og_display
global cy_display
global average_pixel_count


def temp_folder():
    print("check for or create temp folder to store temp files")


def save_folder():
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


def you_sure():
    answer = tkinter.messagebox.askquestion("", "Are you sure you want to load a new image")
    if answer == "yes":
        load_image()


def hoop_size_select():
    global pop
    global hoop_choice
    global lock
    global custom
    hoop_choice = IntVar()
    lock = IntVar()
    custom = IntVar()

    pop = Toplevel(second_frame)
    pop.title("Hoop Size")
    pop_geometry(300, 250)

    pop_frame1 = Frame(pop)
    pop_frame1.pack()
    pop_label_1 = Label(pop_frame1, text='Select a Hoop Size:')
    pop_label_1.grid(row=0, column=0, padx=20, pady=10)
    pop_label_2 = Label(pop_frame1, text='4"x4" Hoop (110x110mm)')
    pop_label_2.grid(row=1, column=0)
    pop_label_3 = Label(pop_frame1, text='2"x2" Hoop (50x50mm)')
    pop_label_3.grid(row=2, column=0)
    pop_label_4 = Label(pop_frame1, text='5.5"x8" Hoop (140x200mm)')
    pop_label_4.grid(row=3, column=0)
    pop_label_3 = Label(pop_frame1, text='5"x4" Hoop (127x110mm)')
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

    # separator = ttk.Separator(pop_frame1, orient='horizontal')
    # separator.place(relx=0, rely=0.4, relwidth=1, relheight=1)
    custom = IntVar()
    custom_check = Checkbutton(pop_frame1, variable=custom, command=custom_option)
    custom_check.grid(row=6, column=1)
    pop_label_7 = Label(pop_frame1, text="Custom size:")
    pop_label_7.grid(row=6, column=0)

    global pop_frame2
    pop_frame2 = Frame(pop)
    pop_frame2.pack()

    global pop_frame3
    pop_frame3 = Frame(pop)
    pop_frame3.pack()
    pop_button = Button(pop_frame3, text="OK", command=lambda: [sizing_check(hoop_choice.get(), custom.get())])  # pop.destory
    pop_button.grid(row=8, column=1, pady=10)
    pop_button = Button(pop_frame3, text="Back", command=lambda: [undo_hoop_choice(), pop.destroy()])
    pop_button.grid(row=8, column=0, pady=10)


def pop_geometry(width, height):
    pop_width = width
    pop_height = height
    pop_x = centre_width - (pop_width / 2)
    pop_y = centre_height - (pop_height / 2)
    pop.geometry(f'{pop_width}x{pop_height}+{int(pop_x)}+{int(pop_y)}')
    pop.update()


class ValueError1(ValueError):
    pass


class ValueError2(ValueError):
    pass


class ValueError3(ValueError):
    pass


def error_message(message):
    error_message = Toplevel(second_frame)
    error_message.title("Error")
    error_width = 300
    error_height = 100
    error_x = centre_width - (error_width / 2)
    error_y = centre_height - (error_height / 2)
    error_message.geometry(f'{error_width}x{error_height}+{int(error_x)}+{int(error_y)}')
    error_label = Label(error_message, text="Error: " + message)
    error_label.pack(pady=20)
    error_button = Button(error_message, text="OK", command=lambda:
    [error_message.destroy()])
    error_button.pack(pady=10)


def warn_message(message, function, hoop, option, width, height):
    global hp
    global op
    global w
    global h

    hp = hoop
    op = option
    w = width
    h = height
    warn_message = Toplevel(second_frame)
    warn_message.title("Warning")
    warn_width = 280
    warn_height = 100
    warn_x = centre_width - (warn_width / 2)
    warn_y = centre_height - (warn_height / 2)
    warn_message.geometry(f'{warn_width}x{warn_height}+{int(warn_x)}+{int(warn_y)}')
    warn_label = Label(warn_message, text="Warning: " + message)
    warn_label.grid(row=0, column=0, columnspan=3, pady=15, padx=35)
    warn_button_back = Button(warn_message, text="Back", width=10, command=lambda: [warn_message.destroy()])
    warn_button_back.grid(row=1, column=0, pady=10, sticky=E)
    warn_button_ok = Button(warn_message, text="OK", width=10, command=lambda: [eval(function), warn_message.destroy(), pop.destroy()])
    warn_button_ok.grid(row=1, column=2, pady=10, sticky=W)


def sizing_check(hoopchoice, customcheck):
    hoop_width = IntVar()
    hoop_height = IntVar()
    img_w = int()
    img_h = int()

    go = int()
    try:
        if hoopchoice == 1:
            hoop_width = 110
            hoop_height = 110

        elif hoopchoice == 2:
            hoop_width = 127
            hoop_height = 177

        elif hoopchoice == 3:
            hoop_width = 152
            hoop_height = 254

        elif hoopchoice == 4:
            hoop_width = 127
            hoop_height = 177

        elif hoopchoice == 5:
            hoop_width = 152
            hoop_height = 254

        else:
            raise ValueError1
    except ValueError1:
        global error_message

        error_message("Select a Hoop SIze")

    if hoopchoice > 0 and customcheck == 1:
        try:
            img_w = enter_width.get()
            img_h = enter_height.get()
            if bool(img_w) == True and bool(img_h) == True:
                img_w = int(enter_width.get())
                img_h = int(enter_height.get())
                go = 1
                print("option 1")
            elif bool(img_w) == False and bool(img_h) == True:
                img_w = 0
                img_h = int(enter_height.get())
                go = 1
                print("option 2")
            elif bool(img_h) == False and bool(img_w) == True:
                img_h = 0
                img_w = int(enter_width.get())
                go = 1
                print("option 3")

            else:
                go = 0
                raise ValueError3

        except ValueError3:
            error_message("Width and Height fields left blank")

        checked = int(lock.get())

        if go > 0:
            if img_h > 0 and img_w > 0:
                if checked == 1:
                    try:
                        if img_w > hoop_width:
                            raise ValueError1
                        else:
                            image_resize(hoopchoice, 3, img_w, img_h)
                            pop.destroy()
                            print("C1 W1 H1 A1 - Custom size to Width")
                    except ValueError1:
                        error_message("Custom width is larger than Hoop Width")
                elif checked == 0:
                    warn_message("Image may be unevenly sized", "image_resize(hp, op, w, h )", hoopchoice, 2, img_w, img_h)  # function must be passed as string
                else:
                    print("Error: Lock Aspect Ratio Checkbox Value ")
            elif img_h > 0:
                try:
                    if checked == 1:
                        try:
                            if img_h > hoop_height:
                                raise ValueError1
                            else:
                                image_resize(hoopchoice, 4, img_w, img_h)
                                pop.destroy()
                                print("C1 W0 H1 A1 - Custom ratio size to only Height")
                        except ValueError1:
                            error_message("Custom Height is larger than Hoop Height")
                    elif checked == 0:
                        raise ValueError2
                    else:
                        print("Error: Lock Aspect Ratio Checkbox Value ")
                except ValueError2:
                    error_message("Complete Width or Select 'Lock Aspect Ratio'")
            elif img_w > 0:
                try:
                    if checked == 1:
                        try:
                            if img_w > hoop_width:
                                raise ValueError1
                            else:
                                image_resize(hoopchoice, 3, img_w, img_h)
                                pop.destroy()
                                print("C1 W1 H0 A1 - Custom ratio size to only Width")

                        except ValueError1:
                            error_message("Custom Width is larger than Hoop Width")
                    elif checked == 0:
                        raise ValueError2
                    else:
                        print("Error: Lock Aspect Ratio Checkbox Value ")
                except ValueError2:
                    error_message("Complete Height or Select 'Lock Aspect Ratio'")
            else:
                print("Error: Custom Height/Width Values")
        #     else:
        #         raise ValueError3
        # except ValueError3:
        #     error_message("Width and Height fields left blank")

    elif hoopchoice > 0 and customcheck == 0:
        image_resize(hoopchoice, 1, img_w, img_h)
        pop.destroy()
        print("C0 W0 H0 A0 - Auto Sizing to Hoop")

    # else:
    #     # if not exceptions
    #     print(" continue")
    # finally:
    #     print("Done")


def custom_option():
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
        pop_geometry(300, 320)

    elif checked == 0:
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


def print_plot(plot):
    height = len(plot)
    width = len(plot[0])

    for y in plot:
        print(y)
        # for x in plot:
        #
        #     print(x,)


def print_pixel_plot(plot):

    for y, row in enumerate(plot):
        p_row = ""
        for x, point in enumerate(row):

            p_row = p_row + str(point) + " "

        print(p_row)

# new
def plot_check(plot):
    for y in plot:
        for x in y:

            if x == 0:
                return True

    return False


# new
def check_index_list(ind_list, y, x):

    try:
        a = ind_list.index((y, x))

    except ValueError:
        a = 0

    return a


# new
def check_fill(image_copy, plot, s_object, colour_list):
    col = s_object.object_id
    pixel_list = []
    colour_count = []
    combine_count = []
    state = 0

    max_y, max_x = s_object.max_yx
    min_y, min_x = s_object.min_yx

    for y, row in enumerate(plot):
        end = 1
        for x, point in enumerate(row):
            if x + 1 <= max_x:
                n_point = row[x + 1]

            if x + 1 > max_x or x < min_x or y > max_y or y < min_y:
                pass

            elif point == col and x + 1 < len(row - 1) and n_point == col:
                end = 0

            elif point == col and x + 1 < len(row - 1) and n_point == 0:

                if state == 0:
                    state = 1
                elif state == 1:
                    state = 0
                end = 0

            elif point == 0 and x + 1 < len(row - 1) and n_point == col:

                if state == 1:
                    pixel_list.append(image_copy[y, x])
                    state = 0
                end = 0

            elif x == 0:

                if state == 1:
                    pixel_list.append(image_copy[y, x])

            elif point != col and point != 0:
                print("Pass")
            pass

        if end == 1:
            break

    count_colour_list(pixel_list, colour_list, colour_count, combine_count)

    if len(colour_list) > 1:
        return False
    elif len(colour_list) == 1:
        return True
    else:
        return "fail"


# new
def find_fill(image_copy, plot, s_object):  # working on this 13/02/2021
    col = s_object.object_id
    pixel_list = []
    colour_list = []
    colour_count = []
    combine_count = []
    state = 0
    end = 0

    max_y, max_x = s_object.max_yx
    min_y, min_x = s_object.min_yx

    for y in plot:
        end = 1
        for x in y:

            if x > max_x or x < min_x or y > max_y or y < min_y:
                pass

            if x == col and x + 1 < len(y - 1) and x + 1 == col:
                end = 0

            elif x == col and x + 1 < len(y - 1) and x + 1 == 0:

                if state == 0:
                    state = 1
                elif state == 1:
                    state = 0
                end = 0

            elif x == 0 and x + 1 < len(y - 1) and x + 1 == col:

                if state == 1:
                    pixel_list.append(image_copy[y, x])
                    state = 0
                end = 0

            elif x == 0:

                if state == 1:
                    pixel_list.append(image_copy[y, x])

            elif x != col and x != 0:
                print("Pass")

        if end == 1:
            break

    count_colour_list(pixel_list, colour_list, colour_count, combine_count)

    if len(colour_list) > 1:
        return False
    elif len(colour_list) == 1:
        return True
    else:
        return "error"


# new
def find_outline(image_copy, plot, s_object, start_pix, start_point):

    ind_list = []

    y, x = start_point

    last_pix = start_pix
    count = 1
    # count = s_object.object_id
    c_colour = s_object.colour
    i = 0
    ind_list.append((y, x))
    plot[y, x] = count
    s_object.plot[y, x] = count
    # x += 1
    print("Colour: ", c_colour)

    for j in range(len(image_copy)*len(image_copy[0])):

        # One
        if last_pix == 8:
            print("#One")
            if y - 1 >= 0 and x - 1 >= 0:

                new_pix = image_copy[y - 1, x - 1]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:

                            pix_a = image_copy[y, x-1]
                            pix_b = image_copy[y-1, x]

                            if pix_a[0] == c_colour[0]:
                                if pix_a[1] == c_colour[1]:
                                    if pix_a[2] == c_colour[2]:
                                        comp_a = True
                                    else:
                                        comp_a = False
                                else:
                                    comp_a = False
                            else:
                                comp_a = False

                            if pix_b[0] == c_colour[0]:
                                if pix_b[1] == c_colour[1]:
                                    if pix_b[2] == c_colour[2]:
                                        comp_b = True
                                    else:
                                        comp_b = False
                                else:
                                    comp_b = False
                            else:
                                comp_b = False

                            if comp_a or comp_b:
                                # if not ind_list:
                                #     y = y - 1
                                #     x = x - 1
                                #     plot[y, x] = count
                                #     s_object.plot[y, x] = count
                                #     ind_list.append((y, x))
                                #
                                #     last_pix = 5
                                #
                                # el
                                if (y - 1, x - 1) == ind_list[0]:
                                    break

                                else:
                                    y = y - 1
                                    x = x - 1
                                    plot[y, x] = count
                                    s_object.plot[y, x] = count
                                    ind_list.append((y, x))
                                    print("Set")
                                    last_pix = 5

            if last_pix != 5:
                last_pix = 1

        # Two
        elif last_pix == 1:
            print("#Two")
            if y - 1 >= 0:

                new_pix = image_copy[y - 1, x]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:

                            # if not ind_list:
                            #     y = y - 1
                            #     plot[y, x] = count
                            #     s_object.plot[y, x] = count
                            #     ind_list.append((y, x))
                            #
                            #     last_pix = 6
                            #
                            # el
                            if (y - 1, x) == ind_list[0]:
                                break

                            else:
                                y = y - 1
                                plot[y, x] = count
                                s_object.plot[y, x] = count
                                ind_list.append((y, x))
                                print("Set")
                                last_pix = 6

            if last_pix != 6:
                last_pix = 2

        # Three
        elif last_pix == 2:
            print("#Three")
            if y - 1 >= 0 and x + 1 < len(image_copy[0]):

                new_pix = image_copy[y - 1, x + 1]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:

                            pix_a = image_copy[y, x + 1]
                            pix_b = image_copy[y - 1, x]

                            if pix_a[0] == c_colour[0]:
                                if pix_a[1] == c_colour[1]:
                                    if pix_a[2] == c_colour[2]:
                                        comp_a = True
                                    else:
                                        comp_a = False
                                else:
                                    comp_a = False
                            else:
                                comp_a = False

                            if pix_b[0] == c_colour[0]:
                                if pix_b[1] == c_colour[1]:
                                    if pix_b[2] == c_colour[2]:
                                        comp_b = True
                                    else:
                                        comp_b = False
                                else:
                                    comp_b = False
                            else:
                                comp_b = False

                            if comp_a or comp_b:

                                # if not ind_list:
                                #     y = y - 1
                                #     x = x + 1
                                #     plot[y, x] = count
                                #     s_object.plot[y, x] = count
                                #
                                #     ind_list.append((y, x))
                                #     last_pix = 7
                                #
                                # el
                                if (y - 1, x + 1) == ind_list[0]:
                                    break

                                else:
                                    y = y - 1
                                    x = x + 1
                                    plot[y, x] = count
                                    s_object.plot[y, x] = count
                                    ind_list.append((y, x))
                                    print("Set")
                                    last_pix = 7

            if last_pix != 7:
                last_pix = 3

        # Four
        elif last_pix == 3:
            print("#Four")
            if x + 1 < len(image_copy[0]):

                new_pix = image_copy[y, x + 1]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:

                            # if not ind_list:
                            #     x = x + 1
                            #     plot[y, x] = count
                            #     s_object.plot[y, x] = count
                            #     ind_list.append((y, x))
                            #
                            #     last_pix = 8
                            #
                            # el
                            if (y, x + 1) == ind_list[0]:
                                break

                            else:
                                x = x + 1
                                plot[y, x] = count
                                s_object.plot[y, x] = count
                                ind_list.append((y, x))
                                print("Set")
                                last_pix = 8

            if last_pix != 8:
                last_pix = 4

        # Five
        elif last_pix == 4:
            print("#Five")
            if y + 1 < len(image_copy) and x + 1 < len(image_copy[0]):

                new_pix = image_copy[y + 1, x + 1]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:

                            pix_a = image_copy[y, x + 1]
                            pix_b = image_copy[y + 1, x]

                            if pix_a[0] == c_colour[0]:
                                if pix_a[1] == c_colour[1]:
                                    if pix_a[2] == c_colour[2]:
                                        comp_a = True
                                    else:
                                        comp_a = False
                                else:
                                    comp_a = False
                            else:
                                comp_a = False

                            if pix_b[0] == c_colour[0]:
                                if pix_b[1] == c_colour[1]:
                                    if pix_b[2] == c_colour[2]:
                                        comp_b = True
                                    else:
                                        comp_b = False
                                else:
                                    comp_b = False
                            else:
                                comp_b = False

                            if comp_a or comp_b:

                                # if not ind_list:
                                #     y = y + 1
                                #     x = x + 1
                                #     plot[y, x] = count
                                #     s_object.plot[y, x] = count
                                #     ind_list.append((y, x))
                                #
                                #     last_pix = 1
                                #
                                # el
                                if (y + 1, x + 1) == ind_list[0]:
                                    break

                                else:
                                    y = y + 1
                                    x = x + 1
                                    plot[y, x] = count
                                    s_object.plot[y, x] = count
                                    ind_list.append((y, x))
                                    print("Set")
                                    last_pix = 1

            if last_pix != 1:
                last_pix = 5

        # Six
        elif last_pix == 5:
            print("#Six")
            if y + 1 < len(image_copy):

                new_pix = image_copy[y + 1, x]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:

                            # if not ind_list:
                            #     y = y + 1
                            #     plot[y, x] = count
                            #     s_object.plot[y, x] = count
                            #     ind_list.append((y, x))
                            #
                            #     last_pix = 2
                            #
                            # el
                            if (y + 1, x) == ind_list[0]:
                                break

                            else:
                                y = y + 1
                                plot[y, x] = count
                                s_object.plot[y, x] = count
                                ind_list.append((y, x))
                                print("Set")
                                last_pix = 2

            if last_pix != 2:
                last_pix = 6

        # Seven
        elif last_pix == 6:
            print("#Seven")
            if y + 1 < len(image_copy) and x - 1 >= 0:

                new_pix = image_copy[y + 1, x - 1]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:

                            pix_a = image_copy[y, x - 1]
                            pix_b = image_copy[y + 1, x]

                            if pix_a[0] == c_colour[0]:
                                if pix_a[1] == c_colour[1]:
                                    if pix_a[2] == c_colour[2]:
                                        comp_a = True
                                    else:
                                        comp_a = False
                                else:
                                    comp_a = False
                            else:
                                comp_a = False

                            if pix_b[0] == c_colour[0]:
                                if pix_b[1] == c_colour[1]:
                                    if pix_b[2] == c_colour[2]:
                                        comp_b = True
                                    else:
                                        comp_b = False
                                else:
                                    comp_b = False
                            else:
                                comp_b = False

                            if comp_a or comp_b:

                                # if not ind_list:
                                #     y = y + 1
                                #     x = x - 1
                                #     plot[y, x] = count
                                #     s_object.plot[y, x] = count
                                #     ind_list.append((y, x))
                                #
                                #     last_pix = 3
                                #
                                # el
                                if (y + 1, x - 1) == ind_list[0]:
                                    break

                                else:
                                    y = y + 1
                                    x = x - 1
                                    plot[y, x] = count
                                    s_object.plot[y, x] = count
                                    ind_list.append((y, x))
                                    print("Set")
                                    last_pix = 3

            if last_pix != 3:
                last_pix = 7

        # Eight
        elif last_pix == 7:
            print("#Eight")
            if x - 1 >= 0:

                new_pix = image_copy[y, x - 1]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:

                            # if not ind_list:
                            #     x = x - 1
                            #     plot[y, x] = count
                            #     s_object.plot[y, x] = count
                            #     ind_list.append((y, x))
                            #
                            #     last_pix = 4
                            #
                            # el
                            if (y, x - 1) == ind_list[0]:
                                break

                            else:
                                x = x - 1
                                plot[y, x] = count
                                s_object.plot[y, x] = count
                                ind_list.append((y, x))
                                print("Set")
                                last_pix = 4

            if last_pix != 4:
                last_pix = 8

        # a = check_index_list(ind_list, y, x)
        i += 1

    max_y = 0
    min_y = 0
    max_x = 0
    min_x = 0

    for k in ind_list:
        y, x = k
        if max_y < y:
            max_y = y
        if max_x < x:
            max_x = x
        if min_y > y:
            min_y = y
        if min_x > x:
            min_x = x

    s_object.max_yx = (max_y, max_x)
    s_object.min_yx = (min_y, min_x)
    s_object.object_outline = ind_list

    print_plot(plot)


def get_inside_object_colour(colour_list, colour):
    print("Colour_list: ", colour_list)
    for i in colour_list:
        if i[0] == colour[0]:
            if i[1] == colour[1]:
                if i[2] == colour[2]:
                    pass
                else:
                    print("i: ", i)
                    return i
            else:
                print("i: ", i)
                return i
        else:
            print("i: ", i)
            return i


def inner_outline_start(image_copy, plot, new_colour, s_object):

    max_y, max_x = s_object.max_yx
    min_y, min_x = s_object.min_yx
    col = s_object.colour
    ob_id = s_object.object_id
    for y, row in enumerate(image_copy):
        for x, pixel in enumerate(row):
            p_x = plot[y, x]
            print("p_x: ", p_x)
            print("x: ", x)

            if x > max_x or x < min_x or y > max_y or y < min_y:
                pass

            else:
                n_pixel = row[x + 1]
                print("n_pixel: ", n_pixel)
                print("new_colour: ", new_colour)
                if pixel[0] == col[0]:
                    if pixel[1] == col[1]:
                        if pixel[2] == col[2]:
                            if new_colour is None:
                                pass
                            elif n_pixel[0] == new_colour[0]:
                                if n_pixel[1] == new_colour[1]:
                                    if n_pixel[2] == new_colour[2]:

                                        if p_x != ob_id and p_x+1 == 0:
                                            start_co = [y, x]
                                            return start_co


# new
def object_create():

    image = images[1]

    pixel_matrix = np.array(image)
    image_copy = pixel_matrix.copy()

    img_height = len(pixel_matrix)
    img_width = len(pixel_matrix[0])
    # Create plot of image
    row = [0]*img_width
    plot = np.array([row]*img_height)
    count = 0
    i = 1
    # find the first 0 in plot
    for y, row in enumerate(plot):
        for x, pixel in enumerate(row):

            pixel = plot[y, x]

            if pixel == 0:
                count += 1
                # ind_y = image_copy.index(y)
                # ind_x = image_copy.index(x)
                print("X: ", x)
                print("Y: ", y)
                c_colour = image_copy[y, x]
                print("Image: ", image_copy[y, x])
                print("C_Colour: ", c_colour)
                s_object = so.StitchObjects(c_colour, count, img_height, img_width)

                find_outline(image_copy, plot, s_object, 8, [0, 0])

                while i != 0:
                    colour_list = []
                    val = check_fill(image_copy, plot, s_object, colour_list)
                    print("Val: ", val)

                    if val == "fail":
                        pass
                    elif val:
                        find_fill(image_copy, plot, s_object)

                        break
                    else:
                        new_colour = get_inside_object_colour(colour_list, c_colour)
                        print("new_cooler: ", new_colour)
                        inner_pix = inner_outline_start(image_copy, plot, new_colour, s_object)

                        find_outline(image_copy, plot, s_object, 4, inner_pix)
                        # search for new_colour start
                        # use outline
                        print("Loop: ", i)
                        if i > 20:
                            break
                    i += 1

                objects.append(s_object)
                # save objects to list
                print("start")
                break
            else:
                print("done")
    print_plot(plot)


# new - used
def create_image_plot():

    image = images[1]
    pixel_matrix = np.array(image)
    image_copy = pixel_matrix.copy()

    img_height = len(pixel_matrix)
    img_width = len(pixel_matrix[0])
    # Create plot of image
    row = [0] * img_width
    plot = np.array([row] * img_height)
    count = 0
    i = 1
    pixel_list = []
    count_list = []
    combine_list = []
    # find the first 0 in plot
    count_colour(image_copy, pixel_list, count_list, combine_list)

    for y, row in enumerate(image_copy):
        for x, pixel in enumerate(row):

            for i in pixel_list:

                if i[0] == pixel[0]:
                    if i[1] == pixel[1]:
                        if i[2] == pixel[2]:
                            ind = pixel_list.index(i)
                            ind += 1
                            plot[y, x] = ind
    print_plot(plot)
    test = 0

    main_plot = po.Plot(plot)
    main_plot.set_num_list(pixel_list)
    main_plot.create_sub_plot()
    main_plot.print_col_matrix_list()

    if test == 0:
        col_obj_list = main_plot.col_matrix_list
        count = 1

        for i in col_obj_list:
            print("count: {}".format(count))
            col_obj = i

            col_obj.process_colour_plot(main_plot.matrix)

            col_obj.create_object_sub_plot()

            for j in col_obj.ob_matrix_list:
                col_sub_obj = j

                col_sub_obj.process_matrix()
                col_sub_obj.create_pathing_lists()

                out_image = create_section_image(col_sub_obj.matrix, images[1])
                col_sub_obj.section_image = out_image

                objects.append(col_sub_obj)

            count += 1

            count = 1
        for ob in objects:
            ob.ob_id = count
            count +=1

    if test == 1:

        col_obj = main_plot.col_matrix_list[0]

        col_obj.process_colour_plot(main_plot.matrix)
        col_obj.create_object_sub_plot()
        # col_obj.print_ob_matrix_list()

        col_sub_obj = col_obj.ob_matrix_list[0]
        po.print_plot(col_sub_obj.ref_plot)

        # not needed?
        # col_sub_obj.process_colour_plot(main_plot.matrix)
        po.print_plot_advanced(col_sub_obj.ref_plot)

        # not needed?
        # col_sub_obj.create_pathing_lists()
        # col_sub_obj.print_ob_part_list()
        col_sub_obj.running_stitch_fill()
        # col_sub_obj.fill_stitch_fill()

        po.stitch_test(col_sub_obj.matrix, col_sub_obj.ob_run_fill)
        out_image = create_section_image(col_sub_obj.matrix, images[1])
        col_sub_obj.section_image = out_image
        images[1] = out_image
        display_cy_image()
        # add image to object
    id = 1

    for i in objects:

        matrix = i.matrix
        stitch_list = []
        stitch_list.append(i.ob_outline)
        stitch_list.append(i.ob_run_fill)
        stitch_list.append(i.ob_fill_all)

        for j in stitch_list:
            if count == 0:
                print("Object {} Outline".format(id))
            elif count == 1:
                print("Object {} "
                      "Running Fill")
            elif count == 2:
                print("Full fill")
            po.stitch_test(matrix, j)
            if count < 2:
                count += 1

        id += 1
        # po.print_plot(matrix)
    stitch_type_pop()

# new
def image_object():
    image = images[1]

    pixel_matrix = np.array(image)
    image_copy = pixel_matrix.copy()
    c_colour = image_copy[0, 0]
    img_height = len(pixel_matrix)
    img_width = len(pixel_matrix[0])
    # Create plot of image
    row = [0] * img_width
    plot = np.array([row] * img_height)
    count = 0
    i = 1

    s_object = so.StitchObjects(c_colour, count, img_height, img_width)

    find_outline(image_copy, plot, s_object, 8, [0, 0])


# new
def image_object1():
    image = images[1]
    pixel_matrix = np.array(image)
    image_copy = pixel_matrix.copy()
    col_num_list = []
    col_val_list = []
    row = [0]*len(pixel_matrix[0])
    plot = np.array([row]*len(pixel_matrix))
    ind_list = []
    plot_check_val = True
    c_x = 0
    c_y = 0
    x = 0
    y = 0
    last_pix = 8
    count = 1
    c_colour = image_copy[y, x]
    i = 0
    a = 0
    while plot_check_val:

        # One
        if last_pix == 8:

            if y - 1 >= 0 and x - 1 >= 0:

                new_pix = image_copy[y - 1, x - 1]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:

                            pix_a = image_copy[y, x-1]
                            pix_b = image_copy[y-1, x]

                            if pix_a[0] == c_colour[0]:
                                if pix_a[1] == c_colour[1]:
                                    if pix_a[2] == c_colour[2]:
                                        comp_a = True
                                    else:
                                        comp_a = False
                                else:
                                    comp_a = False
                            else:
                                comp_a = False

                            if pix_b[0] == c_colour[0]:
                                if pix_b[1] == c_colour[1]:
                                    if pix_b[2] == c_colour[2]:
                                        comp_b = True
                                    else:
                                        comp_b = False
                                else:
                                    comp_b = False
                            else:
                                comp_b = False

                            if comp_a or comp_b:
                                y = y - 1
                                x = x - 1
                                plot[y, x] = count
                                a = check_index_list(ind_list, y, x)

                                if a == 0:
                                    ind_list.append((y, x))
                                    last_pix = 5
                                else:
                                    break

            if last_pix != 5:
                last_pix = 1

        # Two
        elif last_pix == 1:

            if y - 1 >= 0:

                new_pix = image_copy[y - 1, x]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:
                            y = y - 1
                            plot[y, x] = count

                            a = check_index_list(ind_list, y, x)

                            if a == 0:
                                ind_list.append((y, x))
                                last_pix = 6
                            else:
                                break

            if last_pix != 6:
                last_pix = 2

        # Three
        elif last_pix == 2:

            if y - 1 >= 0 and x + 1 < len(image_copy[0]):

                new_pix = image_copy[y - 1, x + 1]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:

                            pix_a = image_copy[y, x + 1]
                            pix_b = image_copy[y - 1, x]

                            if pix_a[0] == c_colour[0]:
                                if pix_a[1] == c_colour[1]:
                                    if pix_a[2] == c_colour[2]:
                                        comp_a = True
                                    else:
                                        comp_a = False
                                else:
                                    comp_a = False
                            else:
                                comp_a = False

                            if pix_b[0] == c_colour[0]:
                                if pix_b[1] == c_colour[1]:
                                    if pix_b[2] == c_colour[2]:
                                        comp_b = True
                                    else:
                                        comp_b = False
                                else:
                                    comp_b = False
                            else:
                                comp_b = False

                            if comp_a or comp_b:
                                y = y - 1
                                x = x + 1
                                plot[y, x] = count
                                a = check_index_list(ind_list, y, x)

                                if a == 0:
                                    ind_list.append((y, x))
                                    last_pix = 7
                                else:
                                    break

            if last_pix != 7:
                last_pix = 3

        # Four
        elif last_pix == 3:

            if x + 1 < len(image_copy[0]):

                new_pix = image_copy[y, x + 1]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:

                            x = x + 1
                            plot[y, x] = count
                            a = check_index_list(ind_list, y, x)

                            if a == 0:
                                ind_list.append((y, x))
                                last_pix = 8
                            else:
                                break

            if last_pix != 8:
                last_pix = 4

        # Five
        elif last_pix == 4:

            if y + 1 < len(image_copy) and x + 1 < len(image_copy[0]):

                new_pix = image_copy[y + 1, x + 1]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:

                            pix_a = image_copy[y, x + 1]
                            pix_b = image_copy[y + 1, x]

                            if pix_a[0] == c_colour[0]:
                                if pix_a[1] == c_colour[1]:
                                    if pix_a[2] == c_colour[2]:
                                        comp_a = True
                                    else:
                                        comp_a = False
                                else:
                                    comp_a = False
                            else:
                                comp_a = False

                            if pix_b[0] == c_colour[0]:
                                if pix_b[1] == c_colour[1]:
                                    if pix_b[2] == c_colour[2]:
                                        comp_b = True
                                    else:
                                        comp_b = False
                                else:
                                    comp_b = False
                            else:
                                comp_b = False

                            if comp_a or comp_b:
                                y = y + 1
                                x = x + 1
                                plot[y, x] = count
                                a = check_index_list(ind_list, y, x)

                                if a == 0:
                                    ind_list.append((y, x))
                                    last_pix = 1
                                else:
                                    break

            if last_pix != 1:
                last_pix = 5

        # Six
        elif last_pix == 5:

            if y + 1 < len(image_copy):

                new_pix = image_copy[y + 1, x]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:
                            y = y + 1

                            plot[y, x] = count
                            a = check_index_list(ind_list, y, x)

                            if a == 0:
                                ind_list.append((y, x))
                                last_pix = 2
                            else:
                                break

            if last_pix != 2:
                last_pix = 6

        # Seven
        elif last_pix == 6:

            if y + 1 < len(image_copy) and x - 1 >= 0:

                new_pix = image_copy[y + 1, x - 1]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:

                            pix_a = image_copy[y, x - 1]
                            pix_b = image_copy[y + 1, x]

                            if pix_a[0] == c_colour[0]:
                                if pix_a[1] == c_colour[1]:
                                    if pix_a[2] == c_colour[2]:
                                        comp_a = True
                                    else:
                                        comp_a = False
                                else:
                                    comp_a = False
                            else:
                                comp_a = False

                            if pix_b[0] == c_colour[0]:
                                if pix_b[1] == c_colour[1]:
                                    if pix_b[2] == c_colour[2]:
                                        comp_b = True
                                    else:
                                        comp_b = False
                                else:
                                    comp_b = False
                            else:
                                comp_b = False

                            if comp_a or comp_b:
                                y = y + 1
                                x = x - 1
                                plot[y, x] = count
                                a = check_index_list(ind_list, y, x)

                                if a == 0:
                                    ind_list.append((y, x))
                                    last_pix = 3
                                else:
                                    break

            if last_pix != 3:
                last_pix = 7

        # Eight
        elif last_pix == 7:

            if x - 1 >= 0:

                new_pix = image_copy[y, x - 1]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:

                            x = x - 1
                            plot[y, x] = count
                            a = check_index_list(ind_list, y, x)

                            if a == 0:
                                ind_list.append((y, x))
                                last_pix = 4
                            else:
                                break

            if last_pix != 4:
                last_pix = 8

        i += 1

    print_plot(plot)


# used for testing image processing
def auto_load():
    file_path = "C:/Users/Joshu/Desktop/Project C/Index.jpg"
    og_img = Image.open(file_path)
    cy_img = og_img
    global loaded_image
    loaded_image = og_img

    length = len(images)

    if length == 0:
        images.append(og_img)
        images.append(cy_img)
    else:
        images[0] = og_img
        images[1] = cy_img

    display_og_image()
    display_cy_image()


def stitch_type_pop():
    global pop
    global section_image_list
    section_image_list = []
    checkbox_list = []
    stitch_drop_list = []
    len_drop_list = []
    order_drop_list = []

    length = len(objects)
    pop = Toplevel(second_frame)
    pop.title("Colour Sample")
    pop_geometry(700, 50 + 35 * length)
    count_list = []
    pop_frame1 = Frame(pop)
    pop_frame1.pack()
    count = 1

    pop_label_1 = Label(pop_frame1, text='Object ID')
    pop_label_1.grid(row=0, column=0, padx=5, pady=5)
    pop_label_1 = Label(pop_frame1, text='Colour')
    pop_label_1.grid(row=0, column=1, padx=5)
    pop_label_1 = Label(pop_frame1, text='Stitch Type')
    pop_label_1.grid(row=0, column=2, padx=5)
    pop_label_1 = Label(pop_frame1, text='Max Stitch Length')
    pop_label_1.grid(row=0, column=3, padx=5)
    pop_label_1 = Label(pop_frame1, text='Order')
    pop_label_1.grid(row=0, column=4, padx=5)
    pop_label_1 = Label(pop_frame1, text='Remove Object')
    pop_label_1.grid(row=0, column=5, padx=5)
    pop_label_1 = Label(pop_frame1, text='Highlight')
    pop_label_1.grid(row=0, column=6, padx=5)
    len_count = 0

    for ob in objects:

        # object ID = if not set then set, then display
        ob_id = ob.ob_id
        pop_label_1 = Label(pop_frame1, text=ob_id)
        pop_label_1.grid(row=count, column=0, padx=5)

        # object colour = get then display
        col = ob.colour
        hex_col = rgb_to_hex(col)
        pop_label_1 = Label(pop_frame1, width=5, bg=hex_col)
        pop_label_1.grid(row=count, column=1, padx=5, pady=5)

        # stitch type drop down = create
        select = StringVar()
        select.set("Stitch Outline")
        stitch_drop = OptionMenu(pop_frame1, select, "Stitch Outline", "Running Stitch Fill", "Fill Stitch")
        stitch_drop.config(width=18)
        stitch_drop.grid(row=count, column=2,  padx=5)
        stitch_drop_list.append(select)

        # max stitch len dropdown = create
        lengths = ["0.3mm", "0.5mm", "1.0mm", "1.2mm", "1.5mm", "2.0mm", "2.5mm", "3.0mm", "3.5mm", "4.0mm", "4.5mm",
                   "5.0mm"]
        stitch_len = StringVar()
        stitch_len.set("0.3mm")
        len_drop = OptionMenu(pop_frame1, stitch_len, *lengths)
        len_drop.config(width=5)
        len_drop.grid(row=count, column=3, padx=5)
        len_drop_list.append(stitch_len)

        # stitch order  = set then display
        object_count = []
        for i in enumerate(objects):
            object_count.append(i[0]+1)

        order = IntVar()
        order.set(count)
        order_drop = OptionMenu(pop_frame1, order, *object_count)
        order_drop.config(width=5)
        order_drop.grid(row=count, column=4, padx=5)
        order_drop_list.append(order)

        # remove
        checked = IntVar()
        checkbox = Checkbutton(pop_frame1, variable=checked)
        checkbox.grid(row=count, column=5, padx=5)
        checkbox_list.append(checked)

        # display section image
        section_image_list.append(ob.section_image)
        var = str(count - 1)
        print(var)
        # exec("display_section_image(section_image_list[" + var + "])")
        exec("pop_button = Button(pop_frame1, text='Display', command=lambda: display_section_image(section_image_list["
             +"" + var + "]))\npop_button.grid(row=count, column=6, padx=5)")
        count += 1

    for i in range(length + 1):
        count_list.append(len_count)
        len_count += 1

    hi = 0
    if hi == 23:

        for pixel in pixel_list:

            ind = pixel_list.index(pixel)
            index = "index_" + str(count - 1)
            index_list.append(index)

            exec(index + ".set(0)")

            hex_colour = rgb_to_hex(pixel)

            pop_label = Label(pop_frame1, text=count)
            pop_label.grid(row=count, column=0)

            colour_label = Label(pop_frame1, width=20, bg=hex_colour)
            colour_label.grid(row=count, pady=5, column=1)

            pix_count = colour_count[ind]

            per = pix_count / total_pix
            per = per * 100
            per_text = "{:.1f}%".format(per)
            per_label = Label(pop_frame1, text=per_text)
            per_label.grid(row=count, column=2, padx=10)

            exec("drop = OptionMenu(pop_frame1," + index + ", *count_list)")
            exec("drop.grid(row=count, column=3)")

            count += 1

    pop_button = Button(pop_frame1, text="OK", command=lambda: [pop.destroy()])
    pop_button.grid(row=count + 1, column=4, pady=10, columnspan=2)
    pop_button = Button(pop_frame1, text="Print", command=lambda: [print_lists(stitch_drop_list, len_drop_list, checkbox_list, order_drop_list)])
    pop_button.grid(row=count + 1, column=3, pady=10, )
    pop_button = Button(pop_frame1, text="Back", command=lambda: [pop.destroy()])
    pop_button.grid(row=count + 1, column=1, pady=10, columnspan=2)


def print_lists(a, b, c, d):
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
    print("Delete Y/N")
    print(c_str)
    print("Order Change")
    print(d_str)


def display_section_image(image):
    images[1] = image
    display_cy_image()


def rgb_to_hex(pixel):
    test = 0

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


def colour_select_pop():
    global pop
    global floor_choice
    global lock
    global custom
    floor_choice = IntVar()
    lock = IntVar()
    custom = IntVar()

    pop = Toplevel(second_frame)
    pop.title("Colour Sample")
    pop_geometry(300, 220)

    pop_frame1 = Frame(pop)
    pop_frame1.pack()
    pop_label_1 = Label(pop_frame1, text='Select the number of Colours:')
    pop_label_1.grid(row=0, column=0, columnspan=4)
    pop_label_2 = Label(pop_frame1, text='1000')
    pop_label_2.grid(row=1, column=0)
    pop_label_3 = Label(pop_frame1, text='729')
    pop_label_3.grid(row=2, column=0)
    pop_label_4 = Label(pop_frame1, text='512')
    pop_label_4.grid(row=3, column=0)
    pop_label_5 = Label(pop_frame1, text='343')
    pop_label_5.grid(row=4, column=0)
    pop_label_6 = Label(pop_frame1, text='216')
    pop_label_6.grid(row=5, column=0)
    pop_label_7 = Label(pop_frame1, text='125')
    pop_label_7.grid(row=1, column=2)
    pop_label_8 = Label(pop_frame1, text='64')
    pop_label_8.grid(row=2, column=2)
    pop_label_9 = Label(pop_frame1, text='27')
    pop_label_9.grid(row=3, column=2)
    pop_label_10 = Label(pop_frame1, text='8')
    pop_label_10.grid(row=4, column=2)
    pop_label_11 = Label(pop_frame1, text='1')
    pop_label_11.grid(row=5, column=2)

    # ** Pre-run alg before pop-up **
    # ** Colour button must run auto_colour_step()
    # ** - Runs colour_display(floor_choice)
    r_button_1 = Radiobutton(pop_frame1, variable=floor_choice, value=1, command=lambda: [colour_display(floor_choice)])
    r_button_1.grid(row=1, column=1, padx=10)
    r_button_2 = Radiobutton(pop_frame1, variable=floor_choice, value=2, command=lambda: [colour_display(floor_choice)])
    r_button_2.grid(row=2, column=1)
    r_button_3 = Radiobutton(pop_frame1, variable=floor_choice, value=3, command=lambda: [colour_display(floor_choice)])
    r_button_3.grid(row=3, column=1)
    r_button_4 = Radiobutton(pop_frame1, variable=floor_choice, value=4, command=lambda: [colour_display(floor_choice)])
    r_button_4.grid(row=4, column=1)
    r_button_5 = Radiobutton(pop_frame1, variable=floor_choice, value=5, command=lambda: [colour_display(floor_choice)])
    r_button_5.grid(row=5, column=1)
    r_button_6 = Radiobutton(pop_frame1, variable=floor_choice, value=6, command=lambda: [colour_display(floor_choice)])
    r_button_6.grid(row=1, column=3)
    r_button_7 = Radiobutton(pop_frame1, variable=floor_choice, value=7, command=lambda: [colour_display(floor_choice)])
    r_button_7.grid(row=2, column=3)
    r_button_8 = Radiobutton(pop_frame1, variable=floor_choice, value=8, command=lambda: [colour_display(floor_choice)])
    r_button_8.grid(row=3, column=3)
    r_button_9 = Radiobutton(pop_frame1, variable=floor_choice, value=9, command=lambda: [colour_display(floor_choice)])
    r_button_9.grid(row=4, column=3)
    r_button_10 = Radiobutton(pop_frame1, variable=floor_choice, value=10, command=lambda: [colour_display(floor_choice)])
    r_button_10.grid(row=5, column=3)

    pop_button = Button(pop_frame1, text="OK", command=lambda: [set_colour_change(floor_choice.get()), stats(), pop.destroy()])  # pop.destory
    pop_button.grid(row=8, column=3, pady=10)
    pop_button = Button(pop_frame1, text="Back", command=lambda: [pop.destroy()])
    pop_button.grid(row=8, column=0, pady=10)


def manuel_merge_pop():
    global pop
    image = images[1]
    pixel_matrix = np.array(image)
    y_len = len(pixel_matrix)
    x_len = len(pixel_matrix[0])
    total_pix = y_len * x_len
    pixel_list = []
    colour_count = []
    combine_count = []
    index_0 = IntVar()
    index_1 = IntVar()
    index_2 = IntVar()
    index_3 = IntVar()
    index_4 = IntVar()
    index_5 = IntVar()
    index_6 = IntVar()
    index_7 = IntVar()
    index_8 = IntVar()
    index_9 = IntVar()
    index_10 = IntVar()
    index_11 = IntVar()
    index_12 = IntVar()
    index_13 = IntVar()
    index_14 = IntVar()
    index_15 = IntVar()
    index_16 = IntVar()
    index_17 = IntVar()
    index_18 = IntVar()
    index_19 = IntVar()
    index_20 = IntVar()
    index_0.set(21)
    index_1.set(21)
    index_2.set(21)
    index_3.set(21)
    index_4.set(21)
    index_5.set(21)
    index_6.set(21)
    index_7.set(21)
    index_8.set(21)
    index_9.set(21)
    index_10.set(21)
    index_11.set(21)
    index_12.set(21)
    index_13.set(21)
    index_14.set(21)
    index_15.set(21)
    index_16.set(21)
    index_17.set(21)
    index_18.set(21)
    index_19.set(21)
    index_20.set(21)
    count_colour(pixel_matrix, pixel_list, colour_count, combine_count)
    length = len(pixel_list)
    pop = Toplevel(second_frame)
    pop.title("Colour Sample")
    pop_geometry(300, 50+35*length)
    count_list = []
    pop_frame1 = Frame(pop)
    pop_frame1.pack()
    count = 1
    index_list = []
    pop_label_1 = Label(pop_frame1, text='Colour Num')
    pop_label_1.grid(row=0, column=0, padx=5)
    pop_label_1 = Label(pop_frame1, text='Colour')
    pop_label_1.grid(row=0, column=1, padx=5)
    pop_label_1 = Label(pop_frame1, text='% of Image:')
    pop_label_1.grid(row=0, column=2, padx=5)
    len_count = 0

    for i in range(length + 1):
        count_list.append(len_count)
        len_count += 1

    for pixel in pixel_list:

        ind = pixel_list.index(pixel)
        index = "index_" + str(count - 1)
        index_list.append(index)

        exec(index + ".set(0)")

        hex_colour = rgb_to_hex(pixel)

        pop_label = Label(pop_frame1, text=count)
        pop_label.grid(row=count, column=0)

        colour_label = Label(pop_frame1, width=5, bg=hex_colour)
        colour_label.grid(row=count, column=1)

        pix_count = colour_count[ind]

        per = pix_count / total_pix
        per = per * 100
        per_text = "{:.1f}%".format(per)
        per_label = Label(pop_frame1, text=per_text)
        per_label.grid(row=count, column=2, padx=10)

        exec("drop = OptionMenu(pop_frame1," + index + ", *count_list)")
        exec("drop.grid(row=count, column=3)")

        count += 1

    pop_button = Button(pop_frame1, text="OK", command=lambda: [get_man_merge_vals(index_0.get(), index_1.get(),
                                                                                   index_2.get(), index_3.get(),
                                                                                   index_4.get(), index_5.get(),
                                                                                   index_6.get(), index_7.get(),
                                                                                   index_8.get(), index_9.get(),
                                                                                   index_10.get(), index_11.get(),
                                                                                   index_12.get(), index_13.get(),
                                                                                   index_14.get(), index_15.get(),
                                                                                   index_16.get(), index_17.get(),
                                                                                   index_18.get(), index_19.get(),
                                                                                   index_20.get(), pixel_list), pop.destroy()])
    pop_button.grid(row=count+1, column=2, pady=10, columnspan=2)
    pop_button = Button(pop_frame1, text="Back", command=lambda: [pop.destroy()])
    pop_button.grid(row=count+1, column=0, pady=10, columnspan=2)


def get_man_merge_vals(index_0, index_1, index_2, index_3, index_4, index_5, index_6, index_7, index_8, index_9,
                       index_10, index_11, index_12, index_13, index_14, index_15, index_16, index_17, index_18,
                       index_19, index_20, pixel_list):  # , val_list):
    image = images[1]
    pixel_matrix = np.array(image)
    index_list = []
    val_list = []
    pixel_change = []
    new_pixel_list = []

    count = 1

    for i in range(21):
        index = "index_" + str(count - 1)
        # print(index)
        index_list.append(index)
        # print(index_list)
        count += 1

    for i in range(20):
        j = index_list[i - 1]
        exec("if " + j + " != 21:\n\tval_list.append(" + j + ")")

    print(val_list)

    for val in val_list:

        if val != 0:
            val_index = val_list.index(val)
            change_ind = val - 1
            pixel_change.append(pixel_list[change_ind])
            new_pixel_list.append(pixel_list[val_index])

    print(pixel_list)
    print(new_pixel_list)
    print(pixel_change)

    image_copy = set_new_pixel_colour(new_pixel_list, pixel_change)

    images[1] = Image.fromarray(image_copy, "RGB")
    display_cy_image()


def set_new_pixel_colour(new_pixel_list, pixel_change):
    image = images[1]
    pixel_matrix = np.array(image)
    image_copy = pixel_matrix.copy()

    for y, row in enumerate(pixel_matrix):
        # print("Y: ", y)
        for x, pixel in enumerate(row):
            # print("(Y,X): ", y, ",", x)

            # count the number of times a pixel appears

            for i in new_pixel_list:

                if i[0] == pixel[0]:
                    if i[1] == pixel[1]:
                        if i[2] == pixel[2]:
                            index = new_pixel_list.index(i)

                            image_copy[y, x] = pixel_change[index]

    return image_copy


def check_delete(deleted_list, pixel):
    value = 0
    for i in deleted_list:

        if i[0] == pixel[0]:
            if i[1] == pixel[1]:
                if i[2] == pixel[2]:

                    value = 1
                    break

    if value == 1:
        return True
    else:
        return False


def get_down_right_pixel(pixel_matrix, y, x, deleted_list):

    pixel_list = []
    change = 0
    count = 0
    while change == 0:

        if count > 10:
            print("stuck in a loop on: ", y + 1, ",", x + 1, " Val :", pixel_matrix[y, x])
            break

        ny = y + 1
        while ny < len(pixel_matrix):

            new_pix = pixel_matrix[ny, x]

            if new_pix[0] == 0 and new_pix[1] == 0 and new_pix[2] == 0:
                break

            val = check_delete(deleted_list, new_pix)

            if val:
                ny += 1
            else:
                pixel_list.append(new_pix)
                break

        if len(pixel_list) > 0:
            change += 1
            break

        nx = x + 1
        while nx < len(pixel_matrix[0]):

            new_pix = pixel_matrix[y, nx]

            if new_pix[0] == 0 and new_pix[1] == 0 and new_pix[2] == 0:
                break

            val = check_delete(deleted_list, new_pix)

            if val:
                nx += 1
            else:
                pixel_list.append(new_pix)
                break

        if len(pixel_list) > 0:
            change += 1
            break

        ny = y - 1
        while ny >= 0:

            new_pix = pixel_matrix[ny, x]

            if new_pix[0] == 0 and new_pix[1] == 0 and new_pix[2] == 0:
                break

            val = check_delete(deleted_list, new_pix)

            if val:
                ny -= 1
            else:
                pixel_list.append(new_pix)
                break

        if len(pixel_list) > 0:
            change += 1
            break

        nx = x - 1
        while nx >= 0:

            new_pix = pixel_matrix[y, nx]

            if new_pix[0] == 0 and new_pix[1] == 0 and new_pix[2] == 0:
                break

            val = check_delete(deleted_list, new_pix)

            if val:
                nx -= 1
            else:
                pixel_list.append(new_pix)
                break

        if len(pixel_list) > 0:
            change += 1
            break
        count += 1

    if not pixel_list:
        pixel = (0, 0, 0)
        return pixel
    else:
        return pixel_list[0]


def get_liner_pixel(pixel_matrix, y, x, deleted_list):
    row_num = len(pixel_matrix)
    col_num = len(pixel_matrix[0])
    pixels = []
    m = 0
    pixel_list = []
    count = 0
    option = 1
# get N E S W pixels that are valid and not black

    while option != 5:
        bool_val = False
        if count > 3:
            option = 5
            count = 0
            print("stuck in a loop on: ", y + 1, ",", x + 1, " Val :", pixel_matrix[y, x])

        if len(pixel_list) > 0:
            option = 5
            break

        if option == 1:

            nx = x - 1
            while nx >= 0:

                new_pix = pixel_matrix[y, nx]

                if new_pix[0] == 0 and new_pix[1] == 0 and new_pix[2] == 0:
                    option = 2
                    break

                bool_val = check_delete(deleted_list, new_pix)

                if bool_val:
                    nx -= 1
                else:
                    pixel_list.append(new_pix)
                    option = 2
                    break

        if option == 2:

            ny = y - 1
            while ny >= 0:

                new_pix = pixel_matrix[ny, x]

                if new_pix[0] == 0 and new_pix[1] == 0 and new_pix[2] == 0:
                    option = 3
                    break

                bool_val = check_delete(deleted_list, new_pix)

                if bool_val:
                    ny -= 1
                else:
                    pixel_list.append(new_pix)
                    option = 3
                    break

        if option == 3:

            nx = x + 1
            while nx < len(pixel_matrix[0]):

                new_pix = pixel_matrix[y, nx]

                if new_pix[0] == 0 and new_pix[1] == 0 and new_pix[2] == 0:
                    option = 4
                    break

                bool_val = check_delete(deleted_list, new_pix)

                if bool_val:
                    nx += 1
                else:
                    pixel_list.append(new_pix)
                    option = 4
                    break

        if option == 4:

            ny = y + 1
            # print("ny:", ny, "pixel: ", pix, "new pixel: ", new_pix, "option: ", option)
            while ny < len(pixel_matrix):

                new_pix = pixel_matrix[ny, x]

                if new_pix[0] == 0 and new_pix[1] == 0 and new_pix[2] == 0:
                    option = 5
                    break

                bool_val = check_delete(deleted_list, new_pix)

                if bool_val:
                    ny += 1
                else:
                    pixel_list.append(new_pix)
                    option = 5
                    break

        count += 1  # ##### this needs checked to make sure the loop breaks

    if len(pixel_list) == 0:
        pixel = (0, 255, 50)

        print("black")
        return pixel

    else:
        colour_count = []
        count_list = []
        z = 0
        for e in pixel_list:

            if len(count_list) == 0:

                count_list.append(list(e))
                colour_count.append(1)

            count = 0
            for i in count_list:

                if i[0] == e[0]:
                    if i[1] == e[1]:
                        if i[2] == e[2]:
                            index = count_list.index(i)

                            ind = index

                            colour_count[ind] += 1
                        else:
                            count += 1
                    else:
                        count += 1
                else:
                    count += 1

                if count >= len(count_list):
                    count_list.append(list(e))
                    colour_count.append(1)
                    break
            z += 1
            # print(z)

        pick = max(colour_count)
        ind = colour_count.index(pick)
        # print("Pixel: ", count_list[ind])
        return count_list[ind]


def get_surrounding_pixels(pixel_matrix, y, x):
    row_num = len(pixel_matrix)
    col_num = len(pixel_matrix[0])
    pixels = []
    a = y - 1
    b = y + 1
    c = x - 1
    d = x + 1

    if y > 0:
        pixels.append(pixel_matrix[a, x])
        if x > 0:
            pixels.append(pixel_matrix[a, c])
        if x < col_num - 1:
            pixels.append(pixel_matrix[a, d])
    if y < row_num - 1:
        pixels.append(pixel_matrix[b, x])
        if x > 0:
            pixels.append(pixel_matrix[b, c])
        if x < col_num - 1:
            pixels.append(pixel_matrix[b, d])
    if x > 0:
        pixels.append(pixel_matrix[y, c])
    if x < col_num - 1:
        pixels.append(pixel_matrix[y, d])
    return pixels


def get_surrounding_pixels_5x5(pixel_matrix, y, x):
    row_num = len(pixel_matrix)
    col_num = len(pixel_matrix[0])
    pixels = []
    a = y - 2
    b = y + 2
    c = x - 2
    d = x + 2
    e = y - 1
    f = y + 1
    g = x - 1
    h = x + 1

    if y > 1:
        pixels.append(pixel_matrix[a, x])
        if x > 1:
            pixels.append(pixel_matrix[a, c])
            pixels.append(pixel_matrix[a, g])
            pixels.append(pixel_matrix[e, c])
        if x < col_num - 2:
            pixels.append(pixel_matrix[a, d])
            pixels.append(pixel_matrix[a, h])
            pixels.append(pixel_matrix[e, d])
    if y < row_num - 2:
        pixels.append(pixel_matrix[b, x])
        if x > 1:
            pixels.append(pixel_matrix[b, c])
            pixels.append(pixel_matrix[b, g])
            pixels.append(pixel_matrix[f, c])
        if x < col_num - 2:
            pixels.append(pixel_matrix[b, d])
            pixels.append(pixel_matrix[b, h])
            pixels.append(pixel_matrix[f, d])
    if x > 0:
        pixels.append(pixel_matrix[y, c])
    if x < col_num - 2:
        pixels.append(pixel_matrix[y, d])
    return pixels


def janome_colours():
    janome_colour_list = [(0, 0, 0), (0, 181, 82), (101, 194, 200), (11, 47, 132), (110, 57, 55), (112, 169, 226),
                          (12, 137, 24), (127, 194, 28), (132, 49, 84), (136, 155, 155), (151, 5, 51), (152, 214, 189),
                          (152, 243, 254), (156, 100, 69), (160, 184, 204), (163, 145, 102), (167, 108, 61),
                          (168, 0, 67), (171, 90, 150), (172, 156, 199), (178, 225, 227), (180, 90, 48),
                          (181, 148, 116), (195, 0, 126), (196, 227, 157), (198, 238, 203), (199, 151, 50),
                          (2, 87, 181), (20, 50, 156), (204, 153, 0), (208, 186, 176), (215, 189, 164), (22, 95, 167),
                          (226, 161, 136), (227, 190, 129), (228, 195, 93), (229, 229, 229), (230, 101, 30),
                          (230, 150, 90), (238, 113, 175), (240, 156, 150), (240, 240, 240), (245, 219, 139),
                          (246, 105, 160), (247, 242, 151), (249, 153, 183), (250, 179, 129), (252, 241, 33),
                          (253, 51, 163), (253, 245, 181), (255, 0, 0), (255, 102, 0), (255, 157, 0), (255, 204, 0),
                          (255, 187, 187), (255, 255, 220), (255, 189, 227), (255, 255, 23), (255, 71, 32),
                          (255, 9, 39), (255, 90, 39), (255, 96, 72), (255, 186, 94), (29, 84, 120), (35, 115, 54),
                          (4, 145, 123), (47, 89, 51), (6, 72, 13), (7, 22, 80), (72, 26, 5), (76, 181, 143),
                          (84, 5, 113), (89, 91, 97), (91, 210, 181), (92, 38, 37), (96, 148, 24),  (96, 133, 65),
                          (98, 49, 189)]

    image = images[1]
    pixel_matrix = np.array(image)
    image_copy = pixel_matrix.copy()
    pixel_list = []

    colour_count = []
    combine_count = []
    count_colour(pixel_matrix, pixel_list, colour_count, combine_count)
    change_pix = [0] * len(pixel_list)

    for i in pixel_list:

        diff_list = get_colour_diff(janome_colour_list, i)

        min_dif = min(diff_list)
        ind = diff_list.index(min_dif)
        pix_ind = pixel_list.index(i)

        change_pix[pix_ind] = janome_colour_list[ind]
        image_copy = set_new_pixel_colour(pixel_list, change_pix)

    images[1] = Image.fromarray(image_copy, "RGB")
    display_cy_image()


def get_colour_diff(pixels, pixel):
    dif_val = []
    dif_list = []

    for i in pixels:
        a = 0
        dif = [0, 0, 0]
        if i[0] == pixel[0] and i[1] == pixel[1] and i[2] == pixel[2]:
            # dif = (1000, 1000, 1000)
            dif = (0, 0, 0)
        else:
            while a < 3:
                if i[a] == pixel[a]:
                    dif[a] = 0
                elif i[a] > pixel[a]:
                    p = pixel[a]
                    o_p = i[a]
                    dif[a] = o_p - p
                elif i[a] < pixel[a]:
                    p = pixel[a]
                    o_p = i[a]
                    dif[a] = p - o_p

                a += 1
        dif_list.append(dif)

    for i in dif_list:
        dif_val.append(i[0] + i[1] + i[2])

    return dif_val

#not used
def background_detect():  # not finished
    pixel_list = []
    colour_count = []
    combine_count = []
    image = images[1]
    pixel_matrix = np.array(image)
    image_copy = pixel_matrix.copy()
    width = len(pixel_matrix[0])
    height = len(pixel_matrix)

    t_l = image_copy[0, 0]
    t_r = image_copy[0, width-1]
    b_l = image_copy[height-1, 0]
    b_r = image_copy[height-1, width-1]

    corners = [t_l, t_r, b_l, b_r]

    count_colour_list(corners, pixel_list, colour_count, combine_count)

    max_val = max(colour_count)
    ind = colour_count.index(max_val)
    bg_colour = pixel_list[ind]


def count_colour(pixel_matrix, pixel_list, colour_count, combine_count):

    for y, row in enumerate(pixel_matrix):
        # print("Y: ", y)
        for x, pix in enumerate(row):
            # print("(Y,X): ", y, ",", x)

            # count the number of times a pixel appears
            if len(pixel_list) == 0:
                pixel_list.append(list(pix))
                colour_count.append(1)
                combine_count.append(int(pix[0]) + int(pix[1]) + int(pix[2]))
            else:
                count = 0
                for i in pixel_list:

                    if i[0] == pix[0]:
                        if i[1] == pix[1]:
                            if i[2] == pix[2]:
                                index = pixel_list.index(i)

                                ind = index

                                colour_count[ind] += 1
                            else:
                                count += 1
                        else:
                            count += 1
                    else:
                        count += 1

                    if count >= len(pixel_list):
                        pixel_list.append(list(pix))
                        colour_count.append(1)
                        combine_count.append(int(pix[0]) + int(pix[1]) + int(pix[2]))
                        break

    # print list of all individual colours

    e = 1
    for x in pixel_list:
        comb = combine_count[e - 1]
        num = colour_count[e - 1]
        print("Colour ", e, " Value: ", x," Comb Val:", comb, " Amount: ", num,)
        e += 1
    # return pixel_list


def count_colour_list(pixels, pixel_list, colour_count, combine_count):

    for x, pix in enumerate(pixels):
        # print("(Y,X): ", y, ",", x)

        # count the number of times a pixel appears
        if len(pixel_list) == 0:
            pixel_list.append(list(pix))
            colour_count.append(1)
            val = int(pix[0]) + int(pix[1]) + int(pix[2])
            combine_count.append(val)
        else:
            count = 0
            for i in pixel_list:

                if i[0] == pix[0]:
                    if i[1] == pix[1]:
                        if i[2] == pix[2]:
                            index = pixel_list.index(i)

                            ind = index

                            colour_count[ind] += 1
                        else:
                            count += 1
                    else:
                        count += 1
                else:
                    count += 1

                if count >= len(pixel_list):
                    pixel_list.append(list(pix))
                    colour_count.append(1)
                    val = int(pix[0]) + int(pix[1]) + int(pix[2])
                    combine_count.append(val)
                    break


def sort_algorithm(pixel_list, combine_value, colour_count):

    for i in range(len(combine_value)-1):
        min_index = i

        for j in range(i+1, len(combine_value)):

            if combine_value[j] < combine_value[min_index]:
                min_index = j

        combine_value[i], combine_value[min_index] = combine_value[min_index], combine_value[i]
        pixel_list[i], pixel_list[min_index] = pixel_list[min_index], pixel_list[i]
        colour_count[i], colour_count[min_index] = colour_count[min_index], colour_count[i]


def stats():

    image = images[1]
    pixel_matrix = np.array(image)
    image_copy = pixel_matrix
    pixel_list = []
    colour_count = []
    av_count = 0
    combine_count = []
    total_pix = len(pixel_matrix) * len(pixel_matrix[0])

    count_colour(pixel_matrix, pixel_list, colour_count, combine_count)

    sort_algorithm(pixel_list, combine_count, colour_count)
    avg = total_pix / len(colour_count)

    for x in colour_count:
        if x > avg:
            av_count += 1

    e = 1
    for x in pixel_list:
        comb = combine_count[e - 1]
        num = colour_count[e - 1]
        print("Colour ", e, " Value: ", x, " Comb Val:", comb, " Amount: ", num, )
        e += 1
    po = 0

    print("Total Pixel Count: ", total_pix)
    print("Total Height: ", len(pixel_matrix),"\nTotal Length: ", len(pixel_matrix[0]))
    print("Number of colours > Average Pixel count: ", av_count, " Average: ", av_count)
    # print("Maxsize: ", po.maxsize )


def delete_list():

    global pix
    print("image merge")

    if len(images) == 2:
        print("yup")

        image = images[1]
        pixel_matrix = np.array(image)
        image_copy = pixel_matrix
        delete_colour = []
        pixel_list = []
        colour_count = []

        for y, row in enumerate(pixel_matrix):
            for x, pix in enumerate(row):
                print("(Y,X): ", y, ",", x)

                # count the number of times a pixel appears
                if len(pixel_list) == 0:
                    pixel_list.append(list(pix))
                    colour_count.append(1)
                else:
                    count = 0
                    for i in pixel_list:

                        if i[0] == pix[0]:
                            if i[1] == pix[1]:
                                if i[2] == pix[2]:
                                    index = pixel_list.index(i)

                                    ind = index

                                    colour_count[ind] += 1
                                else:
                                    count += 1
                            else:
                                count += 1
                        else:
                            count += 1

                        if count >= len(pixel_list):
                            pixel_list.append(list(pix))
                            colour_count.append(1)
                            break

        # print list of all individual colours

        e = 1
        for x in pixel_list:
            num = colour_count[e - 1]
            print("Colour ", e, " Value: ", x, " Amount: ", num, )
            e += 1

        # make a list of the colours that appear the least
        # make into a percentage formula
        # value = len(pixel_matrix) * len(pixel_matrix[0]) / colour
        value = 2000
        index_list = []
        for i in colour_count:
            if i <= value:
                index = colour_count.index(i)
                delete_colour.append(pixel_list[index])
                index_list.append(index)

        print(delete_colour)


def pix_restrict(): # og first different colour

    global pix
    print("image merge")

    if len(images) == 2:
        print("yup")

        image = images[1]
        pixel_matrix = np.array(image)
        image_copy = pixel_matrix
        delete_colour = []
        pixel_list = []
        colour_count = []

        for y, row in enumerate(pixel_matrix):
            for x, pix in enumerate(row):
               # print("(Y,X): ", y, ",", x)

# count the number of times a pixel appears
                if len(pixel_list) == 0:
                    pixel_list.append(list(pix))
                    colour_count.append(1)
                else:
                    count = 0
                    for i in pixel_list:

                        if i[0] == pix[0]:
                            if i[1] == pix[1]:
                                if i[2] == pix[2]:
                                    index = pixel_list.index(i)

                                    ind = index

                                    colour_count[ind] += 1
                                else:
                                    count += 1
                            else:
                                count += 1
                        else:
                            count += 1

                        if count >= len(pixel_list):
                            pixel_list.append(list(pix))
                            colour_count.append(1)
                            break


# print list of all individual colours

        e = 1
        for x in pixel_list:
            num = colour_count[e-1]
            print("Colour ", e, " Value: ", x, " Amount: ", num,)
            e += 1

# make a list of the colours that appear the least
        # make into a percentage formula
        # value = len(pixel_matrix) * len(pixel_matrix[0]) / colour
        value = 2000
        index_list = []
        for i in colour_count:
            if i <= value:
                index = colour_count.index(i)
                delete_colour.append(pixel_list[index])
                index_list.append(index)

# for each pixel in image
        colour_count.clear()
        pixel_list.clear()

        pic = 0
        for y, row in enumerate(pixel_matrix):
            for x, pix in enumerate(row):
                # pic += 1
                # print("Pixel Count: ", pic)
# check pixel against the delete list
                # if it needs to be deleted get surrounding pixels
                d = 0
                for i in delete_colour:
                    if i[0] == pix[0]:
                        if i[1] == pix[1]:
                            if i[2] == pix[2]:
                                pix = get_liner_pixel(pixel_matrix, y, x, delete_colour)

                   # print("delete it: ", d)

                    image_copy[y, x] = pix

# print pixel list
#         j = 1
#         for x in pixel_list:
#             num = colour_count[j - 1]
#             print("Colour ", j, " Value: ", x, " Amount: ", num)
#             j += 1
        print("making image")
        images[1] = Image.fromarray(image_copy, "RGB")
        display_cy_image()
    else:
        print("Error: Pix_change failed")


def pix_change():
    global pix
    colour_count = []
    count_list = []

    if len(images) == 2:

        image = images[1]
        pixel_matrix = np.array(image)
        image_copy = pixel_matrix.copy()
        row_num = len(pixel_matrix)
        col_num = len(pixel_matrix[0])
        pixels = []

        for y, row in enumerate(pixel_matrix):
            for x, pix in enumerate(row):
                # print("X: ", x, "Pixel Matrix Height: ", len(pixel_matrix[0]))

                pixels = get_surrounding_pixels(pixel_matrix, y, x)
                pixel_list = []
                count_colour_list(pixels, pixel_list, colour_count, count_list)

                if len(pixel_list) == 1:

                    image_copy[y, x] = pixels[0]

        for y, row in enumerate(pixel_matrix):
            for x, pix in enumerate(row):
                # print("X: ", x, "Pixel Matrix Height: ", len(pixel_matrix[0]))

                pixels = get_surrounding_pixels_5x5(pixel_matrix, y, x)
                pixel_list = []
                count_colour_list(pixels, pixel_list, colour_count, count_list)
                a = y - 1
                b = y + 1
                c = x - 1
                d = x + 1
                if len(pixel_list) == 1:

                    if y > 0:
                        image_copy[a, x] = pixels[0]
                        if x > 0:
                            image_copy[a, c] = pixels[0]
                        if x < col_num - 1:
                            image_copy[a, d] = pixels[0]
                    if y < row_num - 1:
                        image_copy[b, x] = pixels[0]
                        if x > 0:
                            image_copy[b, c] = pixels[0]
                        if x < col_num - 1:
                            image_copy[b, c] = pixels[0]
                    if x > 0:
                        image_copy[y, c] = pixels[0]
                    if x < col_num - 1:
                        image_copy[y, d] = pixels[0]

        images[1] = Image.fromarray(image_copy, "RGB")
        display_cy_image()
    else:
        print("Error: Pix_change failed")


def floor_step(pixel, floors):

    max_val = 2**8 - 1
    coarseness = max_val / floors

    return [coarseness * np.floor(val / coarseness) for val in pixel]


# ** Working **
def auto_colour_step():
    temp_images.clear()
    levels = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    if len(images) == 2:
        global pix
        pix = (0, 0, 0)
        for x in levels:
            floors = x
            image = images[1]

            pixel_matrix = np.array(image)
            image_copy = pixel_matrix.copy()

            for i, row in enumerate(pixel_matrix):

                for j, pix in enumerate(row):

                    if len(pix) == 4:
                        r, g, b, t = pix
                        pix = (r, g, b)

                    if pix[0] > 230 and pix[1] > 230 and pix[2] > 230:  # Near white equals white
                        pix = (255, 255, 255)
                    pix = list(pix)
                    comb_val = int(pix[0]) + int(pix[1]) + int(pix[2])
                    pix_val = 0
                    if pix[0] < 70:

                        if pix[1] < 70:

                            if pix[2] < 70:
                                pix_val = 1

                    val = 160
                    if comb_val < val and pix_val == 1:  # Near white equals white
                        pix = (0, 0, 0)

                    image_copy[i, j] = floor_step(pix, floors)

            temp = Image.fromarray(image_copy, "RGB")
            temp_images.append(temp)
            print("Image: ", x)

        print("**Finished Process**")
        colour_select_pop()
    else:
        print("failed to run")


def colour_display(option):
    if 0 < option.get() < 11:
        img = temp_images[option.get()-1]
        display_image(img)
    else:
        print("Error: Colour Display function")


def set_colour_change(option):
    images[1] = temp_images[option - 1]
    display_cy_image()


def process_1_colour_selection():
    image = images[1]
    print("image colour mode: ", image.mode)

    # change colour mode
    grey = image.convert("L")

    # edge detection
    edge = image.filter(ImageFilter.FIND_EDGES)

    # update cy_img in list
    images[1] = grey
    images[1] = edge

    # display cy_img from list
    display_cy_image()


def undo_hoop_choice():
    length = len(images)
    if length > 0:
        images[0] = loaded_image
        images[1] = loaded_image
        display_cy_image()
        display_og_image()
    else:
        print("no image selected")


def image_resize(hoop_size, option, new_w, new_h):
    # Message box
    image = images[0]
    img_w, img_h = image.size
    px = 3.77
    new_w = float(new_w) * px
    new_h = float(new_h) * px
    new_w = int(new_w)
    new_h = int(new_h)

    if option == 1:

        if hoop_size == 1:
            print('4x4" hoop')
            set_w = 415
            set_h = 415
        elif hoop_size == 2:
            print('2x2" hoop')
            set_w = 188
            set_h = 188
        elif hoop_size == 3:
            print('5.5x8" hoop')
            set_w = 529
            set_h = 756
        elif hoop_size == 4:
            print('5x4" hoop')
            set_w = 476
            set_h = 415
        elif hoop_size == 5:
            print('8x8" hoop')
            set_w = 756
            set_h = 756
        else:
            set_w = 1
            set_h = 1

        if img_w > w:
            x = img_w / w
            temp_h = img_h / x
            img_h = int(temp_h)
            img_w = int(w)

        if img_h > h:
            x = img_h / h
            temp_w = img_w / x
            img_w = int(temp_w)
            img_h = int(h)

    elif option == 2:
        # new_w = float(new_w) * px
        # new_h = float(new_h) * px
        # new_w = int(new_w)
        # new_h = int(new_h)
        img_w = new_w
        img_h = new_h

    elif option == 3:
        # new_w = float(new_w) * px
        # new_w = int(new_w)
        x = img_w / new_w
        temp_h = img_h / x
        img_h = int(temp_h)
        img_w = int(new_w)

    elif option == 4:
        # new_h = float(new_h) * px
        # new_h = int(new_h)
        x = img_h / new_h
        temp_w = img_w / x
        img_w = int(temp_w)
        img_h = int(new_h)

    image = image.resize((int(img_w), int(img_h)), Image.ANTIALIAS)
    images[0] = image
    images[1] = image

    display_og_image()
    display_cy_image()


# not used
def auto_size(size_option):
    # Message box
    print("resize ", size_option)
    image = images[0]
    img_w, img_h = image.size

    if size_option == 1:
        print('4x4" hoop')
        set_w = 415
        set_h = 415
    elif size_option == 2:
        print('2x2" hoop')
        set_w = 188
        set_h = 188
    elif size_option == 3:
        print('5.5x8" hoop')
        set_w = 529
        set_h = 756
    elif size_option == 4:
        print('5x4" hoop')
        set_w = 476
        set_h = 415
    elif size_option == 5:
        print('8x8" hoop')
        set_w = 756
        set_h = 756
    else:
        set_w = 1
        set_h = 1

    if img_w > set_w:
        x = img_w / set_w
        temp_h = img_h / x
        img_h = int(temp_h)
        img_w = int(set_w)

    if img_h > set_h:
        x = img_h / set_h
        temp_w = img_w / x
        img_w = int(temp_w)
        img_h = int(set_h)

    image = image.resize((img_w, img_h), Image.ANTIALIAS)
    images[0] = image
    images[1] = image

    display_og_image()
    display_cy_image()


def create_section_image(ref_plot, image):
    test = 0
    ref_plot = ref_plot.copy()
    image_array = np.array(image)
    grey_image = image.convert('LA')
    n_g_image = np.array(grey_image)
    # print_plot(n_g_image)
    # p_row = [0] * len(ref_plot[0])
    # g_image = np.array([p_row] * len(ref_plot))
    g_image = image_array.copy()
    print("REFPLOT")
    po.print_plot(ref_plot)

    for y, row in enumerate(n_g_image):
        for x, pixel in enumerate(row):

            val, null = pixel

            if test == 1:
                print("Value: {} Null: {}".format(val, null))

            if val == 255:
                val = val - 50
            elif val == 0:
                val = val + 70

            tup = (val, val, val)
            g_image[y, x] = tup
            if test == 1:
                print("pixel value: {} RBG Pixel:{}".format(pixel, g_image[y, x]))

    for y, row in enumerate(ref_plot):

        for x, point in enumerate(row):
            # print(point.dtype)
            if point == 1:
                # print(" point == 1")

                points, yx_points = po.get_surrounding_points_5x5(ref_plot, y, x)

                for i, val in enumerate(points):
                    # ind = points.index(i)

                    if val == 1:
                        g_image[y, x] = image_array[y, x]

                    # edge highlight not working yet
                    # elif val == 2:
                    #     pass
                    # else:
                    #     y, x = yx_points[i]
                    #     # ref_plot[y, x] = 2
                    #     g_image[y, x] = (216, 0, 255)

    out_image = Image.fromarray(g_image, "RGB")
    # print_plot(g_image)
    # print_plot(image_array)
    return out_image

    #     if x + 1 < len(ref_plot):
    #         if ref_plot[y, x + 1] == "1":
    #             # highlight colour
    #             pass
    #
    #     if x + 2 < len(ref_plot):
    #         if ref_plot[y, x + 2] == "1":
    #             pass
    #
    #     if x + 3 < len(ref_plot):
    #         if ref_plot[y, x + 3] == "1":
    #             pass
    #
    #
    #     # greyscale
    #     pass
    #
    # elif point == "1":
    #     pass


def display_image(image):
    global img
    img = ImageTk.PhotoImage(image)
    cy_label.config(image=img)
    print("Display image")


def display_cy_image():
    global cy_display
    global cy_label
    cy_display = ImageTk.PhotoImage(images[1])
    cy_label.config(image=cy_display)
    print("Display cy image")


def display_og_image():
    global og_display
    global og_label
    og_display = ImageTk.PhotoImage(images[0])
    og_label.config(image=og_display)
    print("Display og image")


# Load Image from file function
def load_image():
    file_path = filedialog.askopenfilename()
# !!!!! exception needs handled
    print(file_path)
    og_img = Image.open(file_path)
    cy_img = og_img
    global loaded_image
    loaded_image = og_img
    undo.clear()
    undo.append(og_img)
    length = len(images)

    if length == 0:
        images.append(og_img)
        images.append(cy_img)
    else:
        images[0] = og_img
        images[1] = cy_img

    display_og_image()
    display_cy_image()


# class GuiWindow:
#
#     def __init__(self, name):
#         # list
#         # from PIL.ImageTk import PhotoImage
#         self.name = name
#         self.loaded_image = ""
#         self.images = []
#         self.undo = []
#         self.temp_images = []
#         self.objects = []
#         # filepath
#         # og_img
#         self.global og_display
#         self.global cy_display
#         self.global average_pixel_count
#
#     def gui_window(self):
root = tk.Tk()
root.title("Pic-to-Stitch")
# Open in full screen
root.wm_state("zoomed")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
# global centre_width
# global centre_height
centre_width = screen_width/2
centre_height = screen_height/2
# ** Main Menu **
menu = Menu(root)
root.config(menu=menu)
sub_menu = Menu(menu)
menu.add_cascade(label="File", menu=sub_menu)
sub_menu.add_command(label="New Project...", command=image_object)
sub_menu.add_command(label="Open Project...", command=delete_list)
sub_menu.add_separator()
sub_menu.add_command(label="Exit")
edit_menu = Menu(menu)
menu.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Redo", command=redo)

# ** Toolbar **
toolbar = Frame(root)
insert_button = Button(toolbar, text="Insert Image", command=you_sure)
insert_button.pack(side=LEFT, padx=2, pady=2)
print_button = Button(toolbar, text="Size", command=hoop_size_select)
print_button.pack(side=LEFT, padx=2, pady=2)
image_button = Button(toolbar, text="Denoise", command=pix_change)
image_button.pack(side=LEFT, padx=2, pady=2)
process1_button = Button(toolbar, text="Colour", command=auto_colour_step)
process1_button.pack(side=LEFT, padx=2, pady=2)
process2_button = Button(toolbar, text="Edges", command=process_1_colour_selection)
process2_button.pack(side=LEFT, padx=2, pady=2)
process3_button = Button(toolbar, text="Colour Merge", command=pix_restrict)
process3_button.pack(side=LEFT, padx=2, pady=2)
process4_button = Button(toolbar, text="Image Stats", command=stats)
process4_button.pack(side=LEFT, padx=2, pady=2)
process5_button = Button(toolbar, text="Manuel Merge", command=manuel_merge_pop)
process5_button.pack(side=LEFT, padx=2, pady=2)
process6_button = Button(toolbar, text="Jan Colour", command=janome_colours)
process6_button.pack(side=LEFT, padx=2, pady=2)
process7_button = Button(toolbar, text="Create Plot", command=create_image_plot)
process7_button.pack(side=LEFT, padx=2, pady=2)
process8_button = Button(toolbar, text="Manuel Merge", command=manuel_merge_pop)
process8_button.pack(side=LEFT, padx=2, pady=2)
process9_button = Button(toolbar, text="Jan Colour", command=janome_colours)
process9_button.pack(side=LEFT, padx=2, pady=2)
toolbar.pack(side=TOP, fill=X)

# Main Frame
main_pane = Frame(root)
main_pane.pack(fill=BOTH, expand=1)

# Scrollbar - Canvas within main frame
main_canvas = Canvas(main_pane)
main_canvas.pack(side=LEFT, fill=BOTH, expand=1)

# Scrollbar - scroll bar
scroll_bar = tk.Scrollbar(main_pane, orient=VERTICAL, command=main_canvas.yview)
scroll_bar.pack(side=RIGHT, fill=Y)

# Scrollbar - config Canvas
main_canvas.configure(yscrollcommand=scroll_bar.set)
main_canvas.bind("<Configure>", lambda e: main_canvas.configure(scrollregion=main_canvas.bbox("all")))

# Scrollbar - frame 2
second_frame = Frame(main_canvas, padx=20, pady=20)

# Scrollbar - new window
main_canvas.create_window((0, 0), window=second_frame, anchor="nw")

og_image_frame = Frame(second_frame)
og_image_frame.pack(side=LEFT, padx=2, pady=2)
og_label = Label(og_image_frame)
og_label.pack(side=LEFT)

cy_image_frame = Frame(second_frame)
cy_image_frame.pack(side=RIGHT, padx=2, pady=2)
cy_label = Label(cy_image_frame)
cy_label.pack(side=LEFT)

# ** Status Bar **
status = Label(root, text="Preparing to do nothing...", bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

root.mainloop()


# if __name__ == '__main__':
#     gui_window()
