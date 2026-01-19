import tkinter as tk
import random
from location import Greasy_Grove, Mosty_Mire, Pleasnat_Park
from player import Player

name = input("Hello! Enter your name to begin: ")

# Create player instance
player = Player(name)

print(f"Hello {name}, you have been chosen to set forth on a journey of rescue! Our friend Jonsey has been taken by a man named Coba. Coba has Jonsey imprisoned in Tilted Towers. Your job is to journey to this city and free Jonsey. But there is one last thing... you will need a golden key to free our friend...good luck!")

print(f"\n⚠️  IMPORTANT: You have 3 LIVES. If you are defeated in battle 3 times, the game will end and you must restart from the beginning. Choose your battle strategies wisely!")
print(f"Current Lives: {player.lives} ❤️")

print(f"\nYour starting spot is the village, Travis Scott says he can give you a ride to Mosty Mire, will you go? Or take the bus to a random location?")

print("\n[1] Ride with Travis Scott to Mosty Mire")
print("[2] Take the bus to a random location")

current_location = None
while current_location is None:
    choice = input("\nEnter your choice (ride with Travis or take the bus): ").strip().lower()
    
    if choice == "ride with travis" or choice == "1" or choice == "ride":
        print(f"\n{name} decides to go with Travis Scott to Mosty Mire!")
        current_location = Mosty_Mire()
        print(f"You arrive at Mosty Mire!")
    elif choice == "take the bus" or choice == "2" or choice == "bus":
        print(f"\n{name} decides to take the bus to a random location!")
        current_location = Greasy_Grove()
        print(f"You arrive at {current_location.name}!")
    else:
        print(f"\n⚠️  Invalid choice. Please enter '1' or 'ride with travis' to go with Travis, or '2' or 'take the bus' to take the bus.")

