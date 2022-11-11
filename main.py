import keyboard
import turtle
stop = 0

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
    return dis0,dis1,dis2,dis3,dis4,dis5
    

# def playermove(speed,movement,walkthrough, offset, stop):
    
#     dis = which(stop)
    
  


#     f = True
#     l = True
#     r = True
#     b = True
#     if dis[0] == "Null" or walkthrough == "Yes":
#         f = True 
#         l = True
#         r = True
#         b = True
#         ny = 0
#         nx = 0
#         py = 0
#         px = 0

#     else:
        
        
#         x = player.xcor()
#         y = player.ycor()
        
#         ny = y + 20
#         nx = x - 20
#         py = y - 20
#         px = x + 20

      
    
#     # Prevents going through objects
#     if dis[0] <offset and dis[2] ==ny and walkthrough == "No":
#         f = False

#     elif dis[0] <offset and dis[1] == nx and walkthrough == "No":
#         l = False

#     elif dis[0] <offset and dis[2] == py and walkthrough == "No":
#         b = False
#     elif dis[0] <offset and dis[1] == px and walkthrough == "No":
#         r = False

# # NOTE TO SELF, ADD INDEVIDUAL DETECTIONS
   
  
#     if key == "w" and f == True:
#         player.forward(movement)

#     if key == "s" and b == True:
#         player.forward(-(movement))

#     if key == "a" and l == True:
#         x = player.xcor()
#         y = player.ycor()
#         x = x - movement
#         player.speed(speed)
#         player.goto(x,y)

#     if key == "d" and r == True:
#         x = player.xcor()
#         y = player.ycor()
#         x = x + movement
#         player.speed(speed)
#         player.goto(x,y)

def dis(li):
    # TRYING A NOTHER WAY, ADD 


# V2, go back to origanal if it doesnot work
def playermove(speed,movement,walkthrough, offset, stop,li):
    
    # Hopfully imporved laggy ness

    # Creates the list in dis, x,y formate
    mi = []
    full = []
    # for help in range(len(which(stop))):
    #     ny = help + 1
    #     dist = player.distance((li[help],li[ny]))
    #     x = li[help]
    #     y = li[ny]
    #     full.append(dist)
    #     full.append(x)
    #     full.append(y)
    #     print(full)


    # For loop for object positions shit balls
    # for de in range(len(which(stop))):
    #     new = de + 1
    #     mi.append(player.distance(li[de],li[new]))
       

      
    mi.append(player.distance((li[0],li[1])))
    mi.append(li[0])
    mi.append(li[1])

    mi.append(player.distance((li[2],li[3])))
    mi.append(li[2])
    mi.append(li[3])

    mi.append(player.distance((li[4],li[5])))
    mi.append(li[4])
    mi.append(li[5])

    mi.append(player.distance((li[6],li[7])))
    mi.append(li[6])
    mi.append(li[7])

    mi.append(player.distance((li[8],li[9])))
    mi.append(li[8])
    mi.append(li[9])

    mi.append(player.distance((li[10],li[11])))
    mi.append(li[10])
    mi.append(li[11])
    print(mi)

    dis1 = [li[0],li[1]]
    dis2 = [li[2],li[3]]
    dis3 = [li[4],li[5]]
    dis4 = [li[6],li[7]]
    dis5 = [li[8],li[9]]
    dis6 = [li[10],li[11]]
    
    dis = min(mi)
   
    
    print(dis)
    f = True
    l = True
    r = True
    b = True
    
   
     

# NOTE TO SELF, ADD INDEVIDUAL DETECTIONS
   
  
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
    start(5,10, 1, 23,stop,li)
    stop = 0
    


