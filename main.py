import turtle

turtle.speed(100)#speed of the turtle
turtle.shape("square")#makes turtle a square
wn = turtle.Screen()
# add a turtle screen
wn.bgcolor("light gray")#sets background screen to light gray

tree = [["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"], ["100111111110000001111001"], ["10011111","11100000","01111001"], ["10011111", "11100000","01111001"], ["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"], 
["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"], ["10011111","11100000","01111001"], ["10011111","11100000","01111001"], ["10011111","11100000","01111001"], ["10011111","11100000","01111001"], ["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"], 
["11111111", "11111111", "11111111"], ["10011111","11100000","01111001"], ["11111111", "11111111", "11111111"], ["10011111","11100000","01111001"], ["10011111","11100000","01111001"], ["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"], 
["10011111","11100000","01111001"], ["10011111","11100000","01111001"], ["11111111", "11111111", "11111111"], ["10010110", "01001011","00000000"], ["11111111", "11111111", "11111111"], ["10011111","11100000","01111001"], ["10011111","11100000","01111001"], ["11111111", "11111111", "11111111"], 
["11111111", "11111111", "11111111"], ["10010110", "01001011","00000000"], ["11111111", "11111111", "11111111"], ["10010110", "01001011","00000000"], ["11111111", "11111111", "11111111"], ["10011111","11100000","01111001"], ["10011111","11100000","01111001"], ["10011111","11100000","01111001"], 
["11111111", "11111111", "11111111"], ["10010110", "01001011","00000000"], ["10010110", "01001011","00000000"], ["11111111", "11111111", "11111111"], ["10010110", "01001011","00000000"], ["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"], ["10010110", "01001011","00000000"], ["10010110", "01001011","00000000"], ["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"], ["10010110", "01001011","00000000"],["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"], ["10010110", "01001011","00000000"], ["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"], ["10010110", "01001011","00000000"], ["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"], ["11111111", "11111111", "11111111"]]

binarylist = [['11111111', '11111111', '11111111'], ['11101011', '11111010', '11101011'], ['11010110', '11110101', '11010110'], ['11000010', '11110000', '11000010'], ['10101101', '11101011', '10101101'], ['10011001', '11100110', '10011001'], ['10000101', '11100000', '10000101'], ['01110000', '11011011', '01110000'], ['01011100', '11010110', '01011100'], ['01000111', '11010001', '01000111'], ['00110011', '11001100', '00110011'], ['00101110', '10111000', '00101110'], ['00101001', '10100011', '00101001'], ['00100100', '10001111', '00100100'], ['00011111', '01111010', '00011111'], ['00011001', '01100110', '00011001'], ['00010100', '01010010', '00010100'], ['00001111', '00111101', '00001111'], ['00001010', '00101001', '00001010'], ['00000101', '00010100', '00000101'], ['00000000', '00000000', '00000000']]

temp = []#temporary list that modifies gradient

def draw(gradient):#Part A: Draw a square:
  turtle.penup()
  count = 0
  while count < 12:#makes 12 rows
    for k in gradient:
      rgb = [int(i, 2) for i in k]
      turtle.color(rgb[0], rgb[1], rgb[2])#makes a color based o each byte in gradient
      turtle.begin_fill()
      square()
      turtle.pencolor(rgb[0], rgb[1], rgb[2])
      turtle.end_fill()
      turtle.fd(20)
    row(gradient)
    count = count + 1
#Part A: Draw a square:
def square():
  turtle.pendown()
  for x in range(4): # repeats the steps below 4 times
    turtle.fd(20)
    turtle.right(90)
def row(rgb_list):#adds a new row once the turtle finishes a row
  turtle.penup()
  turtle.left(180)
  turtle.fd(len(rgb_list)*20)
  turtle.left(90)
  turtle.fd(20)
  turtle.left(90)
#Part A: Removes one bit from each byte in the RGB
def rob(gradient,temp):
  for i in gradient:#removes last character from each bit
    temp.append([i[0][:-1], i[1][:-1], i[2][:-1]])
  return temp
