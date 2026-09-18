import json
import requests
from typing import TypedDict


API_URL = "https://jsonplaceholder.typicode.com/posts"
REQUEST_TIMEOUT = 5
POSTS_FILE = "posts.json"

class Post(TypedDict):
    userId: int
    id: int
    title: str
    body: str



def fetch_posts(api_url:str) -> list[Post]:

    api_response = requests.get(api_url, timeout=REQUEST_TIMEOUT)

    api_response.raise_for_status() 

    posts =  api_response.json()

    return posts


def save_posts(posts: list[Post]) -> None:

    with open(POSTS_FILE, "w", encoding="utf-8")as file:
        json.dump(posts,file,indent=4)


def load_posts() -> list[Post]:

    with open(POSTS_FILE, "r", encoding="utf-8")as file:
        return json.load(file)






def main() -> None:

    try:
        posts = fetch_posts(API_URL)
        save_posts(posts)

    except requests.RequestException:
        print("Unable to fetch data.")

    else:

        loaded_posts = load_posts()

        if not loaded_posts:
            print("No posts available.")
            return


        first_post = loaded_posts[0]

        print(f"Total number of posts: {len(loaded_posts)}")
        print(f"ID of first post: {first_post['id']}")
        print(f"Title of first post: {first_post['title']}")




if __name__ == "__main__":
    main()



