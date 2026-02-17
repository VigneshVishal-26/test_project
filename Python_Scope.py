#L(Local) -> E(Enclosing) -> G(Global) -> B(Build in)
'''
Local Variable
def order():
    food = "Rice"
    print("Your food is : ", food)

order()

# var food can be accessible only within the function.
#########################################################

#Enclosing Variable

def cart():
    discount = 10

    def checkout():
        print("Your checkout is : ", discount)

    checkout()

cart()

###########################################

#Global Variable

user_id = "Vignesh26"

def homepage():
    print("Your homepage is : ", user_id)

def profile():
    print("Welcome to the profile page  : ", user_id)

homepage()
profile()

######################################################

#Build in variable

print(__file__)

'''

#######################################################

delivery_partner = "Swiggy"

def hotel():
    item = "Pizza"

    def order_now():
        quantity = 2
        print(f"Ordering {quantity} {item} using {delivery_partner}")

    order_now()
hotel()