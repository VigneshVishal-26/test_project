test = 'a word'.upper()
print(test)
print(test.lower()) 

John = "helLowoRlD"
print(John.title())  # title() - Converts the first character of each word to upper case

remove = "HelLo woRlDXX"
print(remove.strip('X')) # strip() - Returns a trimmed version of the string

print(dir(remove)) # dir() - Returns a list of the specified object's properties and methods

print(remove.isalpha()) # isalpha() - Returns True if all characters in the string are in the alphabet - Return False - space is present

print(John.isalpha()) # return true - Space is not there.

print(John.capitalize())    # capitalize() - Converts the first character to upper case

center = John.center(13, "P") # conter() - 	Returns a centered string
print(center) 

Replace = "I love Kitties Kitties Kitties Kitties"
print(Replace.replace("Kitties", "Puppies"))   # replace() - Returns a string where a specified value is replaced with a specified value
print(Replace.replace("Kitties", "Puppies",2))

Input = r"D:\Vishal\Studies\methods.py"
print("Replaced : ", Input.replace('\\','/')) # It replaces every backslash (\) in the string with a forward slash (/).