def deprecated(since=None, will_be_removed=None):

    if callable(since):
        func = since
        since = None
        return deprecated()(func)

    def decorator(func):
        def deprecated_func(*args, **kwargs):
            name = func.__name__
            
            string = f"Warning: function {name} is deprecated"
            if since:
                string += f" since version {since}"
            
            string += ". It will be removed in "
            if will_be_removed:
                string += f"version {will_be_removed}."
            else:
                string += f"future versions."
            
            print(string)
            
            return func(*args, **kwargs)

        return deprecated_func

    return decorator

@deprecated
def foo():
    print("Hello from foo")

@deprecated(since="4.2.0", will_be_removed="5.0.1")
def bar():
    print("Hello from bar")

foo()
bar()
