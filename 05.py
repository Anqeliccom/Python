
def specialize(f, *args, **kwargs):
    def partialFunc(*argsRemaining, **kwargsRemaining):
        combArgs = args + argsRemaining
        combKwargs = {**kwargs, **kwargsRemaining}
        return f(*combArgs, **combKwargs)
    
    return partialFunc

def sum(x, y):
    return x + y

plus_one = specialize(sum, y=1)
just_two = specialize(sum, 1, 1)

print(plus_one(10)) # *argsRemaining
print(just_two())
