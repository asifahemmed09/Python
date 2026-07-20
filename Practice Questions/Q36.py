"""
Create a list of 5 of your favourite movies. Print the first, last, and middle movie
from your list using both positive and negative indexing where appropriate.
"""

movies = ["Terminator","Avatar","Fast & Furious","Most Wanted","Sherlock Homes"]

first_movie = movies[0]
last_movie = movies[-1]
length = len(movies)
middle_movie = movies[(length -1) // 2]

print(f"First Movie: {first_movie}")
print(f"Last Movie: {last_movie}")
print(f"Middle Movie: {middle_movie}")
