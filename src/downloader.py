import requests
import os
import re

DOWNLOAD_DIR = "data/downloads"

def _sanitize_filename(title):
    """
    Sanitizes a string to be used as a valid filename.
    Removes or replaces characters that are not allowed in filenames.
    """
    # Replace invalid characters with an underscore
    sanitized_title = re.sub(r'[\\/:*?"<>|]', '_', title)
    # Optionally, you might want to limit the filename length
    return sanitized_title[:200] # Limit to 200 characters

def download_pdf(pdf_url, paper_id, paper_title):
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)

    # Sanitize the paper title to create a valid filename
    sanitized_title = _sanitize_filename(paper_title)
    filename = os.path.join(DOWNLOAD_DIR, f"{sanitized_title}.pdf")
    
    try:
        response = requests.get(pdf_url, stream=True)
        response.raise_for_status()  # Raise an exception for HTTP errors
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded '{filename}'")
        return filename
    except requests.exceptions.RequestException as e:
        print(f"Error downloading PDF: {e}")
        return None