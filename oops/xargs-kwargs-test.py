# converts to tuple as output
# when input is not prior and can be random
def func1(*args):
    print(args)

# converts to dictionary as output
# input should be key-value pair
def func2(**val):
    print(val)

print(func1([1,2,3],5,"akash"))
print(func2(akash=1,batash=2,pavan=3))
