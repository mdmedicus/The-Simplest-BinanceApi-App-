import time;
import urllib
import hmac
import hashlib
import json


API_KEY = "your api_key"
SECRET_KEY = "your secret_key"

def coinPrices():
    requestURL = "https://api.binance.com/api/v3/ticker/price"
    
    res  = urllib.request.Request(requestURL, method="GET")
    
    content = urllib.request.urlopen(res).read().decode("utf-8")
    
    #you can use json or whatever you want to extract spesific objects from content -> example def wallet

    
    print(content)
    
    return content

def orderBook(coinName):
    bodyWallet = "symbol="+coinName+"USDT&limit=5"
    
    requestURL = "https://api.binance.com/api/v3/depth?"
    
    requestURL += bodyWallet
    
    res  = urllib.request.Request(requestURL, method="GET")
    
    content = urllib.request.urlopen(res).read().decode("utf-8")
    
    #you can use json or whatever you want to extract spesific objects from content -> example def wallet

    
    print(content)
    
    return content


def encode(secretKey, data):
    return hmac.new(secretKey.encode("utf-8"), data.encode("utf-8"), hashlib.sha256).hexdigest()

    
def wallet(coinName):
    bodyWallet = "recvWindow=7000&timestamp="+str(int(time.time()*1000))

    requestURL = "https://api.binance.com/api/v3/account?"
    
    requestURL += bodyWallet+"&signature="+encode(SECRET_KEY, bodyWallet)
    
    res  = urllib.request.Request(requestURL, method="GET")
    
    res.add_header("X-MBX-APIKEY", API_KEY)
    res.add_header("Content-Type", "application/x-www-form-urlencoded")
    
    content = urllib.request.urlopen(res).read().decode("utf-8")
    
    json_Wallet = json.loads(content)
    
    for i in range(len(json_Wallet['balances'])):
        if json_Wallet['balances'][i]['asset'] == coinName: 
            content = print(json_Wallet['balances'][i]['free'])
            break
    
    return content
    
def orderMarket( side, coinName, quantity): 
    quan = ""
    if side == "SELL":
        quan = "quantity"   
    else:
        quan = "quoteOrderQty"
        
    bodyWallet = "symbol="+coinName+"USDT&side="+side+"&type=MARKET&"+quan+"="+quantity+"&recvWindow=7000&timestamp="+str(int(time.time()*1000))

    requestURL = "https://api.binance.com/api/v3/order?"
    
    requestURL += bodyWallet+"&signature="+encode(SECRET_KEY, bodyWallet)
    
    res  = urllib.request.Request(requestURL, method="POST")
    
    res.add_header("X-MBX-APIKEY", API_KEY)
    res.add_header("Content-Type", "application/x-www-form-urlencoded")
    
    content = urllib.request.urlopen(res).read().decode("utf-8")
    
    print(content)
    
    return content

def orderLimit( side, coinName, quantity, price): 
    bodyWallet = "symbol="+coinName+"USDT&side="+side+"&type=LIMIT&timeInForce=GTC&quantity="+quantity+"&price="+price+"&recvWindow=7000&timestamp="+str(int(time.time()*1000))

    requestURL = "https://api.binance.com/api/v3/order?"
    
    requestURL += bodyWallet+"&signature="+encode(SECRET_KEY, bodyWallet)
    
    res  = urllib.request.Request(requestURL, method="POST")
    
    res.add_header("X-MBX-APIKEY", API_KEY)
    res.add_header("Content-Type", "application/x-www-form-urlencoded")
    
    content = urllib.request.urlopen(res).read().decode("utf-8")
    
    print(content)
    
    return content

def orderCancel(coinName, orderID):
    bodyWallet = "symbol="+coinName+"USDT&orderId="+orderID+"&recvWindow=7000&timestamp="+str(int(time.time()*1000))
    
    requestURL = "https://api.binance.com/api/v3/order?"
    
    requestURL += bodyWallet+"&signature="+encode(SECRET_KEY, bodyWallet)
    
    res  = urllib.request.Request(requestURL, method="DELETE")
    
    res.add_header("X-MBX-APIKEY", API_KEY)
    res.add_header("Content-Type", "application/x-www-form-urlencoded")
    
    content = urllib.request.urlopen(res).read().decode("utf-8")
    
    print(content)
    
    return content

def orderActive(coinName):
    if coinName != "All":
        bodyWallet = "symbol="+coinName+"USDT&"
    else:
        bodyWallet = ""
    bodyWallet += "recvWindow=7000&timestamp="+str(int(time.time()*1000))
    
    requestURL = "https://api.binance.com/api/v3/openOrders?"
    
    requestURL += bodyWallet+"&signature="+encode(SECRET_KEY, bodyWallet)
    
    res  = urllib.request.Request(requestURL, method="GET")
    
    res.add_header("X-MBX-APIKEY", API_KEY)
    res.add_header("Content-Type", "application/x-www-form-urlencoded")
    
    content = urllib.request.urlopen(res).read().decode("utf-8")
    
    #you can use json or whatever you want to extract spesific objects from content -> example def wallet

    
    print(content)
    
    return content
        
def orderAll(coinName):
    bodyWallet = "symbol="+coinName+"USDT&recvWindow=7000&timestamp="+str(int(time.time()*1000))
    
    requestURL = "https://api.binance.com/api/v3/allOrders?"
    
    requestURL += bodyWallet+"&signature="+encode(SECRET_KEY, bodyWallet)
    
    res  = urllib.request.Request(requestURL, method="GET")
    
    res.add_header("X-MBX-APIKEY", API_KEY)
    res.add_header("Content-Type", "application/x-www-form-urlencoded")
    
    content = urllib.request.urlopen(res).read().decode("utf-8")
    
    #you can use json or whatever you want to extract spesific objects from content -> example def wallet
    
    print(content)
    
    return content




#orderMarket("BUY","USDT","800")

#orderLimit("SELL", "USDT", "800", "9")

#orderCancel("USDT", "orderID")

orderActive("All")

orderAll("RVN")

wallet("USDT")

orderBook("RVN")

coinPrices()
