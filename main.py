
import turtle
import keyboard
stop = 0




# NOW THE CODE IS FULLY AUTOMATIC BESIDES HAVE TO SPECIFY WHERE THE OBJECT IS AND STUFF LIKE THAT 
with open('cords.txt','r') as howlines:
    length = howlines.readlines()
    length = len(length)
    length = length - 1
    length = length / 2
    length = int(length)
howlines.close()
many = length
whole_many = many * 2







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
    return li

    


# V2, go back to origanal if it does not work
# Basicly the start of the program, controls the player and its collitions with other objects
def playermove(speed,movement,walkthrough, offset, stop,li):
    
    # Hopfully imporved laggy ness
    print(li)
    lis = []
    for i in range(0, whole_many,2):
        h = i + 1
        if li[i] == "No" or li[h] == "No":
            print("")
        else:
            d1 = player.distance(li[i],li[h])
            diss = [d1, li[i], li[h]]
            lis.append(diss)

    dis = min(lis)
  
        
    

  
       


    
   
    
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
        
        ny = y + 20
        nx = x - 20
        py = y - 20
        px = x + 20
    
    
        
    error_bound =  21

    # Prevents going through objects
    if dis[0] <offset and dis[2] ==ny and walkthrough == "No" or dis[0] <= error_bound:
        f = False

    elif dis[0] <offset and dis[1] == nx and walkthrough == "No" or dis[0] <= error_bound:
        l = False

    elif dis[0] <offset and dis[2] == py and walkthrough == "No" or y <= -280 or dis[0] <= error_bound:
        b = False
    elif dis[0] <offset and dis[1] == px and walkthrough == "No" or dis[0] <= error_bound:
        r = False
   
     


   
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
def start(speed, movement,chunk,offset,stop,li):
    playermove(speed,movement,"No",offset,stop,li)




player.penup()
player.left(90)

stop = 1
statline2(how_obj,stop,"black",-300,buildspeed)
li = obj_create(stop,buildspeed,many)

# Main loop
while True:
    start(1,10, 1, 23,stop,li)
    stop = 0
    


