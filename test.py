listLegnth = int(input("Enter the amount of numbers: "))
numbers = []

for nums in range(listLegnth):
    num = int(input("Enter a number: "))
    numbers.append(num)

target = int(input("Enter the sum: "))
result = set({})
    
for num1 in range(listLegnth - 1):
    for num2 in range(listLegnth - 1):
        if numbers[num1] + numbers[num2] == target:
            result.add(num1)
            result.add(num2)
            
result = list(result)
print(result)