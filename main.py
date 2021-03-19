import extrapolate
import discord_bot
import paper_trade
import schedule # new module
from web_server import keep_alive
import time
from datetime import datetime

#keep_alive()

def reset():
	extrapolate.weekly_data()
	extrapolate.oscilations()

schedule.every().day.at('21:25').do(paper_trade.open_market)
schedule.every().day.at('20:30').do(reset)
schedule.every().day.at('03:30').do(paper_trade.limit_buy)


while True:
  schedule.run_pending()
  time.sleep(10)