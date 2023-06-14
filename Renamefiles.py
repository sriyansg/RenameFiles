import os

folder_path = "C:/Users/Sriyans/Desktop/coik/Coil_Images"  #path to folder

files = os.listdir(folder_path)

# Sort the files alphabetically
files.sort()

for i, file_name in enumerate(files):
    new_file_name = f"{i+1}.jpg"  # Replace .jpg with the appropriate file extension

    # Construct the full paths to the original and new file names
    original_path = os.path.join(folder_path, file_name)
    new_path = os.path.join(folder_path, new_file_name)

    # Rename the file
    os.rename(original_path, new_path)

print("Files renamed successfully.")
