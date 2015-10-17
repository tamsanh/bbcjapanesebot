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

# begin kludge
text = text.replace('\\n', '')  # remove literal "\n"
text = text.replace('\n\n','\\n')  # double newline -> literal "\n"
text = text.replace('\n', '')  # remove newlines
text = text.replace('\\n', '\n')  # convert literal "\n" back to newline
text = text.replace("\\'", "'")  # fix apostrophes
# end kludge

# assume unimportant or image caption if less than 100 chars
splittext = text.split('\n')
text = []
for line in splittext:
    if len(line) > 100:
        text.append(line)

text = '\n\n'.join(text)
