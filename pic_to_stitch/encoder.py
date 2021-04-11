# One - Top Left
if l_point == 8:  # if previous point was position 8...

    # console testing comment
    if test == 1:
        print("# One")

    if y - 1 >= 0 and x - 1 >= 0:  # if potential point will be within the plot...
        n_point = plot[y - 1, x - 1]  # set new point with the plot points value

        if n_point == col_num:  # if new points value is the same as the colour number...
            pon_a = plot[y, x - 1]  # get point a - Left of current point, Below new point
            pon_b = plot[y - 1, x]  # get point b - Above current point, Right of new point

            if pon_a == pon_b:  # if point a and b are the same...- testing to see if new point is a valid move

                # console testing comment
                if test == 2:
                    print("1 can't go equal points pon_a: {} pon_b: {}".format(pon_a, pon_b))

                # if a and b are the same they could be part of a line
                # if the line cuts off new point from current point then new point is not valid
                # on the other hand if new point an current point are the line,
                # they could be cutting off point a and b making new point a valid move

                # get points in a 5x5 grid surrounding new point - returns list of values & list of co_ordinates
                points, yx_points = get_surrounding_points_5x5(plot, y - 1, x - 1)

                # counts how many time each value appears in value list - return values and amounts
                val_list, amount_list = count_list(points)

                # determines whether new point is a valid move or not
                anw = t_w_p_logic(col_num, pon_a, val_list, amount_list)

                if anw == 1:  # if answer is equal to 1...- new point is a valid move

                    # set new point section
                    y -= 1  # set new y
                    x -= 1  # set new x

                    ref_plot[y, x] = set_to  # set point in reference plot to set_to value
                    ind_list.append((y, x))  # append point y,x to  index list
                    l_point = 5  # set last point to 5 - Bottom Right - direction travelled from

                    # console testing comment
                    if test == 1 or test == 2:
                        print("Che 1 Set ({},{})".format(y, x))

            else:  # else if a and b are not equal...
                if (y - 1, x - 1) == ind_list[0]:  # if new point equals start point...
                    break  # break while loop

                else:  # else if new point is not start point...

                    # set new point section
                    y -= 1  # set new y
                    x -= 1  # set new x

                    ref_plot[y, x] = set_to  # set point in reference plot to set_to value
                    ind_list.append((y, x))  # append point y,x to  index list
                    l_point = 5  # set last point to 5 - Bottom Right - direction travelled from

                    # console testing comment
                    if test == 1 or test == 2:
                        print("Pos 1 Set ({},{})".format(y, x))

    if l_point != 5:  # if last point is not 5... - if the  new point was not set and instead skipped...
        l_point = 1  # set last point to 1 - the next point in a clockwise direction - Top
