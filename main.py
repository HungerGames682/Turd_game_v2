
import turtle
import keyboard
from time import sleep
stop = 0


created_turd = []

# NOW THE CODE IS FULLY AUTOMATIC BESIDES HAVE TO SPECIFY WHERE THE OBJECT IS AND STUFF LIKE THAT 
with open('cords.txt','r') as howlines:
    length = howlines.readlines()
    length = len(length)
   
    length = length / 2
    length = int(length)
howlines.close()
# Defines a bunch of varibles for the game and stuff bc i am too lazy
many = length
whole_many = many * 2
name_list = []
name_list_num = 0
obj_num = length
heath_turd_name = ["1","2","3","4","5","6","7","8","9","10"]
cur_health = 5
max_health = 10
leavel = 0
all_turd_obj = []
pin_locks = []
erase_lock = []






# Customize some settings here
screen = turtle.Screen()
screen.screensize(800,800)
player = turtle.Turtle()
player.shape("square")
buildspeed = 0

        
# Draws the stat bar line
how_obj = 1
statcolor = "black"
statyline = -300
def statline2(how_obj,stop,statcolor,statyline,buildspeed):
    for he in range(-500,500,20):
        with open('obj.txt','r') as b:
            line = b.readlines()
            print(line[how_obj])
        line[how_obj] = turtle.Turtle()
        line[how_obj].speed(buildspeed)
        object("square",statcolor,player, line[how_obj],he,statyline,stop)
        
        how_obj = how_obj + 1
       

# Creats all of the objects based on the cords.txt, colli.txt, shape.txt, color.txt
def obj_create(stop,buildspeed,many):
    # Put how many objects there
    # Your gonna have to define some varibles bro
    li = []
    which = 100
    coli_many = 0
    x = 0
    y = 1
    # The for loop that does it all
    for ob in range(many):
        with open('obj.txt','r') as fs:
            line = fs.readlines()
           
        line[which] = turtle.Turtle()
        all_turd_obj.append(line[which])
        created_turd.append(line[which])
        line[which].speed(buildspeed)
        
        # Creats the object at the cords givin, every 2 lines is a pare of cords
        # EX: line 1 = x-cord, line2 = y-cord, line 3 = x-cord, line 4 = y-cord
        with open('cords.txt','r') as cord:
            main = cord.readlines()
            newx = int(main[x])
            newy = int(main[y])
            print(newx,newy)

        # Opens the collitions file, 0 = walkthrough, 1 = collitions
        with open('colli.txt','r') as f:
            mc = f.readlines()
            coli = mc[coli_many]
            
        # Takes in color for the color.txt file and make the object color that is specified
        with open('color.txt','r') as colo:
            col =  colo.readlines()
            color = col[coli_many]
            color = color.strip('\n')
          


        # Actully creats the object and the saves it to see if has colliotion or not(Clearly)
        has_colition = object("square",color,coli, line[which],newx,newy,stop)
        print(has_colition)
        name_list.append(line[which])
        # Sees if the object can be walked through or not
        if has_colition == "No":
            x = x + 2
            y = x + 1
            which = which + 1
            coli_many = coli_many + 1
            li.append("No")
            li.append("No")
            
        else:
        # Add the x and y add to list 
            li.append(newx)
            li.append(newy)
        # Updates the varibles
            x = x + 2
            y = x + 1
            which = which + 1
            coli_many = coli_many + 1
    return li

    
# Switches the map to a new level design speicifided in the folder :)
def level_switch(stop,buildspeed,level):
    # Put how many objects there
    # Your gonna have to define some varibles bro
    cur_level = '/Users/rwilkes/vscode_projects/Turd_game_v2/level_' + str(level) + '/'
    cords = cur_level + 'cords.txt'
    colli = cur_level + 'colli.txt'
    coller = cur_level + 'color.txt'
    print(cords)
    print(colli)
    print(coller)
    print(created_turd)
    all_turd_obj = []
    li = []
    with open(cords,'r') as howlines:
        length = howlines.readlines()
        
        length = len(length)
        length = length / 2
        length = int(length)
    
    howlines.close()
    many = length
    whole_many = many * 2
    new_obj_num = length
    which = 100
    coli_many = 0
    obj_count_num = 0
    x = 0
    y = 1
    print(many)
    # The for loop that does it all
    for o in range(many):
        
            
        with open('obj.txt','r') as fs:
            line = fs.readlines()
        if o >= len(created_turd):
            line[which] = turtle.Turtle()
            all_turd_obj.append(line[which])
        else:
            line[which] = created_turd[o]
        line[which].speed(buildspeed)
        
        # Creats the object at the cords givin, every 2 lines is a pare of cords
        # EX: line 1 = x-cord, line2 = y-cord, line 3 = x-cord, line 4 = y-cord
        with open(cords,'r') as cord:
            main = cord.readlines()
            newx = int(main[x])
            newy = int(main[y])
            print(newx,newy)

        # Opens the collitions file, 0 = walkthrough, 1 = collitions
        with open(colli,'r') as f:
            mc = f.readlines()
            coli = mc[coli_many]
            
        # Takes in color for the color.txt file and make the object color that is specified
        with open(coller,'r') as colo:
            col =  colo.readlines()
            color = col[coli_many]
            color = color.strip('\n')
          


        # Actully creats the object and the saves it to see if has colliotion or not(Clearly)
        has_colition = object("square",color,coli, line[which],newx,newy,stop)
        print(has_colition)
        obj_count_num = obj_count_num + 1

        # Sees if the object can be walked through or not
        if has_colition == "No":
            x = x + 2
            y = y + 2
            which = which + 1
            coli_many = coli_many + 1
            li.append("No")
            li.append("No")
            
        else:
        # Add the x and y add to list 
            li.append(newx)
            li.append(newy)
        # Updates the varibles
            x = x + 2
            y = y + 2
            which = which + 1
            coli_many = coli_many + 1

    # gets rid of any exxsess objects if the previouse level had more objest than the current level
    if obj_num > new_obj_num:
        new_obj_nums = new_obj_num 
        obj_nums = obj_num  
        
        for i in range(new_obj_nums,obj_nums,1):
            print(i)
            name_list[i].hideturtle()
            
            
           
            

        
    return li, all_turd_obj



