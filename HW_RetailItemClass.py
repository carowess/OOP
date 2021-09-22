
class RetailItem:

    def __init__(self, d, u, p):
        self.__description = d
        self.__units = u
        self.__price = p

    def set_description(self, desc):
        self.__description = desc

    def set_units_in_inv(self, units):
        self.__units = units

    def set_unit_price(self,price):
        self.__price = price

    def get_description(self):
        return self.__description
    
    def get_units_in_inv(self):
        return self.__units

    def get_unit_price(self):
        return self.__price



    