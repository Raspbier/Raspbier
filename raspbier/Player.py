class Player():
    def __init__(self, name, nr):
        self.name = name
        self.nr = nr
        self.orderList = []
        self.purchaseList = []

    def addOrderList(self, order):
        self.orderList.append(order) 

    def addPurchaseList(self, order):
        self.purchaseList.append(order) 
