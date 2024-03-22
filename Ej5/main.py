from src.selenium_strategy import SeleniumStrategy
from src.beautiful_strategy import BeautifulSoupStrategy
from src.Context import Context


def main():
    url = "https://finance.yahoo.com/quote/TSLA"
    context = Context(BeautifulSoupStrategy())
    result = context.scrape(url)
    print(result)

    # context = Context(SeleniumStrategy())
    # result = context.scrape(url)
    # print(result)


if __name__ == "__main__":
    main()
