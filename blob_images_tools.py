from PIL import Image
from logos import show_project_logo, show_animation
from ANSII_colors import *
from azure.storage.blob import BlobServiceClient
import os, time, sys
from dotenv import load_dotenv

load_dotenv()

def convert_images(width, height):
  """
  This function is responsible for convert images to given values for width and height. 
  
  Args:
    width (int): Width value for conversion
    height (int): Height value for conversion
  """

  current_path = os.getcwd()
  images_folder_path = os.path.join(current_path, 'images')
  converted_images_folder_path = os.path.join(current_path, 'converted_images')

  print(f'{GREEN_COLOR}Starting converter{END_COLOR}', end='')
  sys.stdout.flush()
  show_animation()

  start_time = time.time()
  for index, file in enumerate(os.listdir(images_folder_path)):
    show_project_logo()

    print(f'{GREEN_COLOR}Converting{END_COLOR} {file} {GREEN_COLOR}to greyscale and resizing to {END_COLOR}{width}x{height}', end='')
    show_animation()
    image_path = os.path.join(images_folder_path, file)
    image = Image.open(image_path)
    
    new_image = image.convert('L')
    resized_image = new_image.resize((width, height))
    new_image_path = os.path.join(converted_images_folder_path, file)
    resized_image.save(new_image_path)

  end_time = time.time()
  print(f'{GREEN_COLOR}Conversion duration:{END_COLOR} {end_time - start_time}')
  print(f'{GREEN_COLOR}Total converted files:{END_COLOR} {index + 1}')
  time.sleep(5)

def verify_images_size(width, height):
  """
  This function is responsible for verify image sizes comparing given values for width and height. 
  
  Args:
    width (int): Width value for verifying
    height (int): Height value for verifying
  """

  current_path = os.getcwd()
  converted_images_folder_path = os.path.join(current_path, 'converted_images')

  for index, file in enumerate(os.listdir(converted_images_folder_path)):
    show_project_logo()

    print(f'{GREEN_COLOR}Verifying image sizes{END_COLOR}', end='')
    show_animation()
    print(f'{GREEN_COLOR}[{END_COLOR}{file}{GREEN_COLOR}] verified{END_COLOR}')
    time.sleep(1)

    converted_image_path = os.path.join(converted_images_folder_path, file) 
    image = Image.open(converted_image_path)
    image_width, image_height = image.size
    if image_width != width and image_height != height:
      print(f'{YELLOW_COLOR}[!]{END_COLOR} Wrong size in {YELLOW_COLOR}{file}{END_COLOR}')
      time.sleep(3)
      break
      
    
  print(f'{GREEN_COLOR}Files Ok!{END_COLOR}')
  print(f'{GREEN_COLOR}Total verified files:{END_COLOR} {index + 1}')
  time.sleep(5)

def save_in_blob():
  """
  This function is responsible for save images in a blob container. 
  """

  conn_str = os.getenv('CONN_STR')
  container_name = os.getenv('CONTAINER_NAME')
  blob_service_client = BlobServiceClient.from_connection_string(conn_str)
  blob_container = blob_service_client.get_container_client(container=container_name)
  current_path = os.getcwd()
  converted_images_folder_path = os.path.join(current_path, 'converted_images')
  
  for index, file in enumerate(os.listdir(converted_images_folder_path)):
    image_path = os.path.join(converted_images_folder_path, file)

    show_project_logo()

    print(f'{GREEN_COLOR}Saving images in blob{END_COLOR} {container_name}', end='')
    show_animation()

    blob_name = f"converted-{file}"
    blob_client = blob_container.get_blob_client(blob_name)
    
    with open(file=image_path, mode="rb") as data:
        blob_client.upload_blob(data)
        print(f'{GREEN_COLOR}[{END_COLOR}{file}{GREEN_COLOR}] saved{END_COLOR}')
        time.sleep(1)
    
  print(f'{GREEN_COLOR}Total files saved:{END_COLOR} {index + 1}')
  time.sleep(3)