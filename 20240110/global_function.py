global_variable = 10

def my_function():
    print("Inside the function:", global_variable)

def modify_global_variable():
    global global_variable
    global_variable = 20
    print("Inside the function (after mod):", global_variable)

my_function() # Inside the function: 10
print("Outside the function:", global_variable) # Outside the function: 10
modify_global_variable() # Inside the function (after mod): 20
print("Outside the function (after mod):", global_variable) # Outside the function (after mod): 20