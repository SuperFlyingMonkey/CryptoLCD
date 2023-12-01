import lcddriver
import requests
import time
from datetime import datetime
#from pynput import keyboard



def getNewData():
    
    y=requests.get('https://api.exchange.coinbase.com/products/btc-usd/ticker')
    storeString = str(y.json())
    outValue =" "
    printTrigger = 0
    priceDate = ""
    print(storeString)
    #get system time
    now = datetime.now()
    Date = now.strftime("%d/%m/%Y")
    time = now.strftime("%H:%M:%S")
    #parse the json string for the price
    for i in range(len(storeString)):
        charHolder= storeString[i]
     #"}","{", and "," are removed from the string and a new string is build 
        if charHolder!= "u" and charHolder != "}" and charHolder != "," and charHolder !="{" and charHolder !="'" :       
            outValue = outValue + charHolder
            if charHolder =='p':
                printTrigger =1
            
   # resets outValue at th end of each unique set of data
        if charHolder == ',' or charHolder =='}':
            #print Price and set print trigger to 0
            if printTrigger==1:
                priceDate= Date+" "+time+""+" BTC"+outValue
                printTrigger =0
            outValue=''
    return priceDate

display = lcddriver.lcd()
callCount = 0
try:
    print("Start")
#Display to LCD loop
    while True:
	#sample output to terminal
	print(getNewData())
	#output to LCD, wait 10 then clear LCD then wait 1
        display.lcd_display_string(getNewData(),1)
        time.sleep(1799)
        display.lcd_clear()
        time.sleep(1)
except KeyboardInterrupt: # If there is a KeyboardInterrupt (when you press ctrl+c), exit the program and cleanup
    print("Cleaning up!")
    display.lcd_clear()
