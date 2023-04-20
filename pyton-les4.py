# fizz-buzz

fizz = int(input('Введіть число fizz\n'))
buzz = int(input('Введіть число buzz\n'))
num = int(input('Введіть число num\n'))

for i in range(1, num+1):
   if not i%fizz and not i%buzz:
        print("FB", end=" ")
   elif not i%fizz  and i%buzz:
        print("F", end=" ")
   elif i%fizz  and not i%buzz:
        print("B", end=" ")
   else :
        print(i, end=" ")    

