import time
from password import gen
from message import decode
from lockpicking import Lockpick
from spy import Spy

# print("You are on a secret spy mission trying to break into a rich person's house after hearing there is 1 million dollars hidden somewhere.")
# time.sleep(2)
# print("As you approach the house, you go behind to try and enter their backdoor but you realize there is a lock in the way.")
# time.sleep(2)
# print("As you realize this, you take out your lockpick and try your best to enter the house.")
# time.sleep(2)
# lp = Lockpick(length=5, amount=5)
# lp.picking(4)

# time.sleep(2)
# print("As you enter the house, you have to get past the living room without making any noise.")
# time.sleep(2)
# us = Spy(6)
# us.sneak()
# time.sleep(2)
# print("You passed through the living room and were presented with three options.\nWhere would you like to go first?")
# time.sleep(2)

def main():
    while True:
        # print("\nMenu:")
        print("1. Bedroom")
        print("2. Library")
        print("3. Kitchen")
        choice = input("Enter your choice (1-3): ")
        if choice == '1':
            print("You found a chest! Though it has a lock that requires 4 letters.")
            tries = 0
            while True:
                answer = input("What is the password? ")
                if answer == "Echo":
                    print("You opened the chest!\nThough it seems the chest also requires a lock that requires a 5 character password.")
                    for i in range(1,5):
                        answer1 = input("What is it?")    
                        if answer1 == gen():
                            print("You opened the chest!")
                            time.sleep(2)
                            print("Congrats! You left with 1 million dollars")
                            exit()
                        else:
                            tries += 1
                            if tries < 5:
                                print("That doesn't seem right... Try again!")
                            elif tries == 5:
                                print("You used up all your tries and a alarm system broke out. You left with nothing.")
                                exit()
                else:
                    print("That doesn't seem right... You can try again or exit!")
                    if answer.lower() == "exit":
                        break
        elif choice == '2':
            print("As you enter the library you see a book on the table containing a riddle, but it is encrypted.")
            with open("riddle.txt", "r") as file:
                riddle = file.read()
                time.sleep(2)
                print(riddle)
                file.close()
                pass
            time.sleep(2)
            print(f"As you look at this, you realize, you have a tool that can decode this!\nUsing your decoding tool you can finally read the riddle:")
            with open("riddle.txt", "r") as file:
                riddle = file.read()
                time.sleep(2)
                print(decode(riddle))
                file.close()
                pass
            while True:
                time.sleep(2)
                answer = input("What is the answer to this? ")
                if answer.title() == "Echo":
                    print("Correct!")
                    break
                else:
                    time.sleep(1)
                    print("That doesn't seem right... Try again!")
        elif choice == '3':
            time.sleep(1)
            print("You found a note!")
            while True:
                time.sleep(2)
                question = input("What has many keys but can't open a single lock?")
                if question.lower() == "piano":
                    print(f"Fantastic! You found a note containing a password: {gen()}")
                    break
                else:
                    time.sleep(1)
                    print("Incorrect answer. Try again!")
        elif choice == "Stop":
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 3.")
        

# ---------------------------------------------------------------------------------------------

if __name__ == "__main__":
    main()


