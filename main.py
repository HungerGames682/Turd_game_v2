
import turtle
import keyboard
from time import sleep
import random
stop = 0


created_turd = []
gains = []

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
hacks = False
goto_spawn_start = [1]
# For now 1 is lowest and 2 is highest... idk why you would need this, im just board
game_quality = 2

pin_locks = []
livet = []
erase_lock = []
picked_list = [["False",3921039210,145743535]]
selected_item = 0
item_holder = turtle.Turtle()
item_holder.penup()
item_holder.speed(10)
interact_dis = 24
door_interact_dis = interact_dis + 10
door_unlocked_list = []
go_throught_door_dis = 22

sc = turtle.Screen()

# All of this is addign custom skins into the game, i will have to make them tho
shape_list = ['/Users/rwilkes/vscode_projects/Turd_game_v2/sprits/bottom_pick.gif','/Users/rwilkes/vscode_projects/Turd_game_v2/sprits/pins.gif','/Users/rwilkes/vscode_projects/Turd_game_v2/sprits/stats_line.gif','/Users/rwilkes/vscode_projects/Turd_game_v2/sprits/heart.gif','/Users/rwilkes/vscode_projects/Turd_game_v2/sprits/Inventory Frame.gif','/Users/rwilkes/vscode_projects/Turd_game_v2/sprits/Lock Pick.gif','/Users/rwilkes/vscode_projects/Turd_game_v2/sprits/Selected Inventory Frame.gif']
for kjh in range(len(shape_list)):
    sc.register_shape(shape_list[kjh])

# Defines all of the skins here
bottem_lock_pick = shape_list[0]
pins_skin = shape_list[1]
stat_line_skin = shape_list[2]
heart_skin = shape_list[3]
inventory_frame_skin = shape_list[4]
lcok_pick_item_skin = shape_list[5]
selected_inventory_frame_skin = shape_list[6]


# Customize some settings here
screen = turtle.Screen()
screen.screensize(800,800)
player = turtle.Turtle()
player.shape("square")
buildspeed = 0
indecator = []

        
# Draws the stat bar line
how_obj = 1
statcolor = "black"
statyline = -300

# Defines all of the varibles for the files, just so i only have to configure this once, also gives all of the data needed
def get_level_data(level):

    if level == 0:
        dama = '/Users/rwilkes/vscode_projects/Turd_game_v2/damage.txt'
        lo = '/Users/rwilkes/vscode_projects/Turd_game_v2/lock.txt'
        obj_type = '/Users/rwilkes/vscode_projects/Turd_game_v2/type.txt'
        chest_inventory = '/Users/rwilkes/vscode_projects/Turd_game_v2/chest_give.txt'
        cords = '/Users/rwilkes/vscode_projects/Turd_game_v2/cords.txt'

    else:
        dama = '/Users/rwilkes/vscode_projects/Turd_game_v2/level_' + str(level) +'/damage.txt'
        obj_type = '/Users/rwilkes/vscode_projects/Turd_game_v2/level_' + str(level) +'/type.txt'
        lo = '/Users/rwilkes/vscode_projects/Turd_game_v2/level_' + str(level) +'/lock.txt'
        chest_inventory = '/Users/rwilkes/vscode_projects/Turd_game_v2/level_' + str(level) +'/chest_give.txt'
        cords = '/Users/rwilkes/vscode_projects/Turd_game_v2' + "/level_" + str(level) + "/cords.txt"


    return dama,obj_type,lo,chest_inventory,cords


# Draws the stat line for the game
def statline2(how_obj,stop,statcolor,statyline,buildspeed):
    # for he in range(-500,500,20):
    #     with open('obj.txt','r') as b:
    #         line = b.readlines()
    #         print(line[how_obj])
    #     line[how_obj] = turtle.Turtle()
    #     line[how_obj].speed(buildspeed)
        balls = turtle.Turtle()
        object(stat_line_skin,statcolor,player, balls,0,statyline,stop)
        
