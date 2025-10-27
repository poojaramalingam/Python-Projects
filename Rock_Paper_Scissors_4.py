import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user = int(input("What do you want to choose? 0 for Rock, 1 for Paper, 2 for Scissors"))

if user == 0:
    print(rock)
elif user == 1:
    print(paper)
elif user == 2:
    print(scissors)

comp=random.randint(0,3)

print (f"Computer chooses {comp}")

if comp == 0:
    print(rock)
elif comp == 1:
    print(paper)
elif comp == 2:
    print(scissors)

if comp==user:
    print("Draw")
elif user==0 and comp==1:
    print("computer wins")
elif user==0 and comp==2:
    print("user wins")
elif user==1 and comp==0:
    print("user wins")
elif user==1 and comp==2:
    print("computer wins")
elif user==2 and comp==0:
    print("computer wins")
elif user==2 and comp==1:
    print("user wins")
else:
    print("wrong input")