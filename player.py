class Player:
    """Base player class with core attributes"""
    def __init__(self, name, character_class="adventurer"):
        self.name = name
        self.character_class = character_class
        self.health = 100
        self.max_health = 100
        self.attack = 0  # Will be set by weapon choice
        self.defense = 0  # Will be set by protection choice
        self.inventory = []
        self.has_golden_key = False
        self.weapon = None
        self.protection = None
        self.lives = 3  # Player starts with 3 lives
        
    def add_item(self, item):
        """Add an item to inventory"""
        self.inventory.append(item)
        print(f"{self.name} obtained {item}!")

    
    def take_damage(self, amount):
        """Reduce health by damage amount"""
        self.health = max(0, self.health - amount)
        return self.health <= 0
    
    def heal(self, amount):
        """Restore health"""
        self.health = min(self.max_health, self.health + amount)
        print(f"{self.name} healed {amount} HP! Health: {self.health}/{self.max_health}")
    
    def choose_weapon(self):
        """Choose a weapon - affects attack power"""
        print("\n=== Choose Your Weapon ===")
        print("[1] Sword")
        print("[2] Staff")
        print("[3] Dagger")
        
        choice = input("\nEnter your weapon choice (1, 2, or 3): ").strip()
        
        if choice == "1":
            self.weapon = "Sword"
            self.attack = 75
            self.add_item("Sword")
            print(f"\n{self.name} equipped the Sword!")
            print("The Sword grants you +75 Attack power!")
        elif choice == "2":
            self.weapon = "Staff"
            self.attack = 25
            self.add_item("Staff")
            print(f"\n{self.name} equipped the Staff!")
            print("The Staff grants you +25 Attack power!")
        elif choice == "3":
            self.weapon = "Dagger"
            self.attack = 50
            self.add_item("Dagger")
            print(f"\n{self.name} equipped the Dagger!")
            print("The Dagger grants you +50 Attack power!")
        else:
            print("Invalid choice. You start with no weapon.")
            self.weapon = "None"
            self.attack = 15  # Default weak attack
            print(f"\n{self.name} has no weapon equipped.")
            print("You have +15 Attack power (default).")
    
    def choose_protection(self):
        """Choose protection/armor - affects defense"""
        print("\n=== Choose Your Protection ===")
        print("[1] Shield")
        print("[2] Armor")
        print("[3] Cloak")
        
        choice = input("\nEnter your protection choice (1, 2, or 3): ").strip()
        
        if choice == "1":
            self.protection = "Shield"
            self.defense = 75
            self.add_item("Shield")
            print(f"\n{self.name} equipped the Shield!")
            print("The Shield grants you +75 Defense!")
        elif choice == "2":
            self.protection = "Armor"
            self.defense = 50
            self.max_health += 20
            self.health += 20
            self.add_item("Armor")
            print(f"\n{self.name} equipped the Armor!")
            print("The Armor grants you +50 Defense and +20 Max Health!")
        elif choice == "3":
            self.protection = "Cloak"
            self.defense = 100
            self.add_item("Cloak")
            print(f"\n{self.name} equipped the Cloak!")
            print("The Cloak grants you +100 Defense!")
        else:
            print("Invalid choice. You start with no protection.")
            self.protection = "None"
            self.defense = 2  # Default weak defense
            print(f"\n{self.name} has no protection equipped.")
            print("You have +2 Defense (default).")
    
    def attack_enemy(self, enemy):
        """Attack an enemy and deal damage"""
        import random
        # Calculate damage with some randomness (80% to 120% of attack power)
        damage = int(self.attack * random.uniform(0.8, 1.2))
        is_dead = enemy.take_damage(damage)
        print(f"{self.name} attacks {enemy.name} for {damage} damage!")
        if is_dead:
            print(f"{enemy.name} has been defeated!")
        else:
            print(f"{enemy.name} has {enemy.health}/{enemy.max_health} HP remaining.")
        return is_dead
    