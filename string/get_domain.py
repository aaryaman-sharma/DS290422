# email = input("Enter your Email ID : ")

# domain = email.split('@')[1]
# print(domain)
# domain = domain.split('.')[0]
# print(domain)


# # start = email.index('@')
# # end = email.index('.')
# # domain = email[start+1:end]
# # print(domain)


print("Enter your  Email : ")
x = str(input())
l = ""
for index,i in enumerate(x):
    if i=='@':
        l=x[index+1:len(x)]
        print(l)
    else:
        continue
j=l.split('.')
print(j[0])