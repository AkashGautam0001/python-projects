import csv
import requests
from bs4 import BeautifulSoup

HN_URL = "https://news.ycombinator.com/"
CSV_FILE = "hn_top20.csv"

def fetch_top_post():
    try:
        response = requests.get(HN_URL, timeout=10)
        response.raise_for_status()

    except requests.RequestException as e:
        print("Failed to fetch the page", e)
        return []

    soup = BeautifulSoup(response.text, "html.parser")
    post_links = soup.select("span.titleline > a")

    posts = []
    for link in post_links[:20]:
        title = link.text.strip()
        url = link.get("href").strip()
        posts.append({"title": title, "url": url})

    return posts

def save_to_csv(posts):
    if not posts:
        print("No posts found.")
        return
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        fieldnames = ["title", "url"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(posts)

    print(f"Saved {len(posts)} posts to {CSV_FILE}")

def main():
    posts = fetch_top_post()
    save_to_csv(posts)

if __name__ == "__main__":
    main()