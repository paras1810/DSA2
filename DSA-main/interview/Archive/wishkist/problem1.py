def required_starting_amount(earnings_expenses):
    balance = 0
    min_balance = 0
    
    for daily_change in earnings_expenses:
        balance += daily_change
        if balance<0:
            required = -1*balance+1
            min_balance = max(required, min_balance)
    return min_balance

# Example usage:
earnings_expenses = [-4, -2, -3]
required_amount = required_starting_amount(earnings_expenses)
print("Required starting amount:", required_amount)
