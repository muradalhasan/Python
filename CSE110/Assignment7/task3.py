def foo_moo(a):
    if a%2==0 and a%3==0:
        return f"FooMoo"
    elif a%2==0:
        return f"Foo"
    elif a%3==0:
        return f"Moo"
    else:
        return f"Boo"
print(foo_moo(6))