#!/usr/bin/env python

def f1(self): # <1>
    print("Hello from f1()")

def f2(self): # <1>
    print("Hello from f2()")

new_class = type("new_class", (object,), {  # <2>
    'hello1': f1,
    'hello2': f2,
    'color': 'red',
    'state': 'Ohio',
})

n1 = new_class()  # <3>

n1.hello1()  # <4>
n1.hello2()
print(n1.color) # <5>
print()

sub_class = type("sub_class", (new_class,), {'fruit': 'banana'}) # <6>
s1 = sub_class() # <7>
s1.hello1()     # <8>
print(s1.color)  # <9>
print(s1.fruit)
