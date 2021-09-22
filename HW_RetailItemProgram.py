
import HW_RetailItemClass as ri

def main():

    item1 = ri.RetailItem('Jacket',12,59.95)
    item2 = ri.RetailItem('Designer Jeans',40,34.95)
    item3 = ri.RetailItem('Shirt',20,24.95)

    #item_search = print(input('Enter item description: '))

    print()
    print('Item #1:')
    print('Item description:', item1.get_description())
    print('Units in Inventory:', item1.get_units_in_inv(),'units')
    print('Unit Price:', ("${:,.2f}".format(item1.get_unit_price())))
    print()
    print('Item #2:')
    print('Item description:', item2.get_description())
    print('Units in Inventory:', item2.get_units_in_inv(),'units')
    print('Unit Price:', ("${:,.2f}".format(item2.get_unit_price())))
    print()
    print('Item #3:')
    print('Item description:', item3.get_description())
    print('Units in Inventory:', item3.get_units_in_inv(),'units')
    print('Unit Price:', ("${:,.2f}".format(item3.get_unit_price())))

main()


