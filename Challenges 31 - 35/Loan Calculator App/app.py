from matplotlib import pyplot

def get_loan_info():
    # Dict
    loan = {}

    # Get values from user
    loan["Principal"] = float(input("\nEnter the loan amount: "))
    loan["Rate"] = float(input("Enter interest rate: "))
    loan["Rate"] = round(loan["Rate"] / 100, 2)
    loan["Monthly Payment"] = float(input("Enter the desired monthly payment amount: "))
    loan["Money Paid"] = 0
    return loan

def show_loan_info(loan_dict,month):
    print(f"\n----Loan information after {month} months----")
    for key, value in loan_dict.items():
        print(f"{key}: {value}")

def collect_interest(loan_dict):
    loan_dict["Principal"] += (loan_dict["Principal"] * loan_dict["Rate"] / 12) ## 12 months in a year

def make_monthly_payment(loan_dict):
    loan_dict["Principal"] -= loan_dict["Monthly Payment"]
    if loan_dict["Principal"] > 0:
        loan_dict["Money Paid"] += loan_dict["Monthly Payment"]
    else:
        loan_dict["Money Paid"] += loan_dict["Monthly Payment"] + loan_dict["Principal"]
        loan_dict["Principal"] = 0

def summarize_loan(loan_dict,month, initial_loan):
    print("\n----Loan Summary----")
    print(f"Congratulations! You paid off your loan in {month} months!")
    print(f"Your initial loan was ${initial_loan} at a rate of {loan_dict['Rate']*100}%.")
    print(f"You spent ${round(loan_dict['Money Paid'],2)} total.")
    
    interest = round(loan_dict["Money Paid"] - initial_loan, 2) 
    print(f"You spent ${interest} on interest!")

def create_graph(dataset,loan_amount):
    x_values = [] # Represents months
    y_values = [] # Represents principal loan

    for data in dataset:
        x_values.append(data[0])
        y_values.append(data[1])

    pyplot.plot(x_values,y_values)
    pyplot.title(f"{100 * loan['Rate']}% Interest with ${loan['Monthly Payment']} Monthly Payment")
    pyplot.xlabel("Month number")
    pyplot.ylabel("Principal of Loan")

    # Show graph
    pyplot.show()

# Main Code

print("Welcome to the Loan Calculator App!")

month_number = 0 # We start at month 0
loan = get_loan_info() # Get loan info from user
initial_loan = loan["Principal"] # Save the initial loan to use it later
data_to_plot = []

show_loan_info(loan,month_number) # Show loan info
input("Press 'Enter' to start paying your loan.")

while loan["Principal"] > 0:
    if loan["Principal"] > initial_loan:
        break           # Impossible to pay loan
    month_number += 1
    collect_interest(loan)
    make_monthly_payment(loan)
    data_to_plot.append((month_number, loan["Principal"]))
    show_loan_info(loan,month_number)

if loan["Principal"] <= 0: # Show loan summary
    summarize_loan(loan,month_number,initial_loan)
    create_graph(data_to_plot,loan)

else: # Show message
    print("\nYou will never be able to pay your loan!")
    print("You cannot go ahead of the interest! :'c")