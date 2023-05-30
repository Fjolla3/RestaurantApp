from BaseModel import Restaurant
from BaseModel import Client
from BaseModel import Menu
from OrderUtils import OrderPrinter
from OrderUtils import OrderManager
from MenuUtils import MenuPrinter
from LocationUtils import LocationManager
from CalculatorUtils import OrderCalculatorFactory

class RestaurantApp:

    __currentLocation = None

    def start(self, applicationMode, locationAsString):

        self.__currentLocation = LocationManager.getLocationFromString(locationAsString)

        match applicationMode:
            case "ORDER":
                self.runOrderProcess()
                return
            case "TABLE_RESERVATION":
                self.runTableReservationProcess()
                return
            case _:
                raise Exception("No valid application mode selected!")
                
    def runOrderProcess(self):
        restaurant = Restaurant("Route 66", "Te Heroinat, Prishtine")
        client = Client("James Gosling", "+38343123456")

        menu = Menu()
        menuPrinter = MenuPrinter()
        menuPrinter.printMenu(menu)

        orderManager = OrderManager()

        order = orderManager.createOrder(menu)
        orderManager.getOrders().append(order)

        self.calculateAndPrintOrderDetails(restaurant, client, order)

    def calculateAndPrintOrderDetails(self, restaurant, client, order):
        orderCalculator = self.getOrderCalculator()
        orderAmount = orderCalculator.calculateOrderAmount(order)
        
        orderPrinter = OrderPrinter()
        orderPrinter.printOrderInfo(restaurant, client, order, orderAmount, orderCalculator.getVATRate(False))

    def getOrderCalculator(self):
        return OrderCalculatorFactory.getOrderCalculatorByLocation(self.__currentLocation)

    def runTableReservationProcess(self):
       print("Table reservation completed successfully.")


restaurantApp = RestaurantApp()
restaurantApp.start("ORDER", "GERMANY")