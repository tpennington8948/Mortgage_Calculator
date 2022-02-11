# Mortgage affordability calculations
# Uses input from user to calculate either payment based off inputs or loan amount for inputted payment information
# If down payment is less than 20% then give a warning to user about PMI not being included in calculation for payment

# Welcome statement for user.

print('''Welcome to the mortgage affordability calculator pro!
         You can use this program to calculate an estimated monthly mortgage payment based off your inputs.
                                                    "OR"
         The total price of house you can afford based off the monthly payment you are wanting.

         Before we get started let's take some time to make sure we have all of the needed information ready...
         You are going to need:
             1. Either your desired monthly payment or price of house you are looking to purchase
             2. Estimated length of mortgage (typically 15 or 30 years)
             3. Estimated annual interest rate
             4. Estimated annual property tax for the home you are pricing or area you are looking to purchase in
             5. Estimated annual homeowners insurance

        Once you have all of this ready we are ready to start!
        Our first step is to decide which type of calculation we are going to be doing:''')

# Choice of calculation type

choice = input("""
If you know your house price and want to figure out your monthly payment type 'mortgage'. 
If you know your target payment and want to figure out your house price type 'house'
""")

while choice != 'mortgage' and choice != 'house':
  choice = input("Whoops, it looks like you didn't choose 'mortgage' or 'house'. Try selecting one again! ")

if choice == 'mortgage':
    print("Great! You selected to calculate your estimated mortgage payment. First let's start with some details...")
    house_price = int(input("What is the purchase price of the house you are planning to purchase?  "))
else:
    print("Great! You selected to calculate your house price. First let's start with some details...")
    mortgage_pymt = int(input("What is your target monthly mortgage payment?    "))

# Gathering information (Look at adding in validations for individual inputs in the future)

down_pay_input = input("Enter the amount, in dollars, you are planning to use as a down payment:   ")#
mort_len_input = input("Enter the length of your mortgage in number of years (ex. 30):   ")
interest_input = input("Enter the interest rate (ex. 3.87): ")
prop_tax_input = input("Enter your estimated annual property tax (ex. 6500):   ")
insur_input = input("Enter your estimated annual homeowners insurance premium (ex. 1500):   ")

# Moving the information into the correct types and applying calculations

down_payment = int(down_pay_input)
mortgage_length = int(mort_len_input) * 12
interest_rate = round((float(interest_input) / 100) / 12, 4)
property_tax = round(int(prop_tax_input) / 12, 0)
insurance = round(int(insur_input) / 12, 0)
escrow = round(property_tax + insurance, 0)

if choice == 'mortgage':
    house_price_calc = round(house_price - down_payment, 2)
    prin_int = round(house_price_calc * ((interest_rate * (1 + interest_rate) ** mortgage_length) / ( (1 + interest_rate) ** mortgage_length -1)), 2)
    total_payment = round(prin_int + escrow, 2)
else:
    payment_no_escrow = round(mortgage_pymt - escrow, 2)
    house_afford = round((payment_no_escrow / ((interest_rate * (1 + interest_rate) ** mortgage_length) / ( (1 + interest_rate) ** mortgage_length -1))) + down_payment, 2)

# Returning recap of information entered and result

if choice == 'mortgage':
    mortgage_output = """
Based on the information you provided your monthly principal and interest payment would be ${p}. 
Your monthly escrow payment would be ${e}. 
Your total monthly mortgage payment would be ${t}
 
 """.format(p = prin_int, e = escrow, t = total_payment)

if choice == 'house':
    house_price_output = """
Based on your monthly payment target of ${pay}, your down payment of ${down}, and a monthly escrow amount of ${escrow}, your target house price should be ${price}.  

""".format(pay = mortgage_pymt, down = down_payment, escrow = escrow, price = house_afford)

if choice == 'mortgage':
    print(mortgage_output)
    while down_payment < (house_price * .2):
        print('The down payment that you entered is less than 20% of the purchase price of the home. You may incur an additional monthly cost of private mortgage insurance (PMI) that is not included in this calculation.')
        break
else:
    print(house_price_output)
    while down_payment < (house_afford * .2):
        print('The down payment that you entered is less than 20% of the purchase price of the home. You may incur an additional monthly cost of private mortgage insurance (PMI) that is not included in this calculation.')
        break


