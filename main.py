
import turtle
import keyboard
stop = 0
screen = turtle.Screen()
screen.screensize(800,800)
player = turtle.Turtle()
player.shape("square")



def statline(stop):
    # # Stats bar objects
    statcolor = "black"
    statyline = -300
    dis6 = object("square",statcolor,player, obj7,-400,statyline,stop)
    dis7 = object("square",statcolor,player, obj8, -380,statyline,stop)
    dis8 = object("square",statcolor,player, obj9, -360,statyline,stop)
    dis9 = object("square",statcolor,player, obj10, -340,statyline,stop)
    dis10 = object("square",statcolor,player, obj11, -320,statyline,stop)
    dis11 = object("square",statcolor,player, obj12, -300,statyline,stop)

    dis12 = object("square",statcolor,player, obj13,-280,statyline,stop)
    dis13 = object("square",statcolor,player, obj14, -260,statyline,stop)
    dis14 = object("square",statcolor,player, obj15, -240,statyline,stop)
    dis15 = object("square",statcolor,player, obj16, -220,statyline,stop)
    dis16 = object("square",statcolor,player, obj17, -200,statyline,stop)
    dis17 = object("square",statcolor,player, obj18, -180,statyline,stop)

    dis18 = object("square",statcolor,player, obj19,-160,statyline,stop)
    dis19 = object("square",statcolor,player, obj20, -140,statyline,stop)
    dis20 = object("square",statcolor,player, obj21, -120,statyline,stop)
    dis21 = object("square",statcolor,player, obj22, -100,statyline,stop)
    dis22 = object("square",statcolor,player, obj23, -80,statyline,stop)
    dis23 = object("square",statcolor,player, obj24, -60,statyline,stop)
   
        
    
def which(stop):
    # Put any new objects here

    dis0 = object("square","blue",player, obj1,-50,20,stop)
    dis1 = object("square","blue",player, obj2, -30,20,stop)
    dis2 = object("square","blue",player, obj3, -10,20,stop)
    dis3 = object("square","blue",player, obj4, 10,20,stop)
    dis4 = object("square","blue",player, obj5, 30,20,stop)
    dis5 = object("square","blue",player, obj6, 50,20,stop)

    statline(stop)



    
    
   
    mins = min([dis0,dis1,dis2,dis3,dis4,dis5])
    return dis0,dis1,dis2,dis3,dis4,dis5
    


# V2, go back to origanal if it doesnot work
def playermove(speed,movement,walkthrough, offset, stop,li):
    
    # Hopfully imporved laggy ness

  
       

    #   Going to have to make this auto matic later
    # For now every object must be put here
    # Its a pain but its better than watching you computer turn
    # into a nuclear reactor
    d1 = player.distance((li[0],li[1]))
    d2 = player.distance((li[2],li[3]))
    d3 = player.distance((li[4],li[5]))
    d4 = player.distance((li[6],li[1]))
    d5 = player.distance((li[8],li[9]))
    d6 = player.distance((li[10],li[11]))
    


    dis1 = [d1, li[0],li[1]]
    dis2 = [d2, li[2],li[3]]
    dis3 = [d3, li[4],li[5]]
    dis4 = [d4, li[6],li[7]]
    dis5 = [d5, li[8],li[9]]
    dis6 = [d6, li[10],li[11]]
    full_dis = [dis1,dis2,dis3,dis4,dis5,dis6]
    dis = min(full_dis)
    print(dis1)
    
   
    
    print(dis)
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

    elif dis[0] <offset and dis[2] == py and walkthrough == "No" or y <= -320:
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


# Put all turtles below

obj1 = turtle.Turtle()
obj2 = turtle.Turtle()
obj3 = turtle.Turtle()
obj4 = turtle.Turtle()
obj5 = turtle.Turtle()
obj6 = turtle.Turtle()

obj7 = turtle.Turtle()
obj8 = turtle.Turtle()
obj9 = turtle.Turtle()
obj10 = turtle.Turtle()
obj11 = turtle.Turtle()
obj12 = turtle.Turtle()

obj13 = turtle.Turtle()
obj14 = turtle.Turtle()
obj15 = turtle.Turtle()
obj16 = turtle.Turtle()
obj17 = turtle.Turtle()
obj18 = turtle.Turtle()

obj19 = turtle.Turtle()
obj20 = turtle.Turtle()
obj21 = turtle.Turtle()
obj22 = turtle.Turtle()
obj23 = turtle.Turtle()
obj24 = turtle.Turtle()


# _______________________

# Object creator
def object(shape,coler,colition,name,x,y, stop):
    
    if stop == 0:
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
    



li = []
# Don't worry about this
for i in range(len(which(stop))):
    li.append((which(stop)[i])[0])
    
    li.append((which(stop)[i])[1])
    print(li)
    
# Main start function
def start(speed, movement,chunk,offset,stop,li):
    playermove(speed,movement,"No",offset,stop,li)




player.penup()
player.left(90)

stop = 1
# Main loop
while True:
    start(1,10, 1, 23.9,stop,li)
    stop = 0
    


