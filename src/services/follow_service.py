from models.user_follow import UserFollow
from extensions import db

# Follow
def follow_user(follower_id, followed_id):
    
    if follower_id == followed_id:
        return {"error": "You cannot follow yourself"}
    
    existing_follow = UserFollow.query.filter_by(
        follower_id=follower_id, 
        followed_id=followed_id
    ).first()
    if existing_follow:
        return {"error": "You already followed this user"}

    follow = UserFollow(follower_id=follower_id, followed_id=followed_id)
    db.session.add(follow)
    db.session.commit()
    return {"message": "Successfully followed user"}

# Unfollow
def unfollow_user(follower_id, followed_id):
    follow = UserFollow.query.filter_by(follower_id=follower_id, followed_id=followed_id).first()
    if follow:
        db.session.delete(follow)
        db.session.commit()
        return {"message": "Successfully unfollowed user"}
    return {"error": "You not following this user"}