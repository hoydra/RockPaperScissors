import random



left_images = {
"rock":
"""
    _______       
---'   ____)      
      (_____)     
      (_____)     
      (____)      
---.__(___)       
    
""",
"paper":
"""

    ________      
---'    ____)____ 
           ______)
           ______)
         _______) 
---.__________)   

""",
"scissors":
"""
   ________      
---'    ____)____ 
           ______)
       __________)
      (____)      
---.__(___)       


"""
}

right_images = {

"rock":
    """
    
  _______   
(____   '---
(_____)      
(_____)      
 (____)     
  (___)__.---
    
    """,

"paper":
    """
      ________    
 ____(____    '---
(______           
(_______          
 (_______         
   (__________.---

""",

"scissors":
    """
        _______    
 _____(____   '---
(_______          
(__________       
     (____)      
     (___)__.---
    
    
    """




}



class RockPaperScissors:
    pos_1 = 0
    pos_2 = 1
    end = False
    score = 0
    arena = []



    def player(self):
        print("Rock Paper or Scissors")
        choice = input(": ").lower()
        RockPaperScissors.arena.append(choice)
        if choice in list(left_images.keys()):
            print("Its in")
            print("Player chooses...")
            try:
                print(left_images[choice])
            except KeyError:
                print("Rock Paper Scissors!")

    def bot(self):
        print("Bot chooses...")
        rand_choice = random.choice(list(left_images.keys()))
        RockPaperScissors.arena.append(rand_choice)
        print(right_images[rand_choice])
        return RockPaperScissors.arena

    def conditions(self):
        if RockPaperScissors.arena[0] == RockPaperScissors.arena[1]:
            print("Tie")

        if RockPaperScissors.arena[0] == "rock" and RockPaperScissors.arena[1] == "scissors":
            print("You won with rock against scissors!")

        if RockPaperScissors.arena[0] == "rock" and RockPaperScissors.arena[1] == "paper":
            print("You lost with rock against paper")




        if RockPaperScissors.arena[0] == "paper" and RockPaperScissors.arena[1] == "rock":
            print("You won with paper against rock")


        if RockPaperScissors.arena[0] == "paper" and RockPaperScissors.arena[1] == "scissors":
            print("You lost with paper against scissors")

        if RockPaperScissors.arena[0] == "scissors" and RockPaperScissors.arena[1] == "paper":
            print("You won with scissors against paper")


        if RockPaperScissors.arena[0] == "scissors" and RockPaperScissors.arena[1] == "rock":
            print("You lost with scissors against rock")

    def game(self):
        while RockPaperScissors.end == False:

            self.player()
            self.bot()
            RockPaperScissors.pos_1 += 1
            RockPaperScissors.pos_2 += 1
            self.conditions()



if __name__ == '__main__':
    game = RockPaperScissors()
    game.game()