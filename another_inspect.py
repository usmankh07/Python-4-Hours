import inspect
# normal python user-defined function/method

def show_name_age(first_name:str, last_name:str, age:int):
    print("{} {} is {} years old".format(first_name, last_name,age))

# signature of a method: accesses parameters, their inferred or fixed data types.
sig = inspect.signature(show_name_age)
print(sig.parameters)
