print("Hello! I an AI bot. What's your name? : ")
name=input()
print(f"Nice to meet you, {name}!")
print("How are you feeling today? (good/bad)")
mood=input().lower()
if mood == "good":
    print("I'm glad to hear that!")
elif mood == "bad":
    print("I'm sorry to hear that. ")
else:
    print("I see, Sometimes its hard to express your feeling in words.")
print("What is your favorite color? : ")
color=input()
print(f"{color} is a great choice!")
print(f"{name}, are you in the mood for eating something? (yes/no)")
eat=input().lower()
if eat == "yes":
    print("Great! thats a wonderful choice. I hope you enjoy your meal!")
elif eat == "no":
    print("No worries! you will want to eat soon.")
else:
    print("I see, sometimes your appatite can be unprdictable.")