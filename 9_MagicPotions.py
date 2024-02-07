import random
potions = { 
    "Invisibility potion": ["Moonstone", "Dragon scale", "Fairy dust"], 
    "Flying potion": ["Phoenix feather", "Troll tooth", "Mermaid scale"], 
    "Healing potion": ["Unicorn horn", "Elf hair", "Golden apple"] 
}

Delcine = ['Sorry, we dont carry that potion ingredients',
           'Is that even a real potion?, please leave.',
             'Goodness! That sounds like a dark potion, we dont carry those. Guards!!Help!!']

print("""Welcome to the magic potions shop
Here are the list of potions on offer""")
for potion in potions:
    print(potion)
    
selection = input("Which potion would you like to buy ingredients for? ").capitalize()

if selection not in potions:
    print(random.choice(Delcine))
else:
    print(f"""You have chosen {selection}.
The ingredients for {selection} are {potions[selection]}""")
    Required_Ingredients = potions[selection].copy()
    while Required_Ingredients:
        Buyer_Choice = input(f"Would you like to buy {Required_Ingredients[0]}? ").capitalize()
        if Buyer_Choice == 'Yes':
            print(f"Congratulation, you have purchased {Required_Ingredients[0]}")
            Required_Ingredients.pop(0)
        else:
            print("We dont tolerate trouble makers, please leave")
            break
    else:
        print(f"You have purchased all ingredients for {selection}")
        
