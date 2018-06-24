import fileinput

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
        player = Player(line, 1)
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

    amount = 23
    turn = 0
    status = 5
    cycleTime = 60
    playerFrom = 4
    playerTo = 2
    firstBestellung = Bestellung(amount, turn, status, cycleTime, playerFrom, playerTo)
    nfc.writeRFID(data)