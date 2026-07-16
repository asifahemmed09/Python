"""
Write a function called discount_price that takes original_price
and discount_percent as parameters and prints the final
price after discount.
"""

def discount_price(price,discount):
    final_price = price - ( price * discount)
    print(final_price)

discount_price(250, 0.1)
