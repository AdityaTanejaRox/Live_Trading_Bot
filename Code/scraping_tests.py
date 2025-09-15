from scraping.my_fx_book import run_sentiment_scrape
from scraping.bloomberg_com import bloomberg_com
from scraping.fx_calendar import fx_calendar

# run_sentiment_scrape()
#data = bloomberg_com()

#[print(x) for x in data]
print("calling get_fx_calendar")
fx_calendar()