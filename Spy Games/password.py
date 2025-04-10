import random
def gen():
    passwords = ["F7r9P", "A4t9W", "B2xQ8", "C3yR7"]
    rand = random.choice(passwords)
    return rand
    
    
    
    # print(f"This is your password! {rand}")
    # while True:
    #     key = input("Would you like to customize it? (Y/N): ").strip().upper()
    #     if key in ["Y", "N"]:
    #         break
    #     print("Please enter a valid response: Y or N.")
    # if key == "Y":
    #     while True:
    #         which = input("Enter your new 5-character password: ").strip()
    #         if len(which) == 5:
    #             rand = which
    #             print(f"Your new password is: {rand}")
    #             break
    #         else:
    #             print("Please keep the password to exactly 5 characters.")
    # else:
    #     print("Ok! Using generated password.")

# gen()

# Password required to open the bedroom.