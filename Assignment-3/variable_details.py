# Write a program to display data type, memory address, size in byte of varibale entered by the user

import sys
#Accept value from user
x = input("Enter the value: ")

#Display data type
print("Data Type: ", type(x))

#Display Memory Address
print("Memory Address: ", id(x))

#Display size in byte
print("Size in byte: ", sys.getsizeof(x))