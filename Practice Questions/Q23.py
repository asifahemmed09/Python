"""
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * *
    * * * * *
      * * *
        *
"""


for i in range(1,6):
    for _ in range(1,6-i):
        print(" ", end=" ")
    for _ in range(1,i * 2):
        print("*", end=" ")
    print("\n")
for i in range(4, 0, -1):
    for _ in range(1, 6 - i ):
        print(" ", end=" ")
    for _ in range(1, i * 2):
        print("*", end=" ")
    print("\n")

