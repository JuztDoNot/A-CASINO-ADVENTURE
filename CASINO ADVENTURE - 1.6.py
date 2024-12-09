import random

winner = False
def money():
    balance = 500000
    key = False
    green = False
     #Introduction#
    print('Welcome to your "CASINO ADVENTURE"!\nThis is where you make it big, or fall short with your spendings.')
    print('\nYou always had that dream of becoming the "BIG GREEN" himself,', "but with your small balance, you're gonna have to work for it.")
    print('\nAfter you spent money on tickets for Las Vegas, you land yourself infront of the "CLAMS CASINO".\nYour main goal is to become a MILLIONAIR and fight the BIG GREEN HIMSELF!\n-----------------------') 

     #Asks USER for their name while listing games#
    name = input("As soon as you enter the CLAMS CASINO, the clerk gives you a clipboard to sign with your name. (Totally not for legal reasons)\nENTER YOUR NAME: ")
     #Fun Easter Egg for after you beat game & try using MR. GREENZ's name#
    if name == "" or name == " " or name.lower() == "mr. greenz" or name.lower() == "mrgreenz" or name.lower() == "mr greenz"or name.lower() == "mr. green" or name.lower() == "mrgreen" or name.lower() == "mr green":
        print("What an... interesting name...")
    print(f"\nWhy hello there, {name.upper()}! Welcome to the CLAMS CASINO!\nWe got a multitude of games, such as DICE, SLOTS, ROULETTE, and even BLACKJACK.\nPlease, make yourself at home!\n-----------------------")
    print("(You are now on your own, goodluck!)\n")
    main(balance, key, green)



def main(balance, key, green):
    if balance >= 1000000:
        bossfight(balance, key, green)
     #Loops hub until you run out of money#
    elif balance > 0:
        while balance > 0:
            print(f"Your wallet contains: ${balance}")
            where2 = input("Where would you like to go? (BLACKJACK[BJ], SLOTS [$25 MINIMUM], ROULETTE[RL], or DICE [$100 MINIMUM])\nINPUT LOCATION: ")

             #Takes you to BJ#
            if where2.lower() == "blackjack" or where2.lower() == "bj":
                print("\n[You begin to walk yourself to the SIMPLE BLACKJACK TABLE...]\n-----------------------")
                blackjack(balance, key, green)
             #Takes you to SLOTS#
            elif where2.lower() == "slots" or where2.lower() == "slotz" or where2.lower() == "slot" or where2.lower() == "$25 minimum":
                print("\n[You make your way to the SLOTZ ZONE...]")
                if where2.lower() == "$25 minimum":
                    print("[Wait why did you try that?]")
                print("-----------------------")
                slots(balance, key, green)
             #Takes you to RL#
            elif where2.lower() == "roulette" or where2.lower() == "rl":
                print("\n[You begin to walk yourself to the ROULETTE FLOURETTE...]\n-----------------------")
                roulette(balance, key, green)
             #Takes you to DICE#
            elif where2.lower() == "dice" or where2.lower() == "dice dice" or where2.lower() == "dicedice":
                print("\n[You walk towards the DICE DICE section of the CLAMS CASINO...]\n-----------------------")
                dice(balance, key, green)
             #Easter Egg for using BATHROOM#
            elif where2.lower() == "bathroom":
                print("\n[You begin to walk yourself to the... Bathroom?]\n-----------------------")
                bathroom(balance, key, green)
             #Denies user of a false location#
            else:
                print("[I don't think that's a possible location here...]\n")
     #Womp Womp#
    elif balance <= 0:
        lost(balance)


    
def blackjack(balance, key, green):
     #For betting-loop#
    hiddenmark = True
     #Greets USER and asks if they need instructions on how to play#
    response = input('WELCOME TO THE SIMPLE BLACKJACK TABLE! \n\nWould you like me to explain the rules? (Input YES/Y for rules | Press ENTER or OTHER to Skip) ')
    if response.lower() == "yes" or response.lower() == "y":
         #Multiple PRINT lines in order to simplify TEXT#
         #Summary on how to play#
        print("\nOk, here are the rules: \n-----------------------")
        print("The DEALER will draw a total of 4 CARDS, 2 for YOU, and 2 for the DEALER. \nYou will get to see the VALUE of YOUR CARDS, however, you only get to see ONE of the DEALER'S CARDS.")
        print("\nIn order to WIN, you will need to have a HIGHER VALUE than the DEALER, however, \nif you surpass 21, you LOSE the game; the same goes for the DEALER if they happen to draw MORE than 21.")
        print("\nHowever, if YOU and the DEALER have the SAME VALUE in CARDS, it will be a PUSH; A.K.A. a DRAW")
        print("\nYou can either HIT-TO-DRAW a card or STAND-AND-REMAIN at the same value. \nThe DEALER can also draw but CAN NOT go over 17.\n-----------------------")

         #Waits until USER fully understands how to play#
        more = input("\nThose are the rule, feel free to read over them before you continue. \n[Press ENTER to continue] ")
     #EASTER EGG#
    elif response.lower() == "other" or response.lower() =="enter":
        print("\nWait, did you actually try that? I- Whatever, here's 20 bucks...")
        balance = balance + 20

    print("\nAlright then...")
     #The real game starts here#
    while balance > 0 and hiddenmark == True:
         #Asks USER how much to bet#
        bet = int(input(f"How much are you willing to bet? [You have: ${balance}] "))
         #Comes useful later for checks&loops#
        hiddenval = 21
        hiddenmark2 = True
        
         #Checks if the USER actually inputed a reasonable amount within their budget#
        if bet > balance:
            print("\nSorry buddy, you are to broke too bet that much, please input something more reasonable...")
            pass
        if bet <= 0 or bet == 0:
            print("Ha Ha... Real funny dude, you're so funny dude wow...\n")
            pass
        if bet <= balance and bet > 0:
            if bet <= 9:
                print("Uh... okay?")
            print("\nAlright then, commence the game!\n-----------------------")
            balance = balance - bet
            
             #Draws Cards#
            dlrcrd1 = random.randint(1,10)
            usrcrd1 = random.randint(1,10)
            dlrcrd2 = random.randint(1,10)
            usrcrd2 = random.randint(1,10)
            usrtotal = usrcrd1 + usrcrd2
            dlrtotal = dlrcrd1 + dlrcrd2

             #Shows stats of who has what#
            print(f"You hold a {usrcrd1} and {usrcrd2}. ({usrtotal}) \nThe Dealer's face card is {dlrcrd1}. ({dlrcrd1} + ?)")


             #Loops for User
            while hiddenval >= 21 or usrtotal < 21 and dlrtotal < 17:
                 #Asks if USER wants to HIT or STAND#
                action = input("\nDo you want to HIT or STAND? ")
                
                 #Function/Block for HIT#
                if action.lower() == "hit":
                     #Draws a new card#
                    usrnew = random.randint(1,10)
                    print(f"You draw a {usrnew}. \nYour total is now: {usrtotal+usrnew}")
                     #Adds card(s) to deck worth#
                    usrtotal = usrtotal + usrnew
                     #Checks if USER BUSTS#
                    if usrtotal == 21:
                        pass
                    elif usrtotal > 21:
                        hiddenval = 0
                    
                 #Function/Block for STAND#    
                elif action.lower() == "stand":
                    hiddenval = 0
                    print(f"The Dealer reveals his card... \nThe Dealer's second card was a {dlrcrd2}! ({dlrtotal})\n")
                     #Checks if DEALER is above 17#
                    if dlrtotal < 17:
                         #Keeps drawing until at 17 or more#
                        while dlrtotal < 17:
                             #Draws a new card (for DEALER)#
                            dlrnew = random.randint(1,10)
                            print(f"The Dealer draws another card... \nThe Dealer draws a {dlrnew}!")
                             #Adds card(s) to deck worth (for DEALER)#
                            dlrtotal = dlrtotal + dlrnew
                    print(f"The Dealer's new value is now: {dlrtotal}")
                    
                 #Checks if USER inputs a proper response#
                else:
                    print("Please input a proper response")                    


             #Does multiple checks to determine who wins#
             #First Check - Sees if USER BUSTS (THEY CAN LOSE IF THEY KEEP DRAWING)#          
            if usrtotal > 21:
                print ("\nYOU BUST! DEALER WINS!")
                print(f"Your total is now: ${balance}")

             #Second Check - Sees if DEALER BUSTS#
            elif dlrtotal > 21:
                print ("\nDEALER BUSTS! YOU WIN!")
                bet = bet*2
                balance = balance + bet
                print(f"Your total is now: ${balance}")                    

             #Third Check - Sees if USER BEATS DEALER#          
            elif usrtotal > dlrtotal:
                print("\nYOU WIN!")
                bet = bet*2
                balance = balance + bet
                print(f"Your total is now: ${balance}")

             #Fourth Check - Sees if DEALER BEATS USER#          
            elif dlrtotal > usrtotal:
                print("\nDEALER WINS!")
                print(f"Your total is now: ${balance}")

             #Final Check - Sees if USER AND DEALER TIE#          
            elif usrtotal == dlrtotal:
                balance = balance + bet
                print(f"IT'S A PUSH! \nYou lost no money! (${balance})")

            #Checks if USER ran out of cash#
            if balance <= 0:
                print("\nHey... you don't have any more money, GET OUT OF HERE!")
                print("\n[The Dealer kicks you out of the table and you leave empty handed]\n-----------------------")
                main(balance, key, green)
                
             #Traps input error from USER#
            while hiddenmark == True and hiddenmark2 == True and balance > 0:
                 #Asks user if they want to continue#
                advance = input("\nWould you like to continue? (YES/Y or NO/N) ")

                 #Restarts all the way back to "How much will you bet" Question#
                if advance.lower() == "yes" or advance.lower() == "y":
                    print("\nAlright then, just let me shuffle the deck real quick... \nOkay, now...\n")
                    hiddenmark2 = False

                 #Will drop USER out of game#    
                elif advance.lower() == "no" or advance.lower() == "n":
                    print("\nVery well, you're always welcome to come back. \nGood luck on your Gambling Adventure!")
                    print("\n[You leave the Blackjack table to play other games at the casino...]\n-----------------------")
                    hiddenmark = False
                    main(balance, key, green)

                 #Checks if USER inputs a proper response#
                else:
                    print("Sorry, what was that? Maybe I wasn't clear the first time...")



