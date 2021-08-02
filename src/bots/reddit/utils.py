import time

from praw.models.redditors import Redditors


## USER UTILS

def parse_user(user: Redditors):
    i = {}
    i['comment_karma'] = user.comment_karma
    i['link_karma'] = user.link_karma
    i['username'] = user.name
    i['created_utc'] = user.created_utc
    i['created_utc_human'] = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(user.created_utc))
    return i
