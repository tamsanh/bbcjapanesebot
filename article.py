import feedparser

d = feedparser.parse('http://feeds.bbci.co.uk/japanese/rss.xml')

id = d.entries[0].id
title = d.entries[0].title
link = d.entries[0].link
