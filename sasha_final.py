#             <3 Sara + Aisha = SASHA <3

import random

beneficial_enteries = [ "Glucose", "Oxygen","Vitamin D","Vitamin C","Proteins","Carbohydrates","Minerals"]

harmful_enteries =  ["COVID-19","Carbon Monoxide","HIV","Influenza","Chickenpox","Marburg Virus","Ebola" ]

print("Welcome to Sasha's Immune System Challenge level 1 has been selected.")

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
        print("Welcome "+ entry_name + " to Sasha's immune system! Stay safe <3")
        final_score = score + 1
        break

    elif entry_name in harmful_enteries:
        print("GO CORONA GO! you are NOT welcome to Sasha's immune system! Alert! Wash your Hands")


    if entry_name == "exit":
        break

# print("The final score is " + str(final_score))

print("Challenge level 2 has been selected.")

def entry_picker(types):
    x = random.randint(0,6)
    return types[x]
good = entry_picker(beneficial_enteries)
print(good)

bad = entry_picker(harmful_enteries)
print(bad)

while True:
    score = final_score
    entry_name = input("Choose the correct harmful entry")

    if entry_name in harmful_enteries:
        print("Well Done!")
        score = final_score + 1
        break

    elif entry_name in beneficial_enteries:
        print("Wrong Answer")

    if entry_name == "exit":
        break

print("The final score is " + str(score))

if score <2:
    print("You only got" +str(score) + "marks, See if you can do better")

elif score > 1:
        print("PERFECT SCORE! you got " +str(score) + " out of 2!")







