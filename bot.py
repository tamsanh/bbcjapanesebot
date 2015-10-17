import time
import praw

import scraper
from scraper import article

footer = ("\n\n---\n\nI'm a bot! Bleep bloop. You can find my source code "
          "[here](https://github.com/tech4david/bbcjapanesebot).")

r = praw.Reddit('/r/BBCJapanese Bot by /u/magicpurpledinosaur. '
                'GitHub: https://github.com/tech4david/bbcjapanesebot')
r.login()
already_done = []

while True:
    scraper.reload()

    if not article.id in already_done:
        already_done.append(article.id)
        r.submit('bbcjapanesetest', article.title, text=scraper.text + footer)

        time.sleep(10 * 60)
