'''
number= int(input("enter an integer: "))
if number % 2 == 0:
    print( f" {number} is an even number.")
else:
    print( f" {number} is an odd number.")
'''

total_sum = 0
for number in range(1,51):
    total_sum += number
print("the sum of number form 1 to 50 is :",total_sum)
