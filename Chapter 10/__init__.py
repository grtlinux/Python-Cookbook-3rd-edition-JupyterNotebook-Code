# __init__.py

# from .a import A
# from .b import B

# __init__.py

def A():
    from .a import A
    return A()

def B():
    from .b import B
    return B()