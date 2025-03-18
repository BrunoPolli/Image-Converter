from logos import show_project_logo, show_personal_logo
from ANSII_colors import *
from blob_images_tools import *
from menus import *
import sys, time

def main():
  """
  This is the main method, responsible for start, show logos and menus.s
  """

  # Greetings
  show_personal_logo()
  show_project_logo()
  time.sleep(1.5)

  while True:
    show_project_logo()
    show_menu()
  
if __name__:
  main()