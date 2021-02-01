import tkinter as tk
from tkinter import filedialog
from tkinter import *
# from tkinter.ttk import *
from tkinter import ttk
from PIL import Image, ImageTk, ImageChops, ImageFilter
import tkinter.messagebox
import numpy as np

# list
# from PIL.ImageTk import PhotoImage
loaded_image = ""
images = []
undo = []
temp_images = []
# filepath
# og_img
global og_display
global cy_display


def temp_folder():
    print("check for or create temp folder to store temp files")


def save_folder():
    print("check for or create save folder to save project images")


def do_nothing():
    print("C1 W1 H1 A0 - Custom size Squish")


def open_project():
    print("What another project?! Not again")


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
    pop_geometry(300, 200)

    pop_frame1 = Frame(pop)
    pop_frame1.pack()
    pop_label_1 = Label(pop_frame1, text='Select a Hoop Size:')
    pop_label_1.grid(row=0, column=0, padx=20, pady=10)
    pop_label_2 = Label(pop_frame1, text='4"x4" Hoop (101x101mm)')
    pop_label_2.grid(row=1, column=0)
    pop_label_3 = Label(pop_frame1, text='5"x7" Hoop (127x177mm)')
    pop_label_3.grid(row=2, column=0)
    pop_label_4 = Label(pop_frame1, text='6"x10" Hoop (152x254mm)')
    pop_label_4.grid(row=3, column=0)
    r_button_1 = Radiobutton(pop_frame1, variable=hoop_choice, value=1)
    r_button_1.grid(row=1, column=1)
    r_button_2 = Radiobutton(pop_frame1, variable=hoop_choice, value=2)
    r_button_2.grid(row=2, column=1)
    r_button_3 = Radiobutton(pop_frame1, variable=hoop_choice, value=3)
    r_button_3.grid(row=3, column=1)

    # separator = ttk.Separator(pop_frame1, orient='horizontal')
    # separator.place(relx=0, rely=0.4, relwidth=1, relheight=1)
    custom = IntVar()
    custom_check = Checkbutton(pop_frame1, variable=custom, command=custom_option)
    custom_check.grid(row=4, column=1)
    pop_label_7 = Label(pop_frame1, text="Custom size:")
    pop_label_7.grid(row=4, column=0)

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
            hoop_width = 101
            hoop_height = 101

        elif hoopchoice == 2:
            hoop_width = 127
            hoop_height = 177

        elif hoopchoice == 3:
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
                raise ValueError3
                go = 0
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
        pop_geometry(300, 270)

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


def colour_select_pop():
    global pop
    global floor_choice
    global lock
    global custom
    floor_choice = IntVar()
    lock = IntVar()
    custom = IntVar()

    pop = Toplevel(second_frame)
    pop.title("Colour Simp")
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

    # ** Run Alg every click **
    # r_button_1 = Radiobutton(pop_frame1, variable=floor_choice, value=1, command=lambda: [colour_step(floor_choice)])
    # r_button_1.grid(row=1, column=1, padx=10)
    # r_button_2 = Radiobutton(pop_frame1, variable=floor_choice, value=2, command=lambda: [colour_step(floor_choice)])
    # r_button_2.grid(row=2, column=1)
    # r_button_3 = Radiobutton(pop_frame1, variable=floor_choice, value=3, command=lambda: [colour_step(floor_choice)])
    # r_button_3.grid(row=3, column=1)
    # r_button_4 = Radiobutton(pop_frame1, variable=floor_choice, value=4, command=lambda: [colour_step(floor_choice)])
    # r_button_4.grid(row=4, column=1)
    # r_button_5 = Radiobutton(pop_frame1, variable=floor_choice, value=5, command=lambda: [colour_step(floor_choice)])
    # r_button_5.grid(row=5, column=1)
    # r_button_6 = Radiobutton(pop_frame1, variable=floor_choice, value=6, command=lambda: [colour_step(floor_choice)])
    # r_button_6.grid(row=1, column=3)
    # r_button_7 = Radiobutton(pop_frame1, variable=floor_choice, value=7, command=lambda: [colour_step(floor_choice)])
    # r_button_7.grid(row=2, column=3)
    # r_button_8 = Radiobutton(pop_frame1, variable=floor_choice, value=8, command=lambda: [colour_step(floor_choice)])
    # r_button_8.grid(row=3, column=3)
    # r_button_9 = Radiobutton(pop_frame1, variable=floor_choice, value=9, command=lambda: [colour_step(floor_choice)])
    # r_button_9.grid(row=4, column=3)
    # r_button_10 = Radiobutton(pop_frame1, variable=floor_choice, value=10, command=lambda: [colour_display(floor_choice)])
    # r_button_10.grid(row=5, column=3)

    pop_button = Button(pop_frame1, text="OK", command=lambda: [set_colour_change(floor_choice.get()), pop.destroy()])  # pop.destory
    pop_button.grid(row=8, column=3, pady=10)
    pop_button = Button(pop_frame1, text="Back", command=lambda: [pop.destroy()])
    pop_button.grid(row=8, column=0, pady=10)


