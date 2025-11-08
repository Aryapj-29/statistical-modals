numbers = []
n = int(input("Enter how many numbers: "))

for i in range(n):
    num = float(input(f"Enter number{i+1}:"))
    numbers.append(num)
mean = sum(numbers) / len(numbers)
print("Mean = :",mean)
