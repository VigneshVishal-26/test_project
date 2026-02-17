# a = input("Enter a number for A: ")
# b = input("Enter a number for B: ")
#
# print(int(a) + int(b))

import sys

'''
if len(sys.argv) != 3:

    print("Usage: python input_Handling.py 'full_name and last_name'")
    sys.exit()

full_name = sys.argv[1:]
last_name = sys.argv[2]
#Format name
email = full_name.lower().replace(" ", ".") + last_name.lower().replace(" ", ".") + "@valeo.com"

print("\n----Your Profile----")
print("Full name: " + full_name + last_name)
print("Email: " + email)
'''

full_name = " ".join(sys.argv[1:])
print("Full name : ",full_name)

email = full_name.lower().replace(" ", ".") + "@valeo.com"

print("\n----Your Profile----")
print("Full name: " + full_name)
print("Email: " + email)