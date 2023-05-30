from abc import ABC, abstractmethod
from BaseModel import OrderAmount as OrderAmount
from BaseEnums import OrderItemSize as OrderItemSize

class AbstractOrderCalculator(ABC):
    
    def calculateTotalOrderAmount(self, order):
        orderItems = order.getOrdersItems()
        totalOrderAmount = 0.0
        for orderItem in orderItems:
            totalOrderAmount += self.calculateOrderItemPrice(orderItem)

        return totalOrderAmount

    def calculateOrderItemPrice(self, orderItem):
        sizeRateAmount = self._getSizeRateAmount(orderItem.getorderItemSize())
        product = orderItem.getProduct()
        totalOrderItemPriceSingle = product.getPrice() * sizeRateAmount
        orderItem.setOrderItemPrice(totalOrderItemPriceSingle)

        return totalOrderItemPriceSingle * orderItem.getQuantity()

    def getVATRate(self, decimal):
        pass

        if decimal == True:
            return self._getVATRate()
        else:
            return self._getVATRate() * 100

    def calculateTotalOrderAmountVAT(self, totalOrderAmount):
            return totalOrderAmount * self._getVATRate()
        
    def calculateOrderAmount(self, order): 
        totalOrderAmount = self.calculateTotalOrderAmount(order)
        
        totalOrderAmountVAT = self.calculateTotalOrderAmountVAT(totalOrderAmount)
        totalOrderAmountWithVAT = totalOrderAmount + totalOrderAmountVAT

        orderAmount = OrderAmount(totalOrderAmount, totalOrderAmountVAT, totalOrderAmountWithVAT)

        return orderAmount

    @abstractmethod        
    def _getVATRate(self):
        pass

    @abstractmethod        
    def _getSizeRateAmount(self, orderItemSize):
        pass
 
class OrderCalculatorKS (AbstractOrderCalculator):
    
    def __init__(self):
        self.__VAT_RATE = 0.18

    def _getVATRate(self):
        return self.__VAT_RATE
 
    def _getSizeRateAmount(self, orderItemSize):
        match orderItemSize:
            case OrderItemSize.SMALL:
                return 0.7
            case OrderItemSize.MEDIUM:
                return 1
            case OrderItemSize.LARGE:
                return 1.2
            case OrderItemSize.XXL:
                return 1.25
            case _:
                print("No Valid order item size: " + orderItemSize)
                return 1

class OrderCalculatorGER (AbstractOrderCalculator):

    def __init__(self):
        self.__VAT_RATE = 0.19
 
    def _getVATRate(self):
        return self.__VAT_RATE

    def _getSizeRateAmount(self, orderItemSize):
        match orderItemSize:
            case OrderItemSize.SMALL:
                return 0.8
            case OrderItemSize.MEDIUM:
                return 1
            case OrderItemSize.LARGE:
                return 1.25
            case OrderItemSize.XXL:
                return 1.3
            case _:
                print("No Valid order item size: " + OrderItemSize)
                return 1