# Decides if the closest object if you can walkthrough it or not
def walkthrough_list(dis,walkthrough):

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
        f = True
        l = True
        r = True
        b = True
        
        x = player.xcor()
        y = player.ycor()
        
        obj_x = dis[1]
        obj_yy = dis[2]

        obj_x = int(obj_x)
        obj_yy = int(obj_yy)


        ny = y + 20
        nx = x - 20
        py = y - 20
        px = x + 20

        ny = int(ny)
        py = int(py)
        nx = int(nx)
        px = int(px)

    return f,l,b,r, nx,ny,px,py, x,y

    





#  Generates all of the objects list, then it will have to get sorted out
def all_obj_list(lis,dama,obj_type,lo,):
    dd =0
    ddd = 0
    for i in range(0, whole_many,2):
        
        with open(dama, 'r') as chi:
            dam = chi.readlines()
            sh = int(dam[dd])
            damage = sh
        
            dd = dd + 1
        
        with open(obj_type, 'r') as t:
            shit = t.readlines()
            shi = str(shit[ddd])
            
            shi = shi.replace("\n","")
            type_of_object = shi

            

        with open(lo, 'r') as los:
            chicks = los.readlines()
            amout_of_pins = int(chicks[ddd])
            chest_num = ddd
            ddd = ddd + 1
        
        h = i + 1
        if li[i] == "No" or li[h] == "No":
            print("")
        else:
            d1 = player.distance(li[i],li[h])
            # Chest_num also is used for doors and shit
            diss = [d1, li[i], li[h],damage,type_of_object,amout_of_pins,chest_num]
            
            
            lis.append(diss)

    return lis  



# Takes the list made by all_obj_list and then gets the closest 3, aka sorts it out
def get_closest_objectes(ls):
    close1 = min(ls)
    ind = ls.index(close1)
    ls.pop(ind)


    close2 = min(ls)
    ind = ls.index(close2)
    ls.pop(ind)

    close3 = min(ls)
    ind = ls.index(close3)
    ls.pop(ind)
    


    return close1,close2,close3
       
# Takes the objects and will return the 2 closest values
def filter_closest_objects(close1,close2,close3):
    if close1[0] == close2[0]:
        print(close1,close2)
        return(close1,close2)

    elif close1[0] == close3[0]:
        print(close1,close3)
        return(close1,close3)
    
    elif close2[0] == close3[0]:
        print(close2,close3)
        return(close2,close3)




    else:
        error("Filter Failure",0)
        return "null","null"
        

 


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

    hehe = len(all_turd_obj)
    hehe = hehe - 1
    all_turd_obj.pop(hehe)
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

    goto_spawn(level)
            
            
           
            

        
    return li, all_turd_obj



