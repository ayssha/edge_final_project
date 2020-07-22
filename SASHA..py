#                         <3 Sara + Aisha = SASHA <3

import random

beneficial_enteries = [ "Glucose", "Oxygen","Vitamin D","Vitamin C","Protiens","Carbohydrates","Minerals"]

harmful_enteries =  ["COVID-19","Carbon Monoxide","HIV","Influenza","Chickenpox","Marburg Virus","Ebola" ]

print("Welcome to Sasha's Immune System Challenge level 1 has being selected.")

def entry_picker(types):
    x = random.randint(0,6)
    return types[x]
good = entry_picker(beneficial_enteries)
print(good)

bad = entry_picker(harmful_enteries)
print(bad)


while True:
    score = 0
    entry_name = input("Choose the correct beneficial entry")

    if entry_name in beneficial_enteries:
        print("Welcome "+ entry_name + ",to Sasha's immune system! Stay safe <3")
        score = score + 1
        break

    elif entry_name in harmful_enteries:
        print("GO CORONA GO! you are NOT welcome to Sasha's immune system! Alert! Wash your Hands")


    if entry_name == "exit":
        break

print("The final score is: " + str(score))
