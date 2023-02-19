from math import tan

side_n = int(input("Number of sides: "))
side_l = int(input("length of a side: "))

area = (side_l*side_l*side_n)/(4*tan((180/side_n)*3.14159/180))

print("the are of polygon is: {}".format(int(area)))