import feedparser
from bs4 import BeautifulSoup

def extract_description(entry):
    html_content = entry.get("summary", "")

    # parse the HTML and extract the event description
    soup = BeautifulSoup(html_content, "html.parser")
    description_div = soup.find("div", class_="description")

    if description_div:
        return description_div.get_text()
    return None

# TODO use the "link" field to uniquely ID events and prevent duplicates in the DB
def scrape_campus_pulse():
    # cache RSS file locally?
    feed = feedparser.parse("https://umassamherst.campuslabs.com/engage/events.rss")
    events = []
    for entry in feed.entries:
        event = {
            "title": entry.title,
            "link": entry.link,
            "description": extract_description(entry),
            # categories?
            "published": entry.published,
            "start": entry.start,
            "end": entry.end,
            "location": entry.location,
            # status?
            "author": entry.get("author", None),
            # host?
        }
        events.append(event)
    return events

if __name__ == "__main__":
    for event in scrape_campus_pulse():
        print(event)
        print()

