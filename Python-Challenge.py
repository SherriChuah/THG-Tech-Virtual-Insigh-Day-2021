# class colour
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


whey_protein = 8.99
protein_bar = 1.50
workout_leggings = 42.00
mp_t_shirt = 15.00
multivitamin_tablets = 7.99
cycling_shorts = 19.99
shaker = 5.00
pre_workout = 39.99
sugar_free_syrup = 6.49
protein_spread = 6.99

def total_order_price_after_discount(total):
  return total * (85/100)

print("Welcome to THG!")

products_price = [whey_protein, protein_bar, workout_leggings, mp_t_shirt, multivitamin_tablets, cycling_shorts, shaker, pre_workout, sugar_free_syrup, protein_spread]
products = ["Whey Protein", " Protein Bar ", "Workout Leggings", "MP T Shirt", "Multivitamin Tablets", "Cycling Shorts", "Shaker", "Pre Workout", "Sugar Free Syrup", "Protein Spread"]

menu = """
              Menu
  1.  Whey Protein          8.99  
  2.  Protein Bar           1.50
  3.  Workout Leggings      42.00
  4.  MP T Shirt            15.00
  5.  Multivitamin Tablets  7.99
  6.  Cycling Shorts        19.99
  7.  Shaker                5.00
  8.  Pre Workout           39.99
  9.  Sugar Free Syrup      6.49
  10. Protein Spread        6.99
  """
comfirmation = 'yes'

total_order = 0

while (comfirmation == 'yes' or comfirmation == "Yes"):
  print(bcolors.HEADER + menu + bcolors.ENDC)

  product_no = input("What would you like to order? enter number ")

  if (product_no.isnumeric() == False or int(product_no) > 10 or int(product_no) < 1):
  	print("Invalid product number")
  	continue

  product_no = int(product_no)

  print(bcolors.OKCYAN + products[product_no - 1] + " has been added to the cart\n" + bcolors.ENDC)
  total_order += products_price[product_no - 1]

  valid = False
  while not valid:
  	comfirmation = input(bcolors.BOLD + "Buy more? (yes/no) " + bcolors.ENDC)
  	if (comfirmation == "yes" or comfirmation =="Yes" or comfirmation == "no" or comfirmation == "No"):
  		valid = True
  	else:
	  	print(bcolors.WARNING + "Invalid statement" + bcolors.ENDC)

print(bcolors.OKBLUE + "\nThank you for buying with us! Your total order after discount is " + str(total_order_price_after_discount(total_order)) + bcolors.ENDC)