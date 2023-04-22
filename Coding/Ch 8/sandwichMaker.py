# Write your code here :-)
#import modules
import pyinputplus as pyin
#make menu
sandwichMenu = {'bread': {'wheat': 0.5, 'sour dough': 0.5, 'white': 0.0}, 'protein': {'chicken': 1.00, 'turkey': 0.50, 'ham': 0.0, 'tofu': 0.0}, 'cheese': {'cheddar': 0.0, 'swiss': 0.0, 'mozzarella': 0.5}, 'condiments': {'mayo': 0.5, 'mustard': 0.0, 'lettuce': 0.0, 'tomato': 0.0}}

#New order


#List
order = []
price = 4

print('Welcome to the Sandwich Shop! Let\'s get started on your order.')
# bread (3 options)
breadOrder = pyin.inputChoice(list(sandwichMenu['bread'].keys()))
order.append(breadOrder)
price += sandwichMenu['bread'][breadOrder]
# protein (four options)
print('Would you like some protein?')
proteinOrder = pyin.inputMenu(list(sandwichMenu['protein'].keys()))
order.append(proteinOrder)
price += sandwichMenu['protein'][proteinOrder]
# cheese (y/n)
print('Do you want cheese?')
cheeseYN = pyin.inputYesNo()
# if cheese, which type? (3 options)
if cheeseYN == 'yes':
    cheeseOrder = pyin.inputMenu(list(sandwichMenu['cheese'].keys()))
    order.append(cheeseOrder)
    price += sandwichMenu['cheese'][cheeseOrder]
# which condiments? (4 options)
for condiment in list(sandwichMenu['condiments'].keys()):
    print('Do you want %s?' % condiment)
    condimentYN = pyin.inputYesNo()
    if condimentYN == 'yes':
        order.append(condiment)
        price += sandwichMenu['condiments'][condiment]
# how many sandwiches (num)
print('How many sandwiches would you like?')
quantity = pyin.inputInt(min=0)

# display price
print('Great! It looks like we got everything we need for your order. Here is a confirmation.')
print(', '.join(order))
print('The price is: %i' % (price * quantity))
print('Does everything look right?')
confirmation = pyin.inputYesNo()
if confirmation == 'yes':
    print('Great! Your order will be right up.')
else:
    print('Sorry about that! Let\'s try that again')
