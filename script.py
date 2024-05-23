import os
import shutil
import random
from tqdm import tqdm

def select_random_images(source_folder, destination_folder, fraction=0.25):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate through each folder in the source folder
    for folder_name in tqdm(os.listdir(source_folder), desc="Processing folders"):
        folder_path = os.path.join(source_folder, folder_name)
        if os.path.isdir(folder_path):
            # Create a subfolder in the destination folder
            subfolder_destination = os.path.join(destination_folder, folder_name)
            os.makedirs(subfolder_destination, exist_ok=True)
            
            # List all files in the current folder
            files = os.listdir(folder_path)
            num_files_to_select = max(1, int(len(files) * fraction))

            # Select random files
            selected_files = random.sample(files, num_files_to_select)

            # Copy selected files to the destination subfolder
            for file_name in selected_files:
                source_file_path = os.path.join(folder_path, file_name)
                destination_file_path = os.path.join(subfolder_destination, file_name)
                shutil.copyfile(source_file_path, destination_file_path)

# Replace these paths with your actual source and destination folder paths
source_folder_path = "/media/aayush/New Volume/cmfd_merge1"
destination_folder_path = "/media/aayush/New Volume/cmfd_merge1"

# Fraction of images to select (1/4 in this case)
fraction = 0.25

# Call the function
# select_random_images(source_folder_path, destination_folder_path, fraction)
import os

def rename_files(directory):
    for filename in os.listdir(directory):
        if filename.endswith("_Mask.jpg"):
            new_filename = os.path.join(directory, filename.replace("_Mask", ""))
            os.rename(os.path.join(directory, filename), new_filename)
            print(f"Renamed {filename} to {os.path.basename(new_filename)}")

# Replace 'path_to_your_directory' with the actual path to your directory
# directory = 'path_to_your_directory'

rename_files(destination_folder_path)
