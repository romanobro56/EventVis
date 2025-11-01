# Filtering?
# Scrape data from Facebook via some API
# Put data into JSON to put into the backend
# What fields should the events have?
import facebook_scraper as fbs

# pip install (all the libraries)
# makes the requirements.txt

credents = ("Redacted")

if __name__ == "__main__":
    # Test searching for Amherst events.
    for post in fbs.get_posts('TownofAmherst', start_url="https://mbasic.facebook.com/TownofAmherst?v=timeline", cookies="sample_facebook_cookies.txt", pages=11):
        # Test getting text from the iterator.
        print(post['text'])
    for post in fbs.get_posts('NVIDIA', start_url="https://mbasic.facebook.com/NVIDIA?v=timeline", cookies="sample_facebook_cookies.txt", pages=11):
        # Test getting text from the iterator.
        print(post['text'])
        
        

    