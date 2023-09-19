# even_numbers = []
# for i in range(1, 101):  # You can adjust the range as needed
#     if i % 2 == 0:
#         even_numbers.append(i)

# print(even_numbers)

import time
A = []

# Step 2 and 3: Continuously receive input and add it to the list
while True:
    bolaji = int(input("Enter a value (or '-1' to quit): "))
    # Check if the user wants to quit (you can use any condition you like)
    if bolaji == -1:
        break  # Exit the loop if the user enters 'b'
    
    # Add the input to the list A
    A.append(bolaji)
# Print the final list A
print("List A:", A)

for i in A:
    if (i) % 2 == 0:
        print(i)
    time.sleep(1)
