from lxml import html
import requests
import html2text

import article

page = requests.get(article.link)
tree = html.fromstring(page.text)
content = tree.cssselect('div.story-body > div.story-body__inner')[0]

htmlcode = html.tostring(content)

h = html2text.HTML2Text()
h.ignore_links = True
h.ignore_images = True

text = h.handle(str(htmlcode))
text = text[2:-3].replace('\n','').replace('\\n','\n')

print(text)