# V2, go back to origanal if it does not work
# Basicly the start of the program, controls the player and its collitions with other objects
def playermove(speed,movement,walkthrough, offset, stop,li,cur_health,level):
    
    # Hopfully imporved laggy ness
    lis = []
    whole_many = len(li)
    dd = 0
    if leavel == 1:
        dama = '/Users/rwilkes/vscode_projects/Turd_game_v2/level_1/damage.txt'

    else:
        dama = '/Users/rwilkes/vscode_projects/Turd_game_v2/damage.txt'
    for i in range(0, whole_many,2):
        
        with open(dama, 'r') as chi:
            dam = chi.readlines()
            sh = int(dam[dd])
        
            dd = dd + 1
        
        h = i + 1
        if li[i] == "No" or li[h] == "No":
            print("")
        else:
            d1 = player.distance(li[i],li[h])
            
            diss = [d1, li[i], li[h],sh]
            lis.append(diss)

    # Gets the distance, x,y of the closest block
    dis = min(lis)
    # print(dis)
  
        
    

  
       


    
   
    
    # print(dis)
    f = True
    l = True
    r = True
    b = True
    if dis[0] == "Null" or walkthrough == "Yes":
        f = True 
        l = True
        r = True
        b = True
        ny = 0
        nx = 0
        py = 0
        px = 0

    else:
        
        x = player.xcor()
        y = player.ycor()
        
        obj_x = dis[1]
        obj_yy = dis[2]

        obj_x = int(obj_x)
        obj_yy = int(obj_yy)

        obj_y = obj_yy - y
        p_obj_y = y  - obj_yy

        ny = y + 20
        nx = x - 20
        py = y - 20
        px = x + 20

        ny = int(ny)
        py = int(py)

        
   
    # TURN dis{2} into a int
    
    # Inside Perimiter Blocker
    error_bound =  17

    # Outside perimiter blocker
    less_error_bound = 18


    # Prevents going through objects
   
 


    if walkthrough == "Yes":
        print("Walk")

    else:
        # Detects if you glitch through a wall
       
        if dis[0] <= error_bound:
                print('\n' * 100)
                print("Error code: Glitch through wall")
                player.goto(0,0)
        
        # Makes the player take damage if they are close to a obj that damages them
        if dis[0] <= offset and dis[3] == 1:
            cur_health = heath_change(HCT, cur_health, -1,max_health)
            sleep(.1)
            
    #    The colition detection code, allows you to walkthrough a block or not
        if int(dis[0]) <= offset and dis[2] == ny and walkthrough == "No":
         f = False
         a = 0
        elif int(dis[0]) <= offset and dis[1] == nx and walkthrough == "No":
         l = False
         a = 0
        elif int(dis[0]) <= offset and dis[2] == py and walkthrough == "No" or y <= -230:
            b = False
            a = 0
        elif int(dis[0]) <= offset and dis[1] == px and walkthrough == "No":
            r = False
            a = 0
       


   
    # Makes player move and shit
    if keyboard.is_pressed("W") and f == True:
             player.forward(movement)
    if keyboard.is_pressed("S") and b == True:
            player.forward(-(movement))
    if keyboard.is_pressed("A") and l == True:
    
            x = player.xcor()
            y = player.ycor()
            x = x - movement
            player.speed(speed)
            player.goto(x,y)
    if keyboard.is_pressed("D") and r == True:
      
            x = player.xcor()
            y = player.ycor()
            x = x + movement
            player.speed(speed)
            player.goto(x,y)
    return cur_health


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
    
# Main start function
def start(speed, movement,chunk,offset,stop,li,cur_health,leavel):

      
        
    cur_health = playermove(speed,movement,"No",offset,stop,li,cur_health,leavel)
    return cur_health

