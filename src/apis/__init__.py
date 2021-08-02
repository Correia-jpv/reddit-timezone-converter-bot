from config import reddit_config

from .reddit import RedditAPI

reddit_api = RedditAPI(**reddit_config.AUTH).api
