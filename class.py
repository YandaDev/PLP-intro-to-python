# Main Pirate class - serves as the base for all pirates
class Pirate:
    # Set up a new pirate with basic information
    def __init__(self, name, role, bounty):
        self.name = name    # Public attribute
        self.role = role    # Public attribute
        self.__bounty = bounty  # Private attribute - Hideen bounty value

    # What happens when a pirate attacks
    def attack(self):
        print(f"{self.name} attacks with their signature move!")

    # Getter for private bounty
    def get_bounty(self):
        return f"🪙 {self.__bounty:,} Berries"

# Child class Inherits from Pirate (Straw Hat Pirates)
class StrawHatPirate(Pirate):
    def __init__(self, name, role, bounty, devil_fruit_power):
        super().__init__(name, role, bounty)  # Inherit parent attributes
        self.devil_fruit_power = devil_fruit_power  # Unique to Straw Hats

    #  Special attack using devil fruit power
    def attack(self):
        print(f"{self.name} uses {self.devil_fruit_power}!")

# Create objects/test pirates
generic_pirate = Pirate("Eustass Captain Kid", "Brawler", 470_000_000)
luffy = StrawHatPirate("Monkey D. Luffy", "Captain", 3_000_000_000, "Gomu Gomu no Pistol")

# Test how they work
generic_pirate.attack()  
luffy.attack()           
print(luffy.get_bounty())  




