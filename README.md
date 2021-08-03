# Reddit Timezone Conversion Bot

## Getting Started

1. Follow the [getting started guide](docs/1-getting-started.md) to create your Reddit app and learn how to configure
   the bot.

2. Then follow the [macOS/Linux](docs/2-linux-macos.md), or [Windows](docs/3-windows.md)
   or [docker](docs/4-docker-guide.md) guides to start the bot after everything is set up.

## Features

- Run on Linux, MacOS, or Windows.
- Continuously listen and answer requested timezone conversions on Reddit.
- Auto detects if the account is shadowbanned.

## How to use it

- Convert a date/time in a given original timezone to another target timezone. You may ommit the target timezone and the bot will convert to UTC. 
- Comment on any subreddit with the format ```!TimezoneConverter DateTime timezone timezone(optional)```

### Examples

- ```!TimezoneConverter 9:30 EDT```
- ```!TimezoneConverter 4/10 14:23 PST Asia/Tokyo```
- ```!TimezoneConverter 7/15 21:10 Asia/Tokyo America/New_York```

## How it works

- The bot listens to a stream of every new comment on Reddit and looks for its keyword ```!TimezoneConverter```
- Parses and attempts to convert the comment in the format ```DateTime timezone timezone(optional)```

## Warnings

### Reddit

New Reddit accounts will likely get banned with the bot. Let an account sit for a few days before using it. Do not use
an account that you love, as it's possible to be permanently banned.

### Heroku

The bot used to have a Heroku option - till they found out and now using the bot on heroku will get your account banned.

## Links/Resources

[Awesome Reddit Bots](https://github.com/huckingfoes/awesome-reddit-bots)

[Reddit Karma Farming Bot](https://github.com/MrPowerScripts/reddit-karma-farming-bot)

[Build a Reddit Bot](https://www.pythonforengineers.com/build-a-reddit-bot-part-1/)
[]()
[]()
[]()
[]()

## Contributing

Contributions are welcome! Read the [contribution guidelines](docs/contributing.md) first.