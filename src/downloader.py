import requests
import os

DOWNLOAD_DIR = "data/downloads"

def download_pdf(pdf_url, paper_id):
    if not os.path.exists(DOWNLOAD_DIR):
        os.makedirs(DOWNLOAD_DIR)

    filename = os.path.join(DOWNLOAD_DIR, f"{paper_id}.pdf")
    
    try:
        response = requests.get(pdf_url, stream=True)
        response.raise_for_status()  # Raise an exception for HTTP errors
        with open(filename, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
        print(f"Downloaded {filename}")
        return filename
    except requests.exceptions.RequestException as e:
        print(f"Error downloading PDF: {e}")
        return None