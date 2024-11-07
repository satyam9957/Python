# # n = int(input('Enter the Number: '))

# # for i in range(2, n):
# #     if(n%i) == 0:
# #         print("Not prime")
# #         break
# # else:
# #     print("this is prime")

# # sum of first natural number

# # m = int(input("Enter the number: "))
# # i = 1
# # sum = 0
# # while(i<=m):
# #     sum += i 
# #     i+=1

# # print(sum)

# for i in range (1,6):
#     print(i*'*')
#     i +=1

# i = 0
# a = int(input("Enter the number: "))
# main = 0
# while (i<=a):
#     main += i
#     i+=1

# print(main*'*')


m = int(input("Enter the number: "))

for i in range(1, m+1):
    print(' ', m+1, end='')
    print('*', (2*i-1), end='')
    print('')
