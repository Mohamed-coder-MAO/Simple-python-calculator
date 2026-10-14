import math
x=float(input("you want inter 1 or 2 numbers"))
if x == 1:
    y=float(input("tab number"))
    o=str(input("choose (sqrt)(sin)(cos)(tan)"))
    if o=='sqrt':
     print(math.sqrt(y))
    elif o =='sin':
     print(math.sin(y))
    elif o=='cos':
     print(math.cos(y))
    elif o=='tan':
     print(math.tan(y))
if x == 2:
    x , c=map(float, input("tab 2 numbers").split())
    operation=str(input("choose(/)(*)(+)(-)(sqrt)(sin)(cos)(tan)"))
    if operation == '*':
     print(x*c)
    if operation == '/':
      if c !=0:
       print(x/c)
      elif c ==0:
       print("error")
    if operation =='+':
        print(x+c)
    if operation == '-':
        print(x-c)
    if operation=='sqrt':
       v=str(input("what do you want do with numbers (+)(-)(*)(/)"))
       if v == '*':
            print(math.sqrt(x*c))
       if v == '/':
             if c !=0:
              print(math.sqrt(x/c))
             elif c ==0:
              print("error")
       if v=='+':
               print(math.sqrt(x+c))
       if v == '-':
               print(math.sqrt(x-c))
    if operation=='sin':
       v=str(input("what do you want do with numbers (+)(-)(*)(/)"))
       if v == '*':
          print(math.sin(x*c))
       if v == '/':
            if c !=0:
             print(math.sin(x/c))
            elif c ==0:
              print("error")
       if v=='+':
           print(math.sin(x+c))
       if v == '-':
           print(math.sin(x-c))
    if operation=='cos':
      v=str(input("what do you want do with numbers (+)(-)(*)(/)"))
      if v == '*':
        print(math.cos(x*c))
      if v == '/':
        if c !=0:
          print(math.cos(x/c))
        if c ==0:
          print("error")
      if v=='+':
       print(math.cos(x+c))
      if v == '-':
        print(math.cos(x-c))
    if operation=='tan':
       v=str(input("what do you want do with numbers (+)(-)(*)(/)"))
       if v == '*':
         print(math.tan(x*c))
       if v == '/':
         if c !=0:
          print(math.tan(x/c))
         if c ==0:
           print("error")
       if v=='+':
         print(math.tan(x+c))
       if v == '-':
          print(math.tan(x-c))
elif x>2:
   print("i say 1 or 2 only")