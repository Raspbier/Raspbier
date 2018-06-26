import fileinput
from Player import Player
from Game import Game
from NFC import NFC
from Order import Order
from Article import Article
import time
import StringIO

def validateIntInput(myInt):  
    parsed = False
    while not parsed:
        try:
            x = int(myInt)
            parsed = True # we only get here if the previous line didn't throw an exception
            if (parsed == True):
                fileinput.close()
        except ValueError:
            print 'Invalid value! Please enter standard text.'
            break

def validateStringInput(myString):  
    parsed = False
    while not parsed:
        try:
            x = str(myString)
            parsed = True # we only get here if the previous line didn't throw an exception
            if (parsed == True):
                fileinput.close()
        except ValueError:
            print 'Invalid value! Please enter standard text.'
            break






if __name__=='__main__':

    
    print("Please enter your name")
    for line in fileinput.input():   
        validateStringInput(line)
        myString = str(line)
        player = Player(myString, 1)
        fileinput.close()
    
    print("How many rounds do you want to play?")
    for line in fileinput.input():   
        validateIntInput(line)
        game = Game(line)
        fileinput.close()

    ##test and write an order to a rfid
    print("Test now your Raspi and your RFID reader")
    nfc = NFC()
    ##testdata

    firstOrder = True
    amount = 5
    turn = 0
    status = 5
    cycleTime = 1
    playerFrom = 4
    playerTo = 2
    articleNr = 1
    order = Order(amount, turn, status, cycleTime, playerFrom, playerTo, articleNr)
#    data = order.createRFIDArrays()

    data = order.createRFIDArrays()

    nfc.writeRFID(data)

    print ("")
    print ("Your RFID Tag and your Reader is working. Lets play!")
    print ("")
    print ("")


    while (turn < game.getRoundLimit()):

        print ("this is the " + str(turn) + " round")
        firstOrder=False
        print ("hold your order to the reader")
        job = nfc.readRFID(8)
        player.addOrderList(Order(job[0], job[1], job[2], job[3], job[4], job[5], job [6]))

        print ("The order from your customer is saved.")
        print ("")
        print ("how much beer do you like to order?")
        for line in fileinput.input():
            validateIntInput(line)
            order = Order(int(line), status, turn, cycleTime, playerFrom, playerTo, articleNr)
            fileinput.close()

        player.addPurchaseList(order)

        turn += 1


    ## print data to csv

    s = StringIO.StringIO(text)
    with open('fileName.csv', 'w') as f:
        for line in s:
            f.write(line)