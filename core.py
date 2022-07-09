from utils.scrape import Scraper
import matplotlib
matplotlib.use("Agg") # use non-GUI backend so that plots can be made
import matplotlib.pyplot as plt

scraper = Scraper()

def scrape_by_series_id(id: str) ->:

    # NOTE: add 'caching' logic to skip expensive scraping
    vals,dates = clean_series_response(scraper.get_series(id))
    plt.plot(dates,vals)
    fstring = f"static/images/{id}-plot.png"
    plt.savefig(fstring)
