# ScrapeThatJob

## In this python program, users will be scraping the main [Hacker News website]("https://news.ycombinator.com/news")

## Installation and Steps
```
from bs4 import BeautifulSoup
import requests
```
 - Use `html.parser`
```
soup = BeautifulSoup(yc_webpage, "html.parser")
```
 - To get them all, we change the soup.find to soup.find_all in `article_tag` and `article_upvote`
```
articles = soup.find_all(name="a", class_="storylink")
```
 - Create empty lists to fill up in for loops
```
article_texts = []
article_links = []
```

  - for loop to get the text and the link
```
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

```
 - article_upvotes for loop, same as above but one line:
```

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
```
 - Get the largest upvote count currently on site:
```
largest_number = max(article_upvotes)
print(largest_number)
```
 - save to `largest_index`
```
largest_index = article_upvotes.index(largest_number)
print(largest_index) 
```
 - Print the next two items, text and link, that correspond to the same index with the largest article
```
print(article_texts[largest_index]) 
print(article_links[largest_index]) 
```

## Contact
<img src="https://avatars0.githubusercontent.com/u/17928947?v=4" alt="Github profile image" width="80px" height="80px" />

__Jon Christie__ 

GitHub: [mathcodes](https://github.com/mathcodes) 

[<code><img width="72px" src="https://img.icons8.com/color/48/000000/linkedin.png"/></code>](https://www.linkedin.com/jonchristie)       
[<code><img width="72px" src="https://img.icons8.com/color/48/000000/twitter--v2.png"/></code>](https://twitter.com/jonpchristie)       
[<code><img width="72px" src="https://img.icons8.com/color/48/000000/youtube-play.png"/></code>](https://www.youtube.com/channel/UC5GFnN-lv8Yuqc9O3b79k6g)       
[<code><img width="72px" src="https://img.icons8.com/color/48/000000/facebook.png"/></code>](https://www.facebook.com/jonpchristie)       
[<code><img width="72px" src="https://img.icons8.com/color/48/000000/instagram-new--v2.png"/></code>](https://www.instagram.com/fullstack11235)       
[<code><img width="72px" src="https://img.icons8.com/color/48/000000/soundcloud.png"/></code>](https://soundcloud.com/jonchristie#/)       
[<code><img width="72px" src="https://img.icons8.com/color/48/000000/spotify--v1.png"/></code>](https://open.spotify.com/artist/07S7aLfxH70VAX64g1WuFw?si=tlOj1OMBRLm-y4sY8Lox3Q)