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