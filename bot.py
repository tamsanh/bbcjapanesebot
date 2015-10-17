import time
import praw

import scraper
from scraper import article

r = praw.Reddit('BBCJapanese Bot by /u/magicpurpledinosaur. '
                'GitHub: https://github.com/tech4david/bbcjapanesebot')
r.login()
already_done = []

while True:
    scraper.reload()

    if not article.id in already_done:
        already_done.append(article.id)
        r.submit('bbcjapanesetest', article.title, text=scraper.text)

        time.sleep(10 * 60)
