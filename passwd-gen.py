import random
import time

lettre_minuscule = "qwertzuiopasdfghjklyxcvbnm"
lettre_majuscule = "QWERTZUIOPASDFGHJKLYXCVBNM"
chiffres = "1234567890"
symboles = "/\*&@#$%?!-_"

use = lettre_minuscule + lettre_majuscule + chiffres + symboles
raw_taille_mdp = input("\n\n[1]  Taille de votre mot de passe [Min:1, Max:74]: ")

try:
    taille_mdp = int(raw_taille_mdp)
    password = "".join(random.sample(use, taille_mdp))
    print("\n\n[2]  Votre mot de passe :\n\n" + password)
except ValueError:
    print("\n[ /!\ ] Vous n'avez pas saisi un nombre valide [Min:1, Max:74]")
    time.sleep(2.5)
    exit()

#github
x=input("\n\n\n\n> Github: github.com/GabziDev")
print(x) 
