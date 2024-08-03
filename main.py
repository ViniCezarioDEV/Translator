from translate import Translator as tr
from os import system
from colorama import Fore, Back, Style, init
init()

def start():
    global categoryChoice
    print(f'''{Fore.RED}
  _____                                _           _                  
 |_   _|  _ __    __ _   _ __    ___  | |   __ _  | |_    ___    _ __ 
   | |   | '__|  / _` | | '_ \  / __| | |  / _` | | __|  / _ \  | '__|
   | |   | |    | (_| | | | | | \__ \ | | | (_| | | |_  | (_) | | |   
   |_|   |_|     \__,_| |_| |_| |___/ |_|  \__,_|  \__|  \___/  |_|
    {Fore.WHITE}
    {Style.BRIGHT}Your Current Language:{Style.NORMAL} {myLanguage} 
    ''')

    categoryChoice = int(input(f'''
    {Style.BRIGHT}Choose the Option{Style.NORMAL}
    [1] Change your language
    [2] Translate
    
    {Style.BRIGHT}>>> {Style.NORMAL}'''))


def changeLanguage():
    global myLanguageCode, myLanguage
    print(f'{Style.BRIGHT}Select the Language to change{Style.NORMAL}')
    for i, j in enumerate(languages):
        print(f'[{i + 1}] {j}')
    choice = int(input(f'{Style.BRIGHT}>>> {Style.NORMAL}'))
    choice -= 1 #index
    myLanguageCode = list(languages.values())[choice]
    myLanguage = listOfLanguages[choice]
    system('cls')
    

def translate():
    text = input(f'{Style.BRIGHT}Text to Translate\n>>> {Style.NORMAL}')
    print(f'{Style.BRIGHT}Select the Language to Translate{Style.NORMAL}')
    for i, j in enumerate(languages):
        print(f'[{i + 1}] {j}')
    choice = int(input(f'{Style.BRIGHT}>>> {Style.NORMAL}'))
    choice -= 1 #index
    theLanguageCode = list(languages.values())[choice]
    translatorRequest = tr(from_lang=myLanguageCode, to_lang=theLanguageCode)
    translatedText = translatorRequest.translate(text)
    system('cls')
    print(f'''{Fore.YELLOW}========================================================={Fore.WHITE}
Translated text: {translatedText}

{Fore.YELLOW}========================================================={Fore.WHITE}''') 

languages = {
    'English':'en',
    'Português (Portugal)' : 'pt',
    'Português (Brasil)' : 'pt-br',
    'Espanhol' : 'es',
    'Japanese' : 'ja',
    'Chinese' : 'zh',
    'Korean' : 'ko',
    'French' : 'fr',
    'Italian' : 'it',
    'Russian' : 'ru',
    'Arabic' : 'ar'
}
myLanguageCode = languages['English']
listOfLanguages = list(languages.keys())
myLanguage = listOfLanguages[0]


while True:
  start()
  if categoryChoice == 1:
    changeLanguage()
  elif categoryChoice == 2:
    translate()
  else:
    system('cls')