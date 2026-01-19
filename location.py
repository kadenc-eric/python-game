from curses import COLOR_BLACK


class Enemy:
    """Enemy class for combat encounters"""
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.max_health = health
        self.attack = attack
    
    def take_damage(self, amount):
        """Reduce enemy health by damage amount"""
        self.health = max(0, self.health - amount)
        return self.health <= 0
    
    def attack_player(self, player):
        """Enemy attacks the player"""
        import random
        # Calculate damage with some randomness (80% to 120% of attack power)
        damage = int(self.attack * random.uniform(0.8, 1.2))
        # Reduce damage by player's defense
        actual_damage = max(1, damage - player.defense)
        is_dead = player.take_damage(actual_damage)
        print(f"{self.name} attacks {player.name} for {actual_damage} damage!")
        if is_dead:
            print(f"{player.name} has been defeated!")
        else:
            print(f"{player.name} has {player.health}/{player.max_health} HP remaining.")
        return is_dead


class Location:
    """Base class for all game locations"""
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.enemies = []
        self.items = []
        
    def add_enemy(self, enemy):
        """Add an enemy to this location"""
        self.enemies.append(enemy)
    
    def add_item(self, item):
        """Add an item to this location"""
        self.items.append(item)


class Mosty_Mire(Location):
    """Swamp location - murky, dangerous waters"""
    def __init__(self):
        super().__init__(
            name="Mosty Mire",
            description="A murky, fog-covered swamp with dark waters. Strange creatures lurk beneath the surface."
        )
        self.hazard = "quicksand"  # Special hazard
        self.visibility = "low"
        # Add coba enemy for later in the game
        loki = Enemy("loki", health=150, attack=50)
        self.enemies.append(loki)
        
    def get_description(self):
        return f"{self.description} The air is thick with fog, making it hard to see."


class Pleasnat_Park(Location):
    """Forest location - dense woodland"""
    def __init__(self):
        super().__init__(
            name="Pleasant Park",
            description="A dense, ancient forest with tall trees and winding paths. Birds chirp overhead."
        )
        self.tree_cover = "dense"
        self.visibility = "medium"

        peely = Enemy("peely", health=150, attack=50)
        self.enemies.append(peely)
        
    def get_description(self):
        return f"{self.description} Sunlight filters through the canopy above."


class Tilted_Towers(Location):
    """City location - bustling urban area"""
    def __init__(self):
        super().__init__(
            name="Tilted Towers",
            description="A bustling city with stone buildings, busy markets, and friendly townspeople."
        )
        self.has_shops = True
        self.has_inn = True
        self.population = "high"
        self.visibility = "high"

        Coba = Enemy("coba", health=150, attack=50)
        self.enemies.append(Coba)
        
    def get_description(self):
        return f"{self.description} You can hear merchants calling out their wares."


class Salty_Springs(Location):
    """Desert location - hot, arid wasteland"""
    def __init__(self):
        super().__init__(
            name="Salty Springs",
            description="A vast, scorching desert with endless sand dunes. The sun beats down mercilessly."
        )
        self.hazard = "sandstorm"
        self.water_sources = False
        self.visibility = "high" 
        
        mitus = Enemy("mitus", health=150, attack=50)
        self.enemies.append(mitus) # Clear skies but harsh conditions
        
    def get_description(self):
        return f"{self.description} You must be careful not to run out of water in this heat."


class Greasy_Grove(Location):
    """Village location - small, peaceful settlement"""
    def __init__(self):
        super().__init__(
            name="Greasy Grove",
            description="A small, peaceful village with friendly villagers, a tavern, and basic shops."
        )
        self.has_tavern = True
        self.has_basic_shops = True
        self.population = "medium"
        self.visibility = "high"
        
        Omega = Enemy("omega", health=150, attack=50)
        self.enemies.append(Omega)


    def get_description(self):
        return f"{self.description} Villagers greet you warmly as you pass by."

class Loot_Lake(Location):
    """Loot Lake location - mysterious lake with hidden treasures"""
    def __init__(self):
        super().__init__(
            name="Loot Lake",
            description="A mysterious lake with crystal clear waters. Legends say treasures are hidden beneath its surface."
        )
        self.has_water = True
        self.can_swim = True
        self.visibility = "high"
        
    def get_description(self):
        return f"{self.description} The water shimmers in the sunlight, calling to adventurers."
