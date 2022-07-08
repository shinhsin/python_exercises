import feedparser

Weekday = ['Sun', 'Mon', 'Tue',
           'Wed', 'Thu', 'Fri', 'Sat']

rss = feedparser.parse('http://feeds.feedburner.com/cnaFirstNews')

for cnt in range(1, len(rss)+1):
    x = rss.entries[cnt-1]
    t = x['published_parsed']
    wd = Weekday[t.tm_wday+1]
    news = x['summary'][1:x['summary'].find('<')]
    news = news[news.find('）')+1:]
    print(f"==== Entry{cnt} ====")
    print(f"{t.tm_year}-{t.tm_mon}-{t.tm_mday}, {wd}\
  {t.tm_hour:02d}:{t.tm_min:02d}, ", x['title'])
    print(f"{news}\n{x['link']}")
    print("==================\n")
