def collatz(a):
 while a!=1: 
  if a%2==0:
   print("a =",a)
   a/=2
  else:
   print("a =",a)
   a=(3*a)+1
 print("a =",a)