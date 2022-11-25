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
damage = 1
type = "Chest"
lock_difficulty = 0





obj_list = []
color_list = []
collition_list = []
big_del = []
damage_list = []
type_list = []
lock_difficulty_list = []
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
def blockplace(x, y,curcolor,collition,damage,type,lock_difficulty):

    
    # If these keys are pressed when click then all blocks will be saved for the game
    if keyboard.is_pressed("b"):
            print(obj_list)
            print("Overiting save list")
            while True:
                # Gonna have to add more levels by adding to this if statment :)
                # Also every new level that is added you will need to add it to the main and this code bitttch
                if keyboard.is_pressed("s"):
                    print("Exiting without saving")
                    exit()



                if keyboard.is_pressed("0"):
                    level = 0
                    cords = '/Users/rwilkes/vscode_projects/Turd_game_v2/cords.txt'
                    colli = '/Users/rwilkes/vscode_projects/Turd_game_v2/colli.txt'
                    coller = '/Users/rwilkes/vscode_projects/Turd_game_v2/color.txt'
                    dam = '/Users/rwilkes/vscode_projects/Turd_game_v2/damage.txt'
                    ty = '/Users/rwilkes/vscode_projects/Turd_game_v2/type.txt'
                    lik = '/Users/rwilkes/vscode_projects/Turd_game_v2/lock.txt'
                    break

                if keyboard.is_pressed("1"):
                    level = 1
                    cords = '/Users/rwilkes/vscode_projects/Turd_game_v2/level_' + str(level) + '/cords.txt'
                    colli = '/Users/rwilkes/vscode_projects/Turd_game_v2/level_' + str(level) + '/colli.txt'
                    coller = '/Users/rwilkes/vscode_projects/Turd_game_v2/level_' + str(level) + '/color.txt'
                    dam = '/Users/rwilkes/vscode_projects/Turd_game_v2/level_' + str(level) + '/damage.txt'
                    ty = '/Users/rwilkes/vscode_projects/Turd_game_v2/level_' + str(level) + '/type.txt'
                    lik = '/Users/rwilkes/vscode_projects/Turd_game_v2/level_' + str(level) + '/lock.txt'
                    break

            
            # Writes the cords for the objects
            with open(cords, 'w') as ba:
                for i in range(len(obj_list)):
                    print(obj_list[i])
                    cl = obj_list[i]
                    cl = int(cl)
                    cl = str(cl)
                    cl = cl + '\n'
                    ba.write(cl)

            # Writes the colors for the objects
            with open(coller,'w') as c:
                for j in range(len(color_list)):
                    print(color_list[j])
                    k = color_list[j]
                    k = str(k)
                    k = k + '\n'
                    c.write(k)

            # Writes the colitions
            with open(colli,'w') as co:
                for b in range(len(collition_list)):
                    print(collition_list)
                    yo = collition_list[b]
                    yo = str(yo)
                    yo = yo + '\n'
                    co.write(yo)
            # Writes the damage values
            with open(dam, 'w') as da:
                for c in range(len(damage_list)):
                    print(damage_list)
                    dd = damage_list[c]
                    dd = str(dd)
                    dd = dd + '\n'
                    da.write(dd)
            # Writes the type values
            with open(ty, 'w') as ltt:
                for lit in range(len(type_list)):
                    print(type_list)
                    ttt = type_list[lit]
                    ttt = str(ttt)
                    ttt = ttt + '\n'
                    ltt.write(ttt)
            # Writes the lock difficulty values
            with open(lik, 'w') as differ:
                for ah in range(len(lock_difficulty_list)):
                    print(lock_difficulty_list)
                    lll = lock_difficulty_list[ah]
                    lll = str(lll)
                    lll = lll + '\n'
                    differ.write(lll)




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
            name = line[which]
            b = turtle.Turtle()
            b.color(curcolor)
            b.speed(0)
            b.shape("square")
            b.penup()
            b.goto(x,y)
            hehe = [name]
            big_del.append(hehe)

            which = which + 1


        


            # Adds the different values to a list
            obj_list.append(x)
            obj_list.append(y)
            color_list.append(curcolor)
            collition_list.append(collition)
            damage_list.append(damage)
            type_list.append(type)
            lock_difficulty_list.append(lock_difficulty)
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
        # coloricon.color("red")
        builder.color("red")
        sleep(.1)
        return"red"

    if cc[0] == "red":
        # coloricon.color("blue")
        builder.color("blue")
        sleep(.1)
        return"blue"

    if cc[0] == "blue":
        # coloricon.color("yellow")
        builder.color("yellow")
        sleep(.1)
        return"yellow"

    if cc[0] == "yellow":
        # coloricon.color("green")
        builder.color("green")
        sleep(.1)
        return"green"

    if cc[0] == "green":
        # coloricon.color("brown")
        builder.color("brown")
        sleep(.1)
        return"brown"

    if cc[0] == "brown":
        # coloricon.color("black")
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
    
