a= int(input( " Input a: "))
b= int(input( " Input b: "))
c= int(input( " Input c: "))

exist = all((a + b > c,a + c > b, c + b > a))

result = exist and (a == b or b == c or c == a)

msg= " Is the triangle isosceles?"
msg += "\nAnswer:" + str(result)

print (msg)