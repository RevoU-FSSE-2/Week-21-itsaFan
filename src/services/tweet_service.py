from models.tweet import Tweet
from extensions import db

def post_tweet(user_id, tweet_content):
    new_tweet = Tweet(user_id=user_id, tweet=tweet_content)
    db.session.add(new_tweet)
    db.session.commit()
    return new_tweet