import fun
ch=int(input("enter /n 1. add /n 2.sub /n 3.multiply /n 4. divide"))
a=int(input("enter number:"))
b=int(input("enter number:")) 
if(ch==1):
      x=fun.add(a,b)
      print(x)
if(ch==2):
      x=fun.sub(a,b)
      print(x)
if(ch==3):
      x=fun.mul(a,b)
      print(x)
if(ch==4):
      x=fun.div(a,b)
      print(x)
else:
      print("operation not valid!")