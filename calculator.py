def find_operator(str1):
  add="+"
  sub="-"
  mult="*"
  div="/"
  mod="%"
  for i in range(0,len(str1)+1):
    if str1[i] == add:
      return "addition"
    elif str1[i] == sub:
      return "subtraction"
    elif str1[i] == mult:
      return "multiplication"
    elif str1[i]==div:
      return "division"
    elif str1[i]==mod:
      return "modulus"
def do_operation(x):
  for i in range(len(x)):
    if x[i]=="+" or  x[i]=="-" or  x[i]=="*" or  x[i]=="/" or x[i]=="%":
      l=i
      ans1=int(x[0:l])
      ans2=int(x[l+1:])
      if find_operator(x)=="addition":
        return ans1+ans2
      elif find_operator(x)=="subtraction":
        return ans1-ans2
      elif find_operator(x)=="multiplication":
        return ans1*ans2
      elif find_operator(x)=="division":
        # if ans1<ans2:
        #   return "small number"
        # else:
        return ans1/ans2
      elif find_operator(x)=="modulus":
        return ans1%ans2
x=input("Enter the expression")
print("your result:",do_operation(x))