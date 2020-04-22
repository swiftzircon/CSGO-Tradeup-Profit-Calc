def main():
    #Disclaimers#
    print("----------------------------------------")
    print("----CSGO Trade up Profit Calculator-----")
    print("------Author: Piotr Rajchel, 2020-------")
    print("--------------Ver.1.0-------------------\n")
    print("This program will tell you the percentage\nof profitability a trade"
          + "-up contract has\nbased on your inputs.\n")
    print("Information to keep in mind:\n")
    print("1. This program takes in limited inputs,\nplease don't include symbols"
          + " such as $\nor % when entering numbers. Both should\nbe in ##.##"
          + " format.\n")
    print("2. To find out how much each item costs\nand yields for being sold,"
          + " check the\nsteam market for the most current values.\nThis program"
          + " will account for the market\ntax, so just enter the number that's\n"
          + "listed per item.\n")
    print("3. To get the chances for profit or loss,\nuse a tradeup site such"
          + " as\nhttps://csgo.exchange/contract/tradeup.\n(Make sure to select"
          + " New Theory Method)\nRemember the steam prices"
          + " of each of these\nitems relative to their chance, because\nthe chance"
          + " will be asked after the list of\nprices is input.\n")

    #Program Loop#
    primary_loop = True
    while primary_loop == True:
        #Variable & Import Setup#
        import random
        cost = 0
        total_cost = 0
        profits = []
        profits_chances = []
        losses = []
        losses_chances = []
        totals = 0
        primary_loop_check = ""

        #Cost#
        print("-----------------Costs------------------")
        print("Enter the cost of each skin you will input. ")
        for i in range(10):
            cost += eval(input(str(i+1) + ".: "))
        print("Total cost for one contract would be $%.2f" % cost)
        print("----------------------------------------\n")

        #Profit and Loss Lists#
        print("------------Profits & Losses------------")
        print("How many outcomes (skins) are there?")
        outcomes = eval(input("# of Possible Outcomes: "))
        positive_outcomes = eval(input("How many are profitable?: " ))
        negative_outcomes = outcomes - positive_outcomes

        print("Enter the prices of the skins you profit from.")
        for i in range(positive_outcomes):
            profits.append(eval(input(str(i+1) +".: ")))
        print("Enter the prices of the skins you lose from.")
        for i in range(negative_outcomes):
            losses.append(eval(input(str(i+1) +".: "))) 
        print("----------------------------------------\n")

        #Chance Inputs#
        print("----------------Chances-----------------")
        print("Enter the chances for each of those results.")
        print("(They will be displayed in the order you entered them.)")

        for i in range(len(profits)):
            profits_chances.append(eval(input("Chance of getting the item with a value of $"+str(profits[i])+"?\n")))
        for i in range(len(losses)):
            losses_chances.append(eval(input("Chance of getting the item with a value of $"+str(losses[i])+"?\n")))
        print("----------------------------------------\n")

        #Applying Steam Market Tax to Profit and Loss List#
        for i in range(len(profits)):
            profits[i] *= .95
        for i in range(len(losses)):
            losses[i] *= .95

        #Conversion to Large Scale for Probability#
        #The formula takes each possibility and makes it a portion of 10,000, then it can run properly.
        for i in range(len(profits_chances)):
            if i == 0:  
                profits_chances[i] *= 100
            else:
                profits_chances[i] *= 100
                profits_chances[i] += profits_chances[i-1]

        for i in range(len(losses_chances)):
            if i == 0:  
                losses_chances[i] *= 100
                losses_chances[i] += profits_chances[len(profits_chances)-1]
            else:
                losses_chances[i] *= 100
                losses_chances[i] += losses_chances[i-1]

        #Contracts#
        print("---------------Contracts----------------")
        loop_count = eval(input("Enter a number of times to run the contract:"))
        print("...Running " + str(loop_count) + " Contracts...")
        for i in range(loop_count):
            total_cost += cost #Increase the cost for every contract run.
            outcome = random.randrange(1,losses_chances[-1]) #This is the result number.
            for x in range(len(profits_chances)):
                if x == 0:
                     if outcome > 0 and outcome <= profits_chances[x]:
                         totals += profits[x]   
                elif outcome > profits_chances[x-1] and outcome <= profits_chances[x]:
                     totals += profits[x]            
            for y in range(len(losses_chances)):
                if y == 0:
                     if outcome > profits_chances[-1] and outcome <= losses_chances[y]:
                         totals += losses[y]             
                elif outcome > losses_chances[y-1] and outcome <= losses_chances[y]:
                     totals += losses[y] 
        print("..." + str(loop_count) + " Contracts completed...")
        print("----------------------------------------\n")

        #Results for Profitability#
        print("-------------Profitability--------------")
        print("The total amount spent: $%.2f" % total_cost + ".")
        print("The total from the contracts was: $%.2f" % totals + ".\n")
        print("The Profitability percentage for this trade-up is: %.2f" %(((totals-total_cost)/total_cost)*100) +"%.")
        print("----------------------------------------\n")

        #Program Repeat?#
        while (primary_loop_check != "y" and primary_loop_check != "n"):   
            print("Would you like to run the program again? (y/n)")
            primary_loop_check = input("")
            if primary_loop_check == "y":
                primary_loop = True
            elif primary_loop_check == "n":
                primary_loop = False
                print("Thanks for visiting!")
    
main()#Run main
