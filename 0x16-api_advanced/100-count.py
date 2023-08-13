import requests
import re

def count_words(subreddit, word_list):
    if len(word_list) == 0:
        return {}

    response = requests.get(
        f"https://api.reddit.com/r/{subreddit}/hot/.json?limit=100"
    )

    if response.status_code != 200:
        return {}

    posts = response.json()["data"]["children"]

    word_counts = {}

    for post in posts:
        title = post["data"]["title"]
        for word in word_list:
            word = word.lower()
            matches = re.findall(f" {word} ", title)
            word_counts[word] = word_counts.get(word, 0) + len(matches)

    return count_words(subreddit, [word for word in word_counts if word_counts[word]])

def main():
    subreddit = sys.argv[1]
    word_list = sys.argv[2].split()

    count_words(subreddit, word_list)

if __name__ == "__main__":
    main()