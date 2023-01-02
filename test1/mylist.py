def changelist(my_list1):
        my_list1.append("Arpit")
        return None

my_list = [1,2,3]
changelist(my_list)
print(my_list)

# Function definition is here
def printinfo( name, age ):
        '''This prints a passed info into this function'''
        print("Name: ",name)
        print("Age ", age)
        return None

# Now you can call printinfo function
printinfo( age=50, name="miki" )