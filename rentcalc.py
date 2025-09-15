rent= int(input("Enter the room of the rent:"))
food=int(input("Enter the food you've ordered:"))
electricity= int(input("Enter the total electricty spend:"))
electricty_charge=int(input("Enter the rate of electricty per units:"))
people=int(input("How many people leaving in the room:"))

totat_electricity= electricity*electricty_charge

output= (rent+food+totat_electricity)// people
print(output)
