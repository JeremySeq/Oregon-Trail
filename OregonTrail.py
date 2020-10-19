#NOTES


#1. Add more river crossings
#2. Add wagon repairs(wagon axles, wagon tongues, and wagon wheels)
#3. Add a warning for low clothes at 2 sets



milestraveled = 0


import random
import time
import math

#WHO WILL YOU BE?
print("1. Be a banker from Boston")
print("2. Be a carpenter from Ohio")
print("3. Be a farmer from Illinois")
person = input("What is your choice?(1/2/3)")

#HOW MUCH MONEY DO YOU HAVE?
if person == '1':
    money = 1600
elif person == '2':
    money = 1200
elif person == '3':
    money = 900

#SETTING THE RATIONS AND SUPPLY VARIBALES
rations = 35
totaloxen = 0
totalfood = 0
totalammo = 0
totalclothes = 0


complete = 0
complete1 = 0
complete2 = 0
complete3 = 0
complete4 = 0
complete5 = 0
complete6 = 0
complete7 = 0
complete8 = 0


#Places and Dates
month = 'March'
day = 1
place = 'Independence, Missouri'
place2 = 'Courthouse Rock'
place3 = 'Chimney Rock'
place4 = 'Independence Rock'
place5 = 'Fort Bridger'
place6 = 'Fort Hall'
place7 = 'Fort Boise'
place8 = 'Whitman Mission'
destination = 'Oregon City'
current = 'Independence, Missouri'

#WHO ARE THE MEMBERS?
leader = input("What is the name of the wagon leader?")
semem = input("What is the name of the second member?")
thmem = input("What is the name of the third member?")
fomem = input("What is the name of the fourth member?")
fimem = input("What is the name of the fifth member?")


