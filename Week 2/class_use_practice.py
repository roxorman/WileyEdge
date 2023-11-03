class Enemy:
    def __init__(self,health, attack, energy):
        self.health = health
        self.attack = attack
        self.energy = energy
        
    def get_energy(self):
        print(self.energy)
        
    def attack_Player(self, player):
        player.health -= self.attack
        self.energy -= 5
    
    def get_health(self):
        print(self.health)
        
class StrongEnemy(Enemy):
    def __init__(self,health, attack, energy, armor):
        super().__init__(health, attack, energy)
        self.armour = armor
        
    def get_energy(self):
        print(self.energy)
        
class Player:
    def __init__(self,health, attack, energy, armor):
        self.health = health
        self.attack = attack
        self.energy = energy
        self.armor = armor
        
    def get_energy(self):
        print(self.energy)
        
    def get_health(self):
        print(self.health)
        
    def attack_Enemy(self, enemy):
        enemy.health -= self.attack
        self.energy -= 5

        
player = Player(100, 30, 20, 10)
basic_enemy = Enemy(50, 20, 10)
strong_enemy = StrongEnemy(90, 40, 20, 20)

print("You are fighting a basic enemy, followed by a strong enemy")
print("Your health is", player.health)
print("The first enemy's health is", basic_enemy.health)

print("You attack the first enemy")
player.attack_Enemy(basic_enemy)
print("The first enemy's health is", basic_enemy.health)
print("The enemy attacks you")
basic_enemy.attack_Player(player)
print("Your health is", player.health)
print("Then you attack the stronger enemy")
player.attack_Enemy(strong_enemy)
print("The stronger enemy's health is", strong_enemy.health)
print("You attack again")
player.attack_Enemy(strong_enemy)
print("The stronger enemy's health is", strong_enemy.health)
print("Your energy is low, at only ", player.energy)
print("The strong enemy attacks you")
strong_enemy.attack_Player(player)
print("Your health is", player.health)
print("You attack one last time")
player.attack_Enemy(strong_enemy)

print("You are out of energy ", player.energy, " energy remaining"  "and the enemy's health is ", strong_enemy.health, ", you have won the battle!")

