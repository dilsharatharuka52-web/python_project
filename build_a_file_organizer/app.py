import os
import shutil

path = os.path.join(os.path.expanduser("~"),"Documents")
file =  os.listdir(path)

file_extenthion = ["image file", "video file", "text file"]

for folder in file_extenthion:
    target_dir  = os.path.join(path,folder)

    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
        print(f"Create directory :{target_dir}")
    else:
        print(f"Directory already exists: {target_dir}")


print("\n--- Scanning and moving files in Documents ---")

extension_mapping = {
    # Text folder extensions
    ".txt": "text file",
    ".pdf": "text file",
    ".docx": "text file",
    ".doc": "text file",
    
    # Image folder extensions
    ".png": "image file",
    ".jpg": "image file",
    ".jpeg": "image file",
    ".gif": "image file",
    
    # Video folder extensions
    ".mp4": "video file",
    ".avi": "video file",
    ".mov": "video file",
    ".mkv": "video file"
}



for item in os.listdir(path):
    full_path = os.path.join(path, item)

    if os.path.isfile(full_path):
      filename, extension = os.path.splitext(item)
      extension = extension.lower() # convert into lowercase to each .TXT otr .JPG

      if not extension:
          extension = "[No Extension]"
          print(f"Skippend : {item} (No extension)")
          continue

      if extension in extension_mapping:
          folder_name = extension_mapping[extension]
          target_folder = os.path.join(path,folder_name)
          destination_path = os.path.join(target_folder, item)

          shutil.move(full_path,destination_path)
          print(f"Move: {item} -> {folder_name}/")

      else:
          print(f"Skipped: {item} (Extension '{extension}' has on rule)")
