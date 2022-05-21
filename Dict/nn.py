special_characters = ""!@#$%^&*()-+?_=,<>/""
s=input()
# Example: $tackoverflow

if any(c in special_characters for c in s):
    print("yes")
else:
    print("no")