def get_liner_pixel(pixel_matrix, y, x, deleted_list):
    row_num = len(pixel_matrix)
    col_num = len(pixel_matrix[0])
    pixels = []
    m = 0
    pixel_list = []

    option = 0

    while option != 5:

        if option == 1:

            nx = x - 1
            while x >= 0:
                found = 0
                new_pix = pixel_matrix[y, nx]

                if new_pix == (255, 255, 255):
                    option = 2
                    break

                for i in deleted_list:
                    if i[0] == new_pix[0]:
                        if i[1] == new_pix[1]:
                            if i[2] == new_pix[2]:
                                nx -= 1
                                found += 1

                if found == 0:
                    pixel_list.append(new_pix)
                    option = 2
                    break

        if option == 2:

            ny = y - 1
            while y >= 0:
                found = 0
                new_pix = pixel_matrix[ny, x]

                if new_pix == (255, 255, 255):
                    option = 3
                    break

                for i in deleted_list:
                    if i[0] == new_pix[0]:
                        if i[1] == new_pix[1]:
                            if i[2] == new_pix[2]:
                                ny -= 1
                                found += 1

                if found == 0:
                    pixel_list.append(new_pix)
                    option = 3
                    break

        if option == 3:

            nx = x + 1
            while x < len(pixel_matrix[0]):
                found = 0
                new_pix = pixel_matrix[y, nx]

                if new_pix == (255, 255, 255):
                    option = 4
                    break

                for i in deleted_list:
                    if i[0] == new_pix[0]:
                        if i[1] == new_pix[1]:
                            if i[2] == new_pix[2]:
                                nx += 1
                                found += 1

                if found == 0:
                    pixel_list.append(new_pix)
                    option = 4
                    break

        if option == 4:

            ny = y + 1
            while y < len(pixel_matrix):
                found = 0
                new_pix = pixel_matrix[ny, x]

                if new_pix == (255, 255, 255):
                    option = 5
                    break

                for i in deleted_list:
                    if i[0] == new_pix[0]:
                        if i[1] == new_pix[1]:
                            if i[2] == new_pix[2]:
                                ny += 1
                                found += 1

                if found == 0:
                    pixel_list.append(new_pix)
                    option = 5
                    break

    if len(pixel_list) == 0:
        pixel_matrix[y, x] = (255, 255, 255)

    else:
        colour_count = []
        count_list = []
        for e in pixel_list:

            if len(count_list) == 0:

                count_list.append(list(e))
                colour_count.append(1)
            count = 0
            for i in count_list:

                if i[0] == e[0]:
                    if i[1] == e[1]:
                        if i[2] == pix[2]:
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
        pick = max(colour_count)
        ind = colour_count.index(pick)
        pixel_matrix[y, x] = count_list[ind]

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


def get_colour_diff(pixels, pix):
    dif_val = []
    dif_list = []

    for i in pixels:
        a = 0
        dif = [0, 0, 0]
        if i[0] == pix[0] and i[1] == pix[1] and i[2] == pix[2]:
            # dif = (1000, 1000, 1000)
            dif = (0, 0, 0)
        else:
            while a < 3:
                if i[a] == pix[a]:
                    dif[a] = 0
                elif i[a] > pix[a]:
                    p = pix[a]
                    o_p = i[a]
                    dif[a] = o_p - p
                elif i[a] < pix[a]:
                    p = pix[a]
                    o_p = i[a]
                    dif[a] = p - o_p

                a += 1
        dif_list.append(dif)

    for i in dif_list:
        dif_val.append(i[0] + i[1] + i[2])


    return dif_val


def count_colour(pixel_matrix, pixel_list, colour_count, combine_count):


    for y, row in enumerate(pixel_matrix):
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

# def selection_sort(L):
#     # i indicates how many items were sorted
#     for i in range(len(L)-1):
#         # To find the minimum value of the unsorted segment
#         # We first assume that the first element is the lowest
#         min_index = i
#         # We then use j to loop through the remaining elements
#         for j in range(i+1, len(L)-1):
#             # Update the min_index if the element at j is lower than it
#             if L[j] < L[min_index]:
#                 min_index = j
#         # After finding the lowest item of the unsorted regions, swap with the first unsorted item
#         L[i], L[min_index] = L[min_index], L[i]


