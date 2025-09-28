# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Aisha", color="purple")
define odd = Character("Ghost")

# The game starts here.

label start:
    scene bg creepy
    show aisha at right
    show boy at left
    with fade
    a "Hi, I'm Aisha!"
    odd "Who Are You?"
    "...well this is awkward."
    hide mean
    with dissolve
    # These display lines of dialogue.

    a "They just disappeared/ Where did they go?"

    # This ends the game.

    return