# V2, go back to origanal if it does not work
# Basicly the start of the program, controls the player and its collitions with other objects
def playermove(speed,movement,walkthrough, offset, stop,li,cur_health,level,picked_list,inventory,selected_item):
    
    # Hopfully imporved laggy ness
    lis = []
    l_and_r = False
    up_and_down = False
    eraselocks = False
    hacks = False
    
    # gets and returns all of the data from the .txt files
    dama,obj_type,lo,chest_inventory,cords = get_level_data(leavel)
 
    # Generates the entire obj_list
    lis = all_obj_list(lis,dama,obj_type,lo)
           
    close1,close2,close3 = get_closest_objectes(lis)
    # Gets All of the atributes of the closest block
    print(close1)
    print(close2)
    print(close3)
    # closest1,closest2 = filter_closest_objects(close1,close2,close3)
    # print(closest1)
    # print(closest2)
  


    # I cant replace dis, to many things of the code rely on it.
    dis = close1
    # print(dis)
  
        
    

  
    # Just here to chunk my code into functions
    f,l,b,r, nx,ny,px,py, x,y = walkthrough_list(dis,walkthrough)

    
   
    
    
    # Inside Perimiter Blocker
    error_bound =  17



    if walkthrough == "Yes":
        print("Walk")

    else:
        #This is the interact button :)
        if keyboard.is_pressed("e"):
        
         
           

            # Detects if you are close to a chest
          type_s = str(dis[4])
          type_s = type_s.replace("\n","")
          type_s = type_s.replace("_up_down","")
          type_s = type_s.replace("_left_right","")
          print(type_s)

          if dis[0] <= interact_dis and type_s == "Chest":
            fff = -1
            new_picked_list = []
              # Builds the list of locks that you have already picked
            for shits in range(0,len(picked_list)):
                    shitt = shits + 1
                    fff = fff + 1
                    holy = picked_list[fff]
                    jfk = player.distance(holy[1],holy[2])
                    goofy = [holy[0],holy[1],holy[2]]
                    goofy.insert(0,jfk)
                    new_picked_list.append(goofy)
                    
                
            chosen = min(new_picked_list)
            # Gives you the item in the cheast if it does not have a lock or something
            if dis[0] <= interact_dis and type_s == "Chest" and dis[5] == 0:
                       # Gives them items based on what is determined in the list
                            with open(chest_inventory,'r') as cinven:
                                give_what = cinven.readlines()
                                gives = give_what[dis[6]]
                                
                                
                                # Sees if the player already has that item
                                if len(gains) == 0:
                                        player.write("Gained " + str(gives))
                            
                                        inventory = give_item(gives,icon_inventory_list,inventory)
                                        sleep(1.2)
                                        player.clear()
                                        gains.append(dis[6])
                                        print(gains)


                                for help in range(len(gains)):
                                    if gains[help] == dis[6]:
                                        print("Already searched")
                                        break
                                    else:
                                
                                        player.write("Gained " + str(gives))
                            
                                        inventory = give_item(gives,icon_inventory_list,inventory)
                                        sleep(1.2)
                                        player.clear()
                                        gains.append(dis[6])
                                        print(gains)
                                        break

            #   Detects if you have the lockpick in your inventory
            if dis[0] <= interact_dis and type_s == "Chest" and dis[5] != 0:
              if inventory[0] == lcok_pick_item_skin:
                        

                print(selected_item)
                if selected_item == lcok_pick_item_skin:

                    # Detects if you have already picked this chest
                    if dis[0] <= 24 and type_s == "Chest" and chosen[1] == True and dis[1] == chosen[2] and dis[2] == chosen[3]:
                        player.write("      You have already picked this")
                        sleep(.2)
                        player.clear()
                    # Lets you pick this chest
                    elif dis[0] <= 24 and type_s == "Chest" and dis[5] != 0:
                        unlocked = lockpick(dis[5],5)
                        if unlocked == True:
                            # Gives them items based on what is determined in the list
                            with open(chest_inventory,'r') as cinven:
                                give_what = cinven.readlines()
                                gives = give_what[dis[6]]
                                player.write("Gained " + str(gives))
                            
                                inventory = give_item(gives,icon_inventory_list,inventory)
                                sleep(1.2)
                                player.clear()


                                unlockeds = [unlocked,dis[1],dis[2]]
                                picked_list.append(unlockeds)
                    
                                eraselocks = True
                        # There is no lock to pick
                    else:
                        player.write("      There is no lock to pick")
                        sleep(.2)
                        player.clear()
                else:
                    write("         Equip Lockpick",.2)           
              elif inventory[1] == lcok_pick_item_skin:

                                        

                print(selected_item)
                if selected_item == lcok_pick_item_skin:

                    # Detects if you have already picked this chest
                    if dis[0] <= 24 and type_s == "Chest" and chosen[1] == True and dis[1] == chosen[2] and dis[2] == chosen[3]:
                        player.write("      You have already picked this")
                        sleep(.2)
                        player.clear()
                    # Lets you pick this chest
                    elif dis[0] <= 24 and type_s == "Chest" and dis[5] != 0:
                        unlocked = lockpick(dis[5],5)
                        if unlocked == True:
                            # Gives them items based on what is determined in the list
                            with open(chest_inventory,'r') as cinven:
                                give_what = cinven.readlines()
                                gives = give_what[dis[6]]
                                player.write("Gained " + str(gives))
                            
                                inventory = give_item(gives,icon_inventory_list,inventory)
                                sleep(1.2)
                                player.clear()


                                unlockeds = [unlocked,dis[1],dis[2]]
                                picked_list.append(unlockeds)
                    
                                eraselocks = True
                        # There is no lock to pick
                    else:
                        write("         There is no lock to pick", .2)
                else:
                    write("         Equip Lockpick",.2)
              elif inventory[2] == lcok_pick_item_skin:
                                        

                print(selected_item)
                if selected_item == lcok_pick_item_skin:

                    # Detects if you have already picked this chest
                    if dis[0] <= 24 and type_s == "Chest" and chosen[1] == True and dis[1] == chosen[2] and dis[2] == chosen[3]:
                        player.write("      You have already picked this")
                        sleep(.2)
                        player.clear()
                    # Lets you pick this chest
                    elif dis[0] <= 24 and type_s == "Chest" and dis[5] != 0:
                        unlocked = lockpick(dis[5],5)
                        if unlocked == True:
                            # Gives them items based on what is determined in the list
                            with open(chest_inventory,'r') as cinven:
                                give_what = cinven.readlines()
                                gives = give_what[dis[6]]
                                player.write("Gained " + str(gives))
                            
                                inventory = give_item(gives,icon_inventory_list,inventory)
                                sleep(1.2)
                                player.clear()


                                unlockeds = [unlocked,dis[1],dis[2]]
                                picked_list.append(unlockeds)
                    
                                eraselocks = True
                        # There is no lock to pick
                    else:
                        player.write("      There is no lock to pick")
                        sleep(.2)
                        player.clear()
                else:
                    write("         Equip Lockpick",.2)
              else:
                player.write("          Need lock pick")
                sleep(.2)
                player.clear()
          
        #   Detects if you are close to a door
          if dis[0] <= door_interact_dis and (type_s == "Door_lr" or type_s == "Door_ud"):
          
            # Sees if you alredy unlocked it
            if door_unlocked_list.count(dis[6]) > 0:
                write("         Door already unlocked",.2)

            # Sees if you have a lock pick and its equiped
            elif dis[5] != 0 and door_unlocked_list.count(dis[6]) == 0 and selected_item == lcok_pick_item_skin:
                door_unlocked = lockpick(dis[5],5)

                if door_unlocked == True:
                    write("         Door unlocked",.2)
                    door_unlocked_list.append(dis[6])
                    eraselocks = True

            # Looks and sees if you need a lockpick
            elif inventory.count(lcok_pick_item_skin) == 0:
                write("         Need Lock pick",.2)

            # Seese if you need to select the lock pick
            elif inventory.count(lcok_pick_item_skin) > 0 and selected_item != lcok_pick_item_skin:
                write("         Select Lock pick",.2)
            
                

            else:
                write("         Door already open",.2)
                    
            


        


        # Lets you be ableto go through doors that are unlocked
        if (door_unlocked_list.count(dis[6]) == 1 and dis[0] <= go_throught_door_dis) or (dis[0] <= go_throught_door_dis and dis[5] == 0):
            player_x = player.xcor()
            player_y = player.ycor()
            if dis[4] == "Door_ud":
                up_and_down = True

            elif dis[4] == "Door_lr":
                l_and_r = True


            



        else:
        
            walkthrough = "No"
            godoor = False
            hacks = False


        

        
        # Makes the player take damage if they are close to a obj that damages them
        if dis[0] <= offset and dis[3] == 1:
            cur_health = heath_change(HCT, cur_health, -1,max_health)
            sleep(.1)

        if l_and_r == True:
            print("L and R")
            f = False
            l = False
            r = False
            b = False
           
            
        elif up_and_down == True:
            print("UP and down")
            f = False
            l = False
            r = False
            b = False
            
        else:   
            #The colition detection code, allows you to walkthrough a block or not
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
       


            # Colition part for corners
            # Top left corners
            print('\n' * 20)
            
            print(close1)
            print(close2)

            print(nx)
            print(ny)
            print(px)
            print(py)
            print('\n')
            print(x)
            print(y)
            

            # Detection for topleft corner
            if (int(dis[0]) <= offset and dis[1] == nx) and (close2[0] <= offset and close2[2] == ny):
                l = False
                f = False
                print("1")
             
            # Detection foro topright corner
            if (int(dis[0]) <= offset and dis[2] ==ny) and (close2[0] <= offset and close2[2] ==px):
                f = False
                r = False
                print("2")
                

                # Detects if you glitch through a wall
        if dis[0] <= error_bound and hacks == False and l_and_r == False and up_and_down == False and dis[4] != "Spawn":
                print('\n' * 100)
                error("Glitch Through wall",0)
                goto_spawn(level)

        
    # Makes player move and shit
    if keyboard.is_pressed("W") and f == True or up_and_down == True and keyboard.is_pressed("W"):
        
             player.forward(movement)
             held_item(selected_item,item_holder,"up")
             up_and_down = False
            


    if keyboard.is_pressed("S") and b == True or up_and_down == True and keyboard.is_pressed("S"):
            player.forward(-(movement))
            held_item(selected_item,item_holder,"down")
            up_and_down = False
            


    if keyboard.is_pressed("A") and l == True or l_and_r == True and keyboard.is_pressed("A"):
    
            x = player.xcor()
            y = player.ycor()
            x = x - movement
            player.speed(speed)
            player.goto(x,y)
            held_item(selected_item,item_holder,"left")
            l_and_r = False
            

    if keyboard.is_pressed("D") and r == True or l_and_r == True and keyboard.is_pressed("D"):
      
            x = player.xcor()
            y = player.ycor()
            x = x + movement
            player.speed(speed)
            player.goto(x,y)
            held_item(selected_item,item_holder,"right")
            l_and_r = False
            

            
    return cur_health,eraselocks,picked_list,inventory,selected_item


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
def start(speed, movement,chunk,offset,stop,li,cur_health,leavel,picked_list,inventory,selected_item):

      
        
    cur_health,eraselocks,picked_list,inventory,selected_item = playermove(speed,movement,"No",offset,stop,li,cur_health,leavel,picked_list,inventory,selected_item)
    return cur_health,eraselocks,picked_list,inventory,selected_item

