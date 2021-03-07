import discord
import os
import re
from urlextract import URLExtract
from os.path import join, dirname
from dotenv import load_dotenv

client = discord.Client()
extractor = URLExtract()

# Load environment variables
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        await message.channel.send("Hello!")
        return

    original_message: str = message.content

    wikiwand_urls: list = get_wikiwand_urls(message.content)

    if any(wikiwand_urls):
        # delete original message
        # note: this is not necessary if there is a way to delete all embeds from a message.
        await message.delete()

        new_message = f"({message.author}'s Wikiwand link was replaced with Wikipedia link)\n {original_message}"

        for ww_url in wikiwand_urls:
            wikipedia_url = transform_wikiwand_to_wikipedia_url(ww_url)
            new_message = new_message.replace(ww_url, wikipedia_url)

        await message.channel.send(new_message)


def get_wikiwand_urls(content: str) -> list:
    "Returns all wikiwand.com URLs in content."
    all_urls = extractor.find_urls(content)
    return [url for url in all_urls if "www.wikiwand.com" in url]


def transform_wikiwand_to_wikipedia_url(ww_url: str) -> str:
    "Returns a wikiwand.com URL transformed into the equivalent Wikipedia URL."
    m = re.search("://www.wikiwand.com/(?P<lang>\w+)/(?P<page>[\s\S]*)", ww_url)
    lang = m.group("lang")
    page = m.group("page")

    wikipedia_url = f"https://{lang}.wikipedia.org/wiki/{page}"
    return wikipedia_url


client.run(os.getenv("TOKEN"))
