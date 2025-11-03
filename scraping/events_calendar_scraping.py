import requests
from bs4 import BeautifulSoup
import time
from urllib.parse import urljoin

BASE_URL = "https://events.umass.edu"
CALENDAR_URL = "https://events.umass.edu/calendar"
# scaping with description and all pages and save to txt file
def scrape_umass_events():
    events = []
    page_number = 1
    processed_events = set()  
    while True:
  
        if page_number == 1:
            url = CALENDAR_URL
        else:
            url = f"{CALENDAR_URL}/{page_number}"
        
        print(f"Scraping page {page_number}...")
        
        try:
            resp = requests.get(url)
            resp.raise_for_status()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching page {page_number}: {e}")
            break
            
        soup = BeautifulSoup(resp.text, "html.parser")
     
        cards = soup.select("div.em-card")
        
        if not cards:
            print("No more events found. Reached the end.")
            break
        
        page_events_count = 0
        for card in cards:
            title_tag = card.select_one("h3.em-card_title a")
            link = title_tag["href"] if title_tag and title_tag.has_attr("href") else None
            
    
            if link:
                link = urljoin(BASE_URL, link)
                
            title = title_tag.get_text(strip=True) if title_tag else None
            
    
            event_key = f"{title}_{link}"
            if event_key in processed_events:
                continue
            processed_events.add(event_key)

            time_tag = card.select_one("em-local-time")
            start = time_tag["start"] if time_tag and time_tag.has_attr("start") else None
            end = time_tag["end"] if time_tag and time_tag.has_attr("end") else None

            loc_tag = card.select_one("p.em-card_event-text a")
            location = loc_tag.get_text(strip=True) if loc_tag else None

            tag_span = card.select_one("span.em-card_tag")
            category = tag_span.get_text(strip=True) if tag_span else None
           
            description = None
            if link:
                try:
              
                    time.sleep(0.5)
                    detail_resp = requests.get(link)
                    if detail_resp.status_code == 200:
                        detail_soup = BeautifulSoup(detail_resp.text, "html.parser")
                        
                       
                        description_selectors = [
                            "div.em-event_description",
                            "div.em-event-detail_description",
                            "div.event-description",
                            "div.description",
                            ".em-event-page_description"
                        ]
                        
                        for selector in description_selectors:
                            desc_div = detail_soup.select_one(selector)
                            if desc_div:
                                description = desc_div.get_text(strip=True)
                                break
                        
                      
                        if not description:
                            desc_div = detail_soup.find('div', class_=lambda x: x and 'description' in x.lower())
                            if desc_div:
                                description = desc_div.get_text(strip=True)
                                
                except Exception as e:
                    print(f"Error fetching description for '{title}': {e}")

            event_data = {
                "title": title,
                "link": link,
                "start": start,
                "end": end,
                "location": location,
                "category": category,
                "description": description
            }
            
            events.append(event_data)
            page_events_count += 1
            print(f"  - Scraped: {title}")

        print(f"Found {page_events_count} events on page {page_number}")
        
       
        if page_events_count == 0:
            print("No new events found on this page. Stopping.")
            break
            
        page_number += 1
        
   
        if page_number > 100:
            print("Reached safety limit of 100 pages. Stopping.")
            break

    return events

if __name__ == "__main__":
    print("Starting UMass events scraping...")
    events = scrape_umass_events()
    print(f"\nScraping complete! Found {len(events)} unique events in total.")
    

    with open("umass_events.txt", "w", encoding="utf-8") as f:
        f.write(f"UMass Events - Total: {len(events)}\n")
        f.write("=" * 80 + "\n\n")
        
        for i, event in enumerate(events, 1):
            f.write(f"Event {i}:\n")
            f.write(f"Title: {event['title']}\n")
            f.write(f"Category: {event['category']}\n")
            f.write(f"Location: {event['location']}\n")
            f.write(f"Start: {event['start']}\n")
            f.write(f"End: {event['end']}\n")
            f.write(f"Description: {event['description']}\n")
            f.write(f"Link: {event['link']}\n")
            f.write("-" * 80 + "\n\n")
    
    print("Events saved to 'umass_events.txt'")
    

    print("\nSummary of first 5 events:")
    print("=" * 50)
    for i, event in enumerate(events[:5], 1):
        print(f"{i}. {event['title']}")
        print(f"   Category: {event['category']}")
        print(f"   Location: {event['location']}")
        desc_preview = event['description'][:100] + '...' if event['description'] and len(event['description']) > 100 else event['description']
        print(f"   Description: {desc_preview}")
        print()
