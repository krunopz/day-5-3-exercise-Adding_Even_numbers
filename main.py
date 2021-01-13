#Write your code below this row 👇

sum=0
for i in range(0,101,2):
  sum+=i
print(f"Sum of all even numbers from 0 to 100 is equal to {sum}\n")

min_max=input("If you want to sum all \n even numbers from between two other numbers,\n input lower and upper border of range: ").split()

for num in range(0,len(min_max)):
  min_max[num]=int(min_max[num])
print(min_max)
sum_user=0
for i in range(min_max[0],min_max[1],2):
  sum_user+=i
print(f"Sum of all even numbers between {min_max[0]} and {min_max[1]} is equal to {sum_user}")



