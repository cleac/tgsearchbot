# tgsearchbot

A simple bot for Telegram that generates search url to DuckDuckGo search engine using inline mode.


## Why the hell did I make it?

None of bots that should to it did in fact work. So I've implemented my one

## How to set it up

Firstly, you have to create your bot using guide from [test](https://core.telegram.org/bots). Than you have to activate [inline mode](https://core.telegram.org/bots/inline).

Than you have to create a configuration file, from where the token and bot name will be given. It uses *ini* format.
Example of configuration:

```
   [searchbot]

   bot_name = asdsearch
   token = <token from botfather>
```


Then run the bot using command `SEARCHBOT_CONFIG=<path_to_config_file> python app.py`

