import json
import requests

url = "https://jsonplaceholder.typicode.com/posts"

def fetch_posts(url):

    response = requests.get(url, timeout=5)

    response.raise_for_status()

    posts =  response.json()

    return posts


def save_posts(posts):

    with open("posts.json", "w", encoding="utf-8")as file:
        json.dump(posts,file,indent=4)


def load_posts():

    with open("posts.json", "r", encoding="utf-8")as file:
        return json.load(file)





     






def main() -> None:

    try:
        posts = fetch_posts(url)
        save_posts(posts)

    except requests.RequestException:
        print("Unable to fetch data.")

    else:

        data = load_posts()

        print(f"Total number of posts: {len(data)}")
        print(f"ID of first post: {data[0]['id']}")
        print(f"Title of first post: {data[0]['title']}")




if __name__ == "__main__":
    main()



