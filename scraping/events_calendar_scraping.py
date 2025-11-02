import requests
from bs4 import BeautifulSoup

URL = "https://events.umass.edu/calendar"

def scrape_umass_events():
    resp = requests.get(URL)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")

    events = []

    for card in soup.select("div.em-card"):
        title_tag = card.select_one("h3.em-card_title a")
        link = title_tag["href"] if title_tag and title_tag.has_attr("href") else None
        title = title_tag.get_text(strip=True) if title_tag else None

        # get date/time from em-local-time
        time_tag = card.select_one("em-local-time")
        start = time_tag["start"] if time_tag and time_tag.has_attr("start") else None
        end = time_tag["end"] if time_tag and time_tag.has_attr("end") else None

        # location
        loc_tag = card.select_one("p.em-card_event-text a")
        location = loc_tag.get_text(strip=True) if loc_tag else None

        # category/tag
        tag_span = card.select_one("span.em-card_tag")
        category = tag_span.get_text(strip=True) if tag_span else None

        events.append({
            "title": title,
            "link": link,
            "start": start,
            "end": end,
            "location": location,
            "category": category
        })

    return events

if __name__ == "__main__":
    ev = scrape_umass_events()
    for e in ev:
        print(e)
        print()


