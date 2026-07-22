"""
Clean Phone Number

Take a phone number as input in the format +91-98765-43210. Remove all dashes
and the country code. Print the cleaned 10-digit number.
"""

phone_number = input("Enter your phone number with country code: ")
cleaned_number_list = phone_number.split("-")[1:]
cleaned_number = "".join(cleaned_number_list)
print(cleaned_number)
