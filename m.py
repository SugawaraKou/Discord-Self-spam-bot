import discord
from discord.ext import commands
from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import string
from os import path


if not path.isfile("gifs.txt"):
	driver = webdriver.Firefox(executable_path="/home/climz/PP/SP/CV/geckodriver")
	# driver.get("https://gifer.com/en/")
	driver.get("https://vgif.ru/best-gifs?page=1")
	for i in range(1, 12):
		driver.get("https://vgif.ru/best-gifs?page=" + str(i))
		sources = driver.find_elements(By.TAG_NAME, "source")
		for i in sources:
			gif = i.get_attribute("src")
			gif = gif.replace("mp4", "gif")
			if gif == "\n" or gif == "":
					pass
			else:
				with open ("gifs.txt", "a") as f:
					f.write(gif + "\n")		
else:
	pass


with open("gifs.txt", "r") as f:
	gifs_list = f.readlines()


def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str


client = commands.Bot(command_prefix='.', self_bot=True)

@client.event
async def on_redy():
    print('log')


@client.command()
async def say(ctx, *, text):
	
	cmd = str(text).split()

	if cmd[0] == "-m":
		# Message and repeat count
		for i in range(0, int(cmd[2])):
			await ctx.send(embed=discord.Embed(description=cmd[1]))
	elif cmd[0] == "-g":
		# Gif from site
		count = int(cmd[1])
		gif_count = len(gifs_list)
		for i in range(0, count):
			random_gif = random.randint(0,gif_count)
			await ctx.send(embed=discord.Embed().set_image(url=gifs_list[random_gif]))
			print(gifs_list[random_gif])

	## Gif from local
	# await ctx.send(embed=discord.Embed().set_image(url=src))
    # await ctx.send(file=discord.File('giphy.gif'))


client.run("", bot = False)
