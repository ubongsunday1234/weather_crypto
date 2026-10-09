import requests
from app_logger import logger
from datetime import datetime, timedelta
import time
from dotenv import load_dotenv
import os
import sys
import json
from pathlib import Path

load_dotenv()
coingecko=os.getenv("coingecko")
headers = {
    "accept": "application/json",
    "x-cg-demo-api-key": coingecko
    }


#total time crypto program should run
def total_run():
    a=0
    hrs=input("Total Time Crypto Program should run and get prices\nNote: your number represent hours e.g 1 for 1hr, 2 for 2hrs: ")
    while True:
        if hrs=='' or hrs.isspace()==True: 
            hrs=input("enter only numbers: ")
        elif isinstance(float(hrs), (int,float))==True:
            break 
        else:
            hrs=input("enter only numbers: ")
        if a==5:
            print("you have continously written a wrong number, program aborted!!!!")
            sys.exit()
            logger.log_program.info("program exited")        
    date_=datetime.now()
    stop_time=date_+ timedelta(hours=float(hrs))
    return stop_time

#time frame
def step_time():
    Time_frame=input("  What Time Frame/Interval do you want the data\nNote this is taken as hour\neg. 1hr is 1, 15mins is 0.25, 30mins is 0.5 etc.: ").strip()
    print("")
    a=0
    while True:
        a+=1
        if Time_frame=='' or Time_frame.isspace()==True: 
            Time_frame=input("enter only numbers: ")
        elif isinstance(float(Time_frame), (int,float))==True:
            break 
        else:
            Time_frame=input("enter only numbers: ")
        if a==5:
            print("you have continously written a wrong number, program aborted!!!!")
            sys.exit()
            logger.log_program.info("program exited")        
    Time_frame=float(Time_frame)*60*60
    return  Time_frame


#TO SAVE CACHE FILE
def save_cache():
    with open(cache_file, "w") as f:
        json.dump(cache,f,indent=2)




#ADD ASSETS TO QUERY
query=[]
query_list={
    1:'bitcoin',
    2:'ethereum',
    3:'litecoin',
    4:'binancecoin',
    5:'bitcoin-cash',
    6:'ripple'
    }

#TO ADD ASSETS TO TRACK PRICE
def assets_():
    x=0
    y=0
    assets=input("Type the appropriate number to get start getting their prices\nBitcoin (1)\nEthereum (2)\nLitecoin (3)\nBinance coin (4)\nBitcoin Cash (5)\nRipple (XRP) (6)\n:")
    while True:
        y+=1
        if assets.isnumeric()==True and 0<int(assets)<7:
            break 
        else:
            assets=input("enter only numbers from 1 to 6 : ")
        if y==5:
            print("you have continously written a wrong number, program aborted!!!!")
            sys.exit()
            logger.log_program.info("program exited")        
    query.append(query_list[int(assets)])
    print(f"\n{query_list[int(assets)]}, Added\n")
    while True:
        check=input("To stop adding asset type (quit) or type any thing else to continue adding: ").lower()
        print("\n")
        if check=="quit":
            break
        x+=1
        y=0
        assets=input("Add another asset\nBitcoin (1)\nEthereum (2)\nLitecoin (3)\nBitcoin Casg (4)\nRipple (XRP) (5)\nUnited states dollar (6)\nNigerian Naira (7)\n:")
        while True:
            y+=1
            if assets.isnumeric()==True and 0<int(assets)<7:
                break 
            else:
                assets=input("enter only from 1 to 7: ")
            if y==5:
                print("you have continously written a wrong number, program aborted!!!!")
                sys.exit()
                logger.log_program.info("program exited")        
        if query_list[int(assets)] in query:
            print(f"\n{query_list[int(assets)]} already in the list\n")
            x=x-1
        else:
            query.append(query_list[int(assets)])
            print(f"\n{query_list[int(assets)]}, Added Successfully\n")
        if x==5:
            print("\n!!!Max amount of allowed data reached, if you attempt to continue, program will exit!!!\n")
        elif x==6:
            print("!!!program aborted!!!!,you added more than 7 assets, try again")
            sys.exit()
            logger.log_program.info("program exited")        
    return query




#PREPARE CACHE FILES
try:
    cache_path=Path(__file__).resolve()
    root=cache_path.parent.parent.parent
    cache_file=next(root.rglob("crypto_cache.json"))
except:
    cache_path=Path(__file__).resolve()
    root=cache_path.parent.parent.parent
    cache_file_=next(root.rglob("cache_crypto"))
    cache_file=os.path.join(cache_file_,"crypto_cache.json")
    with open(cache_file, "w") as file:
        json.dump([],file)
if os.path.exists(cache_file):
    try:
        with open(cache_file, "r") as f:
            cache=json.load(f)
        temp_cache={}
    except json.decoder.JSONDecodeError:
        cache=[]
        temp_cache={}
else:
    cache=[]
    temp_cache={}

#GET AND DISPLAY PRICE
def get_price():
    n=0
    refresh=step_time()
    stop=total_run()
    query=assets_()
    Symbols=""
    for assets in query:
        Symbols+= assets +','
    while True:
        n+=1
        now=datetime.now()
        if now>=stop and n!=1:
            print("completed")
            sys.exit()
            logger.log_program.info("program exited")        
        elif now>=stop and n==1 :
            print ("!!!invalid time frame or invalid total time program should run!!!")
            sys.exit()
            logger.log_program.info("program exited")        
        params = {
            "vs_currencies": "usd",
            "symbols": Symbols[:-1]
        }
        url = f"https://api.coingecko.com/api/v3/simple/price?vs_currencies={params["vs_currencies"]}&ids={params["symbols"]}"
        response=requests.get(url, headers=headers,timeout=10)
        response.raise_for_status()
        logger.log_program.info("crypto info gotten")
        response=response.json()
        now_={"datetime_":str(now)}
        temp_cache.update(response)
        temp_cache.update(now_)
        cache.append(temp_cache)
        save_cache()
        #to print and display results
        ASS=[]
        ASS_PRICE=[]
        for assets in query:
            ASS.append(assets)
            ASS_PRICE.append(response[assets]['usd'])
        lock=list(zip(ASS,ASS_PRICE))
        print("================CRYPTO PRICES===============")
        for results in lock:
            print(results)
        if refresh>=(stop-now).total_seconds():
            print("completed(nice)")
            sys.exit()
            logger.log_program.info("program exited")        
        logger.log_program.info("price displayed")
        print("waiting..program exitedtr + C to abort anytime)")
        time.sleep(refresh)
        print("refreshed")
    
