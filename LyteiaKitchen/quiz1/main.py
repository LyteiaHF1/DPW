'''
Lyteia Kitchen
5/7/14
Quiz1
'''

def calcArea(w, h):
    #area = h times width
    area = h * w
    #this returns the area
    return area
height = 40
width = 20
area = calcArea(height, width)
    #if height is the same a width
if height == width:
        print "The area of your square is " + str(area)+ " square feet."
else:
        print "The area of your rectangle is " + str(area)+ " square feet."


area = calcArea(height,width)
