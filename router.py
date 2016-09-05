from deal import Deal
from flask import render_template
from settings import Settings

def routes():
    return {'/': get_deals}

def get_deals():
    deals = []
    csv_file = Settings.getSetting('DEALS_FILE')
    with open(csv_file, 'r', newline='') as csv:
        deals_dict = Deal.dict_from_csv(csv)
        for deal in deals_dict.values():
            deals.append({
                'date': deal.date.isoformat(),
                'name': deal.name,
                'price': deal.price,
                'savings': deal.savings,
                'description': deal.description,
            })
    return render_template('deals.html', deals=deals)
