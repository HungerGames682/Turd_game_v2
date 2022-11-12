
import turtle
import keyboard
stop = 0




# Put how many objects there are, only thing that is manual
many = 3
whole_many = many *2





screen = turtle.Screen()
screen.screensize(800,800)
player = turtle.Turtle()
player.shape("square")
buildspeed = 0

        

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
       

    
def obj_create(stop,buildspeed,many):
    # Put how many objects there
    li = []
    which = 100
    x = 0
    y = 1
    for ob in range(many):
        with open('obj.txt','r') as fs:
            line = fs.readlines()
            print(line[which])
        line[which] = turtle.Turtle()
        line[which].speed(buildspeed)
        
        # NOTE TO SELF, Finish auto create objects
        with open('cords.txt','r') as cord:
            main = cord.readlines()
            newx = int(main[x])
            newy = int(main[y])
            print(newx,newy)

        object("square",statcolor,player, line[which],newx,newy,stop)
        
        

        # Add the x and y add to list 
        li.append(newx)
        li.append(newy)
        x = x + 2
        y = y + 2
        which = which + 1
    return li

    


# V2, go back to origanal if it does not work
def playermove(speed,movement,walkthrough, offset, stop,li):
    
    # Hopfully imporved laggy ness
    
    lis = []
    for i in range(0, whole_many,2):
        h = i + 1
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
    
    if dis[0] <= 15:
        player.goto(0,0)


    # Prevents going through objects
    if dis[0] <offset and dis[2] ==ny and walkthrough == "No":
        f = False

    elif dis[0] <offset and dis[1] == nx and walkthrough == "No":
        l = False

    elif dis[0] <offset and dis[2] == py and walkthrough == "No" or y <= -280:
        b = False
    elif dis[0] <offset and dis[1] == px and walkthrough == "No":
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

    if colition == 0:
        return "Null"
    else:
        dis = name.distance(colition)
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
    


