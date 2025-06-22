
numbers=[]

for i in range(5):
    number=input("Number: ")
    numbers.append(number)

print(f"The first number is {numbers[0]}")
print(f"The last number is {numbers[-1]}")
print(f"The smallest number is {min(numbers)}")
print(f"The largest number is {max(numbers)}")
average_number=sum(numbers)/len(numbers)
print(f"The average of the numbers is {average_number:.1f}")