# Part A: Adds 01 to each byte in the RGB
def add1(temp):
  temp = [['11111111', '11111111', '11111111'], ['11101011', '11111010', '11101011'], ['11010110', '11110101', '11010110'], ['11000010', '11110000', '11000010'], ['10101101', '11101011', '10101101'], ['10011001', '11100110', '10011001'], ['10000101', '11100000', '10000101'], ['01110000', '11011011', '01110000'], ['01011100', '11010110', '01011100'], ['01000111', '11010001', '01000111'], ['00110011', '11001100', '00110011'], ['00101110', '10111000', '00101110'], ['00101001', '10100011', '00101001'], ['00100100', '10001111', '00100100'], ['00011111', '01111010', '00011111'], ['00011001', '01100110', '00011001'], ['00010100', '01010010', '00010100'], ['00001111', '00111101', '00001111'], ['00001010', '00101001', '00001010'], ['00000101', '00010100', '00000101'], ['00000000', '00000000', '00000000']]
  return temp
#Part A: Converting to RG Dichrome palette
def rg_d(gradient):
  turtle.penup()
  count = 0
  while count < 12:
    for k in gradient:
      rgb = [int(i,2)for i in k]
      turtle.color(rgb[0], rgb[1], 0)
      turtle.begin_fill()
      square()
      turtle.pencolor(rgb[0], rgb[1], 0)
      turtle.end_fill()
      turtle.fd(20)
    row(gradient)
    count = count + 1
  return gradient

def gb_d(gradient):
  turtle.penup()
  count = 0
  while count < 12:#makes 12 rows for the gradient
    for k in gradient:
      rgb = [int(i,2)for i in k]#takes the colors from red and green and leaves 0 for blue colors
      turtle.color(0, rgb[1], rgb[2])
      turtle.begin_fill()
      square()
      turtle.pencolor(0, rgb[1], rgb[2])
      turtle.end_fill()
      turtle.fd(20)
    row(gradient)
    count = count + 1
  return gradient
#First part: Converting the GB Dichrome Palette

def rb_d(gradient):
  turtle.penup()
  count = 0
  while count < 12:
    for k in gradient:
      rgb = [int(i,2)for i in k]#takes colors from green and blue and leave 0 for red colors
      turtle.color(rgb[0], 0, rgb[2])
      turtle.begin_fill()
      square()
      turtle.pencolor(rgb[0], 0, rgb[2])
      turtle.end_fill()
      turtle.fd(20)
    row(gradient)
    count = count + 1
  return gradient

#Part A: converts to RB dichrome Palette
#part B
  #show an example of each procedure in action using python turtle to print the resulting gradient.
print('Enter 1 to draw the original gradient.')
print('Enter 2 to remove one bit from each byte in the RGB.')
print('Enter 3 to add 01 to each byte in the RGB.')
print('Enter 4 to convert to RG Dichrome Palette.')
print('Enter 5 to convert to GB Dichrome Palette')
print('Enter 6 to convert to RB Dichrome Palette.')

c = int(input())#taking user input

if c == 1:
  wn.colormode(255)
  turtle.penup()
  turtle.goto(-210, 120)
  square()
  draw(binarylist)
  print()
  print(binarylist)
  print(len(binarylist))
elif c == 2:#make a gradient with 1 less bit for each byte from gradient
  wn.colormode(255)
  turtle.penup()
  turtle.goto(-210, 120)
  square()
  rob(binarylist, temp)
  draw(temp)#draw gradient with 1 less bit in each byte after drawing gradient
  print()
  print(temp)
elif c == 3:#choice #3
  wn.colormode(255)
  turtle.penup()
  turtle.goto(-210, 120)
  square()
  print(draw(add1(temp)))
  print(add1(temp))
  #choice 4
elif c == 4:#draws the red and green dichrome
  wn.colormode(255)
  turtle.penup()
  turtle.goto(-210, 120)
  square()
  rg_d(binarylist)
  #choice #5
elif c == 5:#draws the green and blue dichrome
  wn.colormode(255)
  turtle.penup()
  turtle.goto(-210, 120)
  gb_d(binarylist)
#------------------
  #choice 6
elif c == 6:#draws the red and blue dichrome
  wn.colormode(255)
  turtle.penup()
  turtle.goto(-210, 120)
  rb_d(binarylist)
elif c == 8:
  wn.colormode(255)
  turtle.penup()
  turtle.goto(-210, 120)
  square()
  draw(tree)
  print()
  print(tree)
  print(len(tree))
else:#prints an error message if the user types in anything besided the numbers from 1-6 b 
  print("try again")