def sort_algorithm(pixel_list, combine_value, colour_count):

    for i in range(len(combine_value)-1):
        min_index = i

        for j in range(i+1, len(combine_value)):

            if combine_value[j] < combine_value[min_index]:
                min_index = j

        combine_value[i], combine_value[min_index] = combine_value[min_index], combine_value[i]
        pixel_list[i], pixel_list[min_index] = pixel_list[min_index], pixel_list[i]
        colour_count[i], colour_count[min_index] = colour_count[min_index], colour_count[i]


# def darkest_pixel(pixel_matrix, pixel_list):
#
#     count_colour(pixel_matrix, pixel_list)

    # sort

def stats():

    image = images[1]
    pixel_matrix = np.array(image)
    image_copy = pixel_matrix
    pixel_list = []
    colour_count = []

    combine_count = []

    count_colour(pixel_matrix, pixel_list, colour_count, combine_count)

    sort_algorithm(pixel_list, combine_count, colour_count)

    e = 1
    for x in pixel_list:
        comb = combine_count[e - 1]
        num = colour_count[e - 1]
        print("Colour ", e, " Value: ", x, " Comb Val:", comb, " Amount: ", num, )
        e += 1

    total_pix = len(pixel_matrix) * len(pixel_matrix[0])
    print("Total Pixel Count: ", total_pix)


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
        for y, row in enumerate(pixel_matrix):
            for x, pix in enumerate(row):

# check pixel against the delete list
                # if it needs to be deleted get surrounding pixels
                for i in delete_colour:
                    if i[0] == pix[0]:
                        if i[1] == pix[1]:
                            if i[2] == pix[2]:
                                pixels = get_surrounding_pixels(pixel_matrix, y, x)

# for each surrounding pixel, check it against the delete list
                                # if it is on the list it is removed from surrounding pixel list
                                count = 0
                                for l in pixels:

                                    for m in delete_colour:
                                        if l[0] == m[0]:
                                            if l[1] == m[1]:
                                                if l[2] == m[2]:
                                                    # index = pixels.index(np.logical_and(l))
                                                    del pixels[count]
                                                    break
                                    count += 1

# get the differences of the remaining surrounding pixel values
                                dif_val = get_colour_diff(pixels, pix)

                                n = 0
# find the colour with the least differences and change pix to that
#                                 try:
#                                     min_index = dif_val.index(min(dif_val))
#                                     # print("Min_dif: ", min(dif_val), "Index: ", min_index)
#                                     # print(dif_val)
#                                     pix = pixels[min_index]
#                                 except Exception(ValueError):
#                                     n += 1
#                                     print(str(n) + " got away!")
                                for s in dif_val:
                                    if s > 0:
                                        pix = pixels[dif_val.index(s)]

    # for w in delete_colour:
    #     if pix[0] == w[0]:
    #
    #         if pix[1] == w[1]:
    #
    #             if pix[2] == w[2]:
    #
    #                del pixels[min_index]

# set pixel in image
                    image_copy[y, x] = pix

# print pixel list
        j = 1
        for x in pixel_list:
            num = colour_count[j - 1]
            print("Colour ", j, " Value: ", x, " Amount: ", num)
            j += 1

        images[1] = Image.fromarray(image_copy, "RGB")
        display_cy_image()
    else:
        print("Error: Pix_change failed")