#BUYING SUPPLIES BEFORE YOU LEAVE
print("It is 1848, you are leaving Independence, Missouri in March.")
print("Before leaving, you should buy equipment and supplies. You have ", money, " in cash, but you don't have to spend it all now.\n")
continue1 = input("PRESS 'ENTER' TO CONTINUE")
if continue1 == '':
    continue2 = input("You can buy whatever you need at Matt's General Store.          PRESS 'ENTER' TO CONTINUE\n")
    if continue2 == '':
        #BUYING OXEN
        print("$",money)
        yoke = int(input("There are 2 oxen in a yoke; I recommend at least 3 yoke. I charge $40 a yoke.    How many yoke do you want?\n"))
        money = money - 40*yoke
        totaloxen = totaloxen + 2*yoke
        print("$",money)
        time.sleep(2)
        #BUYING FOOD
        food = int(input("I recommend you take at least 200 lbs. of food for each person in your family. I see that you have 5 people in all. You'll need flour, sugar, bacon, and coffee. My price is 20 cents a pound. How many pounds of food do you want?\n"))
        money = money - .2 * food
        totalfood = totalfood + food
        print("$",money)
        time.sleep(2)
        #BUYING CLOTHES
        clothes = int(input("You will need warm clothing in the mountains. I recommend taking at least 2 sets of clothes per person. Each set is $10. How many sets of clothes do you want?\n"))
        money = money - 10 * clothes
        totalclothes = totalclothes + clothes
        print("$",money)
        time.sleep(2)
        #BUYING AMMO
        ammo = int(input("I sell ammunition in boxes of 20 bullets. Each box costs $2. How many boxes do you want?\n"))
        money = money - 2 * ammo
        totalammo = totalammo + ammo
        print("$",money)
        time.sleep(2)
        print("You're ready to go!")
        continue3 = input("PRESS 'ENTER' TO CONTINUE")

        #TRAVELING THE TRAIL
        if continue3 == '':
            #SETTING THE WHILE STATEMENT
            s = 0
            n = 5
            counter = 1
            while counter <= n:
                #DISPLAYING THE CHOICES
                print(month, day)
                print(current)
                print("Miles Traveled: ", milestraveled)
                print("1. Continue")
                print("2. Hunt")
                print("3. Map")
                print("4. Trade")
                print("5. Rest")
                print("6. Change Rations")
                print("7. Check supplies")
                print("8. Sell Items")

                choice = input("What are you going to do?(1/2/3/4/5/6/7/8)\n")

                #TRADE
                if choice == '4':
                    print("1. Oxen")
                    print("2. Food")
                    print("3. Clothes")
                    print("4. Ammunition")
                    shop = input("What do you want to buy?\n")
                    #BUYING OXEN
                    if shop == '1':
                        print("$",money)
                        oxen = int(input("Oxen cost $30 each. How many oxen do you want?\n"))
                        money = money - oxen * 30
                        totaloxen = totaloxen + oxen
                        print("$",money)
                    #BUYING FOOD
                    elif shop == '2':
                        print("$",money)
                        food = int(input("Food costs 35 cents a pound. How many pounds of food do you want?\n"))
                        money = money - food * .35
                        totalfood = totalfood + food
                        print("$",money)
                    #BUYING CLOTHES
                    elif shop == '3':
                        print("$",money)
                        clothes = int(input("One set of clothing costs $15. How many sets of clothing do you want\n"))
                        money = money - clothes * 15
                        totalclothes = totalclothes + clothes
                        print("$",money)
                    #BUYING AMMUNITON
                    elif shop == '4':
                        print("$",money)
                        ammo = int(input("Ammunition costs 15 cents per bullet.\n"))
                        totalammo = totalammo + ammo
                        money = money - ammo * .15

                        print("$",money)
                    time.sleep(2)

                #MAP
                elif choice == '3':
                    print("You are currently at ", current)
                    print("1. ", place)
                    print("2. ", place2)
                    print("3. ", place3)
                    print("4. ", place4)
                    print("5. ", place5)
                    print("6. ", place6)
                    print("7. ", place7)
                    print("8. ", place8)
                    print("Destination: ", destination)
                    time.sleep(2)

                #HUNT
                elif choice == '2':
                    hunted = random.randrange(1, 200)
                    print("You got ", hunted, " pounds of food.")
                    totalfood = totalfood + hunted
                    totalammo = totalammo - random.randrange(10, 35)
                    print("In total, you have ", totalfood, " pounds of food\n")
                    time.sleep(2)

                #REST
                elif choice == '5':
                    restdays = int(input("How many days do you want to rest?\n"))
                    day = day + restdays
                    totalfood = totalfood - rations * restdays
                    time.sleep(2)

                #CHANGE RATIONS
                elif choice == '6':
                    print("1.     5 lbs. per person")
                    print("2.     7 lbs. per person")
                    print("3.     10 lbs. per person")
                    rations = input("Select ration\n")
                    if rations == '1':
                        rations = 25
                    elif rations == '2':
                        rations = 35
                    elif rations == '3':
                        rations = 50
                    time.sleep(2)

                #CHECK SUPPLIES
                if choice == "7":
                    print("Oxen: ", totaloxen)
                    print("Food: ", totalfood)
                    print("Ammunition: ", totalammo)
                    print("Money: ", money)
                    time.sleep(2)

                #SELL
                if choice == '8':
                    print("1. Oxen")
                    print("2. Food")
                    print("3. Ammunition")
                    sellchoice = input("What do you want to sell?")
                    howmany = int(input("How many do you want to sell?"))
                    if sellchoice == '1':
                        totaloxen = totaloxen - howmany
                        money = money + howmany * 10
                    if sellchoice == '2':
                        totalfood = totalfood - howmany
                        money = money + howmany * .10
                    if sellchoice == '3':
                        totalammo = totalammo + howmany
                        money = money + howmany * .5


                #CONTINUE
                elif choice == '1':
                    #LOW FOOD WARNING
                    if totalfood <= 150:
                        print("WARNING! Low Food!\n")
                    #CHANGING THE DATE
                    if month == 'March' and day >= 31:
                        month = 'April'
                        day = 1
                    elif month == 'April' and day >= 30:
                        month = 'May'
                        day = 1
                    else:
                        day = day + 1
                    totalfood = totalfood - rations
                    time.sleep(2)

                    #PAYING OFF YOUR DEBTS
                    if money < 0:
                        print("You need to pay off your debt.")
                        print("Debt: ", money)
                        print("1. Oxen: ", totaloxen)
                        print("2. Food: ", totalfood)
                        print("3. Ammo: ", totalammo)
                        debt = input("How will you pay off your debt?\n")
                        debtamount = input("How much will you sell to pay off your debt?\n")
                        if debt == 1:
                            totaloxen = totaloxen - debtamount
                            money = money + debtamount*25
                            time.sleep(2)
                        elif debt == 2:
                            totalfood = totalfood - debtamount
                            money = money + debtamount*.35
                            time.sleep(2)
                        elif debt == 3:
                            totalammo = totalammo - debtamount
                            money = money + debtamount*.10

                        time.sleep(2)

                    #PROBLEMS THAT COULD OCCUR ALONG THE TRAIL
                    problems = random.randrange(1,55)
                    if problems == 1 and semem is not 'dead':
                        print(semem, " has died.\n")
                        semem = 'dead'
                    elif problems == 3:
                        print(thmem, " has died.\n")
                        thmem = 'dead'
                    elif problems == 5:
                        print(fomem, " has died.\n")
                        fomem = 'dead'
                    elif problems == 7:
                        print(fimem, " has died.\n")
                        fimem = 'dead'
                    elif problems == 9 and semem is not 'dead':
                        print(semem, " has dysentry.\n")
                    elif problems == 11 and thmem is not 'dead':
                        print(thmem, " has dysentry.\n")
                    elif problems == 13 and fomem is not 'dead':
                        print(fomem, " has dysentry.\n")
                    elif problems == 15 and fimem is not 'dead':
                        print(fimem, " has dysentry.\n")
                    elif problems == 2:
                        print("You lost one oxen.\n")
                        totaloxen = totaloxen - 1
                    elif problems == 4:
                        print("One oxen died.\n")
                        totaloxen = totaloxen - 1
                    elif problems == 6 and semem is not 'dead':
                        print(semem, " has cholera.\n")
                    elif problems == 8 and thmem is not 'dead':
                        print(thmem, " has cholera.\n")
                    elif problems == 10 and fomem is not 'dead':
                        print(fomem, " has cholera.\n")
                    elif problems == 12 and fimem is not 'dead':
                        print(fimem, " has cholera.\n")



                    milestraveled =  milestraveled + 7 * totaloxen

                    #PLACES + RIVERS


                    #COURTHOUSE ROCK
                    if milestraveled > 572:
                        if complete1 == 1:
                            #CHIMNEY ROCK
                            if milestraveled > 712:
                                if complete2 == 1:
                            #INDEPENDENCE ROCK
                                    if milestraveled > 840:
                                        if complete3 == 1:
                                        #FORT BRIDGER
                                            if milestraveled > 1036:
                                                if complete4 == 1:
                                                #FORT HALL
                                                    if milestraveled >  1157:
                                                        if complete5 == 1:
                                                        #FORT BOISE
                                                            if milestraveled > 1400:
                                                                if complete6 == 1:
                                                                #WHITMAN MISSION
                                                                    if milestraveled > 1600:
                                                                        if complete7 == 1:
                                                                            #OREGON CITY, DESTINATION
                                                                            if milestraveled > 1814:
                                                                                current = destination
                                                                                print("YOU HAVE REACHED OREGON CITY!    CONGRATULATIONS! YOU LIVED!")
                                                                                exit()

                                                                        else:
                                                                            current = 'Whitman Mission'
                                                                            print("You have arrived at Whitman Mission!     This is where Marcus Whitman, Narcissa Whitman, and 11 others were killed by Native Americans.\n")
                                                                            complete7 = 1

                                                                else:
                                                                    current = 'Fort Boise'
                                                                    print("You have arrived at Fort Boise!\n")
                                                                    complete6 = 1

                                                        else:
                                                            current = 'Fort Hall'
                                                            print("You have arrived at Fort Hall!\n")
                                                            complete5 = 1

                                                else:
                                                    current = 'Fort Bridger'
                                                    print("You have arrived at Fort Bridger\n")
                                                    complete4 = 1

                                        else:
                                            current = 'Independence Rock'
                                            print("You have arrived at Independence Rock!\n")
                                            complete3 = 1

                                else:
                                    current = 'Chimney Rock'
                                    print("You have arrived at Chimney Rock!\n")
                                    complete2 = 1


                        else:
                            current = place2
                            print("You have arrived at Courthouse Rock!\n")
                            complete1 = 1








                    #MISSOURI RIVER CROSSING
                    elif milestraveled > 150:
                        if complete == 1:
                            pass
                        else:
                            print("You have arrived at the Missouri River.")
                            print("1. Take a ferry across the river for $40")
                            print("2. Fjord the river")
                            print("3. Caulk your wagon an float across")
                            rivercross = input("How will you cross the river?\n")
                            #FERRY ACROSS
                            if rivercross == 1:
                                money = money - 40
                                print("You crossed the river with no problems.\n")
                            #FJORD THE 10-20 FEET DEEP RIVER
                            elif rivercross == 2:
                                riverfjord = random.randrange(1, 5)
                                if riverfjord == 1:
                                    print("One oxen drowned\n")
                                    totaloxen = totaloxen - 1
                                elif riverfjord == 2:
                                    print("Your supplies got wet and you lost 300 pounds of food.\n")
                                    totalfood = totalfood - 300
                                elif riverfjord == 3:
                                    print("Your supplies got wet and you lost 200 pounds of food.\n")
                                    totalfood = totalfood - 200
                                elif riverfjord == 4:
                                    print("Two oxen drowned\n")
                                    totaloxen = totaloxen - 2
                            #CAULK THE WAGON AND FLOAT ACROSS
                            elif rivercross == 3:
                                rivercaulk = random.randrange(1, 5)
                                if rivercaulk == 1:
                                    print("One oxen drowned\n")
                                    totaloxen = totaloxen - 1
                                elif rivercaulk == 2:
                                    print("Your supplies got wet and you lost 300 pounds of food.\n")
                                    totalfood = totalfood - 300
                                elif rivercaulk == 3:
                                    print("Your supplies got wet and you lost 200 pounds of food.\n")
                                    totalfood = totalfood - 200

                            complete = 1


                    if totaloxen == 0:
                        print("You don't have any oxen.")
                        print("Your family died...")
                        exit()
                    if totalfood == 0:
                        print("You ran out of food.")
                        print("Your family died...")
                        exit()
                    if totalclothes <= 3:
                        print("Your family didn't have enough clothes, and died because of the cold.")
                        exit()
                    if semem == 'dead' and thmem == 'dead' and fomem == 'dead' and fimem == 'dead':
                        print("Your entire family is dead...")
                        exit()