def slots(balance, key, green):
     #Useful for later LOOPS#
    hiddenmark = True
    condition = False
    response = input('WELCOME TO THE SLOTZ ZONE! \n\nWould you like to know how these slots work? (Input YES/Y for guide | Press ENTER or OTHER to Skip) ')
    if response.lower() == "yes" or response.lower() == "y":
         #Explains how the POINT SYSTEM works for SLOTZ#
        print("\nOk then, here's how the point system works: \n-----------------------")
        print("These SLOTZ have a variety of different symbols (or numbers if you're a nerd). If you have a certain combo of symbols, you will either get huge bucks, lose money, or get half of what you betted.\nMy- I mean the CLAMS CASINO's SLOTZ mainly revolve around luck and don't give into bribery so easily!\n")
        print("However, if you want to go to higher paying slots, simply return to this hub area!")
        print("There are 3 LEVELS of SLOTS: LOW ($25), MEDIUM ($250), and HIGH ($500).\n\nDepending on how much you put in, you can either get combos horizontal, diagnolly, or vertically!")
         #LIST OF COMBOS#
        print("Anyways, heres a full list of various combos that are avaliable:\n----------------------")
        print("{}[===JACKPOT===]{}\n[7,7,7] | [9,8,5] | [9,9,9]\n")
        print(":===WIN===:\n[3,3,3] | [9,6,9] | [6,9,6]\n")
        print("<~~~COMPENSATION~~~>\n[2,2,2] | [5,5,5] | [3,2,1]\n")
        print("[<>>LOSE<<>]\n[6,6,6] | [4,4,4] | [0,0,0]\n[ANY OTHER COMBINATION]\n----------------------")
         #Waits until USER fully understands how to play#        
        more = input("\nThat's basically everything! But don't worry, if you need to see the guide again, you can call it by saying [GUIDE] after you roll a slot. \n[Press ENTER to continue] ")
     #EASTER EGG#
    elif response.lower() == "other" or response.lower() =="enter":
        print("\nLook here funny guy, you can't just BREAK the 4th wall...\n[The Host of the SLOTZ ZONE gave you a key, what could this be used for?]")
        key = True
     #Loops until USER wants to leave or runs out of money#   
    while balance >= 25 and hiddenmark == True:
         #Asks USER if they want to leave#
        while condition == True:
            leave = input('Welcome back! Would you like to leave the SLOTZ ZONE? (YES/Y or NO/N) ')
            if leave.lower() == "yes" or leave.lower() == "y":
                print("Alright then, the exit is on your left. Goodluck on gambling tonight!\n\n-----------------------")
                hiddenmark = False
                condition = False
                main(balance, key, green)
            elif leave.lower() == "no" or leave.lower() == "n":
                print("Very well then! Now what was I about to say... oh right!")
                condition = False
            else:
                print("Umm... please say something more... understandable?\n")
         #Asks USER what level of SLOTZ they want to go to#           
        location = input("\nWhich level of slots do you want to go to? [LOW ($25) | MEDIUM ($250) | HIGH ($500)] ")
        stay = True

         #Generates COMBOS#
        jp1 = [7,7,7]
        jp2 = [9,8,5]
        jp3 = [9,9,9]
        w1 = [3,3,3]
        w2 = [9,6,9]
        w3 = [6,9,6]
        comp1 = [2,2,2]
        comp2 = [5,5,5]
        comp3 = [3,2,1]
        L1 = [6,6,6]
        L2 = [4,4,4]
        L3 = [0,0,0]

        #LOW SLOTZ#
        if location.lower() == "low" or location.lower() == "l":
            print("[You walk over to the LOW-LEVEL-SLOTZ ZONE]\n-----------------------")
            print("Welcome to the POOR- I mean LOW-LEVEL-SLOTZ ZONE!")
            while balance >= 25 and stay == True:
                 #Usefull for future loops#
                hiddenmark2 = True
                check = False
                times = int(input(f"How many chips (1-8 CHIPS MAX) will you bet? [You have: ${balance}] "))
                 #Sees if USER is trying to actually GAMBLE#
                if times <= 0 or times == 0:
                    print("Uh seriously? You are trying to GAMBLE here? How are you going win man...\n")
                 #Checks if USER puts reasonable amount of chips into machine
                if times > 8:
                    print("I don't think these machines can handle that many chips...\n")    
                if times > 0 and times <= 8:
                    bet = times * 25
                    if bet > balance:
                        print("Woah! You don't have enough to fully pay for all possibilities, try betting less chips?")
                    if bet <= balance and bet > 0:
                        print(f"[You insert the chips into the machine!]\n\nYOU BET: ${bet}\n-----------------------")
                        balance = balance - bet

                         #Generates Spins#    
                        tl = random.randint(0,9)
                        tm = random.randint(0,9)
                        tr = random.randint(0,9)
                        ml = random.randint(0,9)
                        mm = random.randint(0,9)
                        mr = random.randint(0,9)
                        bl = random.randint(0,9)
                        bm = random.randint(0,9)
                        br = random.randint(0,9)

                         #Compiles generated spins into LISTS/ARRAY#
                        top = [tl,tm,tr]
                        mid = [ml,mm,mr]
                        botm = [bl,bm,br]
                        lcm = [tl,ml,bl]
                        mcm = [tm,mm,bm]
                        rcm = [tr,mr,br]
                        dg1 = [tr,mm,br]
                        dg2 = [bl,mm,tr]
                            
                        
                        print(f"\n{top}\n{mid}\n{botm}\n")
                         #Each IF Statement checks how many chips inputed#
                        if times == 1:
                            print("The machine reads only the MIDDLE row!\n-----------------------")
                             #Checks if USER rolled matching number from combo list | Other results in loss#
                            if mid == jp1 or mid == jp2 or mid == jp3:
                                print("NOW WAY! YOU WON THE JACKPOT!!!")
                                bet = bet * 10
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == w1 or mid == w2 or mid == w3:
                                print("You're a WINNER! Congrats BIG SHOT!")
                                bet = bet * 2
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == comp1 or mid == comp2 or mid == comp3:
                                print("Well... You kinda won...")
                                bet = bet - 20
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            else:
                                print("Oh dang, maybe you should gamble more, you might win~")
                                 #Bullies USER for bad luck!#
                                if mid == L1 or mid == L2 or mid == L3:
                                    print("Wait... did you get... THAT COMBO?\nLOSER!LOSER!LOSER!LOSER!LOSER!")
                                bet = 0
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                                
                         #TWO CHIPS inserted | Same as first condition#    
                        if times == 2:
                            print("The machine reads both the MIDDLE and TOP row!\n-----------------------")
                            if mid == jp1 or mid == jp2 or mid == jp3 or top == jp1 or top == jp2 or top == jp3:
                                print("NOW WAY! YOU WON THE JACKPOT!!!")
                                bet = bet * 10
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == w1 or mid == w2 or mid == w3 or top == w1 or top == w2 or top == w3:
                                print("You're a WINNER! Congrats BIG SHOT!")
                                bet = bet * 2
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == comp1 or mid == comp2 or mid == comp3 or top == comp1 or top == comp2 or top == comp3:
                                print("Well... You kinda won...")
                                bet = bet - 25
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            else:
                                print("Oh dang, maybe you should gamble more, you might win~")
                                if mid == L1 or mid == L2 or mid == L3 or top == L1 or top == L2 or top == L3:
                                    print("Wait... did you get... THAT COMBO?\nLOSER!LOSER!LOSER!LOSER!LOSER!")
                                bet = 0
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                                
                         #Three CHIPS inserted#
                        if times == 3:
                            print("The machine reads EVERY row!\n-----------------------")
                            if mid == jp1 or mid == jp2 or mid == jp3 or top == jp1 or top == jp2 or top == jp3 or botm == jp1 or botm == jp2 or botm == jp3:
                                print("NOW WAY! YOU WON THE JACKPOT!!!")
                                bet = bet * 10
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == w1 or mid == w2 or mid == w3 or top == w1 or top == w2 or top == w3 or botm == w1 or botm == w2 or botm == w3:
                                print("You're a WINNER! Congrats BIG SHOT!")
                                bet = bet * 2
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == comp1 or mid == comp2 or mid == comp3 or top == comp1 or top == comp2 or top == comp3 or botm == comp1 or botm == comp2 or botm == comp3:
                                print("Well... You kinda won...")
                                bet = bet - 37
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            else:
                                print("Oh dang, maybe you should gamble more, you might win~")
                                if mid == L1 or mid == L2 or mid == L3 or top == L1 or top == L2 or top == L3 or botm == L1 or botm == L2 or botm == L3:
                                    print("Wait... did you get... THAT COMBO?\nLOSER!LOSER!LOSER!LOSER!LOSER!")
                                bet = 0
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")

                         #FOUR CHIPS inserted#                           
                        if times == 4:
                            print("The machine reads EVERY row and only the LEFT column!\n-----------------------")
                            if mid == jp1 or mid == jp2 or mid == jp3 or top == jp1 or top == jp2 or top == jp3 or botm == jp1 or botm == jp2 or botm == jp3 or lcm == jp1 or lcm == jp2 or lcm == jp3:
                                print("NOW WAY! YOU WON THE JACKPOT!!!")
                                bet = bet * 10
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == w1 or mid == w2 or mid == w3 or top == w1 or top == w2 or top == w3 or botm == w1 or botm == w2 or botm == w3 or lcm == w1 or lcm == w2 or lcm == w3:
                                print("You're a WINNER! Congrats BIG SHOT!")
                                bet = bet * 2
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == comp1 or mid == comp2 or mid == comp3 or top == comp1 or top == comp2 or top == comp3 or botm == comp1 or botm == comp2 or botm == comp3 or lcm == comp1 or lcm == comp2 or lcm == comp3:
                                print("Well... You kinda won...")
                                bet = bet - 50
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            else:
                                print("Oh dang, maybe you should gamble more, you might win~")
                                if mid == L1 or mid == L2 or mid == L3 or top == L1 or top == L2 or top == L3 or botm == L1 or botm == L2 or botm == L3 or lcm == L1 or lcm == L2 or lcm == L3:
                                    print("Wait... did you get... THAT COMBO?\nLOSER!LOSER!LOSER!LOSER!LOSER!")
                                bet = 0
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")

                         #FIVE CHIPS inserted#    
                        if times == 5:
                            print("The machine reads EVERY row and both the LEFT and MIDDLE column!\n-----------------------")
                            if mid == jp1 or mid == jp2 or mid == jp3 or top == jp1 or top == jp2 or top == jp3 or botm == jp1 or botm == jp2 or botm == jp3 or lcm == jp1 or lcm == jp2 or lcm == jp3 or mcm == jp1 or mcm == jp2 or mcm == jp3:
                                print("NOW WAY! YOU WON THE JACKPOT!!!")
                                bet = bet * 10
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == w1 or mid == w2 or mid == w3 or top == w1 or top == w2 or top == w3 or botm == w1 or botm == w2 or botm == w3 or lcm == w1 or lcm == w2 or lcm == w3 or mcm == w1 or mcm == w2 or mcm == w3:
                                print("You're a WINNER! Congrats BIG SHOT!")
                                bet = bet * 2
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == comp1 or mid == comp2 or mid == comp3 or top == comp1 or top == comp2 or top == comp3 or botm == comp1 or botm == comp2 or botm == comp3 or lcm == comp1 or lcm == comp2 or lcm == comp3 or mcm == comp1 or mcm == comp2 or mcm == comp3:
                                print("Well... You kinda won...")
                                bet = bet - 62
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            else:
                                print("Oh dang, maybe you should gamble more, you might win~")
                                if mid == L1 or mid == L2 or mid == L3 or top == L1 or top == L2 or top == L3 or botm == L1 or botm == L2 or botm == L3 or lcm == L1 or lcm == L2 or lcm == L3 or mcm == L1 or mcm == L2 or mcm == L3:
                                    print("Wait... did you get... THAT COMBO?\nLOSER!LOSER!LOSER!LOSER!LOSER!")
                                bet = 0
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")

                         #SIX CHIPS inserted#    
                        if times == 6:
                            print("The machine reads EVERY row and EVERY column!\n-----------------------")
                            if mid == jp1 or mid == jp2 or mid == jp3 or top == jp1 or top == jp2 or top == jp3 or botm == jp1 or botm == jp2 or botm == jp3 or lcm == jp1 or lcm == jp2 or lcm == jp3 or mcm == jp1 or mcm == jp2 or mcm == jp3 or rcm == jp1 or rcm == jp2 or rcm == jp3:
                                print("NOW WAY! YOU WON THE JACKPOT!!!")
                                bet = bet * 10
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == w1 or mid == w2 or mid == w3 or top == w1 or top == w2 or top == w3 or botm == w1 or botm == w2 or botm == w3 or lcm == w1 or lcm == w2 or lcm == w3 or mcm == w1 or mcm == w2 or mcm == w3 or rcm == w1 or rcm == w2 or rcm == w3:
                                print("You're a WINNER! Congrats BIG SHOT!")
                                bet = bet * 2
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == comp1 or mid == comp2 or mid == comp3 or top == comp1 or top == comp2 or top == comp3 or botm == comp1 or botm == comp2 or botm == comp3 or lcm == comp1 or lcm == comp2 or lcm == comp3 or mcm == comp1 or mcm == comp2 or mcm == comp3 or rcm == comp1 or rcm == comp2 or rcm == comp3:
                                print("Well... You kinda won...")
                                bet = bet - 75
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            else:
                                print("Oh dang, maybe you should gamble more, you might win~")
                                if mid == L1 or mid == L2 or mid == L3 or top == L1 or top == L2 or top == L3 or botm == L1 or botm == L2 or botm == L3 or lcm == L1 or lcm == L2 or lcm == L3 or mcm == L1 or mcm == L2 or mcm == L3 or rcm == L1 or rcm == L2 or rcm == L3:
                                    print("Wait... did you get... THAT COMBO?\nLOSER!LOSER!LOSER!LOSER!LOSER!")
                                bet = 0
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")

                         #SEVEN CHIPS inserted#    
                        if times == 7:
                            print("The machine reads EVERY row, EVERY column, and the DIAGONAL from TOP-LEFT to BOTTOM-RIGHT! [help me]\n-----------------------")
                            if mid == jp1 or mid == jp2 or mid == jp3 or top == jp1 or top == jp2 or top == jp3 or botm == jp1 or botm == jp2 or botm == jp3 or lcm == jp1 or lcm == jp2 or lcm == jp3 or mcm == jp1 or mcm == jp2 or mcm == jp3 or rcm == jp1 or rcm == jp2 or rcm == jp3 or dg1 == jp1 or dg1 == jp2 or dg1 == jp3:
                                print("NOW WAY! YOU WON THE JACKPOT!!!")
                                bet = bet * 10
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == w1 or mid == w2 or mid == w3 or top == w1 or top == w2 or top == w3 or botm == w1 or botm == w2 or botm == w3 or lcm == w1 or lcm == w2 or lcm == w3 or mcm == w1 or mcm == w2 or mcm == w3 or rcm == w1 or rcm == w2 or rcm == w3 or dg1 == w1 or dg1 == w2 or dg1 == w3:
                                print("You're a WINNER! Congrats BIG SHOT!")
                                bet = bet * 2
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == comp1 or mid == comp2 or mid == comp3 or top == comp1 or top == comp2 or top == comp3 or botm == comp1 or botm == comp2 or botm == comp3 or lcm == comp1 or lcm == comp2 or lcm == comp3 or mcm == comp1 or mcm == comp2 or mcm == comp3 or rcm == comp1 or rcm == comp2 or rcm == comp3 or dg1 == comp1 or dg1 == comp2 or dg1 == comp3:
                                print("Well... You kinda won...")
                                bet = bet - 87
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            else:
                                print("Oh dang, maybe you should gamble more, you might win~")
                                if mid == L1 or mid == L2 or mid == L3 or top == L1 or top == L2 or top == L3 or botm == L1 or botm == L2 or botm == L3 or lcm == L1 or lcm == L2 or lcm == L3 or mcm == L1 or mcm == L2 or mcm == L3 or rcm == L1 or rcm == L2 or rcm == L3 or dg1 == L1 or dg1 == L2 or dg1 == L3:
                                    print("Wait... did you get... THAT COMBO?\nLOSER!LOSER!LOSER!LOSER!LOSER!")
                                bet = 0
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")

                         #EIGHT CHIPS inserted#    
                        if times == 8:
                            print("The machine reads EVERY POSSIBILITY!\n-----------------------")
                            if mid == jp1 or mid == jp2 or mid == jp3 or top == jp1 or top == jp2 or top == jp3 or botm == jp1 or botm == jp2 or botm == jp3 or lcm == jp1 or lcm == jp2 or lcm == jp3 or mcm == jp1 or mcm == jp2 or mcm == jp3 or rcm == jp1 or rcm == jp2 or rcm == jp3 or dg1 == jp1 or dg1 == jp2 or dg1 == jp3 or dg2 == jp1 or dg2 == jp2 or dg2 == jp3:
                                print("NOW WAY! YOU WON THE JACKPOT!!!")
                                bet = bet * 10
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == w1 or mid == w2 or mid == w3 or top == w1 or top == w2 or top == w3 or botm == w1 or botm == w2 or botm == w3 or lcm == w1 or lcm == w2 or lcm == w3 or mcm == w1 or mcm == w2 or mcm == w3 or rcm == w1 or rcm == w2 or rcm == w3 or dg1 == w1 or dg1 == w2 or dg1 == w3 or dg2 == w1 or dg2 == w2 or dg2 == w3:
                                print("You're a WINNER! Congrats BIG SHOT!")
                                bet = bet * 2
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == comp1 or mid == comp2 or mid == comp3 or top == comp1 or top == comp2 or top == comp3 or botm == comp1 or botm == comp2 or botm == comp3 or lcm == comp1 or lcm == comp2 or lcm == comp3 or mcm == comp1 or mcm == comp2 or mcm == comp3 or rcm == comp1 or rcm == comp2 or rcm == comp3 or dg1 == comp1 or dg1 == comp2 or dg1 == comp3 or dg2 == comp1 or dg2 == comp2 or dg2 == comp3:
                                print("Well... You kinda won...")
                                bet = bet - 100
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            else:
                                print("Oh dang, maybe you should gamble more, you might win~")
                                if mid == L1 or mid == L2 or mid == L3 or top == L1 or top == L2 or top == L3 or botm == L1 or botm == L2 or botm == L3 or lcm == L1 or lcm == L2 or lcm == L3 or mcm == L1 or mcm == L2 or mcm == L3 or rcm == L1 or rcm == L2 or rcm == L3 or dg1 == L1 or dg1 == L2 or dg1 == L3 or dg2 == L1 or dg2 == L2 or dg2 == L3:
                                    print("Wait... did you get... THAT COMBO?\nLOSER!LOSER!LOSER!LOSER!LOSER!")
                                bet = 0
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                        check = True

                 #Checks if USER runs out of money#
                if balance <= 0:
                    print("\nHey... you don't have any more money for these, STOP LOITERING!")
                    print("\n[The Host of the SLOTZ ZONE realized you're out of cash! He kicks you out of the CLAMS CASINO and you leave empty handed]\n-----------------------")
                    main(balance, key, green)
                    
                 #Asks USER if they want to go again or pull up COMBO GUIDE#
                while hiddenmark == True and hiddenmark2 == True and balance > 0 and check == True:
                    advance = input("\nWould you like to continue? (YES/Y or NO/N | GUIDE for COMBOS) ")
                     #The slot perks itself up again if TRUE#
                    if advance.lower() == "yes" or advance.lower() == "y":
                        print("[Your hands get ready as the slot machine perks itself...] \n")
                        hiddenmark2 = False
                     #Shows COMBO GUIDE
                    elif advance.lower() == "guide" or advance.lower() == "help" or advance.lower() == "combo" or advance.lower() == "combos":
                        print("COMBO GUIDE:\n----------------------")
                        print("{}[===JACKPOT===]{}\n[7,7,7] | [9,8,5] | [9,9,9]\n")
                        print(":===WIN===:\n[3,3,3] | [9,6,9] | [6,9,6]\n")
                        print("<~~~COMPENSATION~~~>\n[2,2,2] | [5,5,5] | [3,2,1]\n")
                        print("[<>>LOSE<<>]\n[6,6,6] | [4,4,4] | [0,0,0] | [ANY OTHER COMBINATION]\n----------------------")
                     #Allows USER to return to SLOTZHUB#
                    elif advance.lower() == "no" or advance.lower() == "n":
                        print("[You say goodbye to the LOW-LEVEL-SLOTZ as you return to the SLOTZ HUB, a tear sheds from your eye for some reason~... but why?]\n")
                        hiddenmark2 = False
                        stay = False
                        condition = True
                     #Sees if USER responds humanly#
                    else:
                        print("[Sorry, what did you mean by that?...]")
             #Prevents Softlock#
            if balance <= 25:
                print("Oh dear, it seems you don't have enough money to play these HIGH-LEVEL-SLOTZ anymore...")
                print("[The Host of the SLOTS guides you back to the SLOTZ-HUB]")

        #ASSUME EVERYTHING TO HAVE THE SAME FUNCTION; ONLY DIFFERENCE IS WITH AMOUNT BETTED AND DIALOUGE#
        #MEDIUM SLOTZ#            
        elif location.lower() == "medium" or location.lower() == "med" or location.lower() == "m":
            print("[You walk over to the MEDIUM-LEVEL-SLOTZ ZONE]\n-----------------------")
            print("Welcome to the MEDIUM-LEVEL-SLOTZ ZONE! This won't eat your wallet too much...")
            while balance >= 250 and stay == True:
                hiddenmark2 = True
                check = False
                times = int(input(f"How many chips (1-8 CHIPS MAX) will you bet? [You have: ${balance}] "))
                if times <= 0 or times == 0:
                    print("Uh seriously? You are trying to GAMBLE here? How are you going win man...\n")               
                if times > 8:
                    print("I don't think these machines can handle that many chips...\n")   
                if times > 0 and times <= 8:
                    bet = times * 250
                    if bet > balance:
                        print("Woah! You don't have enough to fully pay for all possibilities, try betting less chips?")
                    if bet <= balance and bet > 0:
                        print(f"[You insert the chips into the machine!]\n\nYOU BET: ${bet}\n-----------------------")
                        balance = balance - bet
                            
                        tl = random.randint(0,9)
                        tm = random.randint(0,9)
                        tr = random.randint(0,9)
                        ml = random.randint(0,9)
                        mm = random.randint(0,9)
                        mr = random.randint(0,9)
                        bl = random.randint(0,9)
                        bm = random.randint(0,9)
                        br = random.randint(0,9)

                        top = [tl,tm,tr]
                        mid = [ml,mm,mr]
                        botm = [bl,bm,br]
                        lcm = [tl,ml,bl]
                        mcm = [tm,mm,bm]
                        rcm = [tr,mr,br]
                        dg1 = [tr,mm,br]
                        dg2 = [bl,mm,tr]
                            
                        print(f"\n{top}\n{mid}\n{botm}\n")

                        if times == 1:
                            print("The machine reads only the MIDDLE row!\n-----------------------")
                            if mid == jp1 or mid == jp2 or mid == jp3:
                                print("NOW WAY! YOU WON THE JACKPOT!!!")
                                bet = bet * 10
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == w1 or mid == w2 or mid == w3:
                                print("You're a WINNER! Congrats BIG SHOT!")
                                bet = bet * 2
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == comp1 or mid == comp2 or mid == comp3:
                                print("Well... You kinda won...")
                                bet = bet - 125
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            else:
                                print("Oh dang, maybe you should gamble more, you might win~")
                                if mid == L1 or mid == L2 or mid == L3:
                                    print("Wait... did you get... THAT COMBO?\nLOSER!LOSER!LOSER!LOSER!LOSER!")
                                bet = 0
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")     
                        if times == 2:
                            print("The machine reads both the MIDDLE and TOP row!\n-----------------------")
                            if mid == jp1 or mid == jp2 or mid == jp3 or top == jp1 or top == jp2 or top == jp3:
                                print("NOW WAY! YOU WON THE JACKPOT!!!")
                                bet = bet * 10
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == w1 or mid == w2 or mid == w3 or top == w1 or top == w2 or top == w3:
                                print("You're a WINNER! Congrats BIG SHOT!")
                                bet = bet * 2
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == comp1 or mid == comp2 or mid == comp3 or top == comp1 or top == comp2 or top == comp3:
                                print("Well... You kinda won...")
                                bet = bet - 250
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            else:
                                print("Oh dang, maybe you should gamble more, you might win~")
                                if mid == L1 or mid == L2 or mid == L3 or top == L1 or top == L2 or top == L3:
                                    print("Wait... did you get... THAT COMBO?\nLOSER!LOSER!LOSER!LOSER!LOSER!")
                                bet = 0
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                        if times == 3:
                            print("The machine reads EVERY row!\n-----------------------")
                            if mid == jp1 or mid == jp2 or mid == jp3 or top == jp1 or top == jp2 or top == jp3 or botm == jp1 or botm == jp2 or botm == jp3:
                                print("NOW WAY! YOU WON THE JACKPOT!!!")
                                bet = bet * 10
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == w1 or mid == w2 or mid == w3 or top == w1 or top == w2 or top == w3 or botm == w1 or botm == w2 or botm == w3:
                                print("You're a WINNER! Congrats BIG SHOT!")
                                bet = bet * 2
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == comp1 or mid == comp2 or mid == comp3 or top == comp1 or top == comp2 or top == comp3 or botm == comp1 or botm == comp2 or botm == comp3:
                                print("Well... You kinda won...")
                                bet = bet - 375
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            else:
                                print("Oh dang, maybe you should gamble more, you might win~")
                                if mid == L1 or mid == L2 or mid == L3 or top == L1 or top == L2 or top == L3 or botm == L1 or botm == L2 or botm == L3:
                                    print("Wait... did you get... THAT COMBO?\nLOSER!LOSER!LOSER!LOSER!LOSER!")
                                bet = 0
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")        
                        if times == 4:
                            print("The machine reads EVERY row and only the LEFT column!\n-----------------------")
                            if mid == jp1 or mid == jp2 or mid == jp3 or top == jp1 or top == jp2 or top == jp3 or botm == jp1 or botm == jp2 or botm == jp3 or lcm == jp1 or lcm == jp2 or lcm == jp3:
                                print("NOW WAY! YOU WON THE JACKPOT!!!")
                                bet = bet * 10
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == w1 or mid == w2 or mid == w3 or top == w1 or top == w2 or top == w3 or botm == w1 or botm == w2 or botm == w3 or lcm == w1 or lcm == w2 or lcm == w3:
                                print("You're a WINNER! Congrats BIG SHOT!")
                                bet = bet * 2
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == comp1 or mid == comp2 or mid == comp3 or top == comp1 or top == comp2 or top == comp3 or botm == comp1 or botm == comp2 or botm == comp3 or lcm == comp1 or lcm == comp2 or lcm == comp3:
                                print("Well... You kinda won...")
                                bet = bet - 500
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            else:
                                print("Oh dang, maybe you should gamble more, you might win~")
                                if mid == L1 or mid == L2 or mid == L3 or top == L1 or top == L2 or top == L3 or botm == L1 or botm == L2 or botm == L3 or lcm == L1 or lcm == L2 or lcm == L3:
                                    print("Wait... did you get... THAT COMBO?\nLOSER!LOSER!LOSER!LOSER!LOSER!")
                                bet = 0
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")        
                        if times == 5:
                            print("The machine reads EVERY row and both the LEFT and MIDDLE column!\n-----------------------")
                            if mid == jp1 or mid == jp2 or mid == jp3 or top == jp1 or top == jp2 or top == jp3 or botm == jp1 or botm == jp2 or botm == jp3 or lcm == jp1 or lcm == jp2 or lcm == jp3 or mcm == jp1 or mcm == jp2 or mcm == jp3:
                                print("NOW WAY! YOU WON THE JACKPOT!!!")
                                bet = bet * 10
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == w1 or mid == w2 or mid == w3 or top == w1 or top == w2 or top == w3 or botm == w1 or botm == w2 or botm == w3 or lcm == w1 or lcm == w2 or lcm == w3 or mcm == w1 or mcm == w2 or mcm == w3:
                                print("You're a WINNER! Congrats BIG SHOT!")
                                bet = bet * 2
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == comp1 or mid == comp2 or mid == comp3 or top == comp1 or top == comp2 or top == comp3 or botm == comp1 or botm == comp2 or botm == comp3 or lcm == comp1 or lcm == comp2 or lcm == comp3 or mcm == comp1 or mcm == comp2 or mcm == comp3:
                                print("Well... You kinda won...")
                                bet = bet - 625
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            else:
                                print("Oh dang, maybe you should gamble more, you might win~")
                                if mid == L1 or mid == L2 or mid == L3 or top == L1 or top == L2 or top == L3 or botm == L1 or botm == L2 or botm == L3 or lcm == L1 or lcm == L2 or lcm == L3 or mcm == L1 or mcm == L2 or mcm == L3:
                                    print("Wait... did you get... THAT COMBO?\nLOSER!LOSER!LOSER!LOSER!LOSER!")
                                bet = 0
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                        if times == 6:
                            print("The machine reads EVERY row and EVERY column!\n-----------------------")
                            if mid == jp1 or mid == jp2 or mid == jp3 or top == jp1 or top == jp2 or top == jp3 or botm == jp1 or botm == jp2 or botm == jp3 or lcm == jp1 or lcm == jp2 or lcm == jp3 or mcm == jp1 or mcm == jp2 or mcm == jp3 or rcm == jp1 or rcm == jp2 or rcm == jp3:
                                print("NOW WAY! YOU WON THE JACKPOT!!!")
                                bet = bet * 10
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == w1 or mid == w2 or mid == w3 or top == w1 or top == w2 or top == w3 or botm == w1 or botm == w2 or botm == w3 or lcm == w1 or lcm == w2 or lcm == w3 or mcm == w1 or mcm == w2 or mcm == w3 or rcm == w1 or rcm == w2 or rcm == w3:
                                print("You're a WINNER! Congrats BIG SHOT!")
                                bet = bet * 2
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == comp1 or mid == comp2 or mid == comp3 or top == comp1 or top == comp2 or top == comp3 or botm == comp1 or botm == comp2 or botm == comp3 or lcm == comp1 or lcm == comp2 or lcm == comp3 or mcm == comp1 or mcm == comp2 or mcm == comp3 or rcm == comp1 or rcm == comp2 or rcm == comp3:
                                print("Well... You kinda won...")
                                bet = bet - 750
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            else:
                                print("Oh dang, maybe you should gamble more, you might win~")
                                if mid == L1 or mid == L2 or mid == L3 or top == L1 or top == L2 or top == L3 or botm == L1 or botm == L2 or botm == L3 or lcm == L1 or lcm == L2 or lcm == L3 or mcm == L1 or mcm == L2 or mcm == L3 or rcm == L1 or rcm == L2 or rcm == L3:
                                    print("Wait... did you get... THAT COMBO?\nLOSER!LOSER!LOSER!LOSER!LOSER!")
                                bet = 0
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                        if times == 7:
                            print("The machine reads EVERY row, EVERY column, and the DIAGONAL from TOP-LEFT to BOTTOM-RIGHT! [help me]\n-----------------------")
                            if mid == jp1 or mid == jp2 or mid == jp3 or top == jp1 or top == jp2 or top == jp3 or botm == jp1 or botm == jp2 or botm == jp3 or lcm == jp1 or lcm == jp2 or lcm == jp3 or mcm == jp1 or mcm == jp2 or mcm == jp3 or rcm == jp1 or rcm == jp2 or rcm == jp3 or dg1 == jp1 or dg1 == jp2 or dg1 == jp3:
                                print("NOW WAY! YOU WON THE JACKPOT!!!")
                                bet = bet * 10
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == w1 or mid == w2 or mid == w3 or top == w1 or top == w2 or top == w3 or botm == w1 or botm == w2 or botm == w3 or lcm == w1 or lcm == w2 or lcm == w3 or mcm == w1 or mcm == w2 or mcm == w3 or rcm == w1 or rcm == w2 or rcm == w3 or dg1 == w1 or dg1 == w2 or dg1 == w3:
                                print("You're a WINNER! Congrats BIG SHOT!")
                                bet = bet * 2
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == comp1 or mid == comp2 or mid == comp3 or top == comp1 or top == comp2 or top == comp3 or botm == comp1 or botm == comp2 or botm == comp3 or lcm == comp1 or lcm == comp2 or lcm == comp3 or mcm == comp1 or mcm == comp2 or mcm == comp3 or rcm == comp1 or rcm == comp2 or rcm == comp3 or dg1 == comp1 or dg1 == comp2 or dg1 == comp3:
                                print("Well... You kinda won...")
                                bet = bet - 875
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            else:
                                print("Oh dang, maybe you should gamble more, you might win~")
                                if mid == L1 or mid == L2 or mid == L3 or top == L1 or top == L2 or top == L3 or botm == L1 or botm == L2 or botm == L3 or lcm == L1 or lcm == L2 or lcm == L3 or mcm == L1 or mcm == L2 or mcm == L3 or rcm == L1 or rcm == L2 or rcm == L3 or dg1 == L1 or dg1 == L2 or dg1 == L3:
                                    print("Wait... did you get... THAT COMBO?\nLOSER!LOSER!LOSER!LOSER!LOSER!")
                                bet = 0
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                        if times == 8:
                            print("The machine reads EVERY POSSIBILITY!\n-----------------------")
                            if mid == jp1 or mid == jp2 or mid == jp3 or top == jp1 or top == jp2 or top == jp3 or botm == jp1 or botm == jp2 or botm == jp3 or lcm == jp1 or lcm == jp2 or lcm == jp3 or mcm == jp1 or mcm == jp2 or mcm == jp3 or rcm == jp1 or rcm == jp2 or rcm == jp3 or dg1 == jp1 or dg1 == jp2 or dg1 == jp3 or dg2 == jp1 or dg2 == jp2 or dg2 == jp3:
                                print("NOW WAY! YOU WON THE JACKPOT!!!")
                                bet = bet * 10
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == w1 or mid == w2 or mid == w3 or top == w1 or top == w2 or top == w3 or botm == w1 or botm == w2 or botm == w3 or lcm == w1 or lcm == w2 or lcm == w3 or mcm == w1 or mcm == w2 or mcm == w3 or rcm == w1 or rcm == w2 or rcm == w3 or dg1 == w1 or dg1 == w2 or dg1 == w3 or dg2 == w1 or dg2 == w2 or dg2 == w3:
                                print("You're a WINNER! Congrats BIG SHOT!")
                                bet = bet * 2
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == comp1 or mid == comp2 or mid == comp3 or top == comp1 or top == comp2 or top == comp3 or botm == comp1 or botm == comp2 or botm == comp3 or lcm == comp1 or lcm == comp2 or lcm == comp3 or mcm == comp1 or mcm == comp2 or mcm == comp3 or rcm == comp1 or rcm == comp2 or rcm == comp3 or dg1 == comp1 or dg1 == comp2 or dg1 == comp3 or dg2 == comp1 or dg2 == comp2 or dg2 == comp3:
                                print("Well... You kinda won...")
                                bet = bet - 1000
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            else:
                                print("Oh dang, maybe you should gamble more, you might win~")
                                if mid == L1 or mid == L2 or mid == L3 or top == L1 or top == L2 or top == L3 or botm == L1 or botm == L2 or botm == L3 or lcm == L1 or lcm == L2 or lcm == L3 or mcm == L1 or mcm == L2 or mcm == L3 or rcm == L1 or rcm == L2 or rcm == L3 or dg1 == L1 or dg1 == L2 or dg1 == L3 or dg2 == L1 or dg2 == L2 or dg2 == L3:
                                    print("Wait... did you get... THAT COMBO?\nLOSER!LOSER!LOSER!LOSER!LOSER!")
                                bet = 0
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                        check = True

                if balance <= 0:
                    print("\nHey... you don't have any more money for these, STOP LOITERING!")
                    print("\n[The Host of the SLOTZ ZONE realized you're out of cash! He kicks you out of the CLAMS CASINO and you leave empty handed]\n-----------------------")
                    main(balance, key, green)
             
                while hiddenmark == True and hiddenmark2 == True and balance > 0 and check == True:
                    advance = input("\nWould you like to continue? (YES/Y or NO/N | GUIDE for COMBOS) ")
                    if advance.lower() == "yes" or advance.lower() == "y":
                        print("[Your hands get ready as the slot machine perks itself...] \n")
                        hiddenmark2 = False
                    elif advance.lower() == "guide" or advance.lower() == "help" or advance.lower() == "combo" or advance.lower() == "combos":
                        print("COMBO GUIDE:\n----------------------")
                        print("{}[===JACKPOT===]{}\n[7,7,7] | [9,8,5] | [9,9,9]\n")
                        print(":===WIN===:\n[3,3,3] | [9,6,9] | [6,9,6]\n")
                        print("<~~~COMPENSATION~~~>\n[2,2,2] | [5,5,5] | [3,2,1]\n")
                        print("[<>>LOSE<<>]\n[6,6,6] | [4,4,4] | [0,0,0] | [ANY OTHER COMBINATION]\n----------------------")
                    elif advance.lower() == "no" or advance.lower() == "n":
                        print("[You leave the MEDIUM-LEVEL-SLOTZ. Perhaphs you have better luck somewhere else...]\n")
                        hiddenmark2 = False
                        stay = False
                        condition = True
                    else:
                        print("[Sorry, what did you mean by that?...]")
            if balance < 250:
                print("Oh dear, it seems you don't have enough money to play these HIGH-LEVEL-SLOTZ anymore...")
                print("[The Host of the SLOTS guides you back to the SLOTZ-HUB]")


        #STILL THE SAME THING AS PREVIOUS LEVELS | LEGIT COPY AN PASTE#
        #HIGH SLOTZ#        
        elif location.lower() == "high" or location.lower() == "h":
            print("[You walk over to the HIGH-LEVEL-SLOTZ ZONE]\n-----------------------")
            print("WELCOME TO THE RICH MAN ZONE!... Sorry, I get excited when people go to this side... this is the HIGH-LEVEL-SLOTZ ZONE by the way...")
            while balance >= 500 and stay == True:
                hiddenmark2 = True
                check = False
                times = int(input(f"How many chips (1-8 CHIPS MAX) will you bet? [You have: ${balance}] "))
                if times <= 0 or times == 0:
                    print("Uh seriously? You are trying to GAMBLE here? How are you going win man...\n")
                if times > 8:
                    print("I don't think these machines can handle that many chips...\n")  
                if times > 0 and times <= 8:
                    bet = times * 500
                    if bet > balance:
                        print("Woah! You don't have enough to fully pay for all possibilities, try betting less chips?\n")
                    if bet <= balance and bet > 0:
                        print(f"[You insert the chips into the machine!]\n\nYOU BET: ${bet}\n-----------------------")
                        balance = balance - bet
                            
                        tl = random.randint(0,9)
                        tm = random.randint(0,9)
                        tr = random.randint(0,9)
                        ml = random.randint(0,9)
                        mm = random.randint(0,9)
                        mr = random.randint(0,9)
                        bl = random.randint(0,9)
                        bm = random.randint(0,9)
                        br = random.randint(0,9)

                        top = [tl,tm,tr]
                        mid = [ml,mm,mr]
                        botm = [bl,bm,br]
                        lcm = [tl,ml,bl]
                        mcm = [tm,mm,bm]
                        rcm = [tr,mr,br]
                        dg1 = [tr,mm,br]
                        dg2 = [bl,mm,tr]
                            
                        print(f"\n{top}\n{mid}\n{botm}\n")

                        if times == 1:
                            print("The machine reads only the MIDDLE row!\n-----------------------")
                            if mid == jp1 or mid == jp2 or mid == jp3:
                                print("NOW WAY! YOU WON THE JACKPOT!!!")
                                bet = bet * 10
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == w1 or mid == w2 or mid == w3:
                                print("You're a WINNER! Congrats BIG SHOT!")
                                bet = bet * 2
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == comp1 or mid == comp2 or mid == comp3:
                                print("Well... You kinda won...")
                                bet = bet - 250
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            else:
                                print("Oh dang, maybe you should gamble more, you might win~")
                                if mid == L1 or mid == L2 or mid == L3:
                                    print("Wait... did you get... THAT COMBO?\nLOSER!LOSER!LOSER!LOSER!LOSER!")
                                bet = 0
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")        
                        if times == 2:
                            print("The machine reads both the MIDDLE and TOP row!\n-----------------------")
                            if mid == jp1 or mid == jp2 or mid == jp3 or top == jp1 or top == jp2 or top == jp3:
                                print("NOW WAY! YOU WON THE JACKPOT!!!")
                                bet = bet * 10
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == w1 or mid == w2 or mid == w3 or top == w1 or top == w2 or top == w3:
                                print("You're a WINNER! Congrats BIG SHOT!")
                                bet = bet * 2
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == comp1 or mid == comp2 or mid == comp3 or top == comp1 or top == comp2 or top == comp3:
                                print("Well... You kinda won...")
                                bet = bet - 500
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            else:
                                print("Oh dang, maybe you should gamble more, you might win~")
                                if mid == L1 or mid == L2 or mid == L3 or top == L1 or top == L2 or top == L3:
                                    print("Wait... did you get... THAT COMBO?\nLOSER!LOSER!LOSER!LOSER!LOSER!")
                                bet = 0
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                        if times == 3:
                            print("The machine reads EVERY row!\n-----------------------")
                            if mid == jp1 or mid == jp2 or mid == jp3 or top == jp1 or top == jp2 or top == jp3 or botm == jp1 or botm == jp2 or botm == jp3:
                                print("NOW WAY! YOU WON THE JACKPOT!!!")
                                bet = bet * 10
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == w1 or mid == w2 or mid == w3 or top == w1 or top == w2 or top == w3 or botm == w1 or botm == w2 or botm == w3:
                                print("You're a WINNER! Congrats BIG SHOT!")
                                bet = bet * 2
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == comp1 or mid == comp2 or mid == comp3 or top == comp1 or top == comp2 or top == comp3 or botm == comp1 or botm == comp2 or botm == comp3:
                                print("Well... You kinda won...")
                                bet = bet - 750
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            else:
                                print("Oh dang, maybe you should gamble more, you might win~")
                                if mid == L1 or mid == L2 or mid == L3 or top == L1 or top == L2 or top == L3 or botm == L1 or botm == L2 or botm == L3:
                                    print("Wait... did you get... THAT COMBO?\nLOSER!LOSER!LOSER!LOSER!LOSER!")
                                bet = 0
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")         
                        if times == 4:
                            print("The machine reads EVERY row and only the LEFT column!\n-----------------------")
                            if mid == jp1 or mid == jp2 or mid == jp3 or top == jp1 or top == jp2 or top == jp3 or botm == jp1 or botm == jp2 or botm == jp3 or lcm == jp1 or lcm == jp2 or lcm == jp3:
                                print("NOW WAY! YOU WON THE JACKPOT!!!")
                                bet = bet * 10
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == w1 or mid == w2 or mid == w3 or top == w1 or top == w2 or top == w3 or botm == w1 or botm == w2 or botm == w3 or lcm == w1 or lcm == w2 or lcm == w3:
                                print("You're a WINNER! Congrats BIG SHOT!")
                                bet = bet * 2
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == comp1 or mid == comp2 or mid == comp3 or top == comp1 or top == comp2 or top == comp3 or botm == comp1 or botm == comp2 or botm == comp3 or lcm == comp1 or lcm == comp2 or lcm == comp3:
                                print("Well... You kinda won...")
                                bet = bet - 1000
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            else:
                                print("Oh dang, maybe you should gamble more, you might win~")
                                if mid == L1 or mid == L2 or mid == L3 or top == L1 or top == L2 or top == L3 or botm == L1 or botm == L2 or botm == L3 or lcm == L1 or lcm == L2 or lcm == L3:
                                    print("Wait... did you get... THAT COMBO?\nLOSER!LOSER!LOSER!LOSER!LOSER!")
                                bet = 0
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")       
                        if times == 5:
                            print("The machine reads EVERY row and both the LEFT and MIDDLE column!\n-----------------------")
                            if mid == jp1 or mid == jp2 or mid == jp3 or top == jp1 or top == jp2 or top == jp3 or botm == jp1 or botm == jp2 or botm == jp3 or lcm == jp1 or lcm == jp2 or lcm == jp3 or mcm == jp1 or mcm == jp2 or mcm == jp3:
                                print("NOW WAY! YOU WON THE JACKPOT!!!")
                                bet = bet * 10
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == w1 or mid == w2 or mid == w3 or top == w1 or top == w2 or top == w3 or botm == w1 or botm == w2 or botm == w3 or lcm == w1 or lcm == w2 or lcm == w3 or mcm == w1 or mcm == w2 or mcm == w3:
                                print("You're a WINNER! Congrats BIG SHOT!")
                                bet = bet * 2
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == comp1 or mid == comp2 or mid == comp3 or top == comp1 or top == comp2 or top == comp3 or botm == comp1 or botm == comp2 or botm == comp3 or lcm == comp1 or lcm == comp2 or lcm == comp3 or mcm == comp1 or mcm == comp2 or mcm == comp3:
                                print("Well... You kinda won...")
                                bet = bet - 1250
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            else:
                                print("Oh dang, maybe you should gamble more, you might win~")
                                if mid == L1 or mid == L2 or mid == L3 or top == L1 or top == L2 or top == L3 or botm == L1 or botm == L2 or botm == L3 or lcm == L1 or lcm == L2 or lcm == L3 or mcm == L1 or mcm == L2 or mcm == L3:
                                    print("Wait... did you get... THAT COMBO?\nLOSER!LOSER!LOSER!LOSER!LOSER!")
                                bet = 0
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                        if times == 6:
                            print("The machine reads EVERY row and EVERY column!\n-----------------------")
                            if mid == jp1 or mid == jp2 or mid == jp3 or top == jp1 or top == jp2 or top == jp3 or botm == jp1 or botm == jp2 or botm == jp3 or lcm == jp1 or lcm == jp2 or lcm == jp3 or mcm == jp1 or mcm == jp2 or mcm == jp3 or rcm == jp1 or rcm == jp2 or rcm == jp3:
                                print("NOW WAY! YOU WON THE JACKPOT!!!")
                                bet = bet * 10
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == w1 or mid == w2 or mid == w3 or top == w1 or top == w2 or top == w3 or botm == w1 or botm == w2 or botm == w3 or lcm == w1 or lcm == w2 or lcm == w3 or mcm == w1 or mcm == w2 or mcm == w3 or rcm == w1 or rcm == w2 or rcm == w3:
                                print("You're a WINNER! Congrats BIG SHOT!")
                                bet = bet * 2
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == comp1 or mid == comp2 or mid == comp3 or top == comp1 or top == comp2 or top == comp3 or botm == comp1 or botm == comp2 or botm == comp3 or lcm == comp1 or lcm == comp2 or lcm == comp3 or mcm == comp1 or mcm == comp2 or mcm == comp3 or rcm == comp1 or rcm == comp2 or rcm == comp3:
                                print("Well... You kinda won...")
                                bet = bet - 1500
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            else:
                                print("Oh dang, maybe you should gamble more, you might win~")
                                if mid == L1 or mid == L2 or mid == L3 or top == L1 or top == L2 or top == L3 or botm == L1 or botm == L2 or botm == L3 or lcm == L1 or lcm == L2 or lcm == L3 or mcm == L1 or mcm == L2 or mcm == L3 or rcm == L1 or rcm == L2 or rcm == L3:
                                    print("Wait... did you get... THAT COMBO?\nLOSER!LOSER!LOSER!LOSER!LOSER!")
                                bet = 0
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                        if times == 7:
                            print("The machine reads EVERY row, EVERY column, and the DIAGONAL from TOP-LEFT to BOTTOM-RIGHT! [help me]\n-----------------------")
                            if mid == jp1 or mid == jp2 or mid == jp3 or top == jp1 or top == jp2 or top == jp3 or botm == jp1 or botm == jp2 or botm == jp3 or lcm == jp1 or lcm == jp2 or lcm == jp3 or mcm == jp1 or mcm == jp2 or mcm == jp3 or rcm == jp1 or rcm == jp2 or rcm == jp3 or dg1 == jp1 or dg1 == jp2 or dg1 == jp3:
                                print("NOW WAY! YOU WON THE JACKPOT!!!")
                                bet = bet * 10
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == w1 or mid == w2 or mid == w3 or top == w1 or top == w2 or top == w3 or botm == w1 or botm == w2 or botm == w3 or lcm == w1 or lcm == w2 or lcm == w3 or mcm == w1 or mcm == w2 or mcm == w3 or rcm == w1 or rcm == w2 or rcm == w3 or dg1 == w1 or dg1 == w2 or dg1 == w3:
                                print("You're a WINNER! Congrats BIG SHOT!")
                                bet = bet * 2
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == comp1 or mid == comp2 or mid == comp3 or top == comp1 or top == comp2 or top == comp3 or botm == comp1 or botm == comp2 or botm == comp3 or lcm == comp1 or lcm == comp2 or lcm == comp3 or mcm == comp1 or mcm == comp2 or mcm == comp3 or rcm == comp1 or rcm == comp2 or rcm == comp3 or dg1 == comp1 or dg1 == comp2 or dg1 == comp3:
                                print("Well... You kinda won...")
                                bet = bet - 1750
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            else:
                                print("Oh dang, maybe you should gamble more, you might win~")
                                if mid == L1 or mid == L2 or mid == L3 or top == L1 or top == L2 or top == L3 or botm == L1 or botm == L2 or botm == L3 or lcm == L1 or lcm == L2 or lcm == L3 or mcm == L1 or mcm == L2 or mcm == L3 or rcm == L1 or rcm == L2 or rcm == L3 or dg1 == L1 or dg1 == L2 or dg1 == L3:
                                    print("Wait... did you get... THAT COMBO?\nLOSER!LOSER!LOSER!LOSER!LOSER!")
                                bet = 0
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                        if times == 8:
                            print("The machine reads EVERY POSSIBILITY!\n-----------------------")
                            if mid == jp1 or mid == jp2 or mid == jp3 or top == jp1 or top == jp2 or top == jp3 or botm == jp1 or botm == jp2 or botm == jp3 or lcm == jp1 or lcm == jp2 or lcm == jp3 or mcm == jp1 or mcm == jp2 or mcm == jp3 or rcm == jp1 or rcm == jp2 or rcm == jp3 or dg1 == jp1 or dg1 == jp2 or dg1 == jp3 or dg2 == jp1 or dg2 == jp2 or dg2 == jp3:
                                print("NOW WAY! YOU WON THE JACKPOT!!!")
                                bet = bet * 10
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == w1 or mid == w2 or mid == w3 or top == w1 or top == w2 or top == w3 or botm == w1 or botm == w2 or botm == w3 or lcm == w1 or lcm == w2 or lcm == w3 or mcm == w1 or mcm == w2 or mcm == w3 or rcm == w1 or rcm == w2 or rcm == w3 or dg1 == w1 or dg1 == w2 or dg1 == w3 or dg2 == w1 or dg2 == w2 or dg2 == w3:
                                print("You're a WINNER! Congrats BIG SHOT!")
                                bet = bet * 2
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            elif mid == comp1 or mid == comp2 or mid == comp3 or top == comp1 or top == comp2 or top == comp3 or botm == comp1 or botm == comp2 or botm == comp3 or lcm == comp1 or lcm == comp2 or lcm == comp3 or mcm == comp1 or mcm == comp2 or mcm == comp3 or rcm == comp1 or rcm == comp2 or rcm == comp3 or dg1 == comp1 or dg1 == comp2 or dg1 == comp3 or dg2 == comp1 or dg2 == comp2 or dg2 == comp3:
                                print("Well... You kinda won...")
                                bet = bet - 4000
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                            else:
                                print("Oh dang, maybe you should gamble more, you might win~")
                                if mid == L1 or mid == L2 or mid == L3 or top == L1 or top == L2 or top == L3 or botm == L1 or botm == L2 or botm == L3 or lcm == L1 or lcm == L2 or lcm == L3 or mcm == L1 or mcm == L2 or mcm == L3 or rcm == L1 or rcm == L2 or rcm == L3 or dg1 == L1 or dg1 == L2 or dg1 == L3 or dg2 == L1 or dg2 == L2 or dg2 == L3:
                                    print("Wait... did you get... THAT COMBO?\nLOSER!LOSER!LOSER!LOSER!LOSER!")
                                bet = 0
                                balance = balance + bet
                                print(f"Your total is now: ${balance}")
                        check = True

                if balance <= 0:
                    print("\nHey... you don't have any more money for these, STOP LOITERING!")
                    print("\n[The Host of the SLOTZ ZONE realized you're out of cash! He kicks you out of the CLAMS CASINO and you leave empty handed]\n-----------------------")
                    main(balance, key, green)
             
                while hiddenmark == True and hiddenmark2 == True and balance > 0 and check == True:
                    advance = input("\nWould you like to continue? (YES/Y or NO/N | GUIDE for COMBOS) ")
                    if advance.lower() == "yes" or advance.lower() == "y":
                        print("[Your hands get ready as the slot machine perks itself...] \n")
                        hiddenmark2 = False
                    elif advance.lower() == "guide" or advance.lower() == "help" or advance.lower() == "combo" or advance.lower() == "combos":
                        print("COMBO GUIDE:\n----------------------")
                        print("{}[===JACKPOT===]{}\n[7,7,7] | [9,8,5] | [9,9,9]\n")
                        print(":===WIN===:\n[3,3,3] | [9,6,9] | [6,9,6]\n")
                        print("<~~~COMPENSATION~~~>\n[2,2,2] | [5,5,5] | [3,2,1]\n")
                        print("[<>>LOSE<<>]\n[6,6,6] | [4,4,4] | [0,0,0] | [ANY OTHER COMBINATION]\n----------------------")
                    elif advance.lower() == "no" or advance.lower() == "n":
                        print("[You leave the HIGH-LEVEL-SLOTZ as FAST as you can! You feel less... anxious now that you left that area of the SLOTZ...]\n")
                        hiddenmark2 = False
                        stay = False
                        condition = True
                    else:
                        print("[Sorry, what did you mean by that?...]")
            if balance < 500:
                print("Oh dear, it seems you don't have enough money to play these HIGH-LEVEL-SLOTZ anymore...")
                print("[The Host of the SLOTS guides you back to the SLOTZ-HUB]")
        else:
            print("Seriously... come on...")
    if balance < 25:
        print(f"\nSorry pal, our minimum bet here is $25.\nI only see that you have ${balance}...")
        if balance <=5:
            print(f"Wait... how did you manage to only have ${balance}, why did you come here? Whatever...")
        print("\nI will just keep kicking you out of here until you have enough money to play, please leave the SLOTZ ZONE...\n[You can see the Host of the SLOTZ almost crying, it seemed that he really wants you to play these machines...]\n----------------------")



 #Rob's Part#
