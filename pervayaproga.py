import math
import numpy
import matplotlib.pyplot as mpp
if __name__=='__main__':
    arguments = numpy.arange(0, 200, 0.1)
    mpp.plot(
        arguments,
        [math.sin(a) * math.sin(a/20.0) for a in arguments]
    )
    mpp.show()