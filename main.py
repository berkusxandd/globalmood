import json 
import asyncio
from reddit_client import fetch_posts
from sentiment_engine import analyze_sentiment
from praw.models import MoreComments
import os
from huggingface_hub import InferenceClient
import numpy as np
import pandas as pd
from training_data import prep_data
from train_model import train_model
LABEL_INDEX = {"negative": 0, "neutral": 1, "positive": 2}
INDEX_TO_EMOTION = ["negative", "neutral","positive"]
def sentiment_analysis(analyzed_posts):
    total_items = 0
    scores = np.zeros(3) #neg,neut,pos
    for title, comments in analyzed_posts.items():
        # print("*******Title: " + title)
        res = analyze_sentiment(title)
        # print("Analyzed: \n")
        # print(res)
        for r in res:
            scores[LABEL_INDEX[r["label"]]] += r["score"]
        total_items += 1
        for comment in comments[1:]:
            #print("-----Comment: " + comment)
            res = analyze_sentiment(comment)
            # print("Analyzed: \n")
            # print(res)
            for r in res:
                scores[LABEL_INDEX[r["label"]]] += r["score"] * 0.2
            total_items += 0.2
    
    return (scores / (total_items))

def main():

    train_model()
    # with open("subreddits.json", "r") as f:
    #     subreddits = json.load(f)

    # rcount = len(subreddits["subreddits"])
    # all_moods = []
    # for i in range(rcount):
    #     analyzed_posts = {}
    #     posts = fetch_posts(subreddits["subreddits"][i], 10)
    #     posts_without_pinned = posts[1:]
    #     for post in posts_without_pinned:
    #         post.comments.replace_more(limit=0)
    #         comments = []
    #         for comment in post.comments:
    #             if '[removed]' not in comment.body:
    #                 comments.append(comment.body)
    #         analyzed_posts[post.title] = comments


    #     sent = sentiment_analysis(analyzed_posts)
    #     final_score = sent[1] + sent[2] # it's reddit right, neutral is positive imo
    #     final_mood = 0
    #     if final_score > 0.4:
    #         final_mood = 2
    #     elif final_score > 0.1:
    #         final_mood = 1
    #     else:
    #         final_mood = 0
    #     all_moods.append((subreddits["subreddits"][i],final_mood))
    
    # print(all_moods)



if __name__ == "__main__":
    main()