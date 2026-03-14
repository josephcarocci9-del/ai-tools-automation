import os
import shutil

def organize_files(folder):
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):
            os.makedirs("text_files", exist_ok=True)
            shutil.move(filename, f"text_files/{filename}")

if __name__ == "__main__":
    organize_files(".")
