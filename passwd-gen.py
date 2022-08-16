import random

lettre_minuscule = "qwertzuiopasdfghjklyxcvbnm"
lettre_majuscule = "QWERTZUIOPASDFGHJKLYXCVBNM"
chiffres = "1234567890"
symboles = "/\*&@#$%?!-_"

use = lettre_minuscule + lettre_majuscule + chiffres + symboles
raw_taille_mdp = input("\nTaille de votre mot de passe ( Min:1, Max:74 ): ")

try:
    taille_mdp = int(raw_taille_mdp)
    password = "".join(random.sample(use, taille_mdp))
    print("Votre mot de passe : " + password)
except ValueError:
    print("\nVous n'avez pas saisi un nombre valide Ex: 28")
    exit()

#github
print("\nGithub: https://github.com/GabziDev")
