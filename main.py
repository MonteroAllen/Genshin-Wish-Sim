#Genshin Wish Sim
#Python3
from Classes import WishSim

wishCount = 90
x = WishSim(wishCount)
x.PopulatePulls()
for item in x.pulls:
    print(item)
print(x.pulls)
