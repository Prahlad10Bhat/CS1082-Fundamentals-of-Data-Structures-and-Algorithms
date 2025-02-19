#SUM OF SERIES:
def sum(n):
  if (n==0):
    return 0
  s=num%10
  return(s+sum(n/10))
n=int(input("Enter value of n: "))
print (sum(n))
