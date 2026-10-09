import statistics
from app_logger import logger
import math
import json
from pathlib import Path

#Read document
cache_path=Path(__file__).resolve()
root=cache_path.parent.parent.parent
h_path=next(root.rglob("crypto_cache.json"))
with open(h_path, "r") as file:
    content=json.load(file)
query_list={
    'bitcoin':'bitcoin',
    'ethereum':'ethereum',
    'litecoin':'litecoin' ,
    'binancecoin':'binancecoin',
    'bitcoin-cash':'bitcoin_cash',
    'ripple':'ripple'
    }
bitcoin=[]
ethereum=[]
litecoin=[]
binancecoin=[]
bitcoin_cash=[]
ripple=[]
#for loop to read all assets and ge their prices appended
for assets in content:
    check=list(assets)
    check=check[:-1]
    for value in check:
        if value=="bitcoin-cash":
            bitcoin_cash.append(float(assets[value]['usd']))
        elif value=="bitcoin":
            bitcoin.append(float(assets[value]['usd']))
        elif value=="ethereum":
            ethereum.append(float(assets[value]['usd']))
        elif value=="litecoin":
            litecoin.append(float(assets[value]['usd']))
        elif value=="binancecoin":
            binancecoin.append(float(assets[value]['usd']))
        elif value=="ripple":
            ripple.append(float(assets[value]['usd']))

#get the calculations
def simple_return():
    btc=float(bitcoin[-1]-bitcoin[0])/bitcoin[0] if len(bitcoin)>1 else "not_enough_data"
    eth=float(ethereum[-1]-ethereum[0])/ethereum[0] if len(ethereum)>1 else "not_enough_data"
    ltc=float(litecoin[-1]-litecoin[0])/litecoin[0] if len(litecoin)>1 else "not_enough_data"
    bnb=float(binancecoin[-1]-binancecoin[0])/binancecoin[0] if len(binancecoin)>1 else "not_enough_data"
    bch=float(bitcoin_cash[-1]-bitcoin_cash[0])/bitcoin_cash[0] if len(binancecoin)>1 else "not_enough_data"
    xrp=float(ripple[-1]-ripple[0])/ripple[0] if len(ripple)>1 else "not_enough_data"
    print(f"=====simple_return=====\nbtc={btc}%\teth={eth}%\tltc={ltc}%\t\nbnb={bnb}%\tbch={bch}%\txrp={xrp}%\n")

def log_return():
    btc=math.log(float(bitcoin[-1]/bitcoin[0])) if len(bitcoin)>1 else "not_enough_data"
    eth=math.log(float(ethereum[-1]/ethereum[0])) if len(ethereum)>1 else "not_enough_data"
    ltc=math.log(float(litecoin[-1]/litecoin[0])) if len(litecoin)>1 else "not_enough_data"
    bch=math.log(float(bitcoin_cash[-1]/bitcoin_cash[0])) if len(bitcoin_cash)>1 else "not_enough_data"
    bnb=math.log(float(binancecoin[-1]/binancecoin[0])) if len(binancecoin)>1 else "not_enough_data"
    xrp=math.log(float(ripple[-1]/ripple[0])) if len(ripple)>1 else "not_enough_data"
    print(f"=====log_return=====\nbtc={btc}%\teth={eth}%\tltc={ltc}%\t\nbnb={bnb}%\tbch={bch}%\txrp={xrp}%\n")

def average_price():
    btc=float(sum(bitcoin)/len(bitcoin)) if len(bitcoin)>1 else "not_enough_data"
    eth=float(sum(ethereum)/len(ethereum)) if len(ethereum)>1 else "not_enough_data"
    ltc=float(sum(litecoin)/len(litecoin)) if len(litecoin)>1 else "not_enough_data"
    bnb=float(sum(binancecoin)/len(binancecoin)) if len(binancecoin)>1 else "not_enough_data"
    bch=float(sum(bitcoin_cash)/len(bitcoin_cash)) if len(bitcoin_cash)>1 else "not_enough_data"
    xrp=float(sum(ripple)/len(ripple)) if len(ripple)>1 else "not_enough_data"
    print(f"=====average_price=====\nbtc={btc}\teth={eth}\tltc={ltc}\t\nbnb={bnb}\tbch={bch}\txrp={xrp}\n")

def highest_price():
    btc=float(max(bitcoin)) if len(bitcoin)>0 else "not_enough_data"
    eth=float(max(ethereum))if len(ethereum)>0 else "not_enough_data"
    ltc=float(max(litecoin)) if len(litecoin)>0 else "not_enough_data"
    bnb=float(max(binancecoin)) if len(binancecoin)>0 else "not_enough_data"
    bch=float(max(bitcoin_cash)) if len(bitcoin_cash)>0 else "not_enough_data"
    xrp=float(max(ripple)) if len(ripple)>0 else "not_enough_data"
    print(f"=====highest_price=====\nbtc={btc}\teth={eth}\tltc={ltc}\t\nbnb={bnb}\tbch={bch}\txrp={xrp}\n")

def lowest_price():
    btc=float(min(bitcoin)) if len(bitcoin)>0 else "not_enough_data"
    eth=float(min(ethereum)) if len(ethereum)>0 else "not_enough_data"
    ltc=float(min(litecoin)) if len(litecoin)>0 else "not_enough_data"
    bnb=float(min(binancecoin)) if len(binancecoin)>0 else "not_enough_data"
    bch=float(min(bitcoin_cash)) if len(bitcoin_cash)>0 else "not_enough_data"
    xrp=float(min(ripple)) if len(ripple)>0 else "not_enough_data"
    print(f"=====lowest_price=====\nbtc={btc}\teth={eth}\tltc={ltc}\t\nbnb={bnb}\tbch={bch}\txrp={xrp}\n")

    

def volatility():
    all_assets =[bitcoin,ethereum,litecoin,binancecoin,bitcoin_cash,ripple]
    temp_log=[]
    for assets in all_assets:
        if len(assets)<3:
            temp_log.append("not_enough_data")
        else:
            temp_log1=[]
            for i in range(1,len(assets)):
                log=float(math.log(assets[i]/assets[i-1]))
                temp_log1.append(log)
            result=statistics.stdev(temp_log1)
            temp_log.append(result)

    print(f"=====volatility=====\nbtc={temp_log[0]}\teth={temp_log[1]}\tltc={temp_log[2]}\t\nbnb={temp_log[3]}\tbch={temp_log[4]}\txrp={temp_log[5]}\n")

def clear_cache():
    cache1=[]
    with open(h_path, "w") as file:
        json.dump(cache1,file)
    print("cache completely cleared!!!")
