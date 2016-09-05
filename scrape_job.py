from bs4 import BeautifulSoup
from urllib import request
from deal import Deal
from settings import Settings
from datetime import date, datetime
from csv import reader, writer

def scrape_job():
    deals = _get_deals()
    _write_deals_to_csv(deals)

def _get_deals():
    url = Settings.getSetting('SCRAPE_URL')
    deals = []
    with request.urlopen(url) as response:
        doc = BeautifulSoup(response, 'html.parser')
        table = doc.select_one('table.shopItems')
        for td in table.find_all('td'):
            shop_item_base = td.select_one('.shopItemBase')
            name = shop_item_base.select_one('.name').get_text()
            price = shop_item_base.select_one('.price').get_text()
            savings_div = shop_item_base.select_one('.savings')
            savings = savings_div.select_one('.value').get_text()
            description = shop_item_base.select_one('.description').get_text().strip()
            deals.append(Deal(date.today(), name, price, savings, description))
    return deals

def _write_deals_to_csv(deals):
    csv_file = Settings.getSetting('DEALS_FILE')
    existing_deals = _get_existing_deals_dict()
    for deal in deals:
        existing_deals[deal.get_key()] = deal
    with open(csv_file, 'w', newline='') as csv:
        csv_writer = writer(csv)
        csv_writer.writerow(('Date', 'Name', 'Price', 'Savings', 'Description'))
        for key in sorted(existing_deals.keys()):
            csv_writer.writerow(existing_deals[key].to_csv())

def _get_existing_deals_dict():
    deals_dict = {}
    csv_file = Settings.getSetting('DEALS_FILE')
    with open(csv_file, 'r', newline='') as csv:
        deals_dict = Deal.dict_from_csv(csv)
    return deals_dict
