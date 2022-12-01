import uuid
import kalshi_python
from kalshi_python.models import CreateOrderRequest
from pprint import pprint

config = kalshi_python.Configuration()
# Comment the line below to use production
config.host = 'https://demo-api.kalshi.co/trade-api/v2'

# Create an API configuration passing your credentials.
# Use this if you want the kalshi_python sdk to manage the authentication for your.
kalshi_api = kalshi_python.ApiInstance(
    email='YOUR_EMAIL_HERE',
    password='YOUR_PASSWORD_HERE',
    configuration=config,
)

# Optionally you can use the
exchangeStatus = kalshi_api.get_exchange_status()
print('Exchange status response: ')
pprint(exchangeStatus)

# Replace the series ticker with the market ticker you want.
marketTicker = 'FED-23DEC-T3.00'
marketResponse = kalshi_api.get_market(marketTicker)
print('\nMarket: ' + marketTicker)
pprint(marketResponse)

balanceResponse = kalshi_api.get_balance()
print('\nUser balance: ')
pprint(balanceResponse)

# Submit an order for 10 yes contracts at 50cents on 'FED-23DEC-T3.00'
orderUuid = str(uuid.uuid4())
orderResponse = kalshi_api.create_order(CreateOrderRequest(
    ticker=marketTicker,
    action='buy',
    type='limit',
    yes_price=50,
    count=10,
    client_order_id=orderUuid,
    side='yes',
))
print('\nOrder submitted: ')
pprint(orderResponse)