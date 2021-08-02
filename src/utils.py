import os
import random
import string
import urllib.request

from config.common_config import ENVAR_PREFIX
from logs.logger import log


def random_string(length: int) -> str:
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


def prefer_envar(configs: dict) -> dict:
    for config in list(configs):
        config_envar = f"{ENVAR_PREFIX}{config}".lower()
        if os.environ.get(config_envar):
            configs[config] = os.environ.get(config_envar)
            log.info(f"loading {config_envar} from envar. Value: {configs.get(config)}")
        else:
            log.debug(f"no environment config for: {config_envar}")

    return configs


# Checks if the machine has internet and also can connect to reddit
def check_internet(host="https://reddit.com", timeout=5):
    try:
        urllib.request.urlopen(host, None, timeout)
        return True
    except Exception as ex:
        log.error(ex)
        return False


def get_public_ip():
    try:
        external_ip = urllib.request.urlopen("https://api.ipify.org")
        if external_ip:
            return external_ip.read().decode("utf-8")
    except Exception as e:
        log.error("could not check external ip")


def chance(value=.20):
    rando = random.random()
    return rando < value
