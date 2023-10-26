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
def initial():
    print("Welcome to TTFT, Text Teamfight Tactics!")

class unit:

    def __init__(self, name, cost, trait1, trait2, trait3):
    
        self.name = name
        self.cost = cost
        self.trait1 = trait1
        self.trait2 = trait2
        self.trait3 = trait3
#class for the game
class tftgame:

    def __init__(self):

        self.players = []
        self.round = 0
        self.unit_pool = {}
        self.item_pool = {}
        self.streak = 0

    def add_player(self, player_name):

        player = Player(player_name)
        self.players.append(Player)

    def initialize_unit_pool(self):

        pass

    def initialize_item_pool(self):

        pass

    def start_round(self):

        self.round += 1
        self.initialize_unit_pool()
        self.initialize_item_pool()
        self.distribute_units()
        self.distribute_items()
        self.prepare_players()

    def distribute_units(self):

        pass

    def distribute_items(self):

        pass

    def prepare_players(self):
        
        for player in self.players:
            player.take_actions()

    def check_game_over(self):

        if self.health <= 0:
            pass
        pass
    def play_game(self):
        
        while not self.check_game_over():
            self.start_round()
            self.battle()
            self.update_streaks()
            self.level_up_players()

class Player():
    
    def __init__(self, name):
        self.name = name
        self.gold = 0
        self.health = 100
        self.units = []
        self.bench = []

    def take_actions(self):
        pass

    def level_up(self):
        pass
    
    def surrender(self):
        pass
    
def main():
    game = tftgame()


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
naafiri = unit("Naafiri", 2, "Darkin", "Shurima", "Challenger")
qiyana = unit("Qiyana", 2, "Ixtal", "Slayer", "Rogue")
sett = unit("Sett", 2, "Ionia", "Juggernaut", None)
soraka = unit("Soraka", 2, "Targon", "Invoker", None)
swain = unit("Swain", 2, "Noxus", "Strategist", "Sorcerer")
taliyah = unit("Taliyah", 2, "Shurima", "Multicaster", None)
twisted_fate = unit("Twisted Fate", 2, "Bilgewater", "Multicaster", None)
vi = unit("Vi", 2, "Piltover", "Bruiser", None)
warwick = unit("Warwick", 2, "Zaun", "Juggernaut", "Challenger")

#3 cost units
darius = unit("Darius", 3, "Noxus", "Juggernaut", "Vanquisher")
ekko = unit("Ekko", 3, "Zaun", "Piltover", "Rogue")
jayce = unit("Jayce", 3, "Piltover", "Gunner", None)
karma = unit("Karma", 3, "Ionia", "Invoker", None)
katarina = unit("Katarina", 3, "Noxus", "Rogue", None)
miss_fortune = unit("Miss Fortune", 3, "Bilgewater", "Strategist", None)
nautilus = unit("Nautilus", 3, "Bilgewater", "Juggernaut", None)
neeko = unit("Neeko", 3, "Ixtal", "Bastion", None)
quinn = unit("Quinn", 3, "Demacia", "Slayer", None)
reksai = unit("Rek'Sai", 3, "Void", "Bruiser", "Slayer")
sona = unit("Sona", 3, "Demacia", "Multicaster", None)
taric = unit("Taric", 3, "Targon", "Bastion", "Sorcerer")
velkoz = unit("Vel'Koz", 3, "Void", "Multicaster", "Sorcerer")

#4 cost units
aphelios = unit("Aphelios", 4, "Targon", "Gunner", None)
azir = unit("Azir", 4, "Shurima", "Strategist", None)
fiora = unit("Fiora", 4, "Demacia", "Challenger", None)
jarvan = unit("Jarvan IV", 4, "Demacia", "Strategist", None)
kaisa = unit("Kai'sa", 4, "Void", "Challenger", None)
mordekaiser = unit("Mordekaiser", 4, "Noxus", "Slayer")
nasus = unit("Nasus", 4, "Shurima", "Juggernaut", None)
nilah = unit("Nilah", 4, "Bilgewater", "Vanquisher", None)
sejuani = unit("Sejuani", 4,  "Freljord", "Bruiser", None)
shen = unit("Shen", 4, "Ionia", "Bastion", "Invoker")
silco = unit("Silco", 4, "Zaun", "Sorcerer", None)
xayah = unit("xayah", 4, "Ionia", "Vanquisher", None)

#5 cost units
aatrox = unit("Aatrox", 5, "Darkin", "Slayer", "Juggernaut")
ahri = unit("Ahri", 5, "Ionia", "Sorcerer", None)
belveth = unit("Bel'Veth", 5, "Empress", "Void", None)
gangplank = unit("Gangplank", 5, "Bilgewater", "Gunner", "Reaver King")
heimerdinger = unit("Heimerdinger", 5, "Piltover", "Technogenius", None)
ksante = unit("K'sante", 5, "Shurima", "Bastion", None)
ryze = unit("Ryze", 5, "Wanderer", "Invoker", None)
sion = unit("Sion", 5, "Noxus", "Bruiser", None)

if __name__ = "__main__":
    main()
    initial()
    prompt = str(input("Do you want to play?"))
    if prompt == "Yes" or "yes" or "y":
        self.name = str(input("Type your username"))
    else:
        print("Have a nice day!")
        quit()



#starting off, how many stages will there be? should there be different stages like set 9 or galaxies
