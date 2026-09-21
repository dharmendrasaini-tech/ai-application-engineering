import json
import csv
import logging
from pathlib import Path
import requests
from typing import TypedDict

#logging
logging.basicConfig(
    level= logging.INFO,
    format= "%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


#path

BASE_DIR = Path(__file__).resolve().parent

DATA_DIR = BASE_DIR / "data"

DATA_DIR.mkdir(exist_ok=True)

JSON_FILE = DATA_DIR / "posts.json"

CSV_FILE = DATA_DIR / "posts.csv"

JSONL_FILE = DATA_DIR / "posts.jsonl"



API_URL = "https://jsonplaceholder.typicode.com/posts"

PARAMS = {
    "userId": 1
}


class Post(TypedDict):
    userId: int
    id: int
    title: str
    body: str


#functions

def fetch_posts() -> list[Post]:

    response = requests.get(url=API_URL, params=PARAMS, timeout=5)

    response.raise_for_status()

    posts = response.json()

    return posts



def save_json(posts: list[Post]) -> None:

    with JSON_FILE.open("w", encoding="utf-8") as file:
        json.dump(posts, file, indent=4)


def save_csv(posts: list[Post]) -> None:

    fieldnames = ["userId", "id", "title", "body"]

    with CSV_FILE.open("w", encoding="utf-8", newline="") as file:

        writer = csv.DictWriter(file,fieldnames = fieldnames)

        writer.writeheader()
        writer.writerows(posts)


def save_jsonl(posts: list[Post]) -> None:

    with JSONL_FILE.open("w", encoding="utf-8") as file:
        for post in posts:
            json_line = json.dumps(post)
            file.write(json_line + "\n")


def load_json() -> list[Post]:

    with JSON_FILE.open("r", encoding="utf-8") as file:
        loaded_file = json.load(file)

    return loaded_file


def display_summary(posts: list[Post]) -> None:

    print(f"Total posts loaded: {len(posts)}")

    if not posts:
        print("No posts available.")
        return

    first_post = posts[0]

    print(f"First post id: {first_post['id']}")
    print(f"First post title: {first_post['title']}")




















def main() -> None:

    logger.info("Application started.")

    try:
        posts = fetch_posts()
        logger.info("HTTP request completed. Number of posts fetched: %s",len(posts))
        

        save_json(posts)
        logger.info("JSON saved.")

        save_csv(posts)
        logger.info("CSV saved.")

        save_jsonl(posts)
        logger.info("JSONL saved.")

        loaded_posts = load_json()
        logger.info("JSON reloaded.")

        display_summary(loaded_posts)


    except requests.RequestException:
        logger.exception("HTTP request failed.")
        print("HTTP request failed.")


    finally:
        logger.info("Application finished.")


if __name__ == "__main__":
    main()



