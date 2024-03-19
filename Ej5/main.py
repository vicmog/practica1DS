

from src.beautiful_strategy import BeautifulSoupStrategy
from src.context import Context


def main():
  url = 'https://finance.yahoo.com/quote/TSLA'
  context = Context(BeautifulSoupStrategy())
  open_value = context.scrape(url)
  print('Open Value:', open_value)


if __name__ == "__main__":
    main()