# Draws the heath bar
def health_bar(x,y,max_health,cur_health):
    heath_created_turd = []
    # Creats little heath things
    HI = turtle.Turtle()
    HI.penup()
    new_x = x - 40
    HI.speed(0)
    HI.goto(new_x,y)
    HI.write("Health ")
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
        if game_quality == 1:
            b.shape("square")
            b.color("red")

        else:
            b.shape(heart_skin)
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
    if game_quality == 1:
        ls.shape("classic")
    else:
        ls.shape(pins_skin)
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
def lockpick(locks,pick_speed):
    all_lock_turd_obj = []
    pick_order = []
    choose_list = []
    hide = turtle.Turtle()
    all_lock_turd_obj.append(hide)
    erase_lock.append(hide)
    hide.shape("square")
    hide.color("white")
    hide.shapesize(50)
    locked = True
    x = -150
    y = 0
    ox = x - 180
    oy = y - 15
    tx = x + 15
    ty = y - 6
    lx = x + 15
    ly = y + 10
    lox = x
    loy = y - 50
    
    # Creates the list of all pins and stuff
    for lk in range(locks):
        choose_list.append(lk)  
    #  Chosses from the list in the code above to randomize which pin needs to be picked in what order
    for fdjakfljeoqwi in range(locks):
        r1 = random.choice(choose_list)
        choose_list.remove(r1)
        pick_order.append(r1)



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
    all_lock_turd_obj.append(wall)
    erase_lock.append(wall)
    wall.penup()
    wall.goto(lox,loy)
    wall.pendown()
    wall.left(90)
    wall.forward(50)
    wall.hideturtle()
    
    l = turtle.Turtle()
    all_lock_turd_obj.append(l)
    erase_lock.append(l)
    l.penup()
    l.goto(ox,oy)
    if game_quality == 1:
        l.shape("square")
    else:
        l.shape(bottem_lock_pick)
    l.shapesize(.5,20)
    tip = turtle.Turtle()
    erase_lock.append(tip)
    all_lock_turd_obj.append(tip)
    tip.penup()
    tx = tx -13
    ty = ty + 6
    tip.goto(tx,ty)
    if game_quality == 1:
        tip.showturtle()
    else:
        tip.hideturtle()
    tip.shape("square")
    tip.shapesize(.6,.5)
    print(pin_locks)
    lox = lox - 5
    loy = loy + 5

   

    while locked == True:
        if pick_order == []:
            print("Lock has been picked")
            break
        # AHHHHHH, i did not think designing a lock pick would be so diffacult
        # More vital stuff
        cors = []
        big_cors = []
        w = True
        s = True
        d = True
        a = True
        b = tip.xcor()
        zl = l.ycor()
        tipx = tip.xcor()
        tipy = tip.ycor()
        place = 0
            # Same thing as the colitions part of the code
        for i in range(locks):
            ll = pin_locks[i]
            xx = ll.xcor()
            yy = ll.ycor()
            cors.append(xx)
            cors.append(yy)
            

        # Same thing as the collitions part of the code, its somewhere...
        for ss in range(0,len(cors),2):
            bb = ss + 1
            xx = cors[ss]
            yy = cors[bb]
            distance = tip.distance(xx,yy)
            big = [distance,xx,yy,place]
            big_cors.append(big)
            place = place + 1
            

        pin = min(big_cors)

        # Detects if you pick ze correct pin  ye bitch
        if pin[0] <= 12:
            where = pin[3]
            if pick_order[0] == pin[3]:
                pick_order.pop(0)
            
                pin_locks[where].forward(50)
                for fjdaskfofehwqio in range(1):
                    lx = l.xcor()
                    ly = l.ycor()
                    ly= ly - 20

                    tipx = tip.xcor()
                    tipy = tip.ycor()
                    tipy = tipy - 20
                    l.goto(lx,ly)
                    tip.goto(tipx,tipy)
                    sleep(.2)
            else:
                 for fehuqwiot in range(1):
                    lx = l.xcor()
                    ly = l.ycor()
                    ly= ly - 20

                    tipx = tip.xcor()
                    tipy = tip.ycor()
                    tipy = tipy - 20
                    l.goto(lx,ly)
                    tip.goto(tipx,tipy)
                    sleep(.2)




        # whole coliition part that stops you from going outside of the lock
        # Stops you from going left
        if b <= -145:
            a = False

        # Stops you from going down
        if zl <= loy:
            s = False

        # Stops you from going up
        if zl >= -3:
            w = False

        # Stops you from moving right
        if b >= lox:
            d = False

        if keyboard.is_pressed("d") and d == True:
            l.forward(pick_speed)
            tip.forward(pick_speed)

        if keyboard.is_pressed("w") and w == True:
            lx = l.xcor()
            ly = l.ycor()
            ly = ly + pick_speed

            tipx = tip.xcor()
            tipy = tip.ycor()
            tipy = tipy + pick_speed
            l.goto(lx,ly)
            tip.goto(tipx,tipy)

        if keyboard.is_pressed("s") and s == True:
            lx = l.xcor()
            ly = l.ycor()
            ly= ly - pick_speed

            tipx = tip.xcor()
            tipy = tip.ycor()
            tipy = tipy - pick_speed
            l.goto(lx,ly)
            tip.goto(tipx,tipy)
        
        if keyboard.is_pressed("a") and a == True:
            l.forward(-(pick_speed))
            tip.forward(-(pick_speed))

    # Eraces everything after picked
    for finished in range(len(erase_lock)):
        erase_lock[finished].clear()
        erase_lock[finished].hideturtle()
        
        
    
    return True