def roulette(balance, key, green):
     #For betting-loop#
    hiddenmark = True
     #Greets USER and asks if they need instructions on how to play#
    response = input('WELCOME TO THE ROULETTE FLOURETTE! \n\nWould you like me to explain the rules? (Input YES/Y for rules | Press ENTER or OTHER to Skip) ')
    if response.lower() == "yes" or response.lower() == "y":
         #Multiple print lines in order to simplify text#
         #Summary on how to play#
        print("\nOk, here are the rules: \n-----------------------")
        print("The dealer will spin a roulette wheel, and it will land on a number between 1 and 36, with each value having their respected color [RED OR BLACK].")
        print("You can bet either on COLOR, or on a SPECIFIC NUMBER. In order to WIN, the 'ball' must land on the color/number of your choosing.")
        print("Although simplier than actual roulette, there are still stakes at hand!")
         #Waits until USER fully understands how to play#
        more = input("\nThose are the rules, feel free to read over them before you continue. \n[Press ENTER or OTHER to continue]\n")
     #EASTER EGG#
    elif response.lower() == "other" or response.lower() =="enter":
        print("\nWoah, you can't be doing stuff like that... On the other hand... You should go to the bathroom for some answers...")
        print("[The ROULETTE MASTER returns to his usual routine...]\n")
        
    print("Very well then...")                
     #Roulette time#
    while balance > 0 and hiddenmark == True:
         #Asks user how much to bet#
        bet = int(input("How much are you willing to bet? "))
         #Comes useful later for checks&loops#
        hiddenmark2 = True
        
         #Checks if the player actually input a reasonable amount within their budget#
        if bet > balance:
            print("\nYou can't bet that high, you're not that rich buddy.")
            pass
        if bet <= balance:
            print("\nVery well, what a nice amount to bet! Let me spin the ROULETTE then!\n[The ROULETTE MASTER spins the wheel]\n-----------------------")
            balance = balance - bet
            choosing = True
            
             #Asks USER what to bet on#
            while choosing == True:
                which = input("\nDo you want to bet on COLOR[C] or NUMBER[N]? ")
                 #Generates WINNING Number#
                winning_number = random.randint(1, 36)
                 #Generate COLORS for corresponding number
                red = [1,3,5,7,9,12,14,16,19,21,23,27,30,32,34,35,36]
                black = [2,4,6,8,10,11,13,15,17,20,22,24,25,26,28,29,31,33]
                 #Generates number fom COLOR list
                blacknum = random.randint(0,18)
                rednum = random.randint(0,16)                
                choosing2 = True

                #Asks USER to guess NUMBER#
                if which.lower() == "number" or which.lower() == "n":            
                    while choosing2 == True:
                        guessnum = int(input("Now then... \nGuess a number between 1 and 36. "))
                         #Sees if USER guessed correctly#
                        if guessnum <= 36 and guessnum >= 1:
                            if guessnum == winning_number:
                                print("You WIN!!!")
                                print(f"Congratulations, you guessed correctly!.")                                    
                                bet = bet * 5
                                balance = balance+bet
                                print(f"You now have: ${balance}") 
                            else:
                                print(f"Dang, sorry buddy, better luck next time... \n[WINNING NUMBER: {winning_number}]")
                                print(f"You now have: ${balance}") 
                            choosing2 = False
                         #Checks if guessed number is valid#   
                        else:
                            if guessnum >= 37:
                                print("Comeone man, the Roulette wheel isn't that big!\n")
                            elif guessnum <= 0:
                                print("Uhmm... can you see?")
                        
                #Asks USER to guess COLOR#        
                elif which.lower() == "color" or which.lower() == "c":
                    while choosing2 == True:
                        guesscolor = input("Two options... Bet on RED[R] or BLACK[B]? ")
                         #IF GUESS RED#
                        if guesscolor.lower() == "red" or guesscolor.lower() == "r":
                            x = 0
                            y = 0
                             #Scans through list#
                            for x in red:
                                 #Rewards USER if theres a match#
                                if winning_number == x:
                                    print(f"You betted on the right color!\n[WINNING NUMBER: {x} COLOR: RED]")
                                    y = x
                                    bet = bet * 2
                                    balance = balance+bet
                                    print(f"You now have: ${balance}")                                    
                             #Shows WINNING NUMBER and its COLOR#
                            if winning_number != y:
                                print(f"Well, at least you betted safely...\n[WINNING NUMBER: {winning_number} COLOR: BLACK]")
                                print(f"You now have: ${balance}") 
                            choosing2 = False
                         #IF GUESS BLACK#
                        elif guesscolor.lower() == "black" or guesscolor.lower() == "b":
                            x = 0
                            y = 0
                             #Scans through list#
                            for x in black:
                                 #Rewards USER if theres a match#
                                if winning_number == x:
                                    print(f"You betted on the right color!\n[WINNING NUMBER: {x} COLOR: BLACK]")
                                    y = x
                                    bet = bet * 2
                                    balance = balance+bet
                                    print(f"Balance: {balance}")
                             #Shows WINNING NUMBER and its COLOR#
                            if winning_number != y:
                                print(f"Well, at least you betted safely...\n[WINNING NUMBER: {winning_number} COLOR: RED]")
                                print(f"You now have: ${balance}") 
                            choosing2 = False
                         #Did you guess a color?#   
                        else:
                            print("It's not that hard... just guess a color...\n")
                            
                 #Checks for real response#
                else:
                    print("Do you want to play or not...\n")
                choosing = False           

         #Checks if user ran out of cash#
        if balance <= 0:
            print("\nNo more money, GET OUT!")
            print("\n[Dealer kicks you out of the table and you leave empty handed]\n-----------------------")
            main(balance, key)
         #Traps input error from USER#
        while hiddenmark == True and hiddenmark2 == True and balance > 0:
             #Asks user if they want to continue#
            advance = input("\nWould you like to continue? (enter yes/y or no/n) ")
             #Restarts all the way back to "How much will you bet" Question#
            if advance.lower() == "yes" or advance.lower() == "y":
                print("\nAlright then, let's reset the wheel... \n")
                hiddenmark2 = False
             #Will drop USER out of game#    
            elif advance.lower() == "no" or advance.lower() == "n":
                print("\nWell played, come back anytime. \nGood luck on your Gambling Adventure!\n-----------------------")
                hiddenmark = False
                main(balance, key, green)
             #Checks if USER inputs a proper response#
            else:
                print("Did you have a stroke")



 #Noah's Part#
