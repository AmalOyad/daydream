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
            "You must pay a toll to pass. (something precious to you)":
                $ memory_count += 1
                jump act1
            "You're cornered with your friend. Only one can escape." :
                $ relation_count += 1
                jump act1
            "Commit murder and kill yourself before it's too late.":
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
            "Lose a memory of a loved one (you'll never remember them and they won't remember you)":
                $ memory_count += 1
                jump act2
            "Sacrifice yourself instead (choose to save your friend over yourself)":
                $ relation_count += 1
                jump act2
            "Choose to kill either a friend or a parent":
                $ moral_count += 1
                jump act2
label act2:
    scene bg room
    "Night falls. The spirit of the mansion confronts you."

    h "The truth is clear now. Your family bound me with their bloodline."
    h "Now, you must choose your final path."

    "The Final Sacrifice: "
    menu:
        "Break the curse (greatest sacrifice)":
            jump ending_break
        "Accept the curse (become heir)":
            jump ending_accept
        "Refuse everything (death)":
            jump ending_refuse


label ending_break:
    if memory_count >= 2:
        "You shatter the curse, but with no memories left, you are made out to be mad and put in a mental hospital."
    elif relation_count >= 2:
        "You break the curse, but doomed to be eternally alone."
    elif moral_count >= 2:
        "You destroy the curse, drenched in blood of loved ones. The mansion falls, and so does your soul."
    else:
        "By balancing your choices, you get to walk free, but not before the spirit has drained you of part of your soul."
    jump the_end

label ending_accept:
    "You accept the mansion's will. Its power flows into you."
    "You are no longer the heir, you are the master."
    "You will remain immortal forever, till someone else comes to take your place, with everyone you ever knew forgetting you."
    jump the_end

label ending_refuse:
    "You reject the mansion's choices. The walls close in."
    "Your body is never found."
    jump the_end

label the_end:
    scene black with fade
    centered "THE END"
    return
