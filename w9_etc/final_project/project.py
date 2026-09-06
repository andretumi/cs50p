import requests
from bs4 import BeautifulSoup
import sys
import re
import schedule
import time


def main():
    url_input = input("Paste shopstar.pe's product URL ")
    if valid_url(url_input):
        try:
            target_price_input = int(input("Input target price "))

            job_args = (url_input, target_price_input)
            schedule.every().day.at("12:00").do(scrape_and_notify, *job_args)
            while True:
                schedule.run_pending()

        except ValueError:
            sys.exit("Invalid price input")
        except KeyboardInterrupt:
            sys.exit("Program ended, sorry to see you go.")


def scrape_and_notify(url, target_price):
    try:
        name, current_price = scrape_data(url)
        current_time = time.localtime()
        formatted_time = time.strftime("%Y-%m-%d", current_time)

        if notify_user(current_price, target_price):
            print(f"DATE: {formatted_time}   TARGET PRICE MET!")
            print(f"The {name} is now at S/.{current_price}")
            sys.exit(0)
        else:
            print(f"NOT YET, currently at S/.{current_price}")

    except Exception as e:
        sys.exit(f"Error: {e}")


def scrape_data(target_url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    response = requests.get(target_url, headers=headers)

    if response.status_code == 200 or response.status_code == 304:
        soup = BeautifulSoup(response.text, "html.parser")
        name = soup.find(
            "span",
            {
                "class": "vtex-store-components-3-x-productBrand vtex-store-components-3-x-productBrand--pdp"
            },
        ).text.strip()
        price = int(
            soup.find(
                "span", {"class": "mercury-interbank-components-0-x-currencyInteger"}
            ).text.strip()
        )
        return name, price
    else:
        raise Exception(f"Failed to retrieve the page. Status code: {response.status_code}")


def notify_user(current_price, target_price):
    return int(current_price) <= int(target_price)


def valid_url(url):
    domain = re.search(r"https?://(?:www\.)?shopstar\.pe/", url)
    product_id = re.search(r"-\d+/p$", url)

    if domain and product_id:
        return True
    sys.exit("Invalid URL")


if __name__ == "__main__":
    main()
