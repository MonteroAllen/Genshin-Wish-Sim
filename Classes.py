import random

class WishSim:
    #Member variables of a class
    #Reminder, All member functions need self passed in
    fiveStarPity = 0
    fourStarPity = 0
    wishRate = 0
    wishCount = 0
    f5starPity = False
    f4sPity = False
    firstwish = True
    pulls = []

    banner5Stars = ["Hu Tao"]
    standard5Stars = ["Jean", "Diluc", "Qiqi", "Mona", "Keqing"]
    banner4Stars = ["Thoma", "Sayu", "Diona"]
    standard4Stars = ["Pending"]

    def __init__(self, wishCount): #Code that runs when you create an object
        self.wishRate = random.randint(1,10000)
        self.wishCount = wishCount
        return

    def PopulatePulls(self):
        for i in range(self.wishCount):
            pull = self.FirstOfPity()
            self.wishRate = random.randint(1,10000)
            self.pulls.append(pull)
        return


    def FirstOfPity(self):

        #Five Star
        if (self.wishRate in (range(300) or self.fiveStarPity == 90)):
            fifty = random.randint(1,2)

            if fifty == 1 or self.f5starPity == True:
                self.f5starPity = False
                self.fiveStarPity = 0
                self.fourStarPity = 0
                return(self.banner5Stars[0])

            if fifty == 2:
                self.f5starPity = True
                self.fiveStarPity = 0
                self.fourStarPity = 0
                return(self.standard5Stars[random.randint(0,4)])

        #Four Star
        elif (self.wishRate in (range(301,1760) or self.fourStarPity == 10)):
            fifty = random.randint(1,2)

            if fifty == 1 or self.f4sPity == True:
                self.f4sPity == False
                self.fiveStarPity += 1
                self.fourStarPity = 0
                return(self.banner4Stars[random.randint(0,2)])

            if fifty == 2:
                self.f4sPity = True
                self.fiveStarPity+=1
                self.fourStarPity = 0
                return(self.standard4Stars[0])

        #Common 3 Star       
        elif (self.wishRate in range(1760, 10000)):
            self.fiveStarPity += 1
            self.fourStarPity += 1
            return("Common Item")

    