# Switches the damage on and off
def damageswitch(damage):
    if damage == 1:
        damage = 0
        damageicon.clear()
        damageicon.write("Damage is off")
        sleep(.2)
        return damage

    elif damage == 0:
        damage = 1
        damageicon.clear()
        damageicon.write("Damage is on")
        sleep(.2)
        return damage

# Switches the type of interactibel it is or something
def typeswitch(type):
    if type == "Chest":
        type = "Null"

    elif type == "Null":
        type = "Chest"
    typeicon.clear()
    typeicon.write("Type is " + type)
    return type

# Changes the difficulty of lock it is
def lockswitch(lock_difficulty):
    if lock_difficulty == 0:
        lock_stat = "Pins = 1"
        lock_difficulty = 1

    elif lock_difficulty == 1:
        lock_stat = "Pins = 2"
        lock_difficulty = 2
    
    elif lock_difficulty == 2:
        lock_stat = "Pins = 3"
        lock_difficulty = 3

    elif lock_difficulty == 3:
        lock_stat = "Pins = 4"
        lock_difficulty = 4

    elif lock_difficulty == 4:
        lock_stat = "Pins = 5"
        lock_difficulty = 5
    
    elif lock_difficulty == 5:
        lock_stat = "Pins = 6"
        lock_difficulty = 6
    
    elif lock_difficulty == 6:
        lock_stat = "Pins = 7"
        lock_difficulty = 7

    elif lock_difficulty == 7:
        lock_stat = "Pins = 8"
        lock_difficulty = 8

    elif lock_difficulty == 8:
        lock_stat = "Pins = 9"
        lock_difficulty = 9

    elif lock_difficulty == 9:
        lock_stat = "Pins = 0"
        lock_difficulty = 0

    chest.clear()
    chest.write(lock_stat)
    return lock_difficulty






# start function.....
def start(speed,curcolor,collition,damage,type,lock_difficulty):
    movement(speed)
    # Places the block

    if keyboard.is_pressed("space"):
        blockplace(builder.xcor(),builder.ycor(),curcolor,collition,damage,type,lock_difficulty)

    


  

# statline2(1,0,"black",-300,10)


# Colition icon Turtle

colitionicon = turtle.Turtle()
colitionicon.penup()
colitionicon.goto(-300,-200)
colitionicon.write("Collition is on")

colitionicon.hideturtle()

# Color Icon turtle
coloricon = turtle.Turtle()
coloricon.penup()
coloricon.hideturtle()
coloricon.goto(-300,-225)
coloricon.write("Coler is: Black")


# Erease status turtle
eraseicon = turtle.Turtle()
eraseicon.penup()
eraseicon.hideturtle()
eraseicon.goto(-300,-250)
eraseicon.write("E = Erase all")

# Damage status turtle
damageicon = turtle.Turtle()
damageicon.penup()
damageicon.hideturtle()
damageicon.goto(-200,-200)
damageicon.write("Damage is on")

# Type Status turtle
typeicon = turtle.Turtle()
typeicon.penup()
typeicon.hideturtle()
typeicon.goto(-200,-225)
typeicon.write("Type is Chest")

# Chest attribute icon
chest = turtle.Turtle()
chest.penup()
chest.hideturtle()
chest.goto(-200,-250)


curcolor = "black"

# Main loop
while True:
    # Prevents objects that have no collition from having damage
    if collition == 0 and damage == 1:
        damage == 0
        damage = damageswitch(damage)
        print(damage)
        sleep(.2)

    # Turns damage on and off
    if keyboard.is_pressed("x"):
   
            
        damage = damageswitch(damage)
        print(damage)


    # Switches the color
    if keyboard.is_pressed("tab"):
        curcolor = colorswitcher()
        coloricon.clear()
        coloricon.write("Color is: " + str(curcolor))

    # Swithces the colition of the objects
    if keyboard.is_pressed("c"):
        
        collition = colitionswitch(collition)



# Enables erease mode
    if keyboard.is_pressed("e"):
     era_list = []
     print("TBA")

    if keyboard.is_pressed("r") and keyboard.is_pressed("shift") and type == "Chest":
        lock_difficulty = lockswitch(lock_difficulty)

    # Switches the type of object
    elif keyboard.is_pressed("r"):
        type = typeswitch(type)
        chest.clear()
        sleep(.2)


    # Sprint button
    if keyboard.is_pressed("shift"):
        speed = 10
        start(speed,curcolor,collition,damage,type,lock_difficulty)
    # Sprint and place button
    if keyboard.is_pressed("shift") and keyboard.is_pressed("space"):
        speed = 20
        start(speed,curcolor,collition,damage,type,lock_difficulty)

    else:    
        speed = 10
        start(speed,curcolor,collition,damage,type,lock_difficulty)
        sleep(.05)
        