# def pix_restrict(): # OG FUZZY EDGES
#
#     global pix
#     print("image merge")
#
#     if len(images) == 2:
#         print("yup")
#
#         image = images[1]
#         pixel_matrix = np.array(image)
#         image_copy = pixel_matrix
#         delete_colour = []
#         pixel_list = []
#         colour_count = []
#         combine_count = []
#
#         count_colour(pixel_matrix, pixel_list, colour_count, combine_count)
#
#
# # make a list of the colours that appear the least
#         # make into a percentage formula
#         value = 3000
#         index_list = []
#         for i in colour_count:
#             if i <= value:
#                 index = colour_count.index(i)
#                 delete_colour.append(pixel_list[index])
#                 index_list.append(index)
#
# # for each pixel in image
#         for y, row in enumerate(pixel_matrix):
#             for x, pix in enumerate(row):
#
# # check pixel against the delete list
#                 # if it needs to be deleted get surrounding pixels
#                 for i in delete_colour:
#                     if i[0] == pix[0]:
#                         if i[1] == pix[1]:
#                             if i[2] == pix[2]:
#                                 pixels = get_surrounding_pixels(pixel_matrix, y, x)
#
# # for each surrounding pixel, check it against the delete list
#                                 # if it is on the list it is removed from surrounding pixel list
#                                 count = 0
#                                 for l in pixels:
#
#                                     for m in delete_colour:
#                                         if l[0] == m[0]:
#                                             if l[1] == m[1]:
#                                                 if l[2] == m[2]:
#                                                     # index = pixels.index(np.logical_and(l))
#                                                     del pixels[count]
#                                                     break
#                                     count += 1
#
# # get the differences of the remaining surrounding pixel values
#                                 dif_val = get_colour_diff(pixels, pix)
#                                 n = 0
#
# # find the colour with the least differences and change pix to that
#                                 try:
#                                     min_index = dif_val.index(min(dif_val))
#                                     # print("Min_dif: ", min(dif_val), "Index: ", min_index)
#                                     # print(dif_val)
#                                     pix = pixels[min_index]
#                                 except Exception(ValueError):
#                                     n += 1
#                                     print(str(n) + " got away!")
#
#     # for w in delete_colour:
#     #     if pix[0] == w[0]:
#     #
#     #         if pix[1] == w[1]:
#     #
#     #             if pix[2] == w[2]:
#     #
#     #                del pixels[min_index]
#
# # set pixel in image
#                     image_copy[y, x] = pix
#
# # print pixel list
# #         j = 1
# #         for x in pixel_list:
# #             num = colour_count[j - 1]
# #             print("Colour ", j, " Value: ", x, " Amount: ", num)
# #             j += 1
#
#         images[1] = Image.fromarray(image_copy, "RGB")
#         display_cy_image()
#     else:
#         print("Error: Pix_change failed")


def pix_change():
    global pix

    if len(images) == 2:

        image = images[1]
        pixel_matrix = np.array(image)
        image_copy = pixel_matrix.copy()

        for y, row in enumerate(pixel_matrix):
            for x, pix in enumerate(row):
                # print("X: ", x, "Pixel Matrix Height: ", len(pixel_matrix[0]))

                pixels = get_surrounding_pixels(pixel_matrix, y, x)

                dif_val = get_colour_diff(pixels, pix)

                try:
                    min_index = dif_val.index(min(dif_val))

                    pix = pixels[min_index]
                    image_copy[y, x] = pix

                except ValueError:
                    print("no need")

        images[1] = Image.fromarray(image_copy, "RGB")
        display_cy_image()
    else:
        print("Error: Pix_change failed")


def floor_step(pix, floors):

    MAX = 2**8 - 1
    coarseness = MAX / floors

    return [coarseness * np.floor(val / coarseness) for val in pix]


# not used
# def colour_step(floor_choice):
#     levels = [70, 63, 50, 42, 32, 21, 10, 5, 3, 2]
#     floor_choice = floor_choice.get()
#     print(type(floor_choice),"\n Value: ", floor_choice)
#
#     if 0 < floor_choice < 11:
#         floors = levels[floor_choice-1]
#
#         image = images[0]
#         pixel_matrix = np.array(image) # .open()
#         image_copy = pixel_matrix.copy()
#         for i, row in enumerate(pixel_matrix):
#             for j, pix in enumerate(row):
#                 print("Pixel value: {}", format(pix))
#                 image_copy[i, j] = floor_step(pix, floors)
#                 print("New Pixel Value: {}", format(pix))
#
#             if not i % 100:
#                 print("Row Number {}", format(i))
#
#         images[1] = Image.fromarray(image_copy, "RGB")
#         display_cy_image()
#     else:
#         print(" no value was selected")