# Draws the heath bar
def health_bar(x,y,max_health,cur_health):
    heath_created_turd = []
    # Creats little heath things
    HI = turtle.Turtle()
    HI.penup()
    new_x = x - 40
    HI.speed(0)
    HI.goto(new_x,y)
    HI.write("Health |")
    HI.hideturtle()
    heath_x = x - 20
    heath_y = y + 5
    # Generates the max heath bars
    for i in range(max_health):
        heath_x = heath_x + 10
        b = heath_turd_name[i]
        b = turtle.Turtle()
        b.penup()
        b.speed(0)
        b.goto(heath_x,heath_y)
        b.shapesize(.5)
        b.shape("square")
        b.color("red")
        heath_created_turd.append(b)


    # Hids the turds based on the heath
   
    for d in range(cur_health, max_health,1):
        turd = heath_created_turd[d]
        turd.hideturtle()

    return heath_created_turd

# It is the function that allows you to add or subtract from the health bar
def heath_change(HCT,cur_health,add, max_health):
    if cur_health == max_health and add == 1:
        print("Max health reached")

    elif cur_health == -1 and add == -1:
        print("You are dead")
        print("Game Over")
        cur_health = -1
        return cur_health
        


    elif add == 1:
        
        HCT[cur_health].showturtle()
       
        cur_health = cur_health + 1
        print(cur_health)


        


    elif add == -1:
        if cur_health == max_health:
            cur_health = cur_health - 1
        print("-1")
        HCT[cur_health].hideturtle()
       
        cur_health = cur_health - 1
        print(cur_health)


    return cur_health

# Makes the ouside of the lock shell
def lock_shell(x,y):
    lo = turtle.Turtle()
    lo.speed(0)
    lo.penup()
    lo.goto(x,y)
    lo.left(90)
    lo.pendown()
    lo.forward(100)
    lo.right(90)
    lo.forward(30)
    lo.right(90)
    lo.forward(100)
    lo.hideturtle()
    erase_lock.append(lo)

# Makes the pins of the lock
def lock_pin(x,y):
    ls = turtle.Turtle()
    ls.speed(0)
    ls.penup()
    ls.goto(x,y)
    ls.left(90)
    pin_locks.append(ls)
    erase_lock.append(ls)
# Makes the outside shell
def lock_out_shell(x,y):
    k = turtle.Turtle()
    k.penup()
    k.speed(0)
    k.goto(x,y)
    k.pendown()
    k.forward(30)
    k.hideturtle()
    erase_lock.append(k)

# Lockpick maker aka adds everything together
def lockpick(locks):
    hide = turtle.Turtle()
    hide.shape("square")
    hide.color("white")
    hide.shapesize(50)
    locked = True
    x = -150
    y = 0
    ox = x - 180
    oy = y - 15
    tx = x + 15
    ty = y - 2
    lx = x + 15
    ly = y + 10
    lox = x
    loy = y - 30

    # All the for loops draw the parts of the locks
    for i in range(locks):
        lock_shell(x,y)
        x = x + 30
    
    for d in range(locks):
        lock_pin(lx,ly)
        lx = lx + 30
    
    for a in range(locks):
        lock_out_shell(lox,loy)
        lox = lox + 30

    # The Turtle varibles for the pick itself
    wall = turtle.Turtle()
    wall.penup()
    wall.goto(lox,loy)
    wall.pendown()
    wall.left(90)
    wall.forward(30)
    wall.hideturtle()
    
    l = turtle.Turtle()
    l.penup()
    l.goto(ox,oy)
    l.shape("square")
    l.shapesize(.5,20)
    tip = turtle.Turtle()
    tip.penup()
    tip.goto(tx,ty)
    tip.shape("square")
    tip.shapesize(.8,.5)
    print(pin_locks)
    
    while locked == True:
        print("TBA")












player.penup()
player.left(90)

stop = 1
# Draws the like stat line for all of the stats 
# statline2(how_obj,stop,"black",-250,0)
# Draws and creats the heath bar
HCT = health_bar(-280,-280,max_health,cur_health)


li = obj_create(stop,buildspeed,many)




# Main loop
while True:
    # ends the game if there health is zero
    if cur_health == -1:
        print('\n' * 20)
        print("Game Over")
        print("You died...")
        exit()

    # Level Switch button, only temporary for testing, will make it when you go off screen of something
    if keyboard.is_pressed("T"):
        li, all_turd_obj = level_switch(stop,0,1)
     
        leavel = 1

    elif keyboard.is_pressed("esc"):
        print("Trying to make a menue of something")
    
    # Give and take away health, just here for testing feaetures
    if keyboard.is_pressed("R"):
        cur_health = heath_change(HCT, cur_health, 1,max_health)
       
        sleep(.2)
    if keyboard.is_pressed("F"):
        cur_health = heath_change(HCT, cur_health, -1,max_health)
        
        sleep(.2)
    

    if keyboard.is_pressed("G"):
        print(all_turd_obj)
        for i in range(len(all_turd_obj)):
            all_turd_obj[i].hideturtle()

    if keyboard.is_pressed("H"):
        print(all_turd_obj)
        for i in range(len(all_turd_obj)):
            all_turd_obj[i].showturtle()

    if keyboard.is_pressed("L"):
      lockpick(5)

        

    cur_health = start(1,10, 1, 23,stop,li,cur_health,leavel)
    stop = 0
    
    