# Builds the inventory frame and the list of icons for the inventory
def inventory_frame():
    icon_list = []
    selected_slot_list = []
    for i in range(100,400,100):
        u = turtle.Turtle()
        icon = turtle.Turtle()
        icon_list.append(icon)
        selected_slot_list.append(u)
        u.speed(0)
        icon.speed(0)
        icon.penup()
        icon.color("blue")
        

        if game_quality == 1:
            u.hideturtle()
        else:
            u.shape(inventory_frame_skin)

        u.penup()
        u.goto(i,-290)
        icon.goto(i,-290)
        icon.forward(4)
    return icon_list,selected_slot_list

# Lets you give the them the item,
# It is goofy, the skin is the item in the inventory list
def give_item(item,icon_inventory_list,inventory):
        if item == "lockpick\n":
            print("Lockpick give")
            item = lcok_pick_item_skin
        elif item == "nothing\n":
            print("give nothing")
            return inventory

        elif item == "Chest\n" or item == "Wall\n" or item == "Door\n":
            error("Bypassing fatal error: Item is a null filler aka chest,wall,door in chest_give.txt",0)
            return inventory

        else:
            error("Item is not defiened",1)
            




        if inventory[0] == "classic":
            inventory[0] = item
            icon_inventory_list[0].shape(item)
            print(inventory)

        elif inventory[1] == "classic":
            inventory[1] = item
            icon_inventory_list[1].shape(item)
            print(inventory)

        elif inventory[2] == "classic":
            inventory[2] = item
            icon_inventory_list[2].shape(item)
            print(inventory)

        else:
            error("Inventory is full",0)
        return inventory

