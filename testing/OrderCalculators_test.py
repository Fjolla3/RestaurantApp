# import the test framework unittest
import unittest   
import OrderCalculators
from BaseModel import Menu
from BaseModel import OrderItem
from BaseModel import Order
from BaseEnums import OrderItemSize

# created special AbstractOrderCalculator implementation for test (so called mock)
class OrderCalculatorMock(OrderCalculators.AbstractOrderCalculator):

    # implemented mock method
    def _getVATRate(self):
        return 0.12
 
    # implemented mock method
    def _getSizeRateAmount(self, orderItemSize):
        return 1.0

class AbstractOrderCalculator_test(unittest.TestCase):

    # used setUp method from unittest to prepare the test
    # method executes 'before each' test method
    def setUp(self):
        self.orderCalculatorMock = OrderCalculatorMock()
        self.menu = Menu()

    # created test method to test the order item price calculation
    def testCalcuateTotalOrderItemPrice(self):
        # prepare test objects (test input)
        hamburger = self.menu.getMenuItems().get(100)
        orderItem = OrderItem(hamburger, OrderItemSize.MEDIUM, 2)

		# execute method to be tested on test object
        totalOrderItemPrice = self.orderCalculatorMock.calcuateTotalOrderItemPrice(orderItem)

		# validate results (test output)
        self.assertEqual(9.0, totalOrderItemPrice)
        self.assertEqual(4.5, orderItem.getOrderItemPrice())

    # created test method to test the total order price calculation
    def testCalculateTotalOrderAmount(self):
        # prepare test objects (test input)
        hamburger = self.menu.getMenuItems().get(100)
        sandwich = self.menu.getMenuItems().get(102)
        cocaCola = self.menu.getMenuItems().get(200)
        iceCream = self.menu.getMenuItems().get(300)

		# created order items (all medium, as mock always returns 1 anyway)
        hamburgerOrderItem = OrderItem(hamburger, OrderItemSize.MEDIUM, 1)
        sandwichOrderItem = OrderItem(sandwich, OrderItemSize.MEDIUM, 1)
        cocaColaOrderItem = OrderItem(cocaCola, OrderItemSize.MEDIUM, 2)
        iceCreamOrderItem = OrderItem(iceCream, OrderItemSize.MEDIUM, 2)

		# created order with order items
        order = Order()
        order.getOrderItems().add(hamburgerOrderItem)
        order.getOrderItems().add(sandwichOrderItem)
        order.getOrderItems().add(cocaColaOrderItem)
        order.getOrderItems().add(iceCreamOrderItem)

		# execute method to be tested on test object
        totalOrderPrice = self.orderCalculatorMock.calculateTotalOrderAmount(order)

		# validate results (test output)
        self.assertEqual(12.0, totalOrderPrice)

    def testCalculateTotalOrderAmountVAT(self):
        totalOrderAmountVAT = self.orderCalculatorMock.calculateTotalOrderAmountVAT(12.0)
        self.assertEqual(1.44, totalOrderAmountVAT)

class OrderCalculatorKS_test(unittest.TestCase):

    # used setUp method from unittest to prepare the test
    # method executes 'before each' test method
    def setUp(self):
        self.orderCalculatorKS = OrderCalculators.OrderCalculatorKS()
    
    # created test method to test the vat rate amount detection
    def test_get_vat_rate(self):
        # execute method to test
        vatRate = self.orderCalculatorKS._getVATRate()

        # validate defined output
        self.assertEqual(vatRate, 0.18)

    # created test method to test the size rate amount detection
    def test_get_size_rate_amounts(self):
        # execute method to test for various order item sizes
        size_rate_amount_small = self.orderCalculatorKS._getSizeRateAmount(OrderItemSize.SMALL)
        size_rate_amount_medium = self.orderCalculatorKS._getSizeRateAmount(OrderItemSize.MEDIUM)
        size_rate_amount_large = self.orderCalculatorKS._getSizeRateAmount(OrderItemSize.LARGE)
        size_rate_amount_xxl = self.orderCalculatorKS._getSizeRateAmount(OrderItemSize.XXL)
        
        self.assertEqual(size_rate_amount_small, 0.7)
        self.assertEqual(size_rate_amount_medium, 1)
        self.assertEqual(size_rate_amount_large, 1.2)
        self.assertEqual(size_rate_amount_xxl, 1.25)

class OrderCalculatorGER_test(unittest.TestCase):

    # used setUp method from unittest to prepare the test
    # method executes 'before each' test method
    def setUp(self):
        self.orderCalculatorGER = OrderCalculators.OrderCalculatorGER()
    
    # created test method to test the vat rate amount detection
    def test_get_vat_rate(self):
        # execute method to test
        vatRate = self.orderCalculatorGER._getVATRate()

        # validate defined output
        self.assertEqual(vatRate, 0.19)

    # created test method to test the size rate amount detection
    def test_get_size_rate_amounts(self):
        # execute method to test for various order item sizes
        size_rate_amount_small = self.orderCalculatorGER._getSizeRateAmount(OrderItemSize.SMALL)
        size_rate_amount_medium = self.orderCalculatorGER._getSizeRateAmount(OrderItemSize.MEDIUM)
        size_rate_amount_large = self.orderCalculatorGER._getSizeRateAmount(OrderItemSize.LARGE)
        size_rate_amount_xxl = self.orderCalculatorGER._getSizeRateAmount(OrderItemSize.XXL)
        
        self.assertEqual(size_rate_amount_small, 0.8)
        self.assertEqual(size_rate_amount_medium, 1)
        self.assertEqual(size_rate_amount_large, 1.25)
        self.assertEqual(size_rate_amount_xxl, 1.3)

# running test using the unittest Test Runner
if __name__ == '__main__':
    unittest.main()