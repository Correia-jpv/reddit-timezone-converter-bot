import sys

import bot
from logs.logger import log
from utils import check_internet, get_public_ip

if __name__ == "__main__":
    if check_internet() is True:
        try:
            log.info(f'Internet connection found : {get_public_ip()}')
            bot.run()
        except KeyboardInterrupt:
            # quit
            sys.exit()
        else:
            log.info('Please check your internet connection')
            sys.exit()
