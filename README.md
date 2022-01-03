# Reddit news reader | Telegram Bot

Telegram bot which fetches posts top submissions from a subreddit. 
NewsBot is used to demo a short, simple Python project from book, [Practical Docker With Python](https://www.apress.com/gp/book/9781484237830). 
Which I recommend for beginners of Docker software.

Most of the code taken from: https://github.com/Apress/practical-docker-with-python

### Getting started 

- Update your environment with:
`pip install -r requirements.txt`
- Set the environment variable `NBT_ACCESS_TOKEN` - Bot token generated using Telegram BotFather.
g Telegram BotFather.
    - See instructions on how to generate the token in Chapter 3 of the book or [refer to this guide](https://core.telegram.org/bots/api#authorizing-your-bot)
    - See this guide on [how to set environment variables](https://core.telegram.org/bots/api#authorizing-your-bot)
- Start the bot: 
    `python newsbot.py`

### Start Docker
```
docker build -t redditnews-bot .
docker run -e NBT_ACCESS_TOKEN=<token> redditnews-bot
```

Where `<token>` is your token from BotFather