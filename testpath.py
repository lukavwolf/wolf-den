import time
import sys
import pygame 
from pygame.key import name
import PySimpleGUI as sg


def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.075)

def intro():
    
    print('')
    print('')
    delay_print("Hello.")
    time.sleep(1)
    delay_print(" My name is . . .")
    print('')
    print('')
    time.sleep(1)
    delay_print("Well . . .")
    time.sleep(1)
    delay_print(" that's not important right now.")
    print('')
    print('')
    time.sleep(1)
    delay_print("Tell me a little about yourself.")
    print('')
    print('')
    time.sleep(1)
    delay_print('What is your name? ')
    name = input()
    print('')
    print('')
    delay_print('Hm, that is a rather peculiar first name.')
    time.sleep(0.5)
    print('')
    print('')
    delay_print('I can only imagine what your last name must be.')
    time.sleep(1.5)
    print('')
    print('')
    delay_print('How old are you, ' + name + '? ')
    age = input()
    print('')
    print('')
    delay_print('Well, that definitely explains a lot.')
    time.sleep(1.5)
    print('')
    print('')
    delay_print('Last but not least, what is your favorite color? ')
    color = input()
    print('')
    print('')
    delay_print(color + ' is such an interesting choice.')
    time.sleep(0.75)
    print('')
    print('')
    delay_print('Not what I would have chosen, but interesting nonetheless.')
    time.sleep(1.5)
    print('')
    print('')
    print('')
    delay_print("Well that's all the time we have for now.")
    time.sleep(1)
    print('')
    print('')
    delay_print("As much as I'd love to talk . . .")
    time.sleep(1.5)
    delay_print(" it's time to wake up, " + name + '.')
    print('')
    print('')
    print('')
    time.sleep(1.5)
    delay_print("Oh,")
    time.sleep(1)
    delay_print(" and don't forget . . . ")
    time.sleep(2 )
    print('')
    print('')
    print('')
    print('')
    delay_print("They hate the light.")
    time.sleep(3)
    print('')
    print('')
    print('')
    print('')
    chapter_one()


def game_mes():
    print('')
    print('')
    print('')
    print('')
    print('Welcome to Scriptscape')
    print('')
    print('*' * 20)
    print('')
    print('')
    print(''' 
              In this script based game, you play the role of a young villager 
              in the small town of Corsica. As the story progresses, you will
              encounter various scenarios in which you will be presented choices.
              Depending on the choices you make, the story can end completely 
              differently than the path the other choices would have taken you.
              Take your time to truly analyze every situation and secure the
              best course of action. Good luck adventurer and remember . . .
              they hate the light. ;)
            ''')
    print('')
    print('')
    print('*' * 20)
    time.sleep(15)
    game_menu()

def game_menu():
    print('')
    print('')
    print('')
    print('*' * 20)
    print('')
    print('')
    gamestart = print('1. Game Start')
    gamerules = print('2. Rules')
    gamequit = print('3. Quit')
    print('')
    print('')
    print('')
    choice = input('What would you like to do?: ')

    if choice == '1':
        intro()
    elif choice == '2':
        game_mes()
    else:
        print('Client Closing')

def chapter_one():
    delay_print('*' * 30)
    print('')
    print('')
    delay_print('Chapter One -- The Harvest Festival')
    print('')
    print('')
    delay_print('*' * 30)
    time.sleep(2)
    print('')
    print('')
    print('Knock!')
    print('')
    print('')
    time.sleep(1.75)
    print('Knock!')
    print('')
    print('')
    time.sleep(1.75)
    print('Knock!')
    print('')
    print('')
    print('')
    time.sleep(1.75)
    delay_print("Rise and shine, little one! We've got a big day ahead of us.")
    time.sleep(1)
    print('')
    delay_print("The Harvest Festival is today and I'm going to need help getting all these decorations ready.")
    time.sleep(1)
    print('')
    print('')
    delay_print("Which decorations do you want to work on -- flowers or candles? ")
    choice1 = input()
    print('')
    if 'flower' in choice1.lower():
        delay_print('''
Flowers! Great choice! You take those and I will take the candles! 
Meet me outside once you're done trimming the thorns and cutting the stems from 
the flowers. Don't forget to grab the water pail so we can keep them hydrated!''')
    elif 'candle' in choice1.lower():
        delay_print('''
Candles! Fantastic choice! You take those and I will take the flowers!
Meet me outside once you're done cleaning out the excess wax and trimming the wicks!
Don't forget to grab the lighter so we have something to light them with!''')
            
    else:
        delay_print("Sorry little one, we don't have those this year.")
    print('')
    print('')
    print('placeholder')

game_menu()


