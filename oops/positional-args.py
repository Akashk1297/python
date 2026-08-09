#args kwargs demonstration

# extra positional, no specific argument list need to be specified
def myfunc_args(*args):
    for i in args:
        print(i)

# extra positional arguments as dict, treat kwargs as a dict
def myfunc_kwargs(**kwargs):
    #print dict
    print(kwargs)

    #display each entry in dict
    for items in kwargs.items():
        print(items)

    #display keys only
    for k in kwargs.keys():
        print(k)

    #display values only
    for v in kwargs.values():
        print(v)

def myfunc_args_kwargs(name,*xargs,**kwargs):
    print('Mandatory input: ',name)
    print('Positional argument, xargs: ',xargs)
    print('Positional keyword argument, kwargs: ',kwargs)

#calling same function with different parameters
myfunc_args([1,2,3,4,5],{1},"hello",'world')
myfunc_args([{1,2},[3,4,5],{7,8}])
myfunc_args({'hey': 'there'})

#using kwargs passing key=value format
myfunc_kwargs(name='alice',country='india')

# function call passing both xargs and kwargs
myfunc_args_kwargs('Tony Stark',[1,2,3,4,5],{1}, job="Engineer", city="New York")
