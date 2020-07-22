
import random

useful_viruses = [ "1LVJ", "1NMA", "3J6Q"]

harmuful_viruses =  ["COVID-19","1D97","2LWB" ]

def virus_picker(types):
    x = random.randint(0,2)
    return types[x]
good = virus_picker(useful_viruses)
print(good)

bad = virus_picker(harmuful_viruses)
print(bad)


while True:
    virus_name = input("What are you?")

    if virus_name in useful_viruses:
        print("Welcome to Sasha's immune system!")
        break


    else:
        print("GO CORONA GO! you are NOT welcome to Sasha's immune system!")







