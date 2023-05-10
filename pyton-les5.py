#
import sys

print(sys.argv)

print("-01---------------------------------")

#a = [10, 20, 30, 40]
#for id, item in enumerate(a):
#    print(id, item, "\t")
   
print("-02---------------------------------")

#filename = sys.argv[0]
#f = open(filename, 'r') 

#for line in f: 
#	print(line, end='')
#f.close() 

print("-03--------------------------------")

#filename = sys.argv[0]
#f = open(filename, 'r') 

#for line in f: 
#	text = line[::-1]
#	print(text, end='')
#f.close() 

print("-04---Bank-------------------------")

sum = int(input('Введіть потрібну суму\n'))
nominal = [1000, 500, 200, 100, 50, 20, 10]

if(sum<10 and sum%10 != 0):
    print("Ви ввели некоректну суму")
else:
    for nom in nominal:
        kilist = sum//nom
        if (kilist>0):
            print("Кількість купюр номіналом " + str(nom) + " = " + str(kilist))
            sum -= kilist*nom
        if (sum==0):
            break

print("-05------------------------------------") #Не можу зрозуміти у чому помилка

f = open("c:/OpenServer/domains/pyton2/5.txt", 'r') 
t = open("c:/OpenServer/domains/pyton2/5-1.txt", 'w') 
 

for line in f: 
    print("\n", line, "\n", end='')
    fizz = int(line[0]) 
    buzz = int(line[1]) 
    num = int(line[2]) 

    for i in range(1, num+1):
        if not i%fizz and not i%buzz:
            print("FB", end=" ")
            t.write("FB", end=" ")
        elif not i%fizz  and i%buzz:
            print("F", end=" ")
            t.write("F", end=" ")
        elif i%fizz  and not i%buzz:
            print("B", end=" ")
            t.write("B", end=" ")
        else :
            print(i, end=" ")
            t.write(i, end=" ")   
        t.write("\n") 

f.close() 
t.close() 



print("-05---Bank2-------------------------")  # Не розібрався в цій задачи

#sum = int(input('Введіть потрібну суму\n'))
#nominal = [10, 20, 50, 100, 200, 500, 1000]

#if(sum<10 and sum%10 != 0):
#    print("Ви ввели некоректну суму")
#else:
#    for id, nom in enumerate(nominal):
#        kilist=0
#        for i in range(1, 11):
#            if(sum!=0 and nominal[id+1]%sum==0):
#                kilist+=1
#                sum-=nom
#            else:
#                break
#        print("Кількість купюр номіналом " + str(nom) + " = " + str(kilist)) 
#        kilist=0

        




