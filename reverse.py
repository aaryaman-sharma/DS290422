# from socket import INADDR_ALLHOSTS_GROUP


# no_1 = int(input("Enter a value : "))

# rev = 0

# # mod =  no_1 % 10 
# # rev = rev * 10 + mod
# # no_1 = no_1 


# while no_1:
#     mod = no_1 % 10
#     rev = rev * 10 + mod
#     no_1 = no_1 // 10 # 0

# print("Reverse : ",rev)


num=int(input("Enter the number : "))
while num!=0:
    mod=num%10
    num//=10
    print(mod,end="")