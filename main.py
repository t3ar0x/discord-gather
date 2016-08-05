import logging
import json
from gather.gatherbot import GatherBot
from gather import views


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s,%(msecs)03d %(levelname)-5.5s [%(name)s] %(message)s",
    )

    with open('config.json') as f:
        config = json.load(f)

    bot = GatherBot()
    bot.register_action('^!help', views.bot_help)
    bot.register_action('^!(?:add|s)#', views.add)
    bot.register_action('^!(?:remove|so)', views.remove)

    bot.run(config['token'])
