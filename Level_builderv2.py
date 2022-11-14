import turtle
import keyboard
from time import sleep


# This is the builder for building those levels
screen = turtle.Screen()
screen.screensize(800,800)
builder = turtle.Turtle()
builder.penup()
builder.shape("square")
builder.speed(0)
builder.left(90)

ws = turtle.Screen()
collition = 1



obj_list = []
color_list = []
collition_list = []
# Draws the statline
def statline2(how_obj,stop,statcolor,statyline,buildspeed):
    for he in range(-500,500,20):
        with open('obj.txt','r') as b:
            line = b.readlines()
            print(line[how_obj])
        line[how_obj] = turtle.Turtle()
        line[how_obj].speed(buildspeed)
        object("square",statcolor,builder, line[how_obj],he,statyline,stop)
        
        how_obj = how_obj + 1

    coloricon = turtle.Turtle()
    coloricon.shape("square")
    coloricon.goto(-300,-300)


# Object creator
def object(shape,coler,colition,name,x,y, stop):
    
    
    name.penup()
    name.shape(str(shape))
    name.color(str(coler))
    name.goto(x,y)

    if colition == "0" or colition == 0 or colition == "0\n":
        return "No"
    else:
        x = name.xcor()
        y = name.ycor()
        return x,y
    

# Places the blocks... like minecraft 
def blockplace(x, y,curcolor,collition):

    
    # If these keys are pressed when click then all blocks will be saved for the game
    if keyboard.is_pressed("b"):
            print(obj_list)
            print("Overiting save list")
            # Writes the cords for the objects
            with open('cords.txt', 'w') as ba:
                for i in range(len(obj_list)):
                    print(obj_list[i])
                    cl = obj_list[i]
                    cl = int(cl)
                    cl = str(cl)
                    cl = cl + '\n'
                    ba.write(cl)

            # Writes the colors for the objects
            with open('color.txt','w') as c:
                for j in range(len(color_list)):
                    print(color_list[j])
                    k = color_list[j]
                    k = str(k)
                    k = k + '\n'
                    c.write(k)

            
            with open('colli.txt','w') as co:
                for b in range(len(collition_list)):
                    print(collition_list)
                    yo = collition_list[b]
                    yo = str(yo)
                    yo = yo + '\n'
                    co.write(yo)




            sleep(3)
            exit()
                    
                
    else:
        builder.goto(x, y)


        # AHHHHHHHHHHHHHH
        with open('builder_list.txt','r') as d:
            which = d.read()
            which = int(which)
        
#       Create the object from the list and shit
        with open('obj.txt', 'r') as f:
            line = f.readlines()
            b = line[which]
            b = turtle.Turtle()
            b.color(curcolor)
            b.speed(0)
            b.shape("square")
            b.penup()
            b.goto(x,y)
            which = which + 1


        


            # Adds the different values to a list
            obj_list.append(x)
            obj_list.append(y)
            color_list.append(curcolor)
            collition_list.append(collition)
            print(collition_list)

# Movement function dumbass
def movement(speed):

    if keyboard.is_pressed("W"):
        builder.forward(speed)

    if keyboard.is_pressed("S"):
        builder.forward(-(speed))

    if keyboard.is_pressed("A"):
        x = builder.xcor()
        y = builder.ycor()
        nx = x - speed
        builder.goto(nx,y)

    if keyboard.is_pressed("D"):
        x = builder.xcor()
        y = builder.ycor()
        nx = x + speed
        builder.goto(nx,y)

# Just switches colors whenever it is called upon
def colorswitcher():
    cc = builder.color()
    print(cc)
    if cc[0] == "black":
        coloricon.color("red")
        builder.color("red")
        sleep(.1)
        return"red"

    if cc[0] == "red":
        coloricon.color("blue")
        builder.color("blue")
        sleep(.1)
        return"blue"

    if cc[0] == "blue":
        coloricon.color("yellow")
        builder.color("yellow")
        sleep(.1)
        return"yellow"

    if cc[0] == "yellow":
        coloricon.color("green")
        builder.color("green")
        sleep(.1)
        return"green"

    if cc[0] == "green":
        coloricon.color("brown")
        builder.color("brown")
        sleep(.1)
        return"brown"

    if cc[0] == "brown":
        coloricon.color("black")
        builder.color("black")
        sleep(.1)
        return"black"

# Switches the colition from on to off
def colitionswitch(collition):
    if collition == 1:
        collition = 0
        colitionicon.clear()
        colitionicon.write("Colitions are off")
        sleep(.2)
        return collition

    elif collition == 0:
        collition = 1
        colitionicon.clear()
        colitionicon.write("Colitions are on")
        sleep(.2)
        return collition
    

    






# start function.....
def start(speed,curcolor,collition):
    movement(speed)
    # Places the block

    if keyboard.is_pressed("space"):
        blockplace(builder.xcor(),builder.ycor(),curcolor,collition)

    


  

# statline2(1,0,"black",-300,10)

# Colition icon Turtle
coloricon = turtle.Turtle()
colitionicon = turtle.Turtle()
colitionicon.penup()
colitionicon.goto(-300,-200)
colitionicon.write("Collition is on")

colitionicon.hideturtle()

# Color Icon turtle
coloricon.penup()
coloricon.shape("square")
coloricon.goto(-410,-350)


curcolor = "black"
# Main loop
while True:
    # Switches the color
    if keyboard.is_pressed("tab"):
        curcolor = colorswitcher()
        print(curcolor)

    if keyboard.is_pressed("c"):
        collition = colitionswitch(collition)


    # Sprint button
    if keyboard.is_pressed("shift"):
        speed = 10
        start(speed,curcolor,collition)
    
    if keyboard.is_pressed("shift") and keyboard.is_pressed("space"):
        speed = 21
        start(speed,curcolor,collition)

    else:    
        speed = 1
        start(speed,curcolor,collition)
        

