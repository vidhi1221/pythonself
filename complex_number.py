# Comple number

# Python can handle real number, but Python can also handle complex number using file 'cmath'

# complex number is represnt by " x + yi".

# Complex number is the combination of real and imaginary part

# python converts real number x and y into complex using complex(x,y) function 
# and real number use real function 
# and imaginary part reprented by imag()

###############
# Some Arguments of complex number
# complex number is the angle between the positive real axis and the vector representing complex number
# phase is returned using phase() 
# range of phase from -pi to +pi

########################################################3
# Example of complex number

from cmath import log


c = 2 + 5j
print(type(c))

print(c.real)
print(c.imag)

print(c.conjugate())

d = 3 + 6j

print("addition of complex number c and d" , c + d)

print("substraction of complex number c and d" , c - d)


 

