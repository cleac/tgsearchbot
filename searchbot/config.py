import os

from configparser import ConfigParser

def load_config():
    config = None
    conf = ConfigParser()
    conf.read(os.environ['SEARCHBOT_CONFIG'])
    for key in ['searchbot', 'DEFAULT']:
        if config:
            break
        if key in conf:
            c = conf[key]
            if c['token'] and c['bot_name']:
                config = c
                break
    else:
        raise RuntimeError('Could not load application config')
    return config
