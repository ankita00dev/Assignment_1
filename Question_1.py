total_number = 50 
n1, n2 = 0, 1
count = 0
if total_number <= 0:
   print("Please enter a positive integer")
elif total_number == 1:
   print("Fibonacci sequence upto",total_number,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   while count < total_number:
       print(n1)
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1