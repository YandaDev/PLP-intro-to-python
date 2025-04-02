# Function to calculate discount
def calculate_discount(price, discount_percent):
   if discount_percent >= 20:
      discount_amount = price * (discount_percent / 100)
      return price - discount_amount
   else:
      return price

# Get user input
original_price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

# Calculate final price
final_price = calculate_discount(original_price, discount_percent)

print(f"Final price is: {final_price:.2f}")