from config.reddit.config_gen import config_gen
from logs.log_utils import log_json
from logs.logger import log
from utils import prefer_envar

AUTH = prefer_envar({
    # app creds
    "reddit_client_id": "",
    "reddit_client_secret": "",
    # reddit account creds
    "reddit_username": "",
    "reddit_password": "",
})

for key in AUTH:
    if AUTH[key] == "":
        # reddit auth not configured correctly.
        # instruct user to generate a .env file
        config_gen()

log.info(f"REDDIT AUTH CONFIG:\n {log_json(AUTH)}")

CONFIG = prefer_envar({
    "reddit_timezone_converter_bot": 1,
    # start the timezoneConverterBot
    "reddit_remove_low_scores": 0.002,
    # posts/comments that get downvoted to this score will be deleted
    "reddit_low_score_threshold": 0,
    # chance to check if the bot is shadowbanned,
    # and shut down the script automatically
    "reddit_shadowban_check": 0.002,
    # bot schedules. all times are UTC
    # add the schedule number to the array
    # and the bot will run within that time range
    # leave the array empty for no schedule: []
    # 1 - 7am-10am ((7,00),(10,00))
    # 2 - 10am-2pm ((10,00),(14,00))
    # 3 - 2pm-6pm ((14,00),(18,00))
    # 4 - 6pm-10pm ((18,00),(22,00))
    # 5 - 10pm-2am ((22,00),(2,00))
    "reddit_sleep_schedule": [],
    # Frequency to check if the bot hit karma limits
    "reddit_karma_limit_check": 0.002,
    # Set to integer with the max comment karma
    # before the bot shuts down. Set as None to ignore
    "reddit_comment_karma_limit": None,
    # Set to integer with the max post/submission karma
    # before the bot shuts down. Set as None to ignore
    "reddit_post_karma_limit": None,
})

log.info(f"REDDIT CONNFIG:\n {log_json(CONFIG)}")
