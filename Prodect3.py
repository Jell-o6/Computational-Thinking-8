import random
#spin list
list = ["high","low", "mid","neg sm", "neg big"]
spin = random.choice(list)
#Make a charture quiz start with a litle bit of money since you can't have negative money
print("This is a charture creater make choices for you charture.")
cha = 0
wis = 0
Dex = 0
str = 0
con = 0
money = 5
#Battle question cha at stake
Battle = input("In battle do you want your chature to fight, run, or hide")
if Battle == "fight":
    str += 2
    con -= 1
    cha -= 1
elif Battle == "run":
    Dex += 2
    cha -= 1
elif Battle == "hide":
    wis += 1
    con += 1
    cha -= 1
#Don't pick the dragon
pet = input("Choose a pet for your charture.")
if pet == "dragon":
    wis -=2
    cha -=2
    str +=3
else:
    cha += 2
#Are you a dare devil?
path = input("Your charture can either go thrue a long path or a short path but its dangerous.")
if path =="short":
    con -=1
    cha -=1
    str +=1
    Dex +=2
if path =="long":
    wis += 1
#Yummy berries
lost = ("Your charture is lost they see some beries eat them.")
if lost == "yes":
    wis -=2
    con +=1
if lost == "no":
    con -=2
    wis +=1
#Always trust strangers
Seller = input("A suspious stangeer offer your charture a priceless artifact for 5 gold does your charture take the deal, leave, or negociate")
if Seller == "take deal":
    wis -=2
    money -=5
    cha +=2
if Seller == "leave":
    wis +=1
if Seller == "negoticate":
    cha += 2
    money -=3
#Don't loose your honor
Bank = input("Your charture is broke you can break into a bank do it or not or beg.")
if Bank == "do it":
    Dex +=2
    money +=3
if Bank == "not" or Bank == "beg":
    wis += 1
    con -=2
    if Bank == "beg":
        con+=1
        cha-=2
        money+=1
#Spin the wheel
wheel = input("A evil over lord asks if you  want to spin the wheel for a reward. But theres a person attatched.")
if wheel== "no":
    con-=3
    cha-=2
    money = 0
if wheel== "yes":
    if spin== "high":
        Dex+=2
        str+=2
        wis+=2
        cha+=2
        con+=2
    if spin== "low":
        Dex+=1
        str+=1
        wis+=1
        cha+=1
        con+=1
    if spin== "mid":
        money = 5
    if spin== "neg sm":
        Dex-=2
        str-=1
        wis-=2
        cha-=1
        con-=2
        money =-1
    if spin== "neg big":
        Dex-=2
        str-=3
        wis-=2
        cha-=3
        con-=2
        money =-3

print(f"Characture score,{cha} charisma, {Dex} dexterity, {str} Strength, {wis} wizdom, {con} contitution, and {money} coins.")
if cha > Dex and cha > str and cha > wis and cha > con:
    print("Your chacture very  bettiful and vain.")
if Dex > cha and Dex > str and Dex > wis and Dex > con:
    print("Your chacture very tricky and sneaky.")
if str > Dex and str > cha and str > wis and str > con:
    print("Your chacture very muscular and brutish.")
if wis > Dex and wis > str and wis > cha and wis > con:
    print("Your chacture very smart and nerdy.")
if con > Dex and con > str and con > wis and con > cha:
    print("Your chacture very tough and healthy.")
if money == "0":
    print("Your chacture is broke.")
if con < 1:
    print("your charure is dead")
if cha < 1:
    print("Your chature is a unlikeable grump.")
if str < 1:
    print("Your charture is a wimpy creature that can't move.")
if Dex < 1:
    print("Your charture is a oaf that stomps around.")
if wis < 1:
    print("Your chature trusts anybody.")
