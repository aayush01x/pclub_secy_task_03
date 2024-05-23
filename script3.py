import os
import shutil
import pandas as pd

# Load the CSV file
csv_file = 'output.csv'
df = pd.read_csv(csv_file)

# Define the source directory where the images are currently stored
source_dir = '/media/aayush/New Volume/cmfd_merge1'

# Define the destination directories for male and female images
dest_dir_male = '/media/aayush/New Volume/dataset/male'
dest_dir_female = '/media/aayush/New Volume/dataset/female'

# Create destination directories if they don't exist
os.makedirs(dest_dir_male, exist_ok=True)
os.makedirs(dest_dir_female, exist_ok=True)

# Iterate over each row in the CSV
for index, row in df.iterrows():
    filename = str(row[0])
    gender = row[1]
    src_path = os.path.join(source_dir, filename + '.jpg')
    
    # Determine the destination path based on the gender
    if gender.lower() == 'male':
        dest_path = os.path.join(dest_dir_male, filename + '.jpg')
    elif gender.lower() == 'female':
        dest_path = os.path.join(dest_dir_female, filename + '.jpg')
    else:
        continue  # Skip if gender is not male or female

    # Move the file to the appropriate directory
    if os.path.exists(src_path):
        shutil.move(src_path, dest_path)
    else:
        print(f"File not found: {src_path}")

print("Images have been moved successfully.")
