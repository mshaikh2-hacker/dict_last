#user interface to the main menu
import data
import functions
def show_main_menu():
  order_items = list()
  while True:
    print("\nMusthak diner") #edit to show your name
    print("__________\n")
    print('Insert N for a new order')
    print('Insert X to close orders and print the check')
    print('Insert C to change the order')
    print('Insert D to check if your desired order is available')
    print('Insert M for manager mode')
    print('Insert Q to quit')
    print('Insert U for most sales items')
    user_menu_choice = input('Your choice: ')
    if user_menu_choice in 'Qq':
      break
    elif user_menu_choice in 'Xx':
      total = 0
      for i in range(len(order_items)):
        print(order_items[i][0],'x',order_items[i][1],'------',int(order_items[i][2])*int(order_items[i][0]))
        total += int(order_items[i][2])*int(order_items[i][0])
      print('Total amount to pay :', total)
    elif user_menu_choice in 'Nn':
      while True:
        quantity,item,price = make_order() #calls a function for adding to the orders
        print(quantity,'x',item)
        order_items.append([quantity,item,price])
        print('\nDo you want to add more items?')
        choice = input('Press "y" for YES and "n" for NO\n')
        if choice in "Yy":
          continue
        elif choice in "Nn":
          break
        else:
          print('invalid choice')
    elif user_menu_choice in 'Cc':
      if len(order_items) == 0:
        print("You haven't ordered anything yet")
      else:
        close_order(user_menu_choice.upper())
        order_items = []
    elif user_menu_choice in 'Dd':
      functions.customer_request()
    elif user_menu_choice in 'Mm':
      functions.manage()
    elif user_menu_choice in 'Uu':
        print('Do you want to show most sales items')
        desire = input('Press "y" for YES and "n" for NO\n')
        if desire in "Yy":
          continue
        elif desire in "Nn":
          break
    else:
      print('invalid choice')

      
def make_order():
  user_selection = functions.get_item_number()
  item_code, quantity = user_selection.split()
  if item_code not in data.drink_items and int(quantity)>data.menu_items[f'{item_code}'][2]:
    print('Sorry! we only have',data.menu_items[f'{item_code}'][2],'items left in stock, Please enter the quantity as per the stock.')
    quantity,product,price = make_order()
    if item_code not in data.drink_items and int(quantity)>data.menu_items[f'{item_code}'][2]:
      data.menu_items[item_code][2]-int(quantity)
      return quantity,product,price
  data.menu_items[item_code][2]-int(quantity)
  return quantity,functions.get_item_information(f'{item_code}')[0],functions.get_item_information(f'{item_code}')[1]

def close_order():
  print('Previous order was removed' )
  print('select N for new order')

if __name__ == '__main__':
    drinks = []
    appetizers = []
    salads = []
    entrees = []
    dessert= []
    show_main_menu()