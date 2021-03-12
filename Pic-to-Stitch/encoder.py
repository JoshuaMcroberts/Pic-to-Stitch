# One
if l_point == 8:  # check loop start
    point_c = 0

    if test == 1:  # testing console comments
        print("# One")

    if y - 1 >= 0 and x - 1 >= 0:  # check if this point is within the plot limits
        n_point = plot[y - 1, x - 1]  # set this point

        if n_point == col_num:  # check against colour_number
# START ***************************************************************************************************************
            if y - 1 == f_y and x - 1 == f_x:  # check if next point is destination

                return goto_yx  # if true then break loop and return goto_yx

            else:  # else record valid point
# END *****************************************************************************************************************
                y -= 1  # set y to y - 1
                x -= 1  # set x to x - 1
# START ***************************************************************************************************************
                if test == 1:  # testing console comments
                    print("Set ({},{})".format(y, x))

                plot[y, x] = set_to  # set point
                ind_list.append((y, x))  # add point to list
                cur_yx = (y, x)  # combine current y, x
                point_c = next_point(cur_yx, goto_yx)  # get next position to check
                s_pat = search_patterns[point_c - 1]  # change to new search pattern
                ind = 0  # reset search pattern start
                loop = 1  # set check value

    if loop != 1:  # check if new current point was set
        ind += 1  # if not, set to the next position
# END *****************************************************************************************************************
# Two
elif l_point == 1:  # check loop start
    point_c = 0

    if test == 1:  # testing console comments
        print("# Two")

    if y - 1 >= 0:  # check if this point is within the plot limits
        n_point = plot[y - 1, x]  # set this point

        if n_point == col_num:  # check against colour_number

            if y - 1 == f_y and x == f_x:  # check if next point is destination

                return goto_yx  # if true then break loop and return goto_yx

            else:  # else record valid point

                y -= 1  # set y to y - 1

                if test == 1:  # testing console comments
                    print("Set ({},{})".format(y, x))

                plot[y, x] = set_to  # set point
                ind_list.append((y, x))  # add point to list
                cur_yx = (y, x)  # combine current y, x
                point_c = next_point(cur_yx, goto_yx)  # get next position to check
                s_pat = search_patterns[point_c - 1]  # change to new search pattern
                ind = 0  # reset search pattern start
                loop = 1  # set check value

    if loop != 1:  # check if new current point was set
        ind += 1  # if not, set to the next position