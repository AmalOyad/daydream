# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define among = Character("Aisha")
define odd = Character("Ghost")

# The game starts here.

label start:
    scene bg creepy
    show aisha at right
    show ghost at left
    with fade
    odd "Welcome to a game of death!!! There is no cancellation option and no preparation can save you."
    among "Who Are You?"
    odd "Good Luck.. You'll need it."
    hide mean
    with dissolve
    # These display lines of dialogue.

    among "They just disappeared/ Where did they go?"

    # This ends the game.

    return
