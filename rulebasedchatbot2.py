import random
destination={
    "beaches":["bali","Ushlanga","Maldives","Goa","Phuket"],
    "mountains":["everest","Table","Pokhara"],
    "cities":["New York","Botswana","Dubai"]
}

food1={
    "seafood":["lobster","crab","prawn"],
    "fastfood":["burger","pizza","fries"],
    "desert":["cake","icecream","brownie"]
}
jokes=[
    "Why don't scientists trust atoms? Because they make up everything!","What do you call a fake noodle? An impasta!","Why did the scarecrow win an award? Because he was outstanding in his field!"]

def recommend():
    a=input("enter beaches mountains or cities")
    if (a in destination):
        place = random.choice(destination[a])
        print("try this:", place)
    else:
        print("Invalid choice.")

def food2():
    b=input("enter seafood fastfood or desert")
    if (b in food1):
            dish = random.choice(food1[b])
            print("try this:", dish)
    else:
            print("Invalid choice")

def packing():
    days=input("input the number of days")
    place=input("enter the place")
    print("enjoy the holidays at ",place,"for", days,"days")


def chat():
    while True:
        msg=input("enter from recommend, food,packing or joke")
        if "recommend" in msg:
            recommend()
        elif "packing" in msg:
            packing()
        elif "food2" in msg:
            food2()
        elif "joke" in msg:
            print(random.choice(jokes))
        elif "exit" in msg:
            print("Goodbye!")
            break
        else:
            print("enter from recommend, food, packing or joke")

chat()
