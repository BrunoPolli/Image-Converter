```
|_ _|_ __ ___   __ _  __ _  ___  ___        
 | || '_ ` _ \ / _` |/ _` |/ _ \/ __|       
 | || | | | | | (_| | (_| |  __/\__ \       
|___|_| |_| |_|\__,_|\__, |\___||___/       
                     |___/     _            
  ___ ___  _ ____   _____ _ __| |_ ___ _ __ 
 / __/ _ \| '_ \ \ / / _ \ '__| __/ _ \ '__|
| (_| (_) | | | \ V /  __/ |  | ||  __/ |   
 \___\___/|_| |_|\_/ \___|_|   \__\___|_|
```

## Images Converter
This project runs an interactive menu, with choices to apply gray scale, convert size, verify and save images in Azure Blob Storage.  

## Requisites
* Python 3.12.6
* Microsoft Azure Storage Explorer
* azure-core-tools
* azurite
* a container in Blob Storage

## Install
```
python -m venv venv  
.\venv\Scripts\activate
pip install -r .\requirements.txt
```

## Run
* Create 2 folders in the root project, 'images' and 'converted_images'
* Put images to convert in 'images' folder
* Create .env file and add 2 variables, 'CONN_STR' and 'CONTAINER_NAME'
* Start azurite instances
* Open Microsoft Azure Storage Explorer and connect to Emulator port
* Run main script:
```python .\main.py```

## Usage
* Arrow keys: navigate through options 
* Enter key: select option
* y/n keys: confirm or reject

### Commands
* Convert images: convert images in folder to given width and height sizes
* Verify image sizes: verify image sizes in folder comparing given width and height values
* Save in Blob Storage: save files in folder to Azure Blob Storage
* Exit: close application

## Example
![image](https://github.com/user-attachments/assets/ea75c1fd-9156-4e9f-8dfb-ed5dd60526ac)

---

![LOGO](https://github.com/user-attachments/assets/aba18c0b-214a-4327-85db-5507e404c475)  

Developed by: Bruno Polli

