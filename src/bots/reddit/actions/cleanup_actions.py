import os
import re
import sys

import requests
from apis import reddit_api
from libs.timezone_converter import TimezoneConverter
from logs.logger import log
from utils import chance


class Cleanup():
    def __init__(self):
        self.rapi = reddit_api
        self.username = None

    def init(self):
        self.me = self.rapi.user.me
        self.username = self.me().name

    def timezoneConvert(self):
        bot_keyword = "!TimezoneConverter"
        subreddit = self.rapi.subreddit('all')
        error_reply = "I couldn't convert your comment. If you believe this is a problem, please contact my maker."
        signature = "\n\n_____" \
                    "\n\n^Hi ^I'm ^a ^timezone ^converter ^bot, ^for ^more ^info, ^issues ^or ^suggestions [^click ^here](http://www.github.com/)"

        if not os.path.isfile("./comments_replied_to.txt"):
            comments_replied_to = []
        else:
            # Read the file into a list and remove any empty values
            with open("./comments_replied_to.txt", "r") as f:
                comments_replied_to = f.read()
                comments_replied_to = comments_replied_to.split("\n")
                comments_replied_to = list(filter(None, comments_replied_to))

        # Open stream of comments
        for comment in subreddit.stream.comments():

            # If we haven't replied to this comment before
            if comment.id not in comments_replied_to:

                # Do a case insensitive search
                if re.search(bot_keyword, comment.body, re.IGNORECASE):
                    comment_body = comment.body.replace(bot_keyword, '')

                    try:
                        # Try to parse comment's date
                        tzConverter = TimezoneConverter(comment_body)
                        converted_date = tzConverter.convertDate()
                        converted_timezone_name = tzConverter.converted_tz_name

                        if converted_date:
                            comment_reply = f'{converted_date.strftime("%m/%d %H:%M")}  {converted_timezone_name}'
                        else:
                            comment_reply = error_reply
                        comment.reply(comment_reply + signature)
                    except Exception as e:
                        comment.reply(error_reply + signature)
                        log.error(f'{comment.body} - {str(e)}')
                        pass

                    # Store the current id into our list
                    comments_replied_to.append(comment.id)

            # Write our updated list back to the file
            with open("./comments_replied_to.txt", "w") as f:
                for comment_id in comments_replied_to:
                    f.write(comment_id + "\n")

    def shadow_check(self, roll=1):
        if chance(roll):
            log.info("performing a shadowban check")
            response = requests.get(f"https://www.reddit.com/user/{self.username}/about.json",
                                    headers={'User-agent': f"hiiii its {self.username}"}).json()
            if "error" in response:
                if response["error"] == 404:
                    log.info(f"account {self.username} is shadowbanned. poor bot :( shutting down the script...")
                    sys.exit()
                else:
                    log.info(response)
            else:
                log.info(f"{self.username} is not shadowbanned! We think..")
