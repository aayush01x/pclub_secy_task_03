import os
import random
import shutil

# Define the source directory and the destination directory
source_dir = '/home/aayush/Documents/pclub_secy/task_3/data2/224'
dest_dir = '/home/aayush/Documents/pclub_secy/task_3/data_ext'
num_photos_to_select = 800

# Create destination directory if it doesn't exist
os.makedirs(dest_dir, exist_ok=True)

# Function to find all photos in folders ending with 'Male'
def find_male_photos(root_dir):
    male_photos = []
    for root, dirs, files in os.walk(root_dir):
        for dir_name in dirs:
            if dir_name.endswith('Male'):
                full_dir_path = os.path.join(root, dir_name)
                for file_name in os.listdir(full_dir_path):
                    if file_name.lower().endswith(('.jpg', '.jpeg', '.png')):
                        full_file_path = os.path.join(full_dir_path, file_name)
                        male_photos.append(full_file_path)
    return male_photos

# Find all male photos
male_photos = find_male_photos(source_dir)

# Randomly select 800 photos (or less if there are not enough)
selected_photos = random.sample(male_photos, min(num_photos_to_select, len(male_photos)))

# Copy selected photos to the destination directory
for photo_path in selected_photos:
    shutil.copy(photo_path, dest_dir)

print(f"{len(selected_photos)} photos have been successfully copied to {dest_dir}.")
