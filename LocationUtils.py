import BaseEnums

class LocationManager:
    
    @staticmethod
    def getLocationFromString(locationAsString):
            for location in BaseEnums.Location:
                if location.name == locationAsString:
                    return location
            raise Exception("No location could be found for given location parameter.")