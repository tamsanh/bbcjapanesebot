import time
import praw
import pickle

import scraper
from scraper import article

footer = ("\n\n---\n\nI'm a bot! Bleep bloop. You can find my source code "
          "[here](https://github.com/tech4david/bbcjapanesebot).")

r = praw.Reddit('/r/BBCJapanese Bot by /u/magicpurpledinosaur. '
                'GitHub: https://github.com/tech4david/bbcjapanesebot')
r.login()

try:
    f = open('already_done.pkl', 'rb')
    already_done = pickle.load(f)
    f.close()
except:
    already_done = []

scraper.reload()

if not article.id in already_done:
    already_done.append(article.id)
    r.submit('bbcjapanesetest', article.title, text=scraper.text + footer)

    f = open('already_done.pkl', 'wb')
    pickle.dump(already_done, f)
    f.close()
