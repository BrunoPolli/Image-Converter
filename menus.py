from InquirerPy import inquirer
from InquirerPy.validator import EmptyInputValidator
from InquirerPy.base.control import Choice
from blob_images_tools import *
from ANSII_colors import GREEN_COLOR, END_COLOR

WIDTH_VALUE = None
HEIGHT_VALUE = None

def insert_size_menu(option):
  """
  This function is responsible for showing menu with size options. 
  After insert width and height size, the option value will decide what function to call. 
  
  Arg: 
      option (str): Option selected in last menu (convert/verify).
  """

  WIDTH_VALUE = inquirer.number(
    message="Insert width value:",
    validate=EmptyInputValidator()
  ).execute()

  HEIGHT_VALUE = inquirer.number(
    message="Insert height value:",
    validate=EmptyInputValidator()
  ).execute()

  CONFIRM = inquirer.confirm(
    message=f"Confirm values? ({WIDTH_VALUE}x{HEIGHT_VALUE})",
    default=True,
    confirm_letter="y",
    reject_letter="n",
    transformer=lambda result: "Yes" if result else "No",
    ).execute()
  
  if CONFIRM:
    match(option):
      case 'convert':
        convert_images(int(WIDTH_VALUE), int(HEIGHT_VALUE))
      case 'verify':
        verify_images_size(int(WIDTH_VALUE), int(HEIGHT_VALUE))
  else:
    print(f"{GREEN_COLOR}[!]{END_COLOR} Ok!")
    time.sleep(2)


def show_menu():
  """
  This function is responsible for showing initial menu.
  """

  OPTION = inquirer.select(
    message="Choose an option:",
    choices=[
      Choice(1, name="Convert images"),
      Choice(2, name="Verify images size"),
      Choice(3, name="Save in Blob Storage"),
      Choice(4, name="Exit"),
    ]
  ).execute()

  match(OPTION):
    case 1:
      insert_size_menu('convert')
    case 2:
      insert_size_menu('verify')
    case 3:
      save_in_blob()
    case 4:
      print(f'{GREEN_COLOR}Bye!{END_COLOR}')
      time.sleep(2)
      os.system('cls')
      exit()
