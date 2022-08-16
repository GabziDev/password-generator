import random

lettre_minuscule = "qwertzuiopasdfghjklyxcvbnm"
lettre_majuscule = "QWERTZUIOPASDFGHJKLYXCVBNM"
chiffres = "1234567890"
symboles = "/\*&@#$%?!-_"

use = lettre_minuscule + lettre_majuscule + chiffres + symboles
taille_mdp = 28 #taille de votre mot de passe

password = "".join(random.sample(use, taille_mdp))

print("Votre mot de passe : " + password) 

#github
x=input("\nGithub: https://github.com/GabziDev")
print(x)