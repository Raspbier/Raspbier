import fileinput
import RPi.GPIO as GPIO
import MFRC522
import requests
import signal
from Tkinter import *
import tkFont
import time


def end_read(signal,frame):
    global continue_reading
    print("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

def readFRID(sektorToRead):
    global continue_reading
    continue_reading = True
    # Hook the SIGINT
    signal.signal(signal.SIGINT, end_read)

    # Create an object of the class MFRC522
    MIFAREReader = MFRC522.MFRC522()

    print ("Press Ctrl-C to stop.")

    # This loop keeps checking for chips. If one is near it will get the UID and authenticate
    while continue_reading:
        
        # Scan for cards    
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

        # If a card is found
        if status == MIFAREReader.MI_OK:
            print ("Card detected")
        
        # Get the UID of the card
        (status,uid) = MIFAREReader.MFRC522_Anticoll()

        # If we have the UID, continue
        if status == MIFAREReader.MI_OK:

            # Print UID
            print ("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3]))
        
            # This is the default key for authentication
            key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
            
            # Select the scanned tag
            MIFAREReader.MFRC522_SelectTag(uid)

            # Authenticate
            status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, sektorToRead, key, uid)

            # Check if authenticated
            if status == MIFAREReader.MI_OK:
                # MIFAREReader.MFRC522_Read(8)
                data = MIFAREReader.MFRC522_Read(sektorToRead)
                
                MIFAREReader.MFRC522_StopCrypto1()
                
                return data
                             
            else:
                print ("Authentication error")


def writeRFID (data):
    global continue_reading
    continue_reading = True
    # Hook the SIGINT
    signal.signal(signal.SIGINT, end_read)

    # Create an object of the class MFRC522
    MIFAREReader = MFRC522.MFRC522()

    # This loop keeps checking for chips. If one is near it will get the UID and authenticate
    while continue_reading:
        (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
        # Get the UID of the card
        (status,uid) = MIFAREReader.MFRC522_Anticoll()
        # If we have the UID, continue
        if status == MIFAREReader.MI_OK:
            # Print UID
            print "Card read UID: %s,%s,%s,%s" % (uid[0], uid[1], uid[2], uid[3])
            # This is the default key for authentication
            key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
            # Select the scanned tag
            MIFAREReader.MFRC522_SelectTag(uid)

            # Authenticate
            status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)
            print "\n"

            # Check if authenticated
            if status == MIFAREReader.MI_OK:
                MIFAREReader.MFRC522_Write(8, data)
                print "show output \n"
                MIFAREReader.MFRC522_Read(8)
                print "\n"
                MIFAREReader.MFRC522_StopCrypto1()

                # Make sure to stop reading for cards
                global continue_reading 
                continue_reading = False
            else:
                print "Authentication error"


continue_reading = True

product = str('')
amountOfOrder = 0
actualRound= 0
roundLimit = 0
amountInWarehouse = 0
player = ''
firstOrder=True
productName = "Beer"
status = "5"
cycleTime = "60"
data = []
articleNr = '123'


print("Please enter your name")
for line in fileinput.input():   
    parsed = False
    while not parsed:
        try:
            x = str(line)
            parsed = True # we only get here if the previous line didn't throw an exception
            if (parsed == True):
                global player
                player = line
                fileinput.close()
        except ValueError:
            print 'Invalid value! Please enter standard text.'
            break


print  ("how many rounds to play (recomme34nded are more than 10")

for line in fileinput.input():   
    parsed = False
    while not parsed:
        try:
            x = int(line)
            parsed = True # we only get here if the previous line didn't throw an exception
            if (parsed == True):
                roundLimit = int(line)
                fileinput.close()
        except ValueError:
            print 'Invalid value! Please enter an integer'
            break

time.sleep(2)
###hard coded first player need to call "Seller" to write the first order
if (player=='Seller'):
    print ("next step ist to prepare a RFID for first order")
    #data = [10, player.decode(), 0,0,0,0,0,0, 0,0,0,0,0,0,0, 0]  
    #writeRFID(data)
    readFRID(8)
    time.sleep(2)


while (actualRound < roundLimit):


    if firstOrder:
        print ('this is the ' + str(actualRound) +' round')
        firstOrder=False
    else:
        print ('this is the ' + str(actualRound) +' round\n')
        print('Hold the RFID from your customer to the reader')
        job = readFRID(8)
        time.sleep(2)
        print ('your customer want to buy ' + str(job[0]) + ' boxes of beer from you.')
        print ('')
        print ('how much beer do you want to supply to your customer?')
        print ('actually you have ' + str(amountInWarehouse) + ' boxes beer in you warehouse')
        for line in fileinput.input():   
            parsed = False
            while not parsed:
                try:
                    x = int(line)
                    parsed = True # we only get here if the previous line didn't throw an exception
                    if (parsed == True):
                        amountOfOrder = int(line)
                        fileinput.close()
                except ValueError:
                    print 'Invalid value! Please enter an integer'
                    break

    print ('Related to your data of the sales in past, please create now your order')
    ##only senseful if more than one product can be ordered
    # print("First: which beer do you want to order?")
    # print("1 = ...")
    # print("2 = ...")
    # print("3 = ...")
    # print("4 = ...")
    # for line in fileinput.input():
    #     product = line
    #     fileinput.close()
    # time.sleep(2)
    
    print("how much beer do you likec?")
    print("Your order ist at least 1 liter at maximum 100 liter")

    for line in fileinput.input():   
        parsed = False
        while not parsed:
            try:
                x = int(line)
                parsed = True # we only get here if the previous line didn't throw an exception
                if (parsed == True):
                    amountOfOrder = int(line)
                    fileinput.close()
            except ValueError:
                print 'Invalid value! Please enter an integer'
                break







    data = bytearray([int(amountOfOrder),int(actualRound),int(cycleTime),int(status), int(articleNr), 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00])


    #data = bytes([amountOfOrder,round,cycleTime,status, 0x08, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00])
    
    #data = [amountOfOrder, round, cycleTime, status, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100  ]

    
    print ('please put your rfid to the reader we will save your order')
    writeResponse = writeRFID(data)

    time.sleep(2)
    actualRound = actualRound +1

