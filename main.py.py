#Genshin Wish Sim
#Python3
import random

fiveStarPity = 0
fourStarPity = 0
f5starPity = False
f4sPity = False
newlist= []

def wishsim():
    #Items
    banner5Stars = ["Hu Tao"]
    standard5Stars = ["Jean", "Diluc", "Qiqi", "Mona", "Keqing"]
    banner4Stars = ["Thoma", "Sayu", "Diona"]
    standard4Stars = ["Pending"]

    #Pity
    global fiveStarPity
    global fourStarPity
    global f5starPity
    global f4sPity
    global newlist
    wish = random.randint(1,10000)

    #Mods
    firstwish = True

    #loop?
    looptillget = True

    #WishTypes
    #first wish on new pity
    def firstofpity():

        global f5starPity #Non local so I can access outside nested
        global f4sPity
        global fiveStarPity
        global fourStarPity

        if (wish in (range(300) or fiveStarPity == 90)):
            fifty = random.randint(1,2)
            if fifty == 1 or f5starPity == True:
                f5starPity = False
                fiveStarPity = 0
                fourStarPity = 0
                return(banner5Stars[0])
            if fifty == 2:
                f5starPity = True
                fiveStarPity = 0
                fourStarPity = 0
                return(standard5Stars[random.randint(0,4)])

        elif (wish in (range(301,1760) or fourStarPity == 10)):
            fifty = random.randint(1,2)
            if fifty == 1 or f4sPity == True:
                f4sPity == False
                fiveStarPity += 1
                fourStarPity = 0
                return(banner4Stars[random.randint(0,2)])
            if fifty == 2:
                f4sPity = True
                fiveStarPity+=1
                fourStarPity = 0
                return(standard4Stars[0])
                
        elif (wish in range(1760, 10000)):
            fiveStarPity += 1
            fourStarPity += 1
            return("Common Item")


    
    newlist.append(firstofpity())


    #standardroll
    # def regularroll():
    #     if (wish in (range(160))):
    #         fifty = random.randint(1,2)
    #         print(fifty)
    #         if fifty == 1 or fstarPity == 1:
    #             fiftypity = 0
    #             return(banner5Stars[0])
    #         if fifty == 2:
    #             fiftypity = 1
    #             return(standard5Stars[random.randint(0,4)])
        






    # print(wish)
    
    # if fiveStarPity == 0 & firstwish == True:
    #     firstofpity()

    # elif fiveStarPity >= 0:
    #     if (wish in (range())):
    #         fifty = random.randint(1,2)
    #         print(fifty)
    #         if fifty == 1 or fiftypity == 1:
    #             return(banner5Stars[0])
    #         if fifty == 2:
    #             return(standard5Stars[random.randint(0,4)])
    
wishcount = 90
while wishcount > 0:
    wishsim()
    wishcount = wishcount-1
    print(wishcount)

print(newlist)
            
