def exact_change(user_total):
    dollar = user_total//100
    user_total -= dollar*100

    quarter = user_total//25
    user_total -= quarter*25

    dime = user_total//10
    user_total -= dime*10

    nickel = user_total//5
    user_total -= nickel*5

    penny = user_total



    return dollar,quarter,dime,nickel,penny


definitions = [["dollar","dollars"],["quarter","quarters"],["dime","dimes"],["nickel","nickels"],["penny","pennies"]]

if __name__ == '__main__':
    change = int(input())
    if change>0:
        numdollars, numquarters, numdimes, numnickels, numpennies = exact_change(change)
        allchange = [numdollars, numquarters, numdimes, numnickels, numpennies]
        for index,thischange in enumerate(allchange):
            if(thischange > 0):
                if (thischange > 1):
                    print(thischange, definitions[index][1])
                else:
                    print(thischange, definitions[index][0])
    else:
        print("no change")
