a = int(input("Enter first number: "));
b = int(input("Enter Second Number: "));
c = int(input("Enter Third Number: "));
if a>=b and a>=c:
    largest = a
elif b>=a and b>=c:
    largest = b
else:
    largest = c
print("Largest Number is: ",largest)


