import time
import random
import pygame
import sys
import os





pygame.mixer.init()

gunshot_sound = pygame.mixer.Sound("gunshot.mp3")
gun_reload = pygame.mixer.Sound("gun_reload.mp3")
bullet_Dead = pygame.mixer.Sound("blood_bullet.mp3")
blank_sound = pygame.mixer.Sound("gun_click.mp3")
drag_sound = pygame.mixer.Sound("dragging.mp3")
hit_sound = pygame.mixer.Sound("hit.mp3")
light_on = pygame.mixer.Sound("light_on.mp3")
blood_dripping = pygame.mixer.Sound("blood_dripping.mp3")
body_Fall = pygame.mixer.Sound("body_fall.mp3")
revive = pygame.mixer.Sound("revive.mp3")

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

def game_over():
    if player_lives <= 0 :
        print()
        print()
        ecrire((f"--- {datetime.now().strftime('%A %-d %B %H:%M')} — Blackwood Hangar, Sector 4, Detroit ---"))
        time.sleep(1)
        print()
        ecrire("one body found")
        time.sleep(1)
        print()
        ecrire(f"Cause of death : {cause_of_death}")
        time.sleep(1)
        ecrire(f"{suffer}")
        time.sleep(2)
        print()
        ecrire("More info : Victim played deadly games for money, sadly he will not have anything left.")
        time.sleep(1)
        print()
        ecrire("Sending patrol to stop the clandestin organisation.")
        time.sleep(1)
        print()
        ecrire("End of the found recording...")
        print()
        print()
        ecrire("-----------------")
def credits():
    ecrire("Thank you for playing the pre beta, game is wip!")
    ecrire("everything was made by me 'Shadrow' !")
    ecrire("Not the sound effect tho...")

ecrire("Disclaimer :")
ecrire("This game contains loud noises and disturbing contents")
ecrire("You have been warned")
time.sleep(5)
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
    ecrire("'\033[3mAlright.....\033[0m'You entered the door and it closed behind you.. Inside, its pich black. As you tried to look around, you feel someone behind you.")
    time.sleep(1)

else :
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
time.sleep(2)
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

print()
print()
ecrire(f"Difficulty choosen : \033[31m{gamemode_choice}\033[0m")
ecrire(f"Player lifes set to \033[31m{player_lives}\033[0m")
print()
ecrire("--------------")
print()
time.sleep(1)
ecrire("'\033[3mIt's...It's way too dark in here... where am i ...? WHERE AM I ?!\033[0m'")
time.sleep(2)
light_on.play()
time.sleep(4)
print()
ecrire("The room light up, you are tied up to a chair, but you can move your arms. Infront of you is a table, with a gun on it...")
time.sleep(1)
print()
ecrire("'\033[3mHey ! W-What the f#ck is that ? where am i !'\033[0m")
time.sleep(1)
print()
ecrire("A men walks up to you : '\033[3mWell... it's money games, you are here to play games remember ? For money.\033[0m'")
time.sleep(1)
print()
ecrire("'\033[3mI didn't know it was those type of games !\033[0m'")
time.sleep(1)
print()
ecrire("'\033[3mShut up \033[0m'say the man'\033[3m Enough talking, so you wanna hear the rules for the first game or nah ?\033[0m' ")
time.sleep(1)
print()
choice = input ("(y/n) : ")

if choice in ["yes", "yes", "y", "Y"] :
    ecrire("'\033[3mYeah, i guess...\033[0m'")
    time.sleep(2)
    print()
    ecrire("Here are the rules for the first game ! 'The solo russian gun' ! ")
    ecrire("The gun will be charged with 3 bullets ! 2 are real, the other is a blank")
    ecrire("You need too use the 3 bullets on yourself or infront of you (nothing)")
    ecrire("If you fire a blank bullet at yourself or a real infront of you, you are safe !")
    ecrire("if you fire a real bullet at yourself or a blank infront of you, you are dead !")
    time.sleep(2)
    ecrire("Alright are you ready ?")
    input("(y/n) : ")
    print()
    ecrire("Actually, we dont care lol")
