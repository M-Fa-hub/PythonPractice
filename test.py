class MyClass:
    def __init__(self, value):
        self._value = value
    
    @property
    def value(self):
        return 545
    

class1 = MyClass(10)


print(class1.value)
print(class1._value)