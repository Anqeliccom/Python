from functools import partial
def deprecated(func = None, since=None, will_be_removed=None):
    if func is None:
            return partial(deprecated, since = since, will_be_removed = will_be_removed)
        
    def deprecated_func(*args, **kwargs):
        
        name = func.__name__
        
        message = f"Warning: function {name} is deprecated"
        if since:
            message += f" since version {since}"
        
        message += ". It will be removed in "
        if will_be_removed:
            message += f"version {will_be_removed}."
        else:
            message += "future versions."
        
        print(message)
        
        return func(*args, **kwargs)

    return deprecated_func

@deprecated
def foo():
    print("Hello from foo")

@deprecated(since="4.2.0", will_be_removed="5.0.1")
def bar():
    print("Hello from bar")

foo()
bar()
