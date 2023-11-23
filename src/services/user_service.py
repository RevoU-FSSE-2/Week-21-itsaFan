from models.user import User
from models.tweet import Tweet

def get_user_profile(user_id):
    
    user = User.query.get(user_id)
    if not user:
        return None

    followers_count = user.followers.count()
    following_count = user.followed.count()
    recent_tweets = Tweet.query.filter_by(user_id=user_id).order_by(Tweet.published_at.desc()).limit(10).all()

    user_data = {
        "username": user.username,
        "bio": user.bio,
        "followers": followers_count,
        "following": following_count,
        "recent_tweets": [{"id": tweet.id, "content": tweet.tweet, "published_at": tweet.published_at} for tweet in recent_tweets]
    }

    return user_data