# After arriving at location, meet enemy and choose equipment
if current_location and current_location.enemies:
    enemy = current_location.enemies[0]  # Get the first enemy at this location
    print(f"\n⚠️  DANGER! {enemy.name.capitalize()} appears before you!")
    print(f"{enemy.name.capitalize()} has {enemy.health} HP and {enemy.attack} attack power!")
    print("\nYou need to prepare for battle! Choose your equipment quickly!")
    
    # Choose weapon
    player.choose_weapon()
    
    # Choose protection
    player.choose_protection()
    
    print(f"\n{player.name} is now ready for battle! The true power of your equipment will be revealed in combat...")
    
    # Battle system with strategies
    battle_won = False
    original_enemy_health = enemy.health
    
    while not battle_won:
        # Check if player has run out of lives
        if player.lives <= 0:
            print(f"\n{'='*60}")
            print("💀 GAME OVER 💀")
            print(f"{'='*60}")
            print(f"{player.name} has been defeated 3 times!")
            print("You have run out of lives. The game must restart from the beginning.")
            print(f"{'='*60}")
            exit()  # End the game
        
        print(f"\n{'='*50}")
        print(f"BATTLE STATUS:")
        print(f"{player.name}: {player.health}/{player.max_health} HP | Lives: {player.lives} ❤️")
        print(f"{enemy.name.capitalize()}: {enemy.health}/{enemy.max_health} HP")
        print(f"{'='*50}")
        
        print("\n=== Choose Your Battle Strategy ===")
        print("[1] Aggressive Attack - Charge forward with all your might!")
        print("[2] Defensive Stance - Wait for the perfect moment to strike!")
        
        strategy = None
        while strategy not in ["1", "2"]:
            strategy = input("\nEnter your strategy choice (1 or 2): ").strip()
            if strategy not in ["1", "2"]:
                print("⚠️  Invalid choice. Please enter '1' for Aggressive Attack or '2' for Defensive Stance.")
        
        if strategy == "1":
            # Aggressive strategy - always leads to losing
            print(f"\n{player.name} charges forward aggressively!")
            print(f"{enemy.name.capitalize()} sees the opening and counters with a devastating blow!")
            
            # Enemy does massive damage (bypasses some defense)
            massive_damage = int(enemy.attack * 2.5)  # Much more damage
            actual_damage = max(1, massive_damage - (player.defense // 2))  # Defense is less effective
            player.health = max(0, player.health - actual_damage)
            print(f"{enemy.name.capitalize()} strikes with overwhelming force for {actual_damage} damage!")
            print(f"{player.name} has {player.health}/{player.max_health} HP remaining.")
            
            # Health warning messages
            if player.health <= player.max_health * 0.25:
                print("⚠️  WARNING: Health is critically low!")
            elif player.health <= player.max_health * 0.5:
                print("⚠️  WARNING: Health is below 50%!")
            
            if player.health <= 0:
                player.lives -= 1
                print(f"\n💀 {player.name} has been defeated!")
                print("The aggressive strategy was too reckless!")
                print(f"❤️  Lives remaining: {player.lives}/3")
                
                # Lives warning
                if player.lives == 1:
                    print("⚠️  WARNING: Only 1 life remaining! Be careful!")
                elif player.lives == 2:
                    print("⚠️  WARNING: 2 lives remaining!")
                if player.lives > 0:
                    print("The battle restarts...")
                    player.health = player.max_health
                    enemy.health = original_enemy_health
                    print(f"{player.name} and {enemy.name.capitalize()} are both restored to full health.")
                continue  # Restart the battle loop or end game
            
            # Player attacks but enemy is ready
            print(f"\n{player.name} tries to attack, but {enemy.name.capitalize()} is ready!")
            player.attack_enemy(enemy)
            
            # Enemy finishes the player off
            print(f"\n{enemy.name.capitalize()} delivers the final blow!")
            damage_taken = enemy.attack_player(player)
            
            if damage_taken or player.health <= 0:
                player.lives -= 1
                print(f"\n💀 {player.name} has been defeated!")
                print("The aggressive strategy was too reckless!")
                print(f"❤️  Lives remaining: {player.lives}/3")
                
                # Lives warning
                if player.lives == 1:
                    print("⚠️  WARNING: Only 1 life remaining! Be careful!")
                elif player.lives == 2:
                    print("⚠️  WARNING: 2 lives remaining!")
                if player.lives > 0:
                    print("The battle restarts...")
                    player.health = player.max_health
                    enemy.health = original_enemy_health
                    print(f"{player.name} and {enemy.name.capitalize()} are both restored to full health.")
                continue  # Restart the battle loop or end game
                
        elif strategy == "2":
            # Defensive strategy - leads to winning
            print(f"\n{player.name} takes a defensive stance, waiting for the perfect moment!")
            print(f"{enemy.name.capitalize()} attacks, but {player.name} blocks it with {player.protection}!")
            print(f"The defense reduces the damage significantly!")
            
            # Enemy attacks but defense is very effective
            damage_taken = enemy.attack_player(player)
            
            # Health warning messages
            if not damage_taken:
                if player.health <= player.max_health * 0.25:
                    print("⚠️  WARNING: Health is critically low!")
                elif player.health <= player.max_health * 0.5:
                    print("⚠️  WARNING: Health is below 50%!")
            
            if damage_taken:
                player.lives -= 1
                print(f"\n💀 {player.name} has been defeated!")
                print(f"❤️  Lives remaining: {player.lives}/3")
                
                # Lives warning
                if player.lives == 1:
                    print("⚠️  WARNING: Only 1 life remaining! Be careful!")
                elif player.lives == 2:
                    print("⚠️  WARNING: 2 lives remaining!")
                if player.lives > 0:
                    print("The battle restarts...")
                    player.health = player.max_health
                    enemy.health = original_enemy_health
                    print(f"{player.name} and {enemy.name.capitalize()} are both restored to full health.")
                continue  # Restart the battle loop or end game
            
            # Player counter-attacks with advantage (does more damage)
            print(f"\n{player.name} sees the perfect opening and strikes with precision!")
            bonus_damage = int(player.attack * 1.5)  # 50% bonus damage
            damage = int(bonus_damage * random.uniform(0.9, 1.1))
            is_dead = enemy.take_damage(damage)
            print(f"{player.name} attacks {enemy.name} for {damage} damage!")
            
            if is_dead:
                print(f"{enemy.name} has been defeated!")
                print(f"\n🎉 VICTORY! {player.name} has defeated {enemy.name.capitalize()}!")
                print(f"💎 {enemy.name.capitalize()} drops a mysterious Rift!")
                player.add_item("Rift to Pleasnat_Park")
                print("You can now use this Rift to travel to Pleasnat Park!")
                battle_won = True
                break
            else:
                print(f"{enemy.name} has {enemy.health}/{enemy.max_health} HP remaining.")
            
            # One more defensive block and counter
            print(f"\n{enemy.name.capitalize()} attacks again, but {player.name} blocks once more!")
            damage_taken = enemy.attack_player(player)
            
            # Health warning messages
            if not damage_taken:
                if player.health <= player.max_health * 0.25:
                    print("⚠️  WARNING: Health is critically low!")
                elif player.health <= player.max_health * 0.5:
                    print("⚠️  WARNING: Health is below 50%!")
            
            if damage_taken:
                player.lives -= 1
                print(f"\n💀 {player.name} has been defeated!")
                print(f"❤️  Lives remaining: {player.lives}/3")
                
                # Lives warning
                if player.lives == 1:
                    print("⚠️  WARNING: Only 1 life remaining! Be careful!")
                elif player.lives == 2:
                    print("⚠️  WARNING: 2 lives remaining!")
                if player.lives > 0:
                    print("The battle restarts...")
                    player.health = player.max_health
                    enemy.health = original_enemy_health
                    print(f"{player.name} and {enemy.name.capitalize()} are both restored to full health.")
                continue  # Restart the battle loop or end game
            
            # Final strike to finish the enemy
            print(f"\n{player.name} delivers the final blow!")
            bonus_damage = int(player.attack * 1.5)
            damage = int(bonus_damage * random.uniform(0.9, 1.1))
            is_dead = enemy.take_damage(damage)
            print(f"{player.name} attacks {enemy.name} for {damage} damage!")
            
            if is_dead:
                print(f"{enemy.name} has been defeated!")
                print(f"\n🎉 VICTORY! {player.name} has defeated {enemy.name.capitalize()}!")
                print(f"💎 {enemy.name.capitalize()} drops a mysterious Rift!")
                player.add_item("Rift to Pleasnat_Park")
                print("You can now use this Rift to travel to Pleasnat Park!")
                battle_won = True
                break
    
    # After winning, check if player has the rift
    if "Rift to Pleasnat_Park" in player.inventory:
        print(f"\n{player.name} can now travel to Pleasnat Park using the Rift!")
        print('Type "Rift" to Travel!')
        
        # Track wrong attempts
        wrong_attempts = 0
        traveled = False
        
        # Wait for player to use the Rift correctly
        while not traveled:
            # Check for game over conditions
            if player.lives <= 0:
                print(f"\n{'='*60}")
                print("💀 GAME OVER 💀")
                print(f"{'='*60}")
                print(f"{player.name} has been defeated!")
                print("You have run out of lives. The game must restart from the beginning.")
                print(f"{'='*60}")
                exit()
            
            if player.health <= 0:
                player.lives -= 1
                print(f"\n💀 {player.name} has been defeated from health loss!")
                print(f"❤️  Lives remaining: {player.lives}/3")
                
                # Lives warning
                if player.lives == 1:
                    print("⚠️  WARNING: Only 1 life remaining! Be careful!")
                elif player.lives == 2:
                    print("⚠️  WARNING: 2 lives remaining!")
                if player.lives > 0:
                    player.health = player.max_health
                else:
                    print(f"\n{'='*60}")
                    print("💀 GAME OVER 💀")
                    print(f"{'='*60}")
                    print(f"{player.name} has been defeated!")
                    print("You have run out of lives. The game must restart from the beginning.")
                    print(f"{'='*60}")
                    exit()
            
            travel_choice = input("\nEnter your choice: ").strip().lower()
            
            if travel_choice == "rift":
                print(f"\n{player.name} activates the Rift!")
                print("A swirling portal opens before you...")
                print("You step through and find yourself in a new location!")
                
                # Travel to Pleasnat_Park
                current_location = Pleasnat_Park()
                print(f"\nYou arrive at {current_location.name}!")
                
                # Meet the enemy at the new location
                if current_location.enemies:
                    enemy = current_location.enemies[0]
                    print(f"\n⚠️  DANGER! {enemy.name.capitalize()} appears before you!")
                    print(f"{enemy.name.capitalize()} has {enemy.health} HP and {enemy.attack} attack power!")
                    print(f"\n{player.name} must face this new threat!")
                    
                    # Peely encounter dialogue (only if enemy is Peely)
                    if enemy.name.lower() == "peely":
                        peely_choice_made = False
                        while not peely_choice_made:
                            # Check for game over
                            if player.lives <= 0:
                                print(f"\n{'='*60}")
                                print("💀 GAME OVER 💀")
                                print(f"{'='*60}")
                                print(f"{player.name} has been defeated!")
                                print("You have run out of lives. The game must restart from the beginning.")
                                print(f"{'='*60}")
                                exit()
                            
                            print("Before you have time to react, Peely puts you in a full box and trolls you. He proceeds to edit his wall and pump you in the head.")
                            print("He starts humping you... before he finishes you he asks what you are doing here?")
                            
                            print("\n[1] Im looking for a key")
                            print("[2] I know jonsey")
                            
                            choice = None
                            while choice not in ["1", "2", "im looking for a key", "i know jonsey", "key", "jonsey"]:
                                choice = input("\nEnter your choice (1 or 2): ").strip().lower()
                                
                                if choice not in ["1", "2", "im looking for a key", "i know jonsey", "key", "jonsey"]:
                                    print("⚠️  Invalid choice. Please enter '1' or '2'")
                            
                            if choice == "1" or choice == "im looking for a key" or choice == "key":
                                print(f"Peely did a donkey laugh then hit the griddy on you. He finishes you and you lose a life")
                                player.lives -= 1
                                print(f"❤️  Lives remaining: {player.lives}/3")
                                
                                # Lives warning
                                if player.lives == 1:
                                    print("⚠️  WARNING: Only 1 life remaining! Be careful!")
                                elif player.lives == 2:
                                    print("⚠️  WARNING: 2 lives remaining!")
                                
                                # Restore health and loop back
                                player.health = player.max_health
                                print(f"💚 {player.name} restored to full health for the rematch!")
                                print("The encounter restarts...")
                                # Loop back to the beginning of the Peely encounter
                                continue
                                
                            elif choice == "2" or choice == "i know jonsey" or choice == "jonsey":
                                print(f"\n{player.name}, Peely revives you and gives you full health. Peely wants proof you know Jonsey.")
                                player.health = player.max_health
                                print(f"💚 {player.name} restored to full health! Health: {player.health}/{player.max_health} HP")
                                
                                # Peely's quiz about Jonsey's best friend
                                quiz_correct = False
                                while not quiz_correct:
                                    # Check for game over
                                    if player.lives <= 0:
                                        print(f"\n{'='*60}")
                                        print("💀 GAME OVER 💀")
                                        print(f"{'='*60}")
                                        print(f"{player.name} has been defeated!")
                                        print("You have run out of lives. The game must restart from the beginning.")
                                        print(f"{'='*60}")
                                        exit()
                                    
                                    print(f"\nPeely asks: Who is Jonsey's best friend? Guess wrong and you lose a life")
                                    print("[1] Tfue")
                                    print("[2] Ninja")
                                    print("[3] DrDisrespect")
                                    print("[4] TimTheTatman")
                                    
                                    quiz_choice = None
                                    while quiz_choice not in ["1", "2", "3", "4", "tfue", "ninja", "drdisrespect", "timthetatman"]:
                                        quiz_choice = input("\nEnter your choice (1, 2, 3, or 4): ").strip().lower()
                                        
                                        if quiz_choice not in ["1", "2", "3", "4", "tfue", "ninja", "drdisrespect", "timthetatman"]:
                                            print("⚠️  Invalid choice. Please enter '1', '2', '3', or '4'")
                                    
                                    # Tfue is the correct answer (option 1)
                                    if quiz_choice == "1" or quiz_choice == "tfue":
                                        print(f"\n✅ Correct! {player.name} knows Jonsey's best friend is Tfue!")
                                        print(f"Peely is impressed and gives you a map to the golden key!")
                                        player.add_item("Map to Golden Key")
                                        quiz_correct = True
                                    else:
                                        player.lives -= 1
                                        print(f"\n❌ Wrong answer! Peely is disappointed. You lose a life!")
                                        print(f"❤️  Lives remaining: {player.lives}/3")
                                        
                                        # Lives warning
                                        if player.lives == 1:
                                            print("⚠️  WARNING: Only 1 life remaining! Be careful!")
                                        elif player.lives == 2:
                                            print("⚠️  WARNING: 2 lives remaining!")
                                        
                                        # Restore health and loop back
                                        player.health = player.max_health
                                        print(f"💚 {player.name} restored to full health for the rematch!")
                                        print("The quiz restarts...")
                                        continue
                                
                                # Riddle on the map
                                print(f"\n{player.name} opens the map and sees a riddle:")
                                print("🔍 RIDDLE: Like Epstein's island, secrets at the core, once stuck to the ground - then rose to the lore. What am I?")
                                
                                riddle_correct = False
                                while not riddle_correct:
                                    # Check for game over
                                    if player.lives <= 0:
                                        print(f"\n{'='*60}")
                                        print("💀 GAME OVER 💀")
                                        print(f"{'='*60}")
                                        print(f"{player.name} has been defeated!")
                                        print("You have run out of lives. The game must restart from the beginning.")
                                        print(f"{'='*60}")
                                        exit()
                                    
                                    riddle_answer = input("\nEnter your answer: ").strip().lower()
                                    
                                    # Loot Lake is the correct answer
                                    if riddle_answer == "loot lake":
                                        print(f"\n✅ Correct! The answer is Loot Lake!")
                                        print(f"Peely gives you the Golden Key!")
                                        player.add_item("Golden Key")
                                        player.has_golden_key = True
                                        riddle_correct = True
                                        
                                        # Peely pushes player in shopping cart to rescue Jonsey
                                        print(f"\n🎉 Peely is impressed with your knowledge!")
                                        print(f"Peely says: 'You've proven yourself! Let's go save Jonsey!'")
                                        print(f"\nPeely grabs a shopping cart and pushes {player.name} in it!")
                                        print(f"They race through the map, heading towards Tilted Towers where Jonsey is imprisoned...")
                                        print(f"You arrive at Tilted Towers and Peely frees Jonsey!")
                                        print(f"As you are leaving, you see Coba and his goons. You have to fight your way out of Tilted Towers with Peely and Jonsey!")
                                        
                                        # Final battle with Coba and his goons
                                        from location import Enemy
                                        final_battle_won = False
                                        coba = Enemy("Coba", health=200, attack=60)
                                        goons = Enemy("Goons", health=100, attack=40)
                                        original_coba_health = coba.health
                                        original_goons_health = goons.health
                                        
                                        while not final_battle_won:
                                            # Check for game over
                                            if player.lives <= 0:
                                                print(f"\n{'='*60}")
                                                print("💀 GAME OVER 💀")
                                                print(f"{'='*60}")
                                                print(f"{player.name} has been defeated!")
                                                print("You have run out of lives. The game must restart from the beginning.")
                                                print(f"{'='*60}")
                                                exit()
                                            
                                            print(f"\n{'='*60}")
                                            print("FINAL BATTLE - ESCAPE FROM TILTED TOWERS")
                                            print(f"{'='*60}")
                                            print(f"{player.name}: {player.health}/{player.max_health} HP | Lives: {player.lives} ❤️")
                                            print(f"Coba: {coba.health}/{coba.max_health} HP")
                                            print(f"Goons: {goons.health}/{goons.max_health} HP")
                                            print(f"{'='*60}")
                                            
                                            print("\n=== Choose Your Battle Strategy ===")
                                            print("[1] Team Attack - Coordinate with Peely and Jonsey for a combined strike!")
                                            print("[2] Distraction Tactics - Create chaos while your team escapes!")
                                            print("[3] Head-on Charge - Face Coba directly with all your might!")
                                            print("[4] Tactical Retreat - Use the Golden Key to create an escape route!")
                                            
                                            strategy = None
                                            while strategy not in ["1", "2", "3", "4"]:
                                                strategy = input("\nEnter your strategy choice (1, 2, 3, or 4): ").strip()
                                                if strategy not in ["1", "2", "3", "4"]:
                                                    print("⚠️  Invalid choice. Please enter '1', '2', '3', or '4'")
                                            
                                            if strategy == "1":
                                                # Team Attack - WINNING strategy
                                                print(f"\n{player.name} coordinates with Peely and Jonsey!")
                                                print("The three of you launch a synchronized attack!")
                                                print("Peely distracts the goons while Jonsey and you focus on Coba!")
                                                
                                                # Team does massive damage
                                                team_damage = int(player.attack * 2.0) + 50  # Bonus from teamwork
                                                coba.take_damage(team_damage)
                                                print(f"Team attack deals {team_damage} damage to Coba!")
                                                
                                                if coba.health <= 0:
                                                    print(f"\n🎉 VICTORY! Coba has been defeated!")
                                                    print(f"The goons flee in terror!")
                                                    final_battle_won = True
                                                    break
                                                else:
                                                    print(f"Coba has {coba.health}/{coba.max_health} HP remaining.")
                                                    
                                                    # Goons attack but are distracted
                                                    goon_damage = max(1, goons.attack - player.defense - 20)  # Reduced by distraction
                                                    player.health = max(0, player.health - goon_damage)
                                                    print(f"Goons attack but Peely distracts them! You take {goon_damage} damage.")
                                                    
                                                    if player.health <= 0:
                                                        player.lives -= 1
                                                        print(f"\n💀 {player.name} has been defeated!")
                                                        print(f"❤️  Lives remaining: {player.lives}/3")
                                                        if player.lives > 0:
                                                            print("The battle restarts...")
                                                            player.health = player.max_health
                                                            coba.health = original_coba_health
                                                            goons.health = original_goons_health
                                                            continue
                                                    
                                                    # Final team strike
                                                    print(f"\nPeely and Jonsey join forces for the final blow!")
                                                    final_damage = int(player.attack * 2.5) + 75
                                                    coba.take_damage(final_damage)
                                                    print(f"Final team strike deals {final_damage} damage!")
                                                    
                                                    if coba.health <= 0:
                                                        print(f"\n🎉 VICTORY! Coba has been defeated!")
                                                        print(f"The goons flee in terror!")
                                                        final_battle_won = True
                                                        break
                                            
                                            elif strategy == "2":
                                                # Distraction Tactics - WINNING strategy
                                                print(f"\n{player.name} creates chaos with distraction tactics!")
                                                print("Peely starts doing the griddy while Jonsey builds walls!")
                                                print("The confusion gives you the perfect opening!")
                                                
                                                # Distraction allows for critical hits
                                                crit_damage = int(player.attack * 2.2) + 40
                                                coba.take_damage(crit_damage)
                                                print(f"Critical strike deals {crit_damage} damage to Coba!")
                                                
                                                if coba.health <= 0:
                                                    print(f"\n🎉 VICTORY! Coba has been defeated!")
                                                    print(f"The goons flee in terror!")
                                                    final_battle_won = True
                                                    break
                                                else:
                                                    print(f"Coba has {coba.health}/{coba.max_health} HP remaining.")
                                                    
                                                    # Coba is confused, does less damage
                                                    coba_damage = max(1, coba.attack - player.defense - 15)
                                                    player.health = max(0, player.health - coba_damage)
                                                    print(f"Coba attacks but is confused! You take {coba_damage} damage.")
                                                    
                                                    if player.health <= 0:
                                                        player.lives -= 1
                                                        print(f"\n💀 {player.name} has been defeated!")
                                                        print(f"❤️  Lives remaining: {player.lives}/3")
                                                        if player.lives > 0:
                                                            print("The battle restarts...")
                                                            player.health = player.max_health
                                                            coba.health = original_coba_health
                                                            goons.health = original_goons_health
                                                            continue
                                                    
                                                    # Finish Coba
                                                    print(f"\nThe distraction worked perfectly!")
                                                    finish_damage = int(player.attack * 2.3) + 60
                                                    coba.take_damage(finish_damage)
                                                    print(f"Finishing blow deals {finish_damage} damage!")
                                                    
                                                    if coba.health <= 0:
                                                        print(f"\n🎉 VICTORY! Coba has been defeated!")
                                                        print(f"The goons flee in terror!")
                                                        final_battle_won = True
                                                        break
                                            
                                            elif strategy == "3":
                                                # Head-on Charge - LOSING strategy
                                                print(f"\n{player.name} charges head-on at Coba!")
                                                print("Coba sees the reckless attack coming and counters!")
                                                print("The goons surround you from all sides!")
                                                
                                                # Massive damage from being surrounded
                                                surrounded_damage = int((coba.attack + goons.attack) * 1.5)
                                                actual_damage = max(1, surrounded_damage - (player.defense // 3))
                                                player.health = max(0, player.health - actual_damage)
                                                print(f"You're surrounded! Coba and goons deal {actual_damage} damage!")
                                                
                                                if player.health <= 0:
                                                    player.lives -= 1
                                                    print(f"\n💀 {player.name} has been defeated!")
                                                    print("The head-on charge was too reckless!")
                                                    print(f"❤️  Lives remaining: {player.lives}/3")
                                                    
                                                    # Lives warning
                                                    if player.lives == 1:
                                                        print("⚠️  WARNING: Only 1 life remaining! Be careful!")
                                                    elif player.lives == 2:
                                                        print("⚠️  WARNING: 2 lives remaining!")
                                                    
                                                    if player.lives > 0:
                                                        print("The battle restarts...")
                                                        player.health = player.max_health
                                                        coba.health = original_coba_health
                                                        goons.health = original_goons_health
                                                        continue
                                                
                                                # Player attacks but it's not enough
                                                player.attack_enemy(coba)
                                                
                                                # Coba finishes the player
                                                print(f"\nCoba delivers a devastating counter-attack!")
                                                coba_damage = int(coba.attack * 1.5)
                                                actual_coba_damage = max(1, coba_damage - player.defense)
                                                player.health = max(0, player.health - actual_coba_damage)
                                                print(f"Coba attacks for {actual_coba_damage} damage!")
                                                coba_final = player.health <= 0
                                                
                                                if coba_final or player.health <= 0:
                                                    player.lives -= 1
                                                    print(f"\n💀 {player.name} has been defeated!")
                                                    print("The head-on charge was too reckless!")
                                                    print(f"❤️  Lives remaining: {player.lives}/3")
                                                    
                                                    if player.lives > 0:
                                                        print("The battle restarts...")
                                                        player.health = player.max_health
                                                        coba.health = original_coba_health
                                                        goons.health = original_goons_health
                                                        continue
                                            
                                            elif strategy == "4":
                                                # Tactical Retreat - LOSING strategy (can't use key to escape, must fight)
                                                print(f"\n{player.name} tries to use the Golden Key to create an escape route!")
                                                print("But Coba blocks the way! The key won't work here!")
                                                print("You're forced to fight!")
                                                
                                                # Coba attacks while you're trying to escape
                                                escape_damage = int(coba.attack * 1.8)
                                                actual_damage = max(1, escape_damage - (player.defense // 2))
                                                player.health = max(0, player.health - actual_damage)
                                                print(f"Coba attacks while you're distracted! You take {actual_damage} damage!")
                                                
                                                if player.health <= 0:
                                                    player.lives -= 1
                                                    print(f"\n💀 {player.name} has been defeated!")
                                                    print("The tactical retreat failed!")
                                                    print(f"❤️  Lives remaining: {player.lives}/3")
                                                    
                                                    if player.lives > 0:
                                                        print("The battle restarts...")
                                                        player.health = player.max_health
                                                        coba.health = original_coba_health
                                                        goons.health = original_goons_health
                                                        continue
                                                
                                                # Goons attack
                                                goon_attack = max(1, goons.attack - player.defense)
                                                player.health = max(0, player.health - goon_attack)
                                                print(f"Goons attack! You take {goon_attack} damage!")
                                                
                                                if player.health <= 0:
                                                    player.lives -= 1
                                                    print(f"\n💀 {player.name} has been defeated!")
                                                    print("The tactical retreat failed!")
                                                    print(f"❤️  Lives remaining: {player.lives}/3")
                                                    
                                                    if player.lives > 0:
                                                        print("The battle restarts...")
                                                        player.health = player.max_health
                                                        coba.health = original_coba_health
                                                        goons.health = original_goons_health
                                                        continue
                                        
                                        # After winning the final battle, offer rift home
                                        if final_battle_won:
                                            print(f"\n🎊 You've successfully escaped Tilted Towers with Peely and Jonsey!")
                                            print(f"Peely says: 'Great job! Let's get you home!'")
                                            print(f"Peely creates a Rift to take you home!")
                                            player.add_item("Rift Home")
                                            print(f"\nYou can now use the Rift to return home!")
                                            print('Type "Rift" or "Home" to travel back to the village!')
                                            
                                            # Rift home loop
                                            home_traveled = False
                                            while not home_traveled:
                                                home_choice = input("\nEnter your choice: ").strip().lower()
                                                
                                                if home_choice == "rift" or home_choice == "home":
                                                    print(f"\n{player.name} activates the Rift!")
                                                    print("A portal opens, leading back to your village...")
                                                    print("You step through with Peely and Jonsey!")
                                                    
                                                    # Arrive at Greasy Grove (home/village)
                                                    print(f"\n{'='*70}")
                                                    print("🏠 YOU'VE RETURNED HOME! 🏠")
                                                    print(f"{'='*70}")
                                                    print(f"\nYou arrive at Greasy Grove with Peely and Jonsey!")
                                                    print(f"The villagers cheer as you return victorious!")
                                                    print(f"\n🎉🎉🎉 YOU WIN THE GAME! 🎉🎉🎉")
                                                    print(f"\n{player.name} has successfully:")
                                                    print(f"  ✅ Rescued Jonsey from Coba")
                                                    print(f"  ✅ Defeated Coba and his goons")
                                                    print(f"  ✅ Returned home safely with friends")
                                                    print(f"\nThank you for playing!")
                                                    print(f"{'='*70}")
                                                    home_traveled = True
                                                    exit()  # End the game
                                                else:
                                                    print("⚠️  Invalid choice. Type 'Rift' or 'Home' to travel home.")
                                        
                                        peely_choice_made = True  # Exit the Peely encounter loop
                                    else:
                                        player.lives -= 1
                                        print(f"\n❌ Wrong answer! You lose a life!")
                                        print(f"❤️  Lives remaining: {player.lives}/3")
                                        
                                        # Lives warning
                                        if player.lives == 1:
                                            print("⚠️  WARNING: Only 1 life remaining! Be careful!")
                                        elif player.lives == 2:
                                            print("⚠️  WARNING: 2 lives remaining!")
                                        
                                        # Restore health and repeat the question
                                        player.health = player.max_health
                                        print(f"💚 {player.name} restored to full health!")
                                        print("The riddle repeats...")
                                        print("🔍 RIDDLE: Like Epstein's island, secrets at the core, once stuck to the ground - then rose to the lore. What am I?")
                                        continue
                    
                    

                    traveled = True
            else:
                wrong_attempts += 1
                # Count words in the wrong input
                word_count = len(travel_choice.split())
                if word_count == 0:
                    word_count = 1  # At least 1 word penalty for empty/whitespace
                
                # Lose 25 health per word
                health_loss = 25 * word_count
                player.health = max(0, player.health - health_loss)
                
                print(f"\n⚠️  That's not the right command! The Rift rejects your input!")
                print(f"You lose {health_loss} HP for the {word_count} word(s) you typed!")
                print(f"{player.name} now has {player.health}/{player.max_health} HP remaining.")
                
                # Health warning messages
                if player.health <= player.max_health * 0.25:
                    print("⚠️  WARNING: Health is critically low!")
                elif player.health <= player.max_health * 0.5:
                    print("⚠️  WARNING: Health is below 50%!")
                
                # After 4 wrong attempts, lose a life
                if wrong_attempts >= 4:
                    player.lives -= 1
                    print(f"\n💀 You've made too many wrong attempts! You lose a life!")
                    print(f"❤️  Lives remaining: {player.lives}/3")
                
                # Lives warning
                if player.lives == 1:
                    print("⚠️  WARNING: Only 1 life remaining! Be careful!")
                elif player.lives == 2:
                    print("⚠️  WARNING: 2 lives remaining!")
                    wrong_attempts = 0  # Reset counter after losing a life
                    
                    if player.lives <= 0:
                        print(f"\n{'='*60}")
                        print("💀 GAME OVER 💀")
                        print(f"{'='*60}")
                        print(f"{player.name} has been defeated!")
                        print("You have run out of lives. The game must restart from the beginning.")
                        print(f"{'='*60}")
                        exit()
                    else:
                        print(f"Try again! Type 'Rift' to travel.")
                else:
                    print(f"Wrong attempts: {wrong_attempts}/4 (You'll lose a life after 4 wrong attempts)")
                    print(f"Try again! Type 'Rift' to travel.")
    else:
        print(f"\n{player.name} does not have a Rift to travel with.")
