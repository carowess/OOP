import InsectClass as i

#this is creating an instance of the insect class

mosquito = i.Insect(2,4)
housefly = i.Insect(2,4)
#usually these would be inputs from user^^

mosquito.flight_length()
housefly.flight_length()



print("The insect can fly up to",str(housefly.flight_length()),"miles.")
print('The housefly can fly up to', str(mosquito.get_miles()), 'miles.')

