def vis(first,second):
    '''This the code prints the two strings '''
    print("Names are:")
    print(first+ " " +second)

def upper_vis(first,second):
    
    '''convert strings to upper case'''
    uf = first.upper()
    us = second.upper()
    print("Upper strings are:")
    print( uf +' '+us)
    
print("using__doc__:")
print(vis.__doc__)
print(upper_vis.__doc__)
print("Using help")
help(vis)
help(upper_vis)