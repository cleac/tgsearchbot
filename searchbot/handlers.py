from searchbot.help import gen_help
from searchbot.duckduck import prep_result as duck_prep_result

def register_handlers(bot, config):

    # TODO: find more beautiful way for this staff

    @bot.message_handler(commands=['start', 'help'])
    def send_help(message):
        bot.reply_to(message, gen_help(config['bot_name']))


    @bot.inline_handler(lambda q: True) # TODO Fix this shit, doesn't work without that
    def gen_url(q):
        query = q.query.strip()
        if len(query) < 1:
            bot.answer_inline_query(q.id, [])
        else:
            bot.answer_inline_query(
                q.id,
                [
                    duck_prep_result(query)
                ],
            )

    return bot, config