def dice(balance, key, green):
    # starting balance and initial bet amount
    bet = 100
    payout_multiplier = 1  # this multiplier doubles after each win
    second_value = 4 #second number in the range that increases after each win

    print("Welcome to the DICE DICE! Where you risk you life on DICE!")
    print(f"Starting balance: ${balance}")
    print(f"Each dice roll costs ${bet}")

    while balance >= bet:
        # deduct the bet from balance at the start of each round
        balance -= bet
        print(f"\nYou bet ${bet}. Current balance: ${balance}")

        # game: guessing a number between 1 and 10
        guess = int(input(f"Guess a number between 1 and {second_value}: "))
        winning_number = random.randint(1, second_value)

        # determine if the player won or lost
        if guess == winning_number:
            winnings = bet * payout_multiplier * 2
            second_value += 3 #increase second number number by 3
            balance += winnings
            print(f"Congratulations! You guessed correctly and won ${winnings}.")
            print(f"New balance: ${balance}")
            payout_multiplier *= 2  # double the multiplier after a win
        else:
            print(f"Sorry, the winning number was {winning_number}.")
            print(f"New balance: ${balance}")
            second_value = 4
            payout_multiplier = 1  # reset the multiplier after a loss

        # check if the player wants to continue or quit
        choice = input("Do you want to roll again? (y to continue, anything else to quit): ").strip().lower()
        if choice != "y":
            print(f"You are leaving with ${balance}. Thanks for playing!\n-----------------------")
            main(balance, key, green)
    if balance < bet:
        print("You do not have enough balance to continue...\n-----------------------")
        main(balance, key, green)


    
