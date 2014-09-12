#Max Louis
#Garden Challenge exercise
#12/09/14

length = float(input("What is the Length in metres?"))
width = float(input("What is the Width in metres?"))

length = length - 1
width = width - 1
area = length * width
cost = area * 10

print("It will cost £{0}.".format(cost))
