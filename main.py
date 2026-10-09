import requests
from app_logger import logger
import sys
from clients import weather
from clients import crypto
from calculations import statistics_crypto

logger.log_program.info("===PROGRAM STARTED===\n")
print("===============WEATHER AND CRYPTO QUICK CHECKER===============\n\n")
print("=======================API DASHBOARD=====================")
terminal=input("1. CRYPTO\n2. WEATHER\n3. STATISTICS\n4. CLEAR CACHE\n5. EXIT\nWrite the number associated with what you want: ")
print("\n")
x=0
while True:
    x+=1
    if terminal.isnumeric()==True and 0<=int(terminal)<6:
        break 
    else:
        terminal=input("enter only numbers from 1 to 5: ")
    if x==5:
        print("you have continously written a wrong number, program aborted!!!!")
        sys.exit()
        logger.log_program.info("program exited")
logger.log_program.info(f"==={terminal}, selected===\n\n")

#to get the lattitude and longitude by ip address
def by_ip():
    url="http://ip-api.com/json/"
    response=requests.get(url).json()
    lat=response["lat"]
    lon=response['lon']
    isp=response['isp']
    country=response['country']
    region=response['regionName']
    return lat,lon,isp,country,region


#for gettin lat and lon by inputed address
def streets():
    street=input("enter a Country, City or Street: ")
    headers={
        'User-Agent':'weather'
    }
    url="https://nominatim.openstreetmap.org/search"
    params={
        'q':{street},
        'format':'json',
        'limit':1
    }

    resp=requests.get(url,headers=headers,params=params).json()
    while len(resp)==0:
        print("!!!cant find the details of this place\nsearch another street or remove one sublocation\nor use a close location to the intended location!!!")
        street=input("enter a street: ")
        if street=="quit":
            exit()
        headers={
            'User-Agent':'weather'
        }
        url="https://nominatim.openstreetmap.org/search"
        params={
            'q':{street},
            'format':'json',
            'limit':1
        }
        resp=requests.get(url,headers=headers,params=params).json()
        print("Type quit to end program")
        
    location=resp[0]["display_name"]
    lat=resp[0]["lat"]
    lon=resp[0]["lon"]
    return location,lat, lon

#lattidue and longitude of pc 
if int(terminal)==2:
    print("To get the weather based on your PC location - Type (1)(Note:this only gets your approximate loaction)\nTo get the weather reports based on your Country, City or direct address Type (2)(Recommended)")
    action=input("enter either 1 or 2: ")
    x=0
    while True:
        x+=1
        if action.isnumeric()==True and 0<int(action)<3:
            break 
        else:
            action=input("enter only numbers 1 0r 2: ")
        if x==5:
            print("!!!you have continously written a wrong number, program aborted!!!!")
            sys.exit()
            logger.log_program.info("program exited")
    if int(action)==1:
        try:
            lat,lon,isp,country,region =by_ip()
            print("\n================ LOCATION ====================")
            print(f"Country={country}, Region/State={region}, ISP={isp}")
            weather.get_weather(lat,lon)
            logger.log_program.info(f"Country={country}, Region/State={region}, ISP={isp} selected")
        except requests.exceptions.HTTPError as e:
            print(f"!!!Server blocked us:{e}!!!") 
            logger.log_program.debug(f"!!!Server blocked us:{e}!!!")
        except requests.exceptions.ConnectionError:
            print("!!!check your internet connection,No internet!!!")
            logger.log_program.debug("bad internet connection")
        except requests.exceptions.Timeout:
            print("!!!Network too slow, Try again!!!")
            logger.log_program.debug("!!!Network too slow, Try again!!!")
        except Exception as e:
            print (f"!!!error:{e}!!!") 
            logger.log_program.debug(f"!!!error:{e}!!!")

    elif int(action)==2:
        try:
            lat,lon,isp,country,region =by_ip()
            location,lat, lon=streets()
            print("\n================ LOCATION ====================")
            print(location)
            print(f"ISP={isp}")
            print("!!!if the street diplayed location does not match the intended location, quit the program and restart with an appropriate address!!!")
            weather.get_weather(lat,lon)
            logger.log_program.info(f"location{location}, ISP={isp} selected")
        except requests.exceptions.HTTPError as e:
            print(f"!!!Server blocked us:{e}!!!") 
            logger.log_program.debug(f"!!!Server blocked us:{e}!!!")
        except requests.exceptions.ConnectionError:
            print("!!!check your internet connection,No internet!!!")
            logger.log_program.debug("bad internet connection")
        except requests.exceptions.Timeout:
            print("!!!Network too slow, Try again!!!")
            logger.log_program.debug("!!!Network too slow, Try again!!!")
        except Exception as e:
            print (f"!!!error:{e}!!!") 
            logger.log_program.debug(f"!!!error:{e}!!!")

#TO CHECK CRYPTO PRICE
if int(terminal)==1:
        try:
            crypto.get_price()
        except requests.exceptions.HTTPError as e:
            print(f"!!!Server blocked us:{e}!!!") 
            logger.log_program.debug(f"!!!Server blocked us:{e}!!!")
        except requests.exceptions.ConnectionError:
            print("!!!check your internet connection,No internet!!!")
            logger.log_program.debug("bad internet connection")
        except requests.exceptions.Timeout:
            print("!!!Network too slow, Try again!!!")
            logger.log_program.debug("!!!Network too slow, Try again!!!")
        except Exception as e:
            print (f"!!!error:{e}!!!") 
            logger.log_program.debug(f"!!!error:{e}!!!")


#STATISTICS 
if int(terminal)==3:
    try:
        statistics_crypto.simple_return()
        statistics_crypto.average_price()
        statistics_crypto.log_return()
        statistics_crypto.highest_price()
        statistics_crypto.lowest_price()
        statistics_crypto.volatility()
    except ZeroDivisionError:
        print("Division by zero encountered!!!")
        logger.log_program.debug("Division by zero encountered!!!")

        sys.exit()
        logger.log_program.info("program exited")

#CLEAR CACHE
if int(terminal)==4:
    statistics_crypto.clear_cache()
    logger.log_program.info("statistics completed")


#EXIT
if int(terminal)==5:
    sys.exit()
    logger.log_program.info("program exited")







