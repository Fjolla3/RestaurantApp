from BaseModel import Order
from BaseModel import OrderAmount
from BaseModel import OrderItem
from BaseEnums import OrderItemSize

class OrderPrinter:

    def printOrderInfo(self, restaurant, client, order, orderAmount, vatRate):
        self.__printOrderInfoHeader(client)
        orderItems = order.getOrdersItems()
        
        for orderItem in orderItems:
            self.__printOrderItemInfo(orderItem)
        
        self.__printOrderInfoFooter(restaurant, orderAmount, vatRate)

    def __printOrderItemInfo(self, orderItem):
        product = orderItem.getProduct()
        totalOrderItemPrice = orderItem.getOrderItemPrice() * orderItem.getQuantity()
        print(str(orderItem.getQuantity() )+ " x| " +str(product.getProductId()) + " . " + product.getName() + " | " + str(orderItem.getOrderItemPrice())+ " | " + str(totalOrderItemPrice) + " Euro ")

    def __printOrderInfoHeader(self, client):
        print("Order from " + (client.getName()) + ": ")
        print("------------------------------------")


    def __printOrderInfoFooter(self, restaurant, orderAmount, vatRate):
        print("------------------------------------")
        print("The total price of the order is: ")
        print("SUB TOTAL: " + str(orderAmount.getTotalAmount()) + " Euro. ")
        print("VAT " + str(int(vatRate)) + "%: " + str(orderAmount.getTotalOrderAmountVAT()) + " Euro. ")
        print("TOTAL: " + str(orderAmount.getTotalOrderAmountWithVAT()) + " Euro. ")
        print("--------------------------------------")
        print(restaurant.getName() +" in " + restaurant.getAddress())

class OrderCalculator:

    def calculateTotalOrderAmount(self, order):
        orderItems = order.getOrdersItems()
        totalOrderAmount = 0.0
        for orderItem in orderItems:
            totalOrderAmount += self.calculateOrderItemPrice(orderItem)

        return totalOrderAmount
    
    def calculateOrderItemPrice(self, orderItem):
        sizeRateAmount = self.getSizeRateAmount(orderItem.getorderItemSize())
        product = orderItem.getProduct()
        totalOrderItemPriceSingle = product.getPrice() * sizeRateAmount
        orderItem.setOrderItemPrice(totalOrderItemPriceSingle)

        return totalOrderItemPriceSingle * orderItem.getQuantity()

    def getSizeRateAmount(self, orderItem):
        return 1.2
   
    def calculateTotalOrderAmountVAT(self, totalOrderAmount):
        return totalOrderAmount * 18/100

    def calculateOrderAmount(self, order):
        totalOrderAmount = self.calculateTotalOrderAmount(order)

        totalOrderAmountVAT = self.calculateTotalOrderAmountVAT(totalOrderAmount)
        totalOrderAmountWithVAT = totalOrderAmount + totalOrderAmountVAT

        orderAmount = OrderAmount(totalOrderAmount, totalOrderAmountVAT, totalOrderAmountWithVAT)

        return orderAmount

class OrderManager:

    def __init__(self):
        self.__orders = [] 

    def getOrders(self):
        return self.__orders

    def createOrder(self, menu):
        order = Order()
        self.addOrderItem(order, menu.getMenuItems().get(100), 1, OrderItemSize.XXL)
        self.addOrderItem(order, menu.getMenuItems().get(101), 1, OrderItemSize.MEDIUM)
        self.addOrderItem(order, menu.getMenuItems().get(200), 2, OrderItemSize.LARGE)
        self.addOrderItem(order, menu.getMenuItems().get(201), 3, OrderItemSize.SMALL)

        return order

    def addOrderItem(self, order, product, quantity, orderItemSize):
        orderItemMeal = self.createOrderItemMeal(product, orderItemSize, quantity,)
        order.getOrdersItems().append(orderItemMeal)

    def createOrderItemMeal(self, product, orderItemSize, quantity):
        orderItem = OrderItem(product, orderItemSize, quantity)
        return orderItem