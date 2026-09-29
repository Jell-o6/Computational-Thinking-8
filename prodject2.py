place = input("Your a common villager you can leave to fing glory or you can stay.")
if place == "stay":
    raid = input("You are bored. raid the village?")
    if raid == "yes":
        print("You get kicked out and gain the mark of the fugitive. The end.")
    else:
        party = input("You learn about a festival want to go.")
        if party == "yes":
            print("You win in a game and gain mark of the winner. The end.")
        else:
            Noparty = input("Do you want to ruin the festival.")
            if Noparty == "yes":
                print("You run around and make kids cry. You gain the mark of the party pooper. The end.")
            else:
                marks = input("You visit the mark master he asks if you want the mark of the marks.")
                if marks == "yes":
                    print("He shakes his head. You are a fool and greedy, He says then he gives you the mark of no marks. The end")
                elif marks == "No":
                    print("His face turn furious. How dare you not except my gift! He shouts then He gives you the mark of no marks. The end.")
                else:
                    print("You do not know? He says then gives you the mark of the idecisive. The end.")
elif place == "leave":
    item = input("Choose between a weapon food or nothing.")
    if item == "food":
        print("You eat a delishous lunch and gain the mark of gluttony. The end.")
    elif item == "weapon":
        monster = input("You pick up you weapon and gain the mark of the dangerous. you see a monster fight or run.")
        if monster == "fight":
            print("You fight and slay the monster and gain the mark of the hero. The end.")
        elif monster == "run":
            print("You run back home were you find that it was a halarious prank and gain the mark of the coward.")
    else:
        print("You die of hunger and gain the mark of the fool. The End")
else:
    ("You can't decide what to do so you stay in bed in think. During that time you fall asleep and gain the marks of lazyness and indeciviness. Sweet dreams.")