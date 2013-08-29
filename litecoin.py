import json
import requests

from util import hook


def getTickerData():
    """ get the latest litecoin information from btc-e.com """

    url = 'https://btc-e.com/api/2/ltc_usd/ticker'

    session = requests.Session()

    r = json.loads(
        session.get(url, headers={'Content-type': 'application/json'}).text
    )

    return r['ticker']


@hook.command('ltc', autohelp=False)
@hook.command(autohelp=False)
def litecoin(inp, say=None):
    "litecoin -- gets current exchange rate for litecoins from btc-e.com"
    ticker = getTickerData()

    return 'Current: $%.2f - High: $%.2f - Low: $%.2f - Volume: %.2f LTC' % (
        ticker.get('last', None),
        ticker.get('high', None),
        ticker.get('low', None),
        ticker.get('vol', None)
    )

if __name__ == '__main__':
    print litecoin("")
