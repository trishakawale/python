customer_no=int(input("EnterCustomer Number: "));
units = int(input("Enter the unit consumed: "));
if units <=100:
    bill=units*1;
elif units<=300:
    bill = 100+(units-100)*1.25;
elif units<=500:
    bill= 350+(units-500)*1.50;
else:
    bill= 650+(units-500)*1.75;
print("Electricity bill")
print("Customer Number: ",customer_no);
print("Units Consumed: ",units);
print("Amount to be paid: ",bill);