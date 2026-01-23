import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"

def fetch_posts():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("API error:", response.status_code)
        return []

def fetch_post(post_id):
    response = requests.get(f"{API_URL}/{post_id}")
    if response.status_code == 200:
        return response.json()
    else:
        return None

def show_posts(posts, limit=5):
    print("\nOverzicht van posts:\n")
    for post in posts[:limit]:
        print(f"Post ID : {post['id']}")
        print(f"Titel   : {post['title']}")
        print(f"Body    : {post['body'][:60]}...")
        print("-" * 40)

def main():
    posts = fetch_posts()
    if not posts:
        return

    show_posts(posts)

    while True:
        choice = input("\nGeef een post-ID (of q om te stoppen): ")
        if choice.lower() in ["q", "quit"]:
            print("Programma afgesloten.")
            break

        if not choice.isdigit():
            print("Ongeldige invoer.")
            continue

        post = fetch_post(choice)
        if post:
            print("\nGeselecteerde post:")
            print("Titel:", post["title"])
            print("Body :", post["body"])
        else:
            print("Post niet gevonden.")

if __name__ == "__main__":
    main()
