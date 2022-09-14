import random
import time
from string import ascii_letters, digits

symbols = "/\*&@#$%?!-_"

use = ascii_letters + digits + symbols
raw_length = input("\n[1] Taille de votre mot de passe [Min:1, Max:74]: >>>")

if raw_length.isdigit():
    length = int(raw_length)
else:
    print("\n[ /!\ ] Vous n'avez pas saisi un nombre valide [Min:1, Max:74]")
    time.sleep(2.5)
    exit()

if 0 < length < 65:
    password = "".join([random.choice(use) for _ in range(length)])
    print("\n\n[2]  Votre mot de passe :\n\n" + password)
else:
    print("\n[ /!\ ] Vous n'avez pas saisi un nombre valide [Min:1, Max:74]")
    time.sleep(2.5)
    exit()
#github
print("\n> Github: github.com/GabziDev")
