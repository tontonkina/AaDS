with open("input.txt")as f:
 a,b = map(int,f.read().split(" "))
 if all(-10**9 <=x<= 10**9 for x in [a,b] ):
  print(a+b)
  with open("output.txt", "a+")as f:
   f.write(str(a+b)+"\n")







