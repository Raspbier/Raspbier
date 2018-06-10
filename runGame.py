import fileinput
import RPi.GPIO as GPIO
import MFRC522
import requests
import signal



class Game:

    def __init__(self, round):
        self.round = round

def end_read(signal,frame):
    global continue_reading
    print("Ctrl+C captured, ending read.")
    continue_reading = False
    GPIO.cleanup()

def readFRID():

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
            status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

            # Check if authenticated
            if status == MIFAREReader.MI_OK:
                # MIFAREReader.MFRC522_Read(8)
                data = MIFAREReader.MFRC522_Read(8)
                
                MIFAREReader.MFRC522_StopCrypto1()
                
                return data
                             
            else:
                print ("Authentication error")

product = str('')
amount = 0
round= 0
roundLimit = 0
amountInWarehouse = 0
player = "Einzelhändler"

print("how many rounds to play (recomme34nded are more than 10")

for line in fileinput.input():
    roundLimit = int(line)
    fileinput.close()


#mycomment
while (round < roundLimit):
    print ('your customer wants to order this amount of beer:')
    print ('please put your rfid to the reader')
    amount = readRFID()
    print (amount)


    print("which beer do you want to order?")
    print("1 = ...")
    print("2 = ...")
    print("3 = ...")
    print("4 = ...")
    for line in fileinput.input():
        product = line
        fileinput.close()

    print("how much beer do you likec?")
    print("Your order ist at least 1 liter at maximum 100 liter")

    for line in fileinput.input():
        amount = line
        fileinput.close()



    round = round +1

