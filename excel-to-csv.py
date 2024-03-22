import zipfile
import os
import shutil
# Example usage
base_path = os.getcwd()
# Get base path
def extract_and_copy_zip_contents(file_name,zip_file_path):
    with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
        zip_ref.extractall('temp')

    # List the contents of the temp directory
    temp_contents = os.listdir('temp')
    
    
    # # Ensure there are at least two items in the list
    if len(temp_contents) < 2:
         print("Error: The zip file does not contain multiple directories.")
         return
    print(temp_contents)
     # Get the path of the second directory within temp
    extracted_folder = os.path.join('temp', temp_contents[1])
    print("Extracted folder:", extracted_folder)

    # # Destination folder to copy the contents into
    destination_folder = os.path.join(base_path, '2022_river')

    # # Ensure destination folder exists, create if not
    os.makedirs(destination_folder, exist_ok=True)

    # # Copy contents of extracted folder to destination folder with renaming
    for i, item in enumerate(os.listdir(extracted_folder)):
         item_path = os.path.join(extracted_folder, item)
         item_name,path=item_path.split(".")
         new_file_name=file_name.split(".")[0]+f"-{i}.{path}"
         if os.path.isfile(item_path):
             shutil.copy(item_path,f"2022_river/{new_file_name}")
    
    # # Clean up temporary directory
    shutil.rmtree('temp')


folder_path = os.path.join(base_path, 'output_2022_rivers')
files = os.listdir(folder_path)

for file in files :
    zip_file_path = os.path.join(folder_path, file)
    extract_and_copy_zip_contents(file,zip_file_path)
