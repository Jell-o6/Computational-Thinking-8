import random
print("You Just entered the Areana of the Abtoles whatever those are. You only have a simple sword and you see a CyBull a terrible creature.")
Cybull_attacks = ["lazer eye","charge", "Swing"]
Cybull_health = 5
your_Health = 3
for i in range(5):
    Cybull = random.choice(Cybull_attacks)
    attack = input("Pick to stab, Dodge,or leave")
    if attack == "stab":
        if Cybull == "Swing":
            print("You stab at it and it swings back.")
            Cybull_Health -=2
            your_Health -=1
        elif Cybull == "charge":
            print("As you move closer to stab it it suddenly charges and you get hit.")
            your_health -=2
        elif Cybull == "lazer eye":
            print("As you move closer it shoot a lazer you make a awsome jump just getting grazed and slame down you sword.")
            your_health -=1
            Cybull_Health -=3
    elif attack == "Dodge":
        if Cybull == "Swing":
            print("It swings but with a leap you avoid it's attack")
        elif Cybull == "charge":
            print("It charges at you but you jump on it back.")
        elif Cybull == "lazer eye": 
            print("It shoot you with it's lazer eye but your to quick")
    elif attack == "Leave":
        print("You leave the areana and live a peaceful life.")
    print(f"Your health {your_Health} and Cybull's {Cybull_health}")
    if Cybull_Health == "0":
        if your_Health == "0":
            print(f"You slayed it nice job and collect a eye and heal by 2 now to fight the 2 eyed Ato")
            Ato_Health = 6
            your_Health +=2
            Ato = ["Splash","Heal","bite"]
            for i in range(5):
                Ato_attack = random.choice(Ato)
            