# Got tired of writeng too many lines for each erorr message    
def error(message,fatal):
    if fatal == 1:
        print('\n' * 20)
        print("Fatal Error Code: " + str(message))
        exit()
    else:
        print('\n' * 20)
        print("Error Code: " + str(message))

# Hilights the slot specifided for ease of shit or something
def select_item(slot):
    # Lets you select and deselect items
    if slot == 1 and selected_slot_list[0].shape() == selected_inventory_frame_skin:
        selected_item = 0
        selected_slot_list[0].shape(inventory_frame_skin)
        

    elif slot == 2 and selected_slot_list[1].shape() == selected_inventory_frame_skin:
        selected_item = 0
        selected_slot_list[1].shape(inventory_frame_skin)

    elif slot == 3 and selected_slot_list[2].shape() == selected_inventory_frame_skin:
        selected_item = 0
        selected_slot_list[2].shape(inventory_frame_skin)
        
    elif slot == 1:
        selected_item = icon_inventory_list[0].shape()
        selected_slot_list[0].shape(selected_inventory_frame_skin)
        selected_slot_list[1].shape(inventory_frame_skin)
        selected_slot_list[2].shape(inventory_frame_skin)

    elif slot == 2:
        selected_item = icon_inventory_list[1].shape()
        selected_slot_list[1].shape(selected_inventory_frame_skin)
        selected_slot_list[2].shape(inventory_frame_skin)
        selected_slot_list[0].shape(inventory_frame_skin)

    elif slot == 3:
        selected_item = icon_inventory_list[2].shape()
        selected_slot_list[2].shape(selected_inventory_frame_skin)
        selected_slot_list[1].shape(inventory_frame_skin)
        selected_slot_list[0].shape(inventory_frame_skin)

    else:
        error("Funtion select_item number 'slot' invalid (1-3)",1)
    
    held_item(selected_item,item_holder,0)
    sleep(.2)
    return selected_item

