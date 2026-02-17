import sys

# name = sys.argv[1]  # name = vignesh murali
name = " ".join(sys.argv[1:]) # Takes all command-line arguments after the script name and joins them into a single string separated by spaces.
message = "python is popular programming language"

print(name.capitalize())  # Vignesh murali

print(name.center(24,"*"))  # *****vignesh murali*****

print(name.casefold())

print(message.count('p'))

