from xtquant import xtdata
def callback (datas):
    print(datas)
xtdata.subscribe_quote(stock_code='600519.SH', period='1d', start_time='20240101', callback=callback)
xtdata.run()
