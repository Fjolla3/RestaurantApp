class Restaurant:

    def __init__(self, name, address):
        self.__name = name
        self.__address = address

    def getName(self):
        return self.__name

    def getAddress(self):
        return self.__address
    
    def setName(self, name):
        self.__name = name
    
    def setAddress(self, adress):
        self.__address = adress

class Client:

    def __init__(self, name, phoneNr):
        self.__name = name
        self.__phoneNr = phoneNr

    def getName(self):
        return self.__name

    def getPhone(self):
        return self.__phoneNr
    
    def setName(self, name):
        self.__name = name
    
    def setPhone(self, phoneNr):
        self.__phoneNr = phoneNr
    
class Product:

    def __init__(self, name, productId, price):
        self.__name = name
        self.__productId = productId
        self.__price = price

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getProductId(self):
        return self.__productId

    def setProductId(self, productId):
        self.__productId = productId

    def getPrice(self):
        return self.__price

    def setPrice(self, price):
        self.__price = price

class Meal(Product):

    def __init__(self, name, productid, price, description=""):
        super().__init__(name, productid, price)
        self.description = description

    def setDescription(self, description):
        self.description = description

    def setDescription(self):
        return self.description

class Drink(Product):

    def __init__(self, name, productid, price, sugarFree):
        super().__init__(name, productid, price)
        self.sugarFree = sugarFree

    def setsugarFree(self, sugarFree):
        self.sugarFree = sugarFree

    def setsugarFree(self):
        return self.sugarFree

class Order:

    def __init__(self):
        self.orderItems = [] 

    def getOrdersItems(self):
        return self.orderItems

class OrderAmount:

    def __init__(self, totalOrderAmount, totalOrderAmountVAT, totalOrderAmountWithVAT):
        self.__totalOrderAmount = totalOrderAmount
        self.__totalOrderAmountVAT = totalOrderAmountVAT
        self.__totalOrderAmountWithVAT = totalOrderAmountWithVAT

    def getTotalOrderAmount(self):
        return self.__totalOrderAmount
    
    def getTotalOrderAmountVAT(self):
        return self.__totalOrderAmountVAT
    
    def getTotalOrderAmountWithVAT(self):
        return self.__totalOrderAmountWithVAT

    def setTotalAmount(self, totalOrderAmount):
        self.__totalOrderAmount = totalOrderAmount
    
    def setTotalOrderAmountVAT(self, totalOrderAmountVAT):
        self.__totalOrderAmountVAT = totalOrderAmountVAT
    
    def setTotalOrderAmountWithVAT(self, totalOrderAmountWithVAT):
        self.__totalOrderAmountWithVAT = totalOrderAmountWithVAT

class OrderItem:
  
    def __init__(self, product, orderItemSize, quantity):
        self.__product = product
        self.__orderItemSize = orderItemSize
        self.__quantity = quantity
    
    def getProduct(self):
        return self.__product

    def getorderItemSize(self):
        return self.__orderItemSize

    def getQuantity(self):
        return self.__quantity

    def setProduct(self, product):
        self.__product = product

    def setorderItemSize(self, orderItemSize):
        self.__orderItemSize = orderItemSize

    def setQuantity(self, quantity):
        self.__quantity = quantity

    def getOrderItemPrice(self):
        return self.__orderItemPrice

    def setOrderItemPrice(self, orderItemPrice):
        self.__orderItemPrice = orderItemPrice

class Menu:        

    def __init__(self):
        self.__menuItems = dict({}) 
        self.__initializeMenuProducts()

    def __initializeMenuProducts(self):
        self.__menuItems.update({100: Meal("Hamburger", 100, 4.5, "")})
        self.__menuItems.update({101: Meal("Cheeseburger", 101, 5, "")})
        self.__menuItems.update({102: Meal("Sandwich", 102, 3.5, "")})
        self.__menuItems.update({103: Meal("Hotdog", 103, 3, "")})
        self.__menuItems.update({104: Meal("Pizza", 104, 6, "")})
        self.__menuItems.update({105: Meal("Fries", 105, 2, "")})
        self.__menuItems.update({200: Drink("Coca Cola", 200, 1, False)})
        self.__menuItems.update({201: Drink("Coca Cola Zero", 201, 1, True)})
        self.__menuItems.update({202: Drink("Fanta", 202, 1, False)})
        self.__menuItems.update({203: Drink("Sprite", 203, 1, False)})
        self.__menuItems.update({204: Drink("Red Bull", 204, 2, False)})
        self.__menuItems.update({205: Drink("Coffee", 205, 0.5, False)})
        self.__menuItems.update({300: Meal("Ice cream", 300, 1)})
        self.__menuItems.update({301: Meal("Waffle", 300, 2.5)})
        self.__menuItems.update({302: Meal("Brownie", 300, 1.5)})

    def getMenuItems(self):
        return self.__menuItems