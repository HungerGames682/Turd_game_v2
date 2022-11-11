import keyboard
import turtle


player = turtle.Turtle()
player.shape("square")

def which(stop):

    # Put any new objects here

    dis0 = object("square","blue",player, obj1,-50,20,stop)
    dis1 = object("square","blue",player, obj2, -30,20,stop)
    dis2 = object("square","blue",player, obj3, -10,20,stop)
    dis3 = object("square","blue",player, obj4, 10,20,stop)
    dis4 = object("square","blue",player, obj5, 30,20,stop)
    dis5 = object("square","blue",player, obj6, 50,20,stop)
    
   
    mins = min([dis0,dis1,dis2,dis3,dis4,dis5])
    return mins
    

def playermove(speed,movement,walkthrough, offset, stop):
    
    dis = which(stop)
    
  


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

      
    
    # Prevents going through objects
    if dis[0] <offset and dis[2] ==ny and walkthrough == "No":
        f = False

    elif dis[0] <offset and dis[1] == nx and walkthrough == "No":
        l = False

    elif dis[0] <offset and dis[2] == py and walkthrough == "No":
        b = False
    elif dis[0] <offset and dis[1] == px and walkthrough == "No":
        r = False


    key = keyboard.read_key()
    print(key)
    if key == "w" and f == True:
        player.forward(movement)

    if key == "s" and b == True:
        player.forward(-(movement))

    if key == "a" and l == True:
        x = player.xcor()
        y = player.ycor()
        x = x - movement
        player.speed(speed)
        player.goto(x,y)

    if key == "d" and r == True:
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
        return dis, x,y
    



    
# Main start function
def start(speed, movement,chunk,offset,stop):
    playermove(speed,movement,"No",offset,stop)




player.penup()
player.left(90)

stop = 1
# Main loop
while True:
    start(5,10, 1, 23,stop)
    stop = 0
    


