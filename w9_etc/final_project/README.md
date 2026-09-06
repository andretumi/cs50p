# Shopstar.pe Price Notifier

### Description:
This is a simple Python script that allows users to track the price of a product on [shopstar.pe]("shopstar.pe")
and receive a notification through the local terminal when the current price of the product matches or drops to a target price that was specified by the user.

#### Video Demo:
If you would like to have a visual guide to know how the program works, please watch: [Video Demo]("https://youtu.be/j_9Y3Bm9_Qg")

## Description:
Before running the script, make sure to install the required pip dependencies by executing the following command in your terminal:
```bash
pip install requirements.txt
```

To use the Shopstar.pe Price Notifier, please follow these steps:

First, to start running the project, execute the following command in your terminal:
```bash
python project.py
```
Second, you will be asked to input the product URL. When prompted, please paste the URL of the product (web page) that you want to track from the [shopstar.pe]("shopstar.pe") website.

Finally, you will be prompted to enter the target price for that product. Be sure to input only an integer (EG: 100).

Then, the script will run in the background and will request the current price of the product every day at midday
and will only notify you if the product's current price matches or drops below your specified target price.

The notification will only be triggered if the current price is equal to or below the target price specified by the user, the notification will be send as a message that is printed in the terminal with the following format:
DATE: YYYY-MM-DD  TARGET PRICE MET!
The PRODUCT'S_NAME is now at S/.PRODUCT'S_CURRENT_PRICE

Thanks CS50 ❤️