# Go tiered, lets you write a message to a player
def write(message,delay): 
    player.write(message)
    sleep(delay)
    player.clear()

# Changes the held item that you are currently holding
def held_item(selected_item,item_holder,direction):
    x = player.xcor()
    y = player.ycor()

    if direction == "right":
        x = x + 20

        item_holder.goto(x,y)
    elif direction == "left":
        x = x - 20
        item_holder.goto(x,y)
    elif direction == "up":
        y = y + 20
        item_holder.goto(x,y)
    elif direction == "down":
        y = y -20
        item_holder.goto(x,y)
    elif direction == 0:
        x = x + 20
        item_holder.goto(x,y)
    
    else:
        error("Can only be 'right', 'left', 'up', 'down'",1)

    if selected_item == 0 or selected_item == "classic":
        item_holder.hideturtle()

    else:
        item_holder.shape(selected_item)
        item_holder.showturtle()

# Displays the open title for what ever in the hell I have created
def opening_titles(title,creator,code):
    # A little bit meassy or something
    word = turtle.Turtle()
    hide = turtle.Turtle()
    hide.penup()
    word.penup()
    hide.shape("square")
    hide.color("white")
    hide.shapesize(200,200)
    word.goto(0,260)
    word.write(title,align="center",font=90)
    word.goto(0,0)
    word.write("Made by " + str(creator), align="center",font=10)
    word.goto(70,250)
    word.settiltangle(50)
    word.write("Over " + str(code) + " Lines of Code!!")
    word.goto(0,-200)
    word.write("Press power button to start...",align="center")


    while True:
        if keyboard.is_pressed("space"):
            break

    word.clear()
    word.hideturtle()
    hide.hideturtle()

