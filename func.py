from math import pi

def printName(name):
    return "Hello Mr/Ms {name}...we've been waiting for you!"

def houseArea(rooms, lengths, widths):
    total_area = 0
    for i in range(rooms):
        area = lengths[i] * widths[i]
        total_area += area

    return total_area

def circumference(radius):
    return 2 * pi * radius