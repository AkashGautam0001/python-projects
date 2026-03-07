import os
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

BASE_URL = "https://books.toscrape.com/"
IMAGE_DIR = "images"

def sanitize_filename(title):
    return re.sub(r'[^\w\-_. ]', '', title).replace(" ", "_")

def download_image(img_url, filename):
    try:
        response = requests.get(img_url, timeout=10)
        response.raise_for_status()

        with open(filename, "wb") as f:
            for chunk in response.iter_content(1024):
                f.write(chunk)
    except Exception as e:
        print(f"Failed to download {filename} : ", e)

def scrape_and_download_images():
    url = BASE_URL
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.select("article.product_pod")[:10]

    if not os.path.exists(IMAGE_DIR):
        os.makedirs(IMAGE_DIR)
    
    for book in books:
        title = book.h3.a['title']
        relative_img = book.find("img")["src"]
        img_url = urljoin(BASE_URL, relative_img)
        print(f"Downloading ImageURL :  {img_url}")

        filename = sanitize_filename(title) + ".jpg"
        filepath = os.path.join(IMAGE_DIR, filename)
        print(f"Saving to Filepath : {filepath}")

        print(f"Downloading : {title} to {filepath}")
        download_image(img_url, filepath)

    print(f"Downloaded {len(books)} images to {IMAGE_DIR}")

if __name__ == "__main__":
    scrape_and_download_images()