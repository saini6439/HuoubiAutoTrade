from huobi.client.account import AccountClient
from huobi.client.trade import TradeClient
from huobi.constant import *
from huobi.utils import *


def trade_new_order(symbol_test,amount,price):
    # symbol_test = "btcusdt"
    print(symbol_test,amount,price)
    account_id = ''
    trade_client = TradeClient(api_key='', secret_key='')
    order_id = trade_client.create_order(symbol=symbol_test, account_id=account_id, order_type='buy-limit', source='spot-api', amount=amount, price=price)
    LogInfo.output("created order id : {id}".format(id=order_id))

    # canceled_order_id = trade_client.cancel_order(symbol_test, order_id)
    # if canceled_order_id == order_id:
    #     LogInfo.output("cancel order {id} done".format(id=canceled_order_id))
    # else:
    #     LogInfo.output("cancel order {id} fail".format(id=canceled_order_id))

    # order_id = trade_client.create_order(symbol=symbol_test, account_id=account_id, order_type=OrderType.BUY_MARKET, source=OrderSource.API, amount=5.0, price=1.292)
    # LogInfo.output("created order id : {id}".format(id=order_id))

    # order_id = trade_client.create_order(symbol=symbol_test, account_id=account_id, order_type=OrderType.SELL_MARKET, source=OrderSource.API, amount=1.77, price=None)
    # LogInfo.output("created order id : {id}".format(id=order_id))

# trade_new_order("xplausdt",18.7466,0.5601)

