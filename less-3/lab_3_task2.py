import numpy
h = 100
a = numpy.pi/3
b = 0.523599
g = 9.8
v = numpy.sqrt(g * h * numpy.tan(b)**2)/(2 * numpy.cos(a) * (1 - numpy.tan(b) * numpy.tan(a)))
print(v)

t = 200
z = 300
k =  1.380649 * 10**(-23)
e = 2.7182818284590452353602874713527
