from bot import Aria
from os import environ

bot = Aria()

extensions = [
    "cogs.manage",
    "cogs.game_controller",
    "cogs.help",
    "cogs.admin",
]
for extension in extensions:
    bot.load_extension(extension)

bot.run(environ['BOT_TOKEN'])
