import praw
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT

reddit = praw.Reddit(
    client_id=REDDIT_CLIENT_ID,
    client_secret=REDDIT_CLIENT_SECRET,
    user_agent=REDDIT_USER_AGENT,
)


def fetch_posts(subreddit_name, limit=10):
    subreddit = reddit.subreddit(subreddit_name)
    posts = []
    for submission in subreddit.hot(limit=limit):
        posts.append(submission)
    return posts


def main():
    posts = fetch_posts("France", 10)
    for post in posts:
        print(post.title)
        print(post.score)
        print(post.url)
        print(post.num_comments)
        print(post.selftext)
        print("--------------------------------")

if __name__ == "__main__":
    main()