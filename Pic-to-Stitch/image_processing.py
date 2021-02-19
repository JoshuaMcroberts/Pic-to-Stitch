import tkinter as tk
from tkinter import filedialog
from tkinter import *
# from tkinter.ttk import *
from PIL import Image, ImageTk, ImageFilter
import tkinter.messagebox
import numpy as np
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



class ValueError1(ValueError):
    pass


class ValueError2(ValueError):
    pass


class ValueError3(ValueError):
    pass

def print_plot(plot):
    height = len(plot)
    width = len(plot[0])

    for y in plot:
        print(y)
        # for x in plot:
        #
        #     print(x,)


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
def check_fill(image_copy, plot, s_object):
    col = s_object.object_id
    pixel_list = []
    colour_list = []
    colour_count = []
    combine_count = []
    state = 0

    max_y, max_x = s_object.max_yx
    min_y, min_x = s_object.min_yx

    for y in plot:
        end = 1
        for x in y:

            if x > max_x or x < min_x or y > max_y or y < min_y:
                pass

            elif x == col and x + 1 < len(y - 1) and x + 1 == col:
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
        return False, colour_list
    elif len(colour_list) == 1:
        return True, colour_list
    else:
        return "error"


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
    count = s_object.object_id
    c_colour = s_object.colour
    i = 0
    print("Colour: ", c_colour)
    for j in range(len(image_copy)*len(image_copy[0])):

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

                                if (y, x) == ind_list[0]:
                                    break
                                else:
                                    y = y - 1
                                    x = x - 1
                                    plot[y, x] = count
                                    s_object.plot[y, x] = count
                                    ind_list.append((y, x))

                                    last_pix = 5

            if last_pix != 5:
                last_pix = 1

        # Two
        elif last_pix == 1:

            if y - 1 >= 0:

                new_pix = image_copy[y - 1, x]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:

                            if (y, x) == ind_list[0]:
                                break
                            else:
                                y = y - 1
                                plot[y, x] = count
                                s_object.plot[y, x] = count
                                ind_list.append((y, x))

                                last_pix = 6

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

                                if (y, x) == ind_list[0]:
                                    break
                                else:
                                    y = y - 1
                                    x = x + 1
                                    plot[y, x] = count
                                    s_object.plot[y, x] = count

                                    ind_list.append((y, x))
                                    last_pix = 7

            if last_pix != 7:
                last_pix = 3

        # Four
        elif last_pix == 3:

            if x + 1 < len(image_copy[0]):

                new_pix = image_copy[y, x + 1]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:

                            if (y, x) == ind_list[0]:
                                break
                            else:
                                x = x + 1
                                plot[y, x] = count
                                s_object.plot[y, x] = count
                                ind_list.append((y, x))

                                last_pix = 8

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
                                if (y, x) == ind_list[0]:
                                    break
                                else:
                                    y = y + 1
                                    x = x + 1
                                    plot[y, x] = count
                                    s_object.plot[y, x] = count
                                    ind_list.append((y, x))

                                    last_pix = 1

            if last_pix != 1:
                last_pix = 5

        # Six
        elif last_pix == 5:

            if y + 1 < len(image_copy):

                new_pix = image_copy[y + 1, x]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:

                            if (y, x) == ind_list[0]:
                                break
                            else:
                                y = y + 1
                                plot[y, x] = count
                                s_object.plot[y, x] = count
                                ind_list.append((y, x))

                                last_pix = 2

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

                                if (y, x) == ind_list[0]:
                                    break
                                else:
                                    y = y + 1
                                    x = x - 1
                                    plot[y, x] = count
                                    s_object.plot[y, x] = count
                                    ind_list.append((y, x))

                                    last_pix = 3

            if last_pix != 3:
                last_pix = 7

        # Eight
        elif last_pix == 7:

            if x - 1 >= 0:

                new_pix = image_copy[y, x - 1]

                if new_pix[0] == c_colour[0]:
                    if new_pix[1] == c_colour[1]:
                        if new_pix[2] == c_colour[2]:

                            if (y, x) == ind_list[0]:
                                break
                            else:
                                x = x - 1
                                plot[y, x] = count
                                s_object.plot[y, x] = count
                                ind_list.append((y, x))

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
    # start_val = 0
    # for y in plot:
    #     for x in y:
    #
    #         co = x
    #
    #         if co == start_val:
    #             for i in col_val_list:
    #
    #         if co == 0 and start_val != 0:
    #             col_val_list.append((y, x))
    #
    #         elif co != 0:
    #             start_val = co
    #
    #         else:
    #             print("x-1")

# new
def get_inside_object_colour(colour_list, colour):

    for i in colour_list:
        if i[0] == colour[0]:
            if i[1] == colour[1]:
                if i[2] == colour[2]:
                    pass
                else:
                    return i
            else:
                return i
        else:
            return i


