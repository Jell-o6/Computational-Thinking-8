place = input("You wake up. Where will you go today?")
if place == "Seattle":
    print("You get bored and die of bordom for there is too many people in seattle.")
else:
    print("You start going when you hear a terrible sound.")
    food = input("It's you stomach pick something to eat")
    if food == "Nothing":
        print("You die of starvation.")
    else:
        print("You have a filling meal and level up.")
        class2 = input("Pick village idiot or knight")
        if class2 == "Knight":
            print("You get hired by the king and live happily ever after.")
        else:
            print("You get bullied by 3 thugs.")
            battle = input("Fight or run.")
            if battle == "Run":
                print("You run back home and cry the end.")
            else:
                print("You beat those thugs up.")
                class3 = ("Pick clumsy theif or Jester.")
                if class3 == "Clumsy Theif":
                    print("You get caught better luck next time.")
                else:
                    print("You travel around and become famous. The End.")
