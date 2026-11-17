import re 

print("Welcome to the jungle")

while True:
    
    user_input = input("You: ").lower()

    if re.search(r"\b(hey+|hello|hii)\b", user_input):
        print("Hey there, how can i help you today.")


    elif re.search(r"\b(doctor|doctors)\b",user_input):
        print("Yes! There are multiple doctors available")

