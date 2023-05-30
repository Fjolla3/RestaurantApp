from BaseEnums import Location
import OrderCalculators

class OrderCalculatorFactory:
    def getOrderCalculatorByLocation(location):
        match(location):
            case Location.KOSOVO:
                return OrderCalculators.OrderCalculatorKS()
            case Location.GERMANY:
                return  OrderCalculators.OrderCalculatorGER()
            case _:
                raise Exception("Current location is invalid. OrderCalculator could not be determined.")