def inner_outline_start(image_copy, plot, new_colour, s_object):

    max_y, max_x = s_object.max_yx
    min_y, min_x = s_object.min_yx
    col = s_object.colour
    ob_id = s_object.object_id
    for y in image_copy:
        for x in y:
            p_x = plot[y, x]
            if x > max_x or x < min_x or y > max_y or y < min_y:
                pass
            elif x == col and x+1 == new_colour and p_x != ob_id and p_x+1 == 0:
                start_co = (y, x)
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
    for y in enumerate(plot):
        print(y)
        for x in enumerate(y):

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

                find_outline(image_copy, plot, s_object, 8, (0, 0))

                while i != 0:
                    val, colour_list = check_fill(image_copy, plot, s_object)

                    if val:
                        find_fill(image_copy, plot, s_object)

                        break
                    else:
                        new_colour = get_inside_object_colour(colour_list, c_colour)

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

        #    print("ny:", ny, "pixel: ", y,",", x, " New pixel: ", new_pix, "option: ", option)

        # if option == 6:
        #
        #     up = 0
        #     subcount = 1
        #     print(pixel_list)
        #     new_x = x + 1
        #     while len(pixel_list) == 0:
        #
        #         print("We got this far ", subcount, " and ", pixel_list, y, ",", new_x)
        #
        #         if new_x >= len(pixel_matrix[0]):
        #             option = 5
        #             break
        #
        #         new_pix = pixel_matrix[y, new_x]
        #
        #         if new_pix[0] == 0 and new_pix[1] == 0 and new_pix[2] == 0:
        #             option = 5
        #             break
        #
        #         if subcount > 50:
        #             option = 5
        #             break
        #
        #         # ny = y + 1
        #         # # print("ny:", ny, "pixel: ", pix, "new pixel: ", new_pix, "option: ", option)
        #         # while ny < len(pixel_matrix) and new_x < len(pixel_matrix[0]):
        #         #
        #         #     new_pix = pixel_matrix[ny, new_x]
        #         #
        #         #     if new_pix[0] == 0 and new_pix[1] == 0 and new_pix[2] == 0:
        #         #         up += 1
        #         #         break
        #         #
        #         #     bool_val = check_delete(deleted_list, new_pix)
        #         #
        #         #     if bool_val:
        #         #         ny += 1
        #         #     else:
        #         #         pixel_list.append(new_pix)
        #         #
        #         #         break
        #
        #         ny = y - 1
        #         while ny >= 0 and new_x < len(pixel_matrix[0]):
        #
        #             new_pix = pixel_matrix[ny, new_x]
        #
        #             if new_pix[0] == 0 and new_pix[1] == 0 and new_pix[2] == 0:
        #                 up += 1
        #
        #                 break
        #
        #             bool_val = check_delete(deleted_list, new_pix)
        #
        #             if bool_val:
        #                 ny -= 1
        #             else:
        #                 pixel_list.append(new_pix)
        #
        #                 break
        #         if up > 0:
        #             new_x += 1
        #         subcount += 1

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

# def pix_restrict(): # og first different colour
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
#
#         for y, row in enumerate(pixel_matrix):
#             for x, pix in enumerate(row):
#                 print("(Y,X): ", y, ",", x)
#
# # count the number of times a pixel appears
#                 if len(pixel_list) == 0:
#                     pixel_list.append(list(pix))
#                     colour_count.append(1)
#                 else:
#                     count = 0
#                     for i in pixel_list:
#
#                         if i[0] == pix[0]:
#                             if i[1] == pix[1]:
#                                 if i[2] == pix[2]:
#                                     index = pixel_list.index(i)
#
#                                     ind = index
#
#                                     colour_count[ind] += 1
#                                 else:
#                                     count += 1
#                             else:
#                                 count += 1
#                         else:
#                             count += 1
#
#                         if count >= len(pixel_list):
#                             pixel_list.append(list(pix))
#                             colour_count.append(1)
#                             break
#
#
# # print list of all individual colours
#
#         e = 1
#         for x in pixel_list:
#             num = colour_count[e-1]
#             print("Colour ", e, " Value: ", x, " Amount: ", num,)
#             e += 1
#
# # make a list of the colours that appear the least
#         # make into a percentage formula
#         # value = len(pixel_matrix) * len(pixel_matrix[0]) / colour
#         value = 2000
#         index_list = []
#         for i in colour_count:
#             if i <= value:
#                 index = colour_count.index(i)
#                 delete_colour.append(pixel_list[index])
#                 index_list.append(index)
#
# # for each pixel in image
#         colour_count.clear()
#         pixel_list.clear()
#
#         pic = 0
#         pic2 = 0
#         for y, row in enumerate(pixel_matrix):
#             for x, pix in enumerate(row):
#                 pic += 1
#                 if pic >= 22658:
#                     pic = 0
#                     pic2 += 1
#                 print("Pixel Count: ", pic)
# # check pixel against the delete list
#                 # if it needs to be deleted get surrounding pixels
#                 val = check_delete(delete_colour, pix)
#
#                 if val:
#
#                     pix = get_down_right_pixel(pixel_matrix, y, x, delete_colour)
#
#                    # print("delete it: ", d)
#
#                     image_copy[y, x] = pix
#
# # print pixel list
# #         j = 1
# #         for x in pixel_list:
# #             num = colour_count[j - 1]
# #             print("Colour ", j, " Value: ", x, " Amount: ", num)
# #             j += 1
#         print("making image")
#         images[1] = Image.fromarray(image_copy, "RGB")
#         display_cy_image()
#     else:
#         print("Error: Pix_change failed")

# def somithing():

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
                    pix_val = 0
                    if pix[0] < 70:

                        if pix[1] < 70:

                            if pix[2] < 70:
                                pix_val = 1

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
        set_w = 400
        set_h = 400
    elif size_option == 2:
        print('5x7" hoop')
        set_w = 480
        set_h = 672
    elif size_option == 3:
        print('6x10" hoop')
        set_w = 576
        set_h = 960
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


def display_image(image):
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

