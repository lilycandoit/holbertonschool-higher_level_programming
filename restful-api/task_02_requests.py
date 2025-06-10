import requests
import json
import csv

BASE_URL = "https://jsonplaceholder.typicode.com"
response = requests.get(f"{BASE_URL}/posts")


def fetch_and_print_posts():
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post["title"])

    else:
        print("Failed to fetch posts")


def fetch_and_save_posts():
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        posts_data = [{"id": post["id"],
                       "title": post["title"],
                       "body": post["body"]} for post in posts]

        # write to CSV using DictWriter
        with open("posts.csv", "w") as csv_file:
            # define column headers
            fieldnames = ["id", "title", "body", 'userId']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            # write header row
            writer.writeheader()

            # write all post
            writer.writerows(posts_data)

        print(f"{len(posts_data)} posts successfully saved to posts.csv file")
    else:
        print(f"Failed to fetch posts: {response.status_code}")
