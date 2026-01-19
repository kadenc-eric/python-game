import tkinter as tk
from location import Greasy_Grove, Mosty_Mire, Pleasnat_Park
from player import Player

name = input("Hello! Enter your name to begin: ")

# Create player instance
player = Player(name)

print(f"Hello {name}, you have been chosen to set forth on a journey of rescue! Our friend Jonsey has been taken by a man named Coba. Coba has Jonsey imprisoned in a city near by. Your job is to journey to this city and free Jonsey. But there is one last thing... you will need a golden key to free our friend...good luck!")

print(f"\nYour starting spot is the village, Travis Scott says he can give you a ride to Mosty Mire, will you go? Or take the bus to a random location?")

print("\n[1] Ride with Travis Scott to Mosty Mire")
print("[2] Take the bus to a random location")

choice = input("\nEnter your choice (ride with Travis or take the bus): ").strip()

if choice == "ride with travis" or choice == "1":
    print(f"\n{name} decides to go with Travis Scott to Mosty Mire!")
    current_location = Mosty_Mire()
    print(f"You arrive at Mosty Mire!")
elif choice == "take the bus" or choice == "2":
    print(f"\n{name} decides to take the bus to a random location!")
    current_location = Greasy_Grove()
    print(f"The bus drops you off at an unexpected location...")
else:
    print(f"\nInvalid choice. {name} must choose ride with travis or take the bus.")
    current_location = None

# After arriving at location, meet enemy and choose equipment
if current_location and current_location.enemies:
    print(f"\n{current_location.get_description()}")
    enemy = current_location.enemies[0]  # Get the first enemy at this location
    print(f"\n⚠️  DANGER! {enemy.name.capitalize()} appears before you!")
    print(f"{enemy.name.capitalize()} has {enemy.health} HP and {enemy.attack} attack power!")
    print("\nYou need to prepare for battle! Choose your equipment quickly!")
    
    # Choose weapon
    player.choose_weapon()
    
    # Choose protection
    player.choose_protection()
    
    print(f"\n{player.name} is now ready for battle!")
    print(f"Final Stats - Attack: {player.attack}, Defense: {player.defense}, Health: {player.health}/{player.max_health}")