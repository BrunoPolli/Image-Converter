import os, time, sys

GREEN_COLOR = "\033[0;32m"
YELLOW_COLOR = "\033[1;33m"
LIGHT_WHITE_COLOR = "\033[1;37m"
END_COLOR = "\033[0m"

PERSONAL_LOGO = [
"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@@@#%@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@@#.%@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@*..%@@@@@@@@@@@@@@@@@@@@@",
"@@@@@*-*+%@@@@@@@@@@@@@@@@@@@@@",
"@@@@*....%@@@@@@@@@@@@@@@@@@@@@",
"@@@@@@#. =%*-*@@%:::*%==%@@@@@@",
"@@@@@@#. %@@+.:@@-.:@@@..#@@@@@",
"@@@@@@#. %@@+.:@@= :@@@..%@@@@@",
"@@@@@@#. %@@+.:@@=.:@@@..%@@@@@",
"@@@@@@+. +@@:..%@:..%@#..-@@@@@",
"@@@@@@#. %@@+.:@@= :@@@..%@@@@@",
"@@@@@@#. %@@+.:@@= :@@@ .%@@@@@",
"@@@@@@#. %@@+.:@@=.:@@@..%@@@@@",
"@@@@@@%-.+@@:.*@@-..%@#.-%@@@@@",
"@@@@@@@@@@@@@@@@@= -@@@@@@@@@@@",
"@@@@@@@@@@@@@@@%@=.-@@@@@@@@@@@",
"@@@@@@@@@@@@@@*::..-@@@@@@@@@@@",
"@@@@@@@@@@@@@@@%%@--@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@#-@@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@%-#@@@@@@@@@@",
"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@  by: Bruno Polli"
]

IMAGES_CONVERTER_LOGO = r"""
{GREEN_COLOR} ___                                        
|_ _|_ __ ___   __ _  __ _  ___  ___        
 | || '_ ` _ \ / _` |/ _` |/ _ \/ __|       
 | || | | | | | (_| | (_| |  __/\__ \       
|___|_| |_| |_|\__,_|\__, |\___||___/       
                     |___/     _            
  ___ ___  _ ____   _____ _ __| |_ ___ _ __ 
 / __/ _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
| (_| (_) | | | \ V /  __/ |  | ||  __/ |   
 \___\___/|_| |_|\_/ \___|_|   \__\___|_|   
{END_COLOR}"""
IMAGES_CONVERTER_LOGO = IMAGES_CONVERTER_LOGO.format(GREEN_COLOR=GREEN_COLOR, END_COLOR=END_COLOR)

def show_personal_logo():
  """
  This function shows my personal logo.
  """

  for row in PERSONAL_LOGO:
    print(f"{LIGHT_WHITE_COLOR}{row}{END_COLOR}")
    time.sleep(0.2)
  time.sleep(1.6)
  os.system('cls')

def show_project_logo():
  """
  This function shows the project logo.
  """
  os.system('cls')
  print(60 * f'{GREEN_COLOR}={END_COLOR}')
  print(IMAGES_CONVERTER_LOGO)
  print(60 * f'{GREEN_COLOR}={END_COLOR}')
  print('\n')

def show_animation():
  """
  This function shows typing animation(...).
  """

  for i in range(3):
    print(f'{GREEN_COLOR}.{END_COLOR}', end='' if i < 2 else '\n')
    sys.stdout.flush()
    time.sleep(1)