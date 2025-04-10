import random

class Spy:
    def __init__(self, sound): #speed
        self.sound = max(0, min(10, sound))
        # self.speed = max(0, min(10, speed))

    # def attempt_lockpick(self, lockpick):
    #     print(f"{self.name} is attempting to pick a lock...")
    #     return lockpick.picking(self.luck)

    def sneak(self):
        base_detection_chance = 0.6
        reduction = (10 - self.sound) / 10 * 0.5
        detection_chance = base_detection_chance - reduction
        print(f"Chance of being detected: {detection_chance * 100:.0f}%")
        # for i in range(1,4):
        if random.random() > detection_chance:
            print("Oops! You were heard.\nBetter luck next time!")
            exit()
        else:
            print("You progressed")
        print("And you made it through!")

# us = Spy(6)
# us.sneak()

    # def escape(self):
    #     escape_chance = 0.2 + (self.speed + self.luck) / 20 * 0.6
    #     print(f"{self.name} is trying to escape...")
    #     print(f"Chance of escape: {escape_chance * 100:.0f}%")
    #     if random.random() < escape_chance:
    #         print("You escaped successfully!")
    #         return True
    #     else:
    #         print("You were caught while escaping.")
    #         return False
