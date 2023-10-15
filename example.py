from pprint import pprint

from techpocket.core import TechPocket

tp = TechPocket('DAC8D4453347487F24CDFCE061DF089FA1ED786B')
print('balance:', tp.get_balance())

pprint(tp.sport.get_sport_scores(sport='NBA', date='2023-01-17'))
pprint(tp.sport.get_sport_odds(sport='NBA', date='2023-01-17'))
pprint(tp.sport.get_sport_lineups(sport='NBA'))

pprint(tp.stock.get_list(key='興櫃股票'))
pprint(tp.stock.get_ticks_realtime(stock_id='TSE'))
pprint(tp.stock.get_price_realtime(stock_list=['2330', '2454']))
