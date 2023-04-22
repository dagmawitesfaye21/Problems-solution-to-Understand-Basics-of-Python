def Main(loan_year, loan_payment):
    interest_rate = 0.05
    increasing_rate = 0.00125

    total_months = 12*loan_year

    total = loan_payment
    for month in range(0,total_months):
        monthly = (total*interest_rate)
        total+=(monthly)
        print(f"interest rate {interest_rate*100}   Monthly {month} {monthly}  Total {total}")
        interest_rate+=increasing_rate

if __name__ == "__main__":
    print("Enter Loan Amount")
    loan_amount = int(input())
    print("Enter loan period")
    loan_period = int(input())
    Main(loan_period, loan_amount)