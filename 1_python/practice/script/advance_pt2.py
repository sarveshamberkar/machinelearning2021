# class Car:
#     pass
# c = Car()
# c.windows = 2
# c.engine = 'V8'
# c1 = Car()
# c1.windows = 4
# c1.engine = '1000cc'

# the above method is inefficient way to write the code

# actual way is to use __init__
import os

asda_dasd_Dsad_DADA__dasdA = 'A'


class Car:

    def __init__(self, windows, engine):
        self.windows = windows
        self.engine = engine


c = Car(windows=2,
        engine='v8')
try:
    c1 = Car()
    c1.windows = 4
    c1.engine = '1000cc'
except TypeError as ex:
    print('argument not mentioned')


# access modifiers
class Bike:
    def __init__(self, engine, weight):
        # access modifier is protected this is done using '_' in front of variable name but it
        self._engine = engine
        # can still be change
        # access modifier is private this is done using '__' in front of variable name but
        self.__weight = weight
        # itcan still be change

        # protected variable concept is that it can only be access using the subclass
        # private variable can be accessed using the


class ApacheRtr(Bike):
    def __init__(self, engine, weight, version, speed):
        super(ApacheRtr, self).__init__(engine=engine, weight=weight)
        self.version = version
        self.speed = speed


a = ApacheRtr(2000, 100, 1.0, 200)
print(a._engine, a.speed, a.version)
