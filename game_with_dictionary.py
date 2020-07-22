#!/usr/bin/python

# /*
#  * Copyright (C) 2020  Abdullah Azzam Olcay
#  * Gebze Technical University
#  * Lınkedin: https://tr.linkedin.com/in/abdullah-azzam-olcay-613453183
#  *
#  * Please do not remove this header.
#  * */

from random import seed
from random import randint
from gtts import gTTS
import os

weapons = {"sword":25,"magic":20,"arrow":15,"gun":30}
defence = {"shield":22,"iron armor":25,"cloak":15,"helmet":10}

print("""
WEAPONS:
-> 'sword'
-> 'magic'
-> 'arrow'
-> 'gun'
DEFENCE:
-> 'shield'
-> 'iron armor'
-> 'cloak'
-> 'helmet'
""")

################################ HERO 1 ####################################

hero_name_1 = input("Enter Hero 1 name:\n")
weapon_name_1 = input("Enter weapon name for first hero:\n")
weapon_1_pow = weapons.get(str(weapon_name_1))
extra_power_1 = "power_1"
power_1 = randint(0,100)
health_1 = "health_1"
h_1 = randint(0,25)
defence_1 =input("Enter defence name for first hero:\n")
d_1 = defence.get(str(defence_1))

################################ HERO 2 ####################################
hero_name_2 = input("Enter Hero 2 name:\n")
weapon_name_2 = input("Enter weapon name for second hero:\n")
weapon_2_pow = weapons.get(str(weapon_name_2))
extra_power_2 = "power_2"
power_2 = randint(0,100)
health_2 = "health_2"
h_2 = randint(0,25)
defence_2 =input("Enter defence name for second hero:\n")
d_2 = defence.get(str(defence_2))
############################################################################

heroes = {hero_name_1:{weapon_name_1:weapon_1_pow,
                       extra_power_1:power_1,
                       health_1:h_1,
                       defence_1:d_1},
          hero_name_2:{weapon_name_2:weapon_2_pow,
                       extra_power_2:power_2,
                       health_2:h_2,
                       defence_2:d_2}}

def war(hero_1,hero_2):
    hero_1_total_power = hero_1.get(weapon_name_1) + hero_1[extra_power_1]
    hero_2_total_power = hero_2.get(weapon_name_2) + hero_2[extra_power_2]
    hero_1_total_defence = hero_1.get(health_1) + hero_1[defence_1]
    hero_2_total_defence = hero_2.get(health_2) + hero_2[defence_2]
    # Hero 1 attack to Hero 2
    hero_2_total_defence -= hero_1_total_power
    # Hero 2 attack to Hero 1
    hero_1_total_defence -= hero_2_total_power
    # print(hero_2_total_defence)
    # print(hero_1_total_defence)
    if hero_1_total_defence > hero_2_total_defence:
        b = "The winner is {}".format(hero_name_1)
        print(b)
        tts = gTTS(text=b, lang='en')
        tts.save("winner.mp3")
        os.system("mpg321 winner.mp3")
    else:
        a = "The winner is {}".format(hero_name_2)
        print(a)
        tts = gTTS(text=a, lang='en')
        tts.save("winner.mp3")
        os.system("mpg321 winner.mp3")

war(heroes[hero_name_1],heroes[hero_name_2])
# print(heroes[hero_name_1])
# print(heroes[hero_name_2])