# Draws the lives bar or something DONT USE, bad idea 
def lives_bar(x,y,lives):
    
    
    lis = turtle.Turtle()
    livet.append(lis)
    lis.penup()
    lis.speed(0)
    new_x = x - 40
    lis.hideturtle()
    lis.goto(new_x,y)
    lis.write("Lives =  " + str(lives))
    
  

    return lives

# DONT USE, It was a bad idea
def lives_change(livet,value,lives):
    if value < 0:
        lives = lives - 1
        lis = livet[0]
        lis.clear()
        lis.write("Lives = " + str(lives))

    elif value > 0:
        lives = lives -+1
        lis = livet[0]
        lis.clear()
        lis.write("Lives = " + str(lives))

    else:
        error("Need value for lives or something", 1)

    return lives

# Just there as a place holder
def nothing():
    print("")

# Make user goto the spawn set
def goto_spawn(level):
    dama,type,lo,chest_inventory,cords = get_level_data(level)

    with open(type,'r') as jk:
        line = jk.readlines()
        ll = 0
        x = 0
        for i in range(0,len(line),1):

            y = x + 1
            
            
            if line[ll] != "Spawn\n":
                print("pass")
            elif line[ll] == "Spawn\n":
                print("spawn Detected")
                with open(cords, 'r') as c:
                    i = i * 2
                    y = i + 1
                    lines2 = c.readlines()
                    xx = lines2[i]
                    yy = lines2[y]
                    print(xx,yy)
                    player.goto(int(xx),int(yy))
                    return
            else:
                error("Spawn is not defined and or found", 1)
                    

            ll = ll + 1
            x = x + 1
        error("Spawn is not defined",1)

   



# Scraped idea
# lives = lives_bar(-280,-300,3)
# print(indecator)

# Draws the inventory frames and the turtles
icon_inventory_list,selected_slot_list = inventory_frame()
inventory = []
# Builds the inventory shit
for hh in range(3):
    j = icon_inventory_list[hh].shape()
    inventory.append(j)

# Stuff
player.penup()
player.left(90)

stop = 1
# Draws the like stat line for all of the stats 

statline2(how_obj,stop,"black",-250,0)
# Draws and creats the heath bar
HCT = health_bar(-280,-280,max_health,cur_health)

# I forgot what this does, but its basicly coconut.jpeg from TF2
li = obj_create(stop,buildspeed,many)


# Displays the opening of the game or something idk
# opening_titles("Insert 'Title' Here", "Ricker",1000)




goto_spawn(level=0)
# Main loop
# ALL BUTTONS ARE THERE FOR FEATURS THAT I CAN ADD, I WILL REMOVE THEM ONCE THEY ARE FULLY OPERATIONAL
while True:
    # ends the game if there health is zero... aka you died dumbass
    if cur_health == -1:
        print('\n' * 20)
        print("Game over")
        print("You Died bozo")
        exit()

     # Changes selected item aka lets you select the item of choic
    if keyboard.is_pressed("1"):
        selected_item = select_item(1)
    if keyboard.is_pressed("2"):
        selected_item = select_item(2)
    if keyboard.is_pressed("3"):
        selected_item = select_item(3)
              

    # Level Switch button, only temporary for testing, will make it when you go off screen of something
    if keyboard.is_pressed("T"):
        li, all_turd_obj = level_switch(stop,0,1)
     
        leavel = 1

    elif keyboard.is_pressed("esc"):
        print("Trying to make a menue of something")
    
    # Give and take away health, just here for testing feaetures
    # if keyboard.is_pressed("R"):
    #     cur_health = heath_change(HCT, cur_health, 1,max_health)
       
    #     sleep(.2)
    # if keyboard.is_pressed("F"):
    #     cur_health = heath_change(HCT, cur_health, -1,max_health)
        
    #     sleep(.2)
    

    if keyboard.is_pressed("L"):
        inventory = give_item(lcok_pick_item_skin,icon_inventory_list,inventory)

    #   lockpick(10,5)
    #   erase_lock = []
    #   pin_locks = []

        

    cur_health,eraselocks,picked_list,inventory,selected_item = start(1,10, 1, 23,stop,li,cur_health,leavel,picked_list,inventory,selected_item)
    # This happends every time a lock is picked to restart the game
    if eraselocks == True:
        erase_lock = []
        pin_locks = []
    stop = 0
    
    


