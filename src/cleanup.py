import os
import re

DOWNLOAD_DIR = "data/downloads"

def cleanup_filename(filename):
    # Replace "_  " with " "
    cleaned_filename = filename.replace("_  ", " ")
    # Replace "_ " with " "
    cleaned_filename = cleaned_filename.replace("_ ", " ")
    return cleaned_filename

def cleanup_downloaded_pdfs():
    if not os.path.exists(DOWNLOAD_DIR):
        print(f"Download directory '{DOWNLOAD_DIR}' does not exist.")
        return

    print(f"Cleaning up filenames in '{DOWNLOAD_DIR}'...")
    for filename in os.listdir(DOWNLOAD_DIR):
        if filename.lower().endswith(".pdf"):
            old_filepath = os.path.join(DOWNLOAD_DIR, filename)
            new_filename = cleanup_filename(filename)
            if new_filename != filename:
                new_filepath = os.path.join(DOWNLOAD_DIR, new_filename)
                try:
                    os.rename(old_filepath, new_filepath)
                    print(f"Renamed '{filename}' to '{new_filename}'")
                except OSError as e:
                    print(f"Error renaming '{filename}' to '{new_filename}': {e}")
    print("Filename cleanup complete.")

if __name__ == "__main__":
    cleanup_downloaded_pdfs()
