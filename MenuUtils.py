class MenuPrinter():

    def printMenu(self, menu):
        print("---------------MENU-----------------")
        menuItems = menu.getMenuItems()
        for key in menuItems:
            menuItem = menuItems[key]
            print(str(menuItem.getProductId()) + " . " + menuItem.getName() + " | " + str(menuItem.getPrice()) + " Euro ")
        print("------------------------------------")
