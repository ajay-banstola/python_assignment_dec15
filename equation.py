def equat(list_x):
    m = 45
    c = 0.5

    for x in list_x:
        y = m * x + c
        print("For x = {0}, y = {1:.2f}".format(x,y))

equat([1, 2.3, 5.6, 7, 78])
