import os


def organize_files(directory):
    # Detect the operating system using os.name
    is_windows = os.name == "nt"
    # Define file categories and corresponding file extensions
    file_types = {
        "Videos": [".mp4", ".mkv", ".avi", ".mov"],
        "Audios": [".mp3", ".wav", ".aac", ".flac"],
        "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Documents": [
            ".pdf",
            ".doc",
            ".docx",
            ".xls",
            ".xlsx",
            ".ppt",
            ".pptx",
            ".txt",
        ],
        "Misc": [],
    }
    # Create folders for each file category if they don't already exist
    for folder in file_types.keys():
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
    # Iterate over the files in the directory
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Determine the file extension
        file_extension = os.path.splitext(file_name)[1].lower()
        # Find the appropriate category for the file
        moved = False
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                # Move the file to the corresponding folder
                destination = os.path.join(directory, folder, file_name)

                # Check if file already exists at the destination
                if not os.path.exists(destination):
                    if is_windows:
                        os.system(f'move "{file_path}" "{destination}"')
                    else:
                        os.system(f'mv "{file_path}" "{destination}"')
                moved = True
                break

        # If no matching category is found, move to the 'Misc' folder
        if not moved:
            misc_destination = os.path.join(directory, "Misc", file_name)
            if not os.path.exists(misc_destination):
                if is_windows:
                    os.system(f'move "{file_path}" "{misc_destination}"')
                else:
                    os.system(f'mv "{file_path}" "{misc_destination}"')
    print("Files have been organized!")

    # if name == __main__:
# user_input = input("Enter the directory path to organize: ")
# if os.path.exists(user_input):
#     organize_files(user_input)
# else:
#     print("Invalid directory path!")
