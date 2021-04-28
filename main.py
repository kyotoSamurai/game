print("Welcome To My World!")
name = input("What is your name, stranger? ")
age = int(input("What is your age? "))
health = 10

if age >= 18:
    print("Let's play")

    left_or_right = input("You are walking down the old road and see a sign. What path will you choose (left/right)? ")
    if left_or_right == "left":
        answer = input("You are entering a dark forest. After a while abandoned house appears on your way. Will you come inside or pass by (enter/pass)? ")

        if answer == "enter":
            answer = input("You push the door slightly and enter the house. You smell the soup bowling on the stove. Would you eat it (yes/no)? ").lower()

            if answer == "yes":
                answer = input("You don't feel well, so you lay down on bed. You are woken up by an angry man shouting 'Leave my house now!' What will you do (leave/explain)? ")
                health -= 5

                if answer == "leave":
                    answer = input("You run away immediately. It's getting cold in the woods. Will you light the fire or keep looking for a way out (light/continue)? ")

                    if answer == "light":
                        print("You make a fireplace and feel safe now. In the morning an old shepard wakes you up. You are saved!")
                    else:
                        health -= 5
                        if health <= 5:
                            print("You can't find the way out. You barely walk and fall on the ground. You froze to death...")
                else:
                    print("A hunter raises his gun and shoots you.")
                    health -= 5

                    if health <= 0:
                        print("You lose all your health. You lost...")
            else:
                answer = input("You browsing the house and suddenly hear a loud shot. You leave the place and run into the forest. You see a hunter grabbing a rabbit by its ears. Will you call for help (yes/no)? ")  

                if answer == "yes":
                    print("A hunter greets and invites you to his cabin. You are saved.")
                else:
                    answer = input("You don't want to mess with a tall bearded hunter and go away. It's getting dark and cold. Would you make a fireplace or follow the path (light/follow)? ")

                    if answer == "light":

                        health -= 10

                        if health <= 10:
                            print("You reach your pocket but can't find a lighter. You may have lost it. You lay on freezing ground. You lost...")
                    else:
                        answer = input("You feel exhausted but you keep walking. You hear wolves howling. You are scared. Will you go back to the hunter's cabin or hide in the bushes (return/hide)? ")

                        if answer == "return":
                            print("You see a dim light in the window. You come closer and shout 'Is anybody here?'")
                            print("A hunter comes out and sees your tired face. 'Ow, you might have lost. Please, come in. Be my guest'.")
                            print("You are saved")
                        else:
                            print("You feel safe now and try to get some sleep. You close your eyes...")

                            health -= 10

                            if health <= 0:
                                print("You were eaten by wolves")
        else:
            answer = input("You walk around the house and see a dog. Will you pet or scare her off (pet/scare)? ")
    
            if answer == "pet":
                health -= 5
                answer = input("She bites you. Are you going to run away or find bandages in the cabin (run/find)? ")

                if answer == "run":
                    answer = input("You run as fast as you can and see a pond. The water is not clean enough, will you wash your wound(yes/no)? ")

                    if answer == "yes":
                        health -= 5

                        if health <= 0:
                            print("The water in the pond was contaminated. You lost...")
                    else:
                        health -= 5
                        if health <= 0:
                            print("You feel weak as you lose too much blood. You fall on the ground. You lost...")
                else: 
                    print("You enter the house and look for bandages. At this moment a hunter walks in and sees blood on your hand. He grabs his kit and heals your wounds. You are saved.")
                    health += 5     
            else:
                print("You threw a stick at her ,and she dissapears in the woods. An owner of the house comes back from the hunt and helps you out. You are saved.")
    else:
        answer = input("You are wandering around and see a scared deer. What will you do (follow/leave)? ")  

        if answer == "follow":
            print("You chase the deer and reach a mountain river. You come closer to take a sip but slip over on a wet stone and fall into the cold stream. Someone grabs your hand and pulls you to the ground.")   
            answer = input("Will you thank your saviour (yes/no)? ")

            health -= 5 

            if answer == "yes":
                answer = input("A shepard invites you to his place to dry the clothes. He looks sad as he has lost his only sheep. What are you going to do (help/ignore)? ") 

                health += 5    

                if answer == "help":
                    print("'Say no more. I will find your sheep.' You leave the cabin and disappear in the darkness.")
                    
                    health -= 10

                    if health <= 0:
                        print("Unfortunately you go down the pit and hit your head. You lost...")

                else: 
                    print("You thank a shepard for his hospitality and go away. You walk into the darkness. After a moment you hear an animal running towards you. It hits you and runs away.")

                    health -= 10

                    if health <= 0:
                        print("You are seriously injured. You lost...")

            else:
                print("You ignore a shepard and continue your trip. You see the smoke afar and follow it until you reach a small village. You are saved.")

        else:
            print("You hear bee's buzzing and walk towards the noise.")

            health -= 10

            if health <= 0:
                print("A furious grizzly comes towards you. You lost...")

else:
    print("Go Away!!!")