elif choice in ["n", "N", "no", "NO"] :
    ecrire("'\033[3mYou already know the rules or what ? Meh, i dont give a sh#t.\033[0m'")
else :
    ecrire("'\033[3mi hope you die dumbass\033[0m'")


bullet_in_gun = ["real", "real2", "blank"]
random.shuffle(bullet_in_gun)
print()
time.sleep(2)
ecrire("You took the gun with shaking hand.....")
time.sleep(2)
print()
#first choice
bullet = bullet_in_gun.pop(0)
while True :
    choice = input("Where are you shooting ? (yourself/air) : ")
    if choice in ["yourself", "me", "myself"] :
        ecrire_lent("you put the gun under your troath...")
        time.sleep(2)
        print()
        ecrire_lent("you pulled the trigger slowly...")
        
        if bullet in ["blank"] :
            time.sleep(2)
            blank_sound.play()
            time.sleep(3)
            print()
            ecrire("Thankfully... It was a blank")
            time.sleep(2)
            print()
            break
        elif bullet in ["real", "real2"] :
            time.sleep(2)
            gunshot_sound.play()
            bullet_Dead.play()
            time.sleep(0.25)
            blood_dripping.play()
            time.sleep(0.2)
            body_Fall.play()
            time.sleep(5)
            player_lives = player_lives - 1
            if player_lives > 0 :
                ecrire_lent("It was a real bullet...")
                time.sleep(1)
                print()
                ecrire_lent(f"You have \033[31m{player_lives}\033[0m life left...")
            break
    elif choice in ["air", "nothing", "infront", "straight"] :
        ecrire("You aim infront of you")
        time.sleep(2)
        print()
        ecrire("You put your finger on the trigger")
        if bullet in ["real", "real2"] :
            time.sleep(2)
            gunshot_sound.play()
            time.sleep(3)
            print()
            ecrire("It was a real bullet, you feel reliefed")
            time.sleep(2)
            print()
            break
        elif bullet in ["blank"] :
            time.sleep(2)
            blank_sound.play()
            time.sleep(3)
            print()
            ecrire_lent("No.... No, no please... PLEA-")
            gunshot_sound.play()
            bullet_Dead.play()
            time.sleep(0.25)
            blood_dripping.play()
            time.sleep(0.2)
            body_Fall.play()
            time.sleep(5)
            player_lives = player_lives - 1
            if player_lives > 0 :
                ecrire_lent(f"You have \033[31m{player_lives}\033[0m life left...")
                time.sleep(2)
                ecrire("but you are still fill with determination...")
                revive.play()
            break


if player_lives == 0 :
    cause_of_death = "Died to a bullet trough the head"
    suffer = "died directly after the trigger was pulled"
    game_over()
    credits()
    sys.exit()

