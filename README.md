# Discord Wiki Bot

Bot for Discord that replaces Wikiwand.com urls with Wikipedia urls.

Because I like Wikiwand, while some people do not. And I was bored fiddling with the URLs manually.

## Setup

```bash
# Create virtual environment
python -m venv .venv

# activate venv
.venv\Scripts\activate

# pip-tools is only needed when managing requirements
pip install pip-tools
```

Create an `.env` file containing

```
TOKEN=MY-SECRET-TOKEN
```

Setup like any other Discord bot otherwise.

### Required Discord Permissions

* Send Messages
* Manage Messages

## Usage

Run like any other Discord bot.

The bot should respond to `$hello` message with `Hello!` when properly setup. It may still require permissions to be set.