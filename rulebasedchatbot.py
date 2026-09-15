import random
destination={
    "beaches":["bali","Ushlanga","Maldives","Goa","Phuket"],
    "mountains":["everest","Table","Pokhara"],
    "cities":["New York","Botswana","Dubai"]

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

def packing():
    days=input("input the number of days")
    place=input("enter the place")
    print("enjoy the holidays at ",place,"for", days,"days")

def chat():
    while True:
        msg=input("enter from recommend, packing or joke")
        if "recommend" in msg:
            recommend()
        elif "packing" in msg:
            packing()
        elif "joke" in msg:
            print(random.choice(jokes))
        elif "exit" in msg:
            print("Goodbye!")
            break
        else:
            print("enter from recommend, packing or joke")

chat()
