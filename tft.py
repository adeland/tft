#possible commands:
#level, roll, purchase, move to battle, check current team
#need dictionary for all units
#make a probability for each unit on each level
#a counter for each unit currently held + bench functionality, a level up unit functionality.
#different traits and items
#classes for items
#stage functionality, neutral rounds, streak functionality
#maybe just randomized winning and losing because it would be too difficult to implement actual battle

#class for each unit and their types
class unit:

    def __init__(self, name, cost, trait1, trait2, trait3):
    
        self.name = name
        self.cost = cost
        self.trait1 = trait1
        self.trait2 = trait2
        self.trait3 = trait3

#creating all the different units
#1 cost units
cassiopeia = unit("Cassiopeia", 1, "Noxus", "Shurima", "Invoker")
chogath = unit("Cho'Gath", 1, "Void", "Bruiser", None)
graves = unit("Graves", 1, "Bilgewater", "Gunner", "Rogue")
illaoi = unit("Illaoi", 1, "Bilgewater", "Bastion", None)
irelia = unit("Irelia", 1, "Ionia", "Challenger", None)
jhin = unit("Jhin", 1, "Ionia", "Vanquisher", None)
kayle = unit("Kayle", 1, "Demacia", "Slayer", None)
malzahar = unit("Malzahar", 1, "Void", "Sorcerer", None)
milio = unit("Milio", 1, "Ixtal", "Invoker", None)
orianna = unit("Orianna", 1, "Piltover", "Sorcerer", None)
poppy = unit("Poppy", 1, "Demacia", "Bastion", None)
renekton = unit("Renekton", 1, "Shurima", "Bruiser", None)
samira = unit("Samira", 1, "Noxus", "Challenger", None)

#2 cost units
ashe = unit("Ashe", 2, "Freljord", "Vanquisher", None)
galio = unit("Galio", 2, "Demacia", "Invoker", None)
jinx = unit("Jinx", 2, "Zaun", "Gunner", None)
kassadin = unit("Kassadin", 2, "Void", "Bastion", None)


#units dictionary with key being the unit name and value being the unit cost

units = {}
bench = {}
curr_gold = 0

