#!/usr/bin/env python

class debugger(object): # <1>
    def __init__(self,func):  # <2>
        self._func = func

    def __call__( self, *args, **kwargs ):  # <3>

        print("*" * 40) # <4>
        print("** function", self._func.__name__,"**") # <4>

        if args:
          print("\targs are ", args) # <4>
        if kwargs:
          print("\tkwargs are ", kwargs) # <4>

        print("*" * 40) # <4>

        return self._func( *args, **kwargs )  # <5>

@debugger # <6>
def hello( greeting, whom="world"):
    print("{}, {}".format( greeting, whom ))
    
hello('hello','world') # <7>
print()

hello('hi','Earth')
print()

hello('greetings')
