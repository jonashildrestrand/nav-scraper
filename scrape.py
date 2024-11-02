import os
import re
import requests
from urllib.parse import urljoin

def download(path="./scraped", verbose=False):
    print(f'Downloading files from NAV into {path}')

    # Remove and recreate the destination directory
    if os.path.exists(path):
        for file in os.listdir(path):
            os.remove(os.path.join(path, file))
    else:
        os.makedirs(path)

    # URL to scrape for file attachments
    url = "https://www.nav.no/no/nav-og-samfunn/statistikk/arbeidssokere-og-stillinger-statistikk/helt-ledige"

    # Fetch the HTML content
    response = requests.get(url)
    html_content = response.text

    # Find all file links ending with .xlsx, .pdf, or .xls
    file_links = re.findall(r'attachment[^"]*\.(?:xlsx)', html_content)

    # Base URL for relative links
    base_url = "https://nav.no/_/"

    # Download each file to the destination directory
    for file in file_links:
        download_url = urljoin(base_url, file)
        file_path = os.path.join(path, os.path.basename(file))
        if verbose:
            print(f"Downloading {file} into {path}")

        # Perform the file download
        file_response = requests.get(download_url)
        if file_response.status_code == 200:
            with open(file_path, 'wb') as f:
                f.write(file_response.content)
        else:
            print(f"Failed to download {file}")

    # Remove files with ".1" suffix
    for file in os.listdir(path):
        if file.endswith(".1"):
            os.remove(os.path.join(path, file))
