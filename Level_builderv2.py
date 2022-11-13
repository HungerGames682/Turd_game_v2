import turtle
import keyboard


# This is the builder for building those levels
screen = turtle.Screen()
screen.screensize(800,800)
builder = turtle.Turtle()
builder.penup()
builder.shape("square")
builder.speed(0)
builder.left(90)

ws = turtle.Screen()



obj_list = []

# Places the blocks... like minecraft 
def blockplace(x, y):

    
    # If these keys are pressed when click then all blocks will be saved for the game
    if keyboard.is_pressed("ctrl") and keyboard.is_pressed("alt"):
            print(obj_list)
            print("Overiting save list bitch")
            with open('cords.txt', 'w') as ba:
                for i in range(len(obj_list)):
                    print(obj_list[i])
                    cl = obj_list[i]
                    cl = int(cl)
                    cl = str(cl)
                    cl = cl + '\n'
                    ba.write(cl)
                    
                
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
            b.shape("square")
            b.penup()
            b.goto(x,y)
            which = which + 1


            # Adds the x and y values to the list
            obj_list.append(x)
            obj_list.append(y)

       
def movement(speed):

    if keyboard.is_pressed("W"):
        builder.forward(speed)



def start(speed):
    movement(speed)


  


# Main loop
while True:
    if keyboard.is_pressed("tab"):
        speed = 10
        start(speed)

    else:    
        speed = 1
        start(speed)

