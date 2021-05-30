from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
# To get them all, we change the soup.find to soup.find_all in `article_tag` and `article_upvote`
# article_tag = soup.find(name="a", class_="storylink")
articles = soup.find_all(name="a", class_="storylink")

# To get all the items for article_text and article_link, we need to use a for loop
# So I'll say for article tag in articles, so articles is of course,
# this list where we find all of the anchor tags with a class of storylink,

# loop through each one of those and for each of the tags,
# I'm going to get the text and also get the Href.
# I'm going to create two new lists, articles_text, and article_links.
# And then I'm going to save each of the new articles into those lists.
article_texts = []
article_links = []

for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get("href")
    article_links.append(link)

# This is not a list so we need to create one:
# article_upvotes = soup.find_all(name="span", class_="score").getText()

# article_upvotes = [score.getText() for score in soup.find_all(name="span", class_="score")]
article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

# print(article_texts) # Amazon Prime inflates prices, using the false promise of ‘free shipping’
# print(article_links)  # https://mattstoller.substack.com/p/amazon-primes-free-shipping-promise
# print(article_upvotes)  # 115 points

# So we've got all of the article upvotes,
# let's go ahead and just print out the first item.
# print(article_upvotes[0].split()) # ['59', 'points']

# Now get the first item and wrap it around an int:
# THIS IS THE METHOD OF HOW WE CAN GET AHOLD OF THE ACTUAL NUMBER OF UPVOTES
# print(int(article_upvotes[0].split()[0])) # 53

# Now we are going to apply these methods into our list comprehension:

# article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
#TODO NOW SEE HOW THESE PRINT INTO LISTS:
print(article_texts) # ['Overkill objects for everyday life', 'Amazon Prime inflates prices, using the false promise of ‘free shipping’', 'Poe’s Best-Selling Book During His Lifetime Was a Guide to Seashells',
print(article_links)  # ['https://neil.computer/notes/overkill-objects-for-everyday-life/', 'https://mattstoller.substack.com/p/amazon-primes-free-shipping-promise', 'https://www.atlasobscura.com/articles/edgar-allen-poe-seashell-book', 'https://old.reddit
print(article_upvotes)  # [70, 166, 50, 237, 834, 26 .... , 7]

#TODO I want to get the index of the list item that has the highest value.
# And then I want to use that index to pick out the title, text,
# and also the link from these two lists, as they are already

# Use the max function to get the largest + of upvotes
# Then we can print this number
largest_number = max(article_upvotes)
print(largest_number) # 869

# Now we can find the index of this largest number:
largest_index = article_upvotes.index(largest_number)
print(largest_index) # 11

# Passing in the largest index to print, and also the the article_links with the same index
print(article_texts[largest_index]) # After a week at my mom’s house I'm getting ads for her toothpaste brand
print(article_links[largest_index]) # https://twitter.com/RobertGReeve/status/1397032784703655938