# ** Working **
def auto_colour_step():
    temp_images.clear()
    levels = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    if len(images) == 2:
        global pix
        pix = (0,0,0)
        for x in levels:
            # print("X: ", x)
            floors = x
            pixel_brightness = []
            image = images[1]

            pixel_matrix = np.array(image)
            image_copy = pixel_matrix.copy()
            # for i, row in enumerate(pixel_matrix):
            #     pixel = pix
            #     for j, pix in enumerate(row):
            #
            #        value = pix[0] + pix[1] + pix[2]
            #         print(value)
            #         pixel_brightness.append(value)
            #
            # darkest = min(pixel_brightness)

            for i, row in enumerate(pixel_matrix):
                pixel = pix
                for j, pix in enumerate(row):

                    if pix[0] > 230 and pix[1] > 230 and pix[2] > 230:  # Near white equals white
                        pix = (255, 255, 255)
                    pix = list(pix)
                    comb_val = int(pix[0]) + int(pix[1]) + int(pix[2])

                    if pix[0] < 80:
                        pix_val = 1
                    elif pix[1] < 80:
                        pix_val = 1
                    elif pix[2] < 80:
                        pix_val = 1
                    else:
                        pix_val = 0
                    val = 160
                    if comb_val < val and pix_val == 1:  # Near white equals white
                        pix = (0, 0, 0)

                    image_copy[i, j] = floor_step(pix, floors)




                # if not i % 100:
                #     print("Row Number {}", format(i))
                #     print("Pixel value: ", format(pixel))
                #     print("Pixel Value: ", format(pix))

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
            w = 400
            h = 400
        elif hoop_size == 2:
            print('5x7" hoop')
            w = 480
            h = 672
        elif hoop_size == 3:
            print('6x10" hoop')
            w = 576
            h = 960
        else:  # never used
            w = 1
            h = 1

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


def auto_size(size_option):
    # Message box
    print("resize ", size_option)
    image = images[0]
    img_w, img_h = image.size

    if size_option == 1:
        print('4x4" hoop')
        w = 400
        h = 400
    elif size_option == 2:
        print('5x7" hoop')
        w = 480
        h = 672
    elif size_option == 3:
        print('6x10" hoop')
        w = 576
        h = 960
    else:
        w = 1
        h = 1

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

    image = image.resize((img_w, img_h), Image.ANTIALIAS)
    images[0] = image
    images[1] = image

    display_og_image()
    display_cy_image()
            # Custom sizing option
    # see existing image size in mm
    # enter new image size in mm
    # size not to exceed Hoop size
    # w, h = image.size
    #
    # print("Width: ", w)
    # print("Height: ", h)

    # new_w =
    # new_h =

    # print("Resize image")
    # image.resize(newsize, Image.BICUBIC)


def dest(widget):
    widget.destroy()
    print("Destroy method called. Widget exists? = ", bool(widget.winfo_exists()))


def exist(widget):
    print("Checking for existance = ", bool(widget.winfo_exists()))


def display_image(image):
    global img
    img = ImageTk.PhotoImage(image)
    cy_label.config(image=img)
    print("Display image")


def display_cy_image():
    global cy_display
    cy_display = ImageTk.PhotoImage(images[1])
    cy_label.config(image=cy_display)
    print("Display cy image")


def display_og_image():
    global og_display
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

    length = len(images)

    if length == 0:
        images.append(og_img)
        images.append(cy_img)
    else:
        images[0] = og_img
        images[1] = cy_img

    display_og_image()
    display_cy_image()


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
subMenu = Menu(menu)
menu.add_cascade(label="File", menu=subMenu)
subMenu.add_command(label="New Project...", command=new_project)
subMenu.add_command(label="Open Project...", command=open_project)
subMenu.add_separator()
subMenu.add_command(label="Exit", command=exit_option)
editMenu = Menu(menu)
menu.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Redo", command=redo)

# ** Toolbar **
toolbar = Frame(root)
insertButton = Button(toolbar, text="Insert Image", command=you_sure)
insertButton.pack(side=LEFT, padx=2, pady=2)
printButton = Button(toolbar, text="Size", command=hoop_size_select)
printButton.pack(side=LEFT, padx=2, pady=2)
imageButton = Button(toolbar, text="Denoise", command=pix_change)
imageButton.pack(side=LEFT, padx=2, pady=2)
process1Button = Button(toolbar, text="Colour", command=auto_colour_step)
process1Button.pack(side=LEFT, padx=2, pady=2)
process2Button = Button(toolbar, text="Edges", command=process_1_colour_selection)
process2Button.pack(side=LEFT, padx=2, pady=2)
process3Button = Button(toolbar, text="Colour Merge", command=pix_restrict)
process3Button.pack(side=LEFT, padx=2, pady=2)
process4Button = Button(toolbar, text="IMage Stats", command=stats)
process4Button.pack(side=LEFT, padx=2, pady=2)
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


# #14 Draw and Delete
# root = Tk()
# canvas = Canvas(root, width=200, height=100)
# canvas.pack()
# blackLine = canvas.create_line(0, 0, 200, 50)
# redLine = canvas.create_line(0, 100, 200, 50, fill="red")
# greenBox = canvas.create_rectangle(25, 25, 130, 60, fill="green")
# canvas.delete(redLine)
# canvas.delete(ALL)

# #15 Image Display
# root = Tk()
# photo = PhotoImage(file="Fluffy.png")
# label = Label(root, image=photo)
# label.pack()


root.mainloop()
