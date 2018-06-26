

class Order():
    def __init__(self, amount, turn, status, cycleTime, playerFrom, playerTo, articleNr):
        self.amount = amount
        self.round = turn
        self.status = status
        self.cycleTime = cycleTime
        self.playerFrom = playerFrom
        self.playerTo = playerTo
        self.articleNr = articleNr

    def createRFIDArrays(self):
        data = bytearray([int(self.amount),int(self.round),int(self.cycleTime),int(self.status), int(self.articleNr), int(self.playerFrom),int(self.playerTo), 0x00, 0x00, 0x00, 0x00, 0x00,0x00, 0x00, 0x00, 0x00])

        return data