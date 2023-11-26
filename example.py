from pprint import pprint
from techpocket.core import TechPocket
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('max_colwidth', 500)

tp = TechPocket('7BC702DEA31E075C54D52C91A9EED7EFF48418C0')
print('balance:', tp.get_balance())

# pprint(tp.sport.get_sport_scores(sport='NBA', date='2023-01-17', df_like=False, save_to="./check/check.csv"))
# pprint(tp.sport.get_sport_scores(sport='NBA', date='2023-01-17', df_like=True, save_to="./check/check.csv"))
# pprint(tp.sport.get_sport_odds(sport='NBA', date='2023-01-17', df_like=False, save_to="check.csv"))
# pprint(tp.sport.get_sport_odds(sport='NBA', date='2023-01-17', df_like=True, save_to="./check"))
# pprint(tp.sport.get_sport_odds(sport='NBA', date='2023-01-17', df_like=True, save_to="./check/check.csv"))
# pprint(tp.sport.get_sport_lineups(sport='NBA', df_like=False, save_to='./check/check.csv'))
# pprint(tp.sport.get_sport_lineups(sport='NBA', df_like=True, save_to='./check'))
# pprint(tp.sport.get_sport_lineups(sport='NBA', df_like=True, save_to='./check/check.csv'))

# pprint(tp.stock.get_list(key='興櫃股票'))
# pprint(tp.stock.get_list(key='興櫃股票', df_like=True, save_to='./check/check.csv'))
pprint(tp.stock.get_ticks_realtime(stock_id='TSE'))
pprint(tp.stock.get_ticks_realtime(stock_id='TSE', df_like=True, save_to='./check/check.csv'))
pprint(tp.stock.get_ticks_realtime(stock_id='TSE', df_like=True, save_to='./check/check.csv', plot=True))
# pprint(tp.stock.get_price_realtime(stock_list=['2330', '2454']))
# pprint(tp.stock.get_price_realtime(stock_list=['2330', '2454'], df_like=True, save_to='./check/check.csv'))
