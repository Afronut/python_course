from time import sleep
# n = 5
# while n > 0:
#     print(n)
#     n = n - 1
# print('Blastoff!')

n = 1

while True:
    n = n - 1
    if n%3==0:
        continue
    print(n) 
    sleep(1)
print('Done!')
# while True:
#     print("Entrez 'q' pour quiter")
#     num=input("Enter un nombre: ")
#     if num=='c':
#         break
#     num=float(num)
#     print(num)
# print('Done')