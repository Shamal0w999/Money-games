import time
import random
import pygame
import sys




pygame.mixer.init()

gunshot_sound = pygame.mixer.Sound("gunshot.mp3")
drag_sound = pygame.mixer.Sound("dragging.mp3")
hit_sound = pygame.mixer.Sound("hit.mp3")
typing_sound = pygame.mixer.Sound("typing.mp3")

from datetime import datetime
JOURS, MOIS = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"], ["janvier", "février", "mars", "avril", "mai", "juin", "juillet", "août", "septembre", "octobre", "novembre", "décembre"]
now = datetime.now()


def ecrire_lent(texte, vitesse=0.2):
    for lettre in texte:
        sys.stdout.write(lettre)
        sys.stdout.flush()
        if lettre in [".", "!", "?", ":"]:
            time.sleep(0.5)
        elif lettre in [",", ";"]:
            time.sleep(0.25)
        else:
            time.sleep(vitesse)
            
    print()

def ecrire(texte, vitesse=0.07):
    for lettre in texte:
        sys.stdout.write(lettre)
        sys.stdout.flush()
        if lettre in [".", "!", "?", ":"]:
            time.sleep(0.5)
        elif lettre in [",", ";"]:
            time.sleep(0.25)
        else:
            time.sleep(vitesse)
            
    print()

print()
print()
ecrire((f"--- {datetime.now().strftime('%A %-d %B %H:%M')} — Blackwood Hangar, Sector 4, Detroit ---"))
time.sleep(1)
ecrire("Coordinates: ██°██'██.█\"N ██°██'██.█\"W [CLASSIFIED]")
time.sleep(1)
ecrire("Starting the found recording...")
time.sleep(1)
print()
print()
ecrire("-----------------")
print()
print()
time.sleep(1)
ecrire("Do you want to skip introduction ? (y/n)")
skip = input("(all other answer will count as yes) : ")

if skip in ["no", "n", "na", "nah", "NO"] :
    time.sleep(1)
    print()
    print()
    ecrire("\033[3m'Mhm..... 'Money Games'... What is that ?\033[0m'")
    time.sleep(1)
    print()
    ecrire("You are curently surfing on the dark web, like always, but you found that ad : Money games. As curosity grind up, you decide to look it up...")
    time.sleep(1)
    print()
    ecrire("\033[3mHey ! Do you want to get money just by playing some games ??? Money Games is here ! By succesfully completing our games, you can earn a lot of money, that is so simple !\033[0m")
    time.sleep(1)
    print()
    ecrire("\033[3mWant to participate ?? Just go to that location :\033[0m ██°██'██.█\" ██°██'██.█\" [CLASSIFIED BY THE ADMINISTRATION]")
    time.sleep(1)
    print()
    ecrire("'\033[3mI mean.... Im kind of broke right now man... But a game from the dark web, im not sure about that... You know what ? fuck it, ima take a look...\033[0m'")
    time.sleep(1)
    print()
    ecrire("You take your car and a camera (for security you said) and drove straight to that place.")
    ecrire("you arrived at the hangar facility and look for the number 4, thats where it take place.")
    time.sleep(1)
    print()
    ecrire("Camera hidden, you take a deep breath and enter the hangar. People are here, armed one too... clearly not the army. You found a poorly made reception.")
    time.sleep(1)
    print()
    ecrire("'\033[3mHey mate,\033[0m' you ask him.'\033[3mIs the Money games here ? Am i at the good place ?\033[0m'")
    time.sleep(1)
    print()
    ecrire("The guy don't say anything, he just point to a door behind him...")
    time.sleep(1)
    print()
    ecrire("'\033[3mAlright\033[0m'You entered the door and it closed behind you.. Inside, its pich black. As you tried to look around, you feel someone behind you.")

print()
ecrire("skipping intro......")
time.sleep(2)
ecrire("---------------")
time.sleep(1)
hit_sound.play()
time.sleep(2)
print()
ecrire_lent("You feel something grab you by the feets.....")
drag_sound.play()
time.sleep(8)
print()
ecrire("'\033[3mWhere... Where am i...?")
time.sleep(3)
print()
ecrire("--------------")
print()
ecrire("Wait ! time to choose difficulty !")
ecrire("you can choose between :")
ecrire("- Discovery 'with 7 lifes'")
ecrire("- chill 'with 5 lifes'")
ecrire("- normal 'with 3 lifes'")
ecrire("- real life 'with 1 life'")
print()
ecrire("Some games will be luck based ! So i recommand normal to have a good gameplay, but its your choice after all.")
print()

player_lives = "not defined"
while player_lives == "not defined" :
    gamemode_choice = input("Your gamemode : ")
    if gamemode_choice in ["discovery", "Discovery"] :
        player_lives = 7
    elif gamemode_choice in ["chill", "Chill"] :
        player_lives = 5
    elif gamemode_choice in ["normal", "Normal"] :
        player_lives = 3
    elif gamemode_choice in ["real life", "Real life"] :
        player_lives = 1
    else :
        ecrire("That is not a valid choice !, choose again !")
        print()
