import os
import shutil

DIRECTORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mpeg", ".wmv"],
    "Audio": [".mp3", ".wav"]
}

def organize_folder(target_path):
    for filename in os.listdir(target_path):
        file_path = os.path.join(target_path, filename)
        
        if os.path.isdir(file_path):
            continue
            
        name, extension = os.path.splitext(filename)
        extension = extension.lower()
        
        for folder_name, extensions_list in DIRECTORIES.items():
            if extension in extensions_list:
                folder_path = os.path.join(target_path, folder_name)
                
                if not os.path.exists(folder_path):
                    os.makedirs(folder_path)
                
                shutil.move(file_path, folder_path)
                print(f"Moved: {filename} -> {folder_name}")
                break

if __name__ == "__main__":
    path_to_clean = input("Enter the folder path to organize: ")
    organize_folder(path_to_clean)
