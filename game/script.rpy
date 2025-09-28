# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define p = Character("You")
define h = Character("Home", color="#582929")
define l = Character("Lawyer")
define f = Character("Friend")
# The game starts here.
default memory_count = 0
default relation_count = 0
default moral_count = 0
image lawyer = "Marika.png"
image friend = "Que.png"
label start:
    play music horror
    scene bg creepy
    with fade

    "The rain hasn't stopped since you arrived at the estate."
    "Your family's mansion is now yours."

    show lawyer at left
    l "Everything in these walls belongs to you now..."
    l "But beware, the house has demands."
    play sound door
    hide lawyer

    show friend at right
    f "Don't worry, I'm sure he was exaggerating."

    hide friend
    scene bg room

    h "A price must be paid. What are you willing to give up?"

    "The First Sacrifice:"
    play music horror
    menu:
            "Forget a memory (a memory fades)":
                $ memory_count += 1
                jump act1
            "Betray your friend (leave them behind)" :
                $ relation_count += 1
                jump act1
            "Commit cruelty (kill your friend)":
                $ moral_count += 1
                jump act1
label act1:
    play music goth
    scene bg hall
    play sound groan
    "The mansion groans as it accepts your offering."
    "It seems as if the scent of death has increased."

    h "Another price must be paid soon..."

    "The Second Sacrifice:"
    menu:
            "Lose another memory":
                $ memory_count += 1
                jump act2
            "Choose to save your parents or your friend":
                $ relation_count += 1
                jump act2
            "Choose to kill either a friend or a parent":
                $ moral_count += 1
                jump act2

    return
