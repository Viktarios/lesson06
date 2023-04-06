a = int(input(" Input a: "))
b = int(input(" Input b: "))
c = int(input(" Input c: "))

result = a == b and b == c

msg = " Is the triangle equilateral?"
msg += "\nAnswer:" + str(result)

print(msg)
