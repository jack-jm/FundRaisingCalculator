# Import libraries


# Functions go here
# Checks that input is either an integer or float. 
def num_check(question, error, num_type):
  valid = False
  while not valid:
    try:
      response = num_type(input(question))
      if response <= 0:
        print(error)
      else:
        return response
    
    except ValueError:
      print(error)

def yes_no(question):
  to_check = ["yes", "no"]
  
  valid = False
  while not valid:
    response = input(question).lower()
    
    for var_item in to_check:
      if response == var_item:
       valid = True
       return response
      elif response == var_item[0]:
       valid = True
       return var_item

    print("Please enter either yes or no.")

# Main routine goes here

want_help = yes_no("Do you want to read the instructions? ")
print("You said {}".format(want_help))

# Gets number of items
get_int = num_check("How many do you need? ", "Please enter an integer/whole number that is more than zero.\n", int)

# Gets cost
get_cost = num_check("How much does it cost? $", "Please enter a number more than zero.\n", float)

print("You need: {}".format(get_int))
print("It costs ${}".format(get_cost))