


# # <--- Interview solving --->

# str = input("Enter an value : ")

# Counter = 0
# for i in str:
#     print(i)
#     Counter +=1

# print("Length of number : ",str,"is",Counter)


word = input("Enter the word here: ")
word_len = len(word)
i = word_len - 1
print("It's  reverse is: ",end="")
while i >= 0:
    print(word[i] , end = "")
    i -= 1