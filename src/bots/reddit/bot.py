import sys
from collections import namedtuple

from apis import reddit_api
from bots.reddit.actions.cleanup_actions import Cleanup
from config import reddit_config
from logs.log_utils import log_json
from logs.logger import log

from .utils import parse_user

BotAction = namedtuple("BotAction", 'name call')


class RedditBot():
    def __init__(self, config=reddit_config.CONFIG):
        self.api = reddit_api
        self.ready = False
        self.config = config
        self.user = None
        self.cleanup = Cleanup()
        self.actions = [
            BotAction("reddit_timezone_converter_bot", self.cleanup.timezoneConvert),
        ]

    def _init(self):
        # check if account is set
        user = self.api.user.me()
        if user is None:
            log.info("User auth failed, Reddit bot shutting down")
            sys.exit()
        else:
            log.info(f"running as user: {user}")

        # check if account is shadowbanned
        self.cleanup.init()
        self.cleanup.shadow_check()
        self.user = parse_user(user)
        log.info(f"account info:\n{log_json(self.user)}")
        self.ready = True
        log.info("The bot is now running.")

    def tick(self):
        for action in self.actions:
            action.call()

    def run(self):
        if self.ready:
            self.tick()
        else:
            self._init()
            self.run()
