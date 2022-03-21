
# import time
# # While loop
# i = 1
# while i <= 10:
#     print(i * '*')
#     i += 1

# # for loop
# numbers = [1, 2, 3, 4, 5]
# for item in numbers:
#     print(item)


# for seconds in range(10, 0, -1):
#     print(seconds)
#     time.sleep(1)

# print("Happy New Year!")

# # nested loops
# rows = int(input("How many rows? "))
# colums = int(input("How many colums? "))
# symbol = input("Enter a symbol to use: ")

# for i in range(rows):
#     for j in range(colums):
#         print(symbol, end="")
#     print()

# Loop control statements = change a loops execution from its normal sequence

# break =       used to terminate the loop entirely
# continue =    skips to the next iteration of the loop
# pass =        does nothing, acts as a placeholder

# while True:
#     name = input("Enter your name:")
#     if name != "":
#         break

# phone_number = "123-456-7890"

# for i in phone_number:
#     if i == "-":
#         continue
#     print(i, end="")

# for i in range(1,21):
#     if i == 13:
#         pass
#     else:
#         print(i)