ecrire("'\033[3mAlright. You survived the first bullet, 2 more to go...")
time.sleep(2)
print()
gun_reload.play()
time.sleep(4)
#bullet n2
bullet = bullet_in_gun.pop(0)
while True :
    choice = input("Where are you shooting ? (yourself/air) : ")
    if choice in ["yourself", "me", "myself"] :
        print()
        ecrire_lent("you put the gun under your troath...")
        time.sleep(2)
        print()
        ecrire_lent("you pulled the trigger slowly...")
        
        if bullet in ["blank"] :
            time.sleep(2)
            blank_sound.play()
            time.sleep(3)
            print()
            ecrire("Thankfully... It was a blank")
            time.sleep(2)
            print()
            break
        elif bullet in ["real", "real2"] :
            time.sleep(2)
            gunshot_sound.play()
            bullet_Dead.play()
            time.sleep(0.25)
            blood_dripping.play()
            time.sleep(0.2)
            body_Fall.play()
            time.sleep(5)
            player_lives = player_lives - 1
            if player_lives > 0 :
                ecrire_lent("It was a real bullet...")
                time.sleep(1)
                print()
                ecrire_lent(f"You have \033[31m{player_lives}\033[0m life left...")
            break
    elif choice in ["air", "nothing", "infront", "straight"] :
        print()
        ecrire("You aim infront of you")
        time.sleep(2)
        print()
        ecrire("You put your finger on the trigger")
        if bullet in ["real", "real2"] :
            time.sleep(2)
            gunshot_sound.play()
            time.sleep(3)
            print()
            ecrire("It was a real bullet, you feel reliefed")
            time.sleep(2)
            print()
            break
        elif bullet in ["blank"] :
            time.sleep(2)
            blank_sound.play()
            time.sleep(3)
            print()
            ecrire_lent("No.... No, no please... PLEA-")
            gunshot_sound.play()
            bullet_Dead.play()
            time.sleep(0.25)
            blood_dripping.play()
            time.sleep(0.2)
            body_Fall.play()
            time.sleep(5)
            player_lives = player_lives - 1
            if player_lives > 0 :
                ecrire_lent(f"You have \033[31m{player_lives}\033[0m life left...")
                time.sleep(2)
                ecrire("but you are still fill with determination...")
                revive.play()
            break


if player_lives == 0 :
    cause_of_death = "Died to a bullet trough the head"
    suffer = "died directly after the trigger was pulled"
    game_over()
    credits()
    sys.exit()

ecrire("'\033[3mStill alive ? I guess you dont want to die...\033[0m'")
gun_reload.play()
time.sleep(4)
#dernier choix
bullet = bullet_in_gun.pop(0)
while True :
    choice = input("Where are you shooting ? (yourself/air) : ")
    if choice in ["yourself", "me", "myself"] :
        print()
        ecrire_lent("you put the gun under your troath...")
        time.sleep(2)
        print()
        ecrire_lent("you pulled the trigger slowly...")
        
        if bullet in ["blank"] :
            time.sleep(2)
            blank_sound.play()
            time.sleep(3)
            print()
            ecrire("Thankfully... It was a blank")
            time.sleep(2)
            print()
            break
        elif bullet in ["real", "real2"] :
            time.sleep(2)
            gunshot_sound.play()
            bullet_Dead.play()
            time.sleep(0.25)
            blood_dripping.play()
            time.sleep(0.2)
            body_Fall.play()
            time.sleep(5)
            player_lives = player_lives - 1
            if player_lives > 0 :
                ecrire_lent("It was a real bullet...")
                time.sleep(1)
                print()
                ecrire_lent(f"You have \033[31m{player_lives}\033[0m life left...")
            break
    elif choice in ["air", "nothing", "infront", "straight"] :
        print()
        ecrire("You aim infront of you")
        time.sleep(2)
        print()
        ecrire("You put your finger on the trigger")
        if bullet in ["real", "real2"] :
            time.sleep(2)
            gunshot_sound.play()
            time.sleep(3)
            print()
            ecrire("It was a real bullet, you feel reliefed")
            time.sleep(2)
            print()
            break
        elif bullet in ["blank"] :
            time.sleep(2)
            blank_sound.play()
            time.sleep(3)
            print()
            ecrire_lent("No.... No, no please... PLEA-")
            gunshot_sound.play()
            bullet_Dead.play()
            time.sleep(0.25)
            blood_dripping.play()
            time.sleep(0.2)
            body_Fall.play()
            time.sleep(5)
            player_lives = player_lives - 1
            if player_lives > 0 :
                ecrire_lent(f"You have \033[31m{player_lives}\033[0m life left...")
                time.sleep(2)
                ecrire("but you are still fill with determination...")
                revive.play()
            break

if player_lives == 0 :
    cause_of_death = "Died to a bullet trough the head"
    suffer = "died directly after the trigger was pulled"
    game_over()
    credits()
    sys.exit()

ecrire("'\033[3mWell... To be fair, i didn't think you would have survive...\033[0m'")

ecrire("Thanks for playing pre-beta, game is still wip")