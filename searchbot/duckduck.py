from urllib.parse import quote_plus

from telebot import types

def _generate_duck_search_term(term):
    if not isinstance(term, str):
        raise RuntimeError('Not string has been passed as term')
    return 'https://duckduckgo.com/?q={query}'.format(query=quote_plus(term))


def prep_result(search_term):
    duck_result = _generate_duck_search_term(search_term)
    return types.InlineQueryResultArticle(
        '1', '{query} - at DuckDuckGo'.format(query=search_term),
        types.InputTextMessageContent(duck_result),
        url=duck_result,
        hide_url=True,
    )
