a = int(input(" Input a: "))
b = int(input(" Input b: "))
c = int(input(" Input c: "))

exist = a + b > c and a + c > b and c + b > a

result = exist and (a ** 2 + b ** 2 == c ** 2
                    or b ** 2 + c ** 2 == a ** 2
                    or a ** 2 + c ** 2 == b ** 2)

msg = " Is the triangle right angled?"
msg += "\n" + ("Yes, the triangle with sides is right angled."
               if result else "No,the triangle with sides isn't right angled.")

print(msg)
