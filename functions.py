#this module will be where most functionality will be stored
#create your def blocks for the assignment in this module
#Use this  function that will return the item name and price for a given item code
# for example, find_menu_item('D2') should return Lemonade, and integer 3 as the result
import data
def get_item_information(item_code):
  """ this  function that will return the item name and price for a given item code.
    For example, find_menu_item('D2') should return Lemonade, and integer 3 as the result """
  if item_code in data.menu_items:
      item = str(item_code)
      return data.menu_items[item]

def display_items():
  pass

def get_item_number():
  while True:
    print('Drinks', [d.replace('\u200b','') for d in data.menu_items if d[0] == 'D'])
    print('Appetizers', [d.replace('\u200b','') for d in data.menu_items if d[0] == 'A'])
    print('Salads', [d.replace('\u200b','') for d in data.menu_items if d[0] == 'S'])
    print('Entrees', [d.replace('\u200b','') for d in data.menu_items if d[0] == 'E'])
    print('Deserts', [d.replace('\u200b','') for d in data.menu_items if d[0] == 'T'])

    order_item = input('Enter dish number and quantity: ')
    if order_item.split()[0].upper() in data.all_items:
      return order_item
    else:
      print('Invalid dish number. Please try again')

def manage():
  while True:
    print("\nHello Manager") #edit to show your name
    print("__________\n")
    print('Insert R to remove an item')
    print('Insert A to add an item')
    print('Insert D to change decription of an item')
    print('Insert S to update stock number of an item')
    print('Insert P to update price of an item')
    print('Insert Q to quit')
    user_menu_choice = input('Your choice: ')
    if user_menu_choice in 'Rr':
      remove_choice = input('Enter the dish number of item  you want to remove: ')
      data.menu_items.pop(remove_choice)
      print(data.menu_items)
    elif user_menu_choice in 'Aa':
      dish_number = input('Enter dish number: ')
      desc = input('Enter dish description: ')
      cost = input('Enter dish price: ')
      stock = input('Enter dish stock number: ')
      data.menu_items[str(dish_number)] = list()
      data.menu_items[str(dish_number)].append(str(desc))
      data.menu_items[str(dish_number)].append(int(cost))
      data.menu_items[str(dish_number)].append(int(stock))
      print(data.menu_items)
    elif user_menu_choice in 'Dd':
      number = input('Enter the number of the dish you want to change the description of: ')
      desciption = input('Enter description: ')
      data.menu_items[number][0] = str(desciption)
      print(data.menu_items)
    elif user_menu_choice in 'Ss':
      number = input('Enter the number of the dish you want to change the stock of: ')
      stock_num = input('Enter new stock details: ')
      data.menu_items[number][2] = int(stock_num)
      print(data.menu_items) 
    elif user_menu_choice in 'Pp':
      number = input('Enter the number of the dish you want to change the price of: ')
      price = input('Enter new price: ')
      data.menu_items[number][1] = int(price) 
      print(data.menu_items)
    elif user_menu_choice in 'Qq':
      break
    else:
      print('Invalid choice')

def customer_request():
     desired_item = input('Enter your desired order: ')
     quantity = input('Enter Quantity')
     dish_number = 0
     for i in data.menu_items:
        dish_number += 1
        #print(data.menu_items[i][0])
        #print(str(desired_item).upper())
        if data.menu_items[i][0] == str(desired_item).upper() and int(quantity)>data.menu_items[i][2]:
          print('we have what you ordered, but we only have',data.menu_items[i][2],'items in the stock')
          print('Please dplace order as per the stock')
        elif data.menu_items[i][0] == str(desired_item).upper() and int(quantity)<=data.menu_items[i][2]:
          print('Great! we have what you ordered.')
          print("Dish number is",i)
          dish_number = i
          break
        elif dish_number == len(data.menu_items):
          print('Sorry! we do not have what you ordered')