def deprecated(since=None, will_be_removed=None):
    def decorator(func):
        def deprecated_func(*args, **kwargs):
            name = func.__name__

            if since and will_be_removed:
                warning = f"Warning: function {name} is deprecated since version {since}. It will be removed in version {will_be_removed}."
            elif since:
                warning = f"Warning: function {name} is deprecated since version {since}. It will be removed in future versions."
            elif will_be_removed:
                warning = f"Warning: function {name} is deprecated. It will be removed in version {will_be_removed}."
            else:
                warning = f"Warning: function {name} is deprecated. It will be removed in future versions."

            print(warning)
            return func(*args, **kwargs)

        return deprecated_func

    return decorator

@deprecated()
def foo():
    print("Hello from foo")

@deprecated(since="4.2.0", will_be_removed="5.0.1")
def bar():
    print("Hello from bar")

foo()
bar()