def bathroom(balance, key, green):
    print("[You enter the bathroom. | It surely is a bathroom...]")
    if key == True:
         #Pointless LORE Drop | Multiple Lines to Simplify#
        print("[You unlock the bathroom door | You see a man in a coat facing the wall]\n")
        print('It seems you defied the confines of our reality and challanged this "program"...')
        print("[He turns around, his skin color green, kind of like a dehydrated lime]\n")
        print("Excuse my... skin care routine, but you're the chosen one.", 'Whether it be from another SAVE-STATE, TIMELINE, WHATEVER; you have to beat the "Green Goblin"')
        print("Look, this world isn't what it seems, have you noticed that the ROULETTE TABLE doesn't even have the GREEN ZEROS?", "Aparrently this world doesn't", 'have "GREEN" anywhere, not even the plants have green!')
        print("I know this might be too early before you get $1,000,000, but he has a weakness. You need to bet more than what he has, I know that sounds impossible but he isn't as rich as he seems!")
        print("Once you beat him, this whole universe will be put at ease and finally rest, no more cycle, no more gambling...\nPlease, win for the greater good...\n[As you know it, he turns to a green pile of dust... what a dumb reference to a popular movie...]")
        print("[But he's right, you need to win in order to stop this cycle, we can't let the GREEN get any GREENER, both in size and money!]\n-----------------------")
        green = True
    else:
        print("[You try opening the door, but it apears to be locked... maybe there's a key somewhere...]\n-----------------------")
    main(balance, key, green)

 #For FUTURE UPDATE#
def bossfight(balance, key, green):
    print(f"[You did it, you made over $1,000,000! now it's time to walk out and ca-]\n[Suddenly, you hear large thuds coming across the casino, with a huge green figure in the distance?]")
    print("Well, well, well... you did it, and now trying to cash out on big Ol' MR. GREENZ...\nWell, there's one thing you should know...\nMR. GREEN ALWAYS WINS!!!")
    print("[TO BE CONTINUED IN update 1.7 OR 1.8 IDK - THE BIG GREENZ HIMSELF]")
    continued()
          
def lost(balance):
    print("[As you get kick out of the CLAMS CASINO, you feel defeated in your small moment of triumph, however, hubris got to you...]")

    print("YOU HAVE LOST!")
    continued()
    
 #THIS IS A SUBSTITUTE FUNCTION#    
def continued():
    finish = input("Continue? ")
    if finish.lower() == "continue" or finish.lower() == "yes" or finish.lower() == "y":
        print("[STARTING NEWGAME+]\n")
        money()
    else:
        print("[Too bad, you need to win...]\n\n[A strange man gives you $2500 and shoves you back into the CLAMS CASINO]\n-----------------------")

 #Loops if WINNER = FALSE | LORE RELATED#        
if winner == False:    
    money()
