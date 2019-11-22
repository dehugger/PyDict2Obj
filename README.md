# PyDict2Obj
Converts nested python dictionaries into objects, converting sub dictionaries and dictionaries in lists as well.

Example Usage:
```python
>>> myDic = {'a':1,'b':{'bNested':2},'c':[1,'two',{'cListNested':3},[4]]}
>>> ro = RecursiveObject(myDic)
>>> ro.a
1
>>> ro.b
<config.RecursiveObject object at 0x0000015B8DA091D0>
>>> ro.b.bNested
2
>>> ro.c
[1, 'two', <config.RecursiveObject object at 0x0000015B8DA09128>, [4]]
>>> ro.c[2].cListNested
3
>>> ro.dump()
obj.__class__ = <class 'config.RecursiveObject'>
obj.__delattr__ = <method-wrapper '__delattr__' of RecursiveObject object at 0x0000015B8D9F0550>
obj.__dict__ = {'a': 1, 'b': <config.RecursiveObject object at 0x0000015B8DA091D0>, 'c': [1, 'two', <config.RecursiveObject object at 0x0000015B8DA09128>, [4]]}
obj.__dir__ = <built-in method __dir__ of RecursiveObject object at 0x0000015B8D9F0550>
obj.__doc__ = None
obj.__eq__ = <method-wrapper '__eq__' of RecursiveObject object at 0x0000015B8D9F0550>
obj.__format__ = <built-in method __format__ of RecursiveObject object at 0x0000015B8D9F0550>
obj.__ge__ = <method-wrapper '__ge__' of RecursiveObject object at 0x0000015B8D9F0550>
obj.__getattribute__ = <method-wrapper '__getattribute__' of RecursiveObject object at 0x0000015B8D9F0550>
obj.__gt__ = <method-wrapper '__gt__' of RecursiveObject object at 0x0000015B8D9F0550>
obj.__hash__ = <method-wrapper '__hash__' of RecursiveObject object at 0x0000015B8D9F0550>
obj.__init__ = <bound method RecursiveObject.__init__ of <config.RecursiveObject object at 0x0000015B8D9F0550>>
obj.__init_subclass__ = <built-in method __init_subclass__ of type object at 0x0000015B8D8E2928>
obj.__le__ = <method-wrapper '__le__' of RecursiveObject object at 0x0000015B8D9F0550>
obj.__lt__ = <method-wrapper '__lt__' of RecursiveObject object at 0x0000015B8D9F0550>
obj.__module__ = 'config'
obj.__ne__ = <method-wrapper '__ne__' of RecursiveObject object at 0x0000015B8D9F0550>
obj.__new__ = <built-in method __new__ of type object at 0x00007FFBE68C6EC0>
obj.__reduce__ = <built-in method __reduce__ of RecursiveObject object at 0x0000015B8D9F0550>
obj.__reduce_ex__ = <built-in method __reduce_ex__ of RecursiveObject object at 0x0000015B8D9F0550>
obj.__repr__ = <method-wrapper '__repr__' of RecursiveObject object at 0x0000015B8D9F0550>
obj.__setattr__ = <method-wrapper '__setattr__' of RecursiveObject object at 0x0000015B8D9F0550>
obj.__sizeof__ = <built-in method __sizeof__ of RecursiveObject object at 0x0000015B8D9F0550>
obj.__str__ = <method-wrapper '__str__' of RecursiveObject object at 0x0000015B8D9F0550>
obj.__subclasshook__ = <built-in method __subclasshook__ of type object at 0x0000015B8D8E2928>
obj.__weakref__ = None
obj.a = 1
obj.b = <config.RecursiveObject object at 0x0000015B8DA091D0>
obj.__class__ = <class 'config.RecursiveObject'>
obj.__delattr__ = <method-wrapper '__delattr__' of RecursiveObject object at 0x0000015B8DA091D0>
obj.__dict__ = {'bNested': 2}
obj.__dir__ = <built-in method __dir__ of RecursiveObject object at 0x0000015B8DA091D0>
obj.__doc__ = None
obj.__eq__ = <method-wrapper '__eq__' of RecursiveObject object at 0x0000015B8DA091D0>
obj.__format__ = <built-in method __format__ of RecursiveObject object at 0x0000015B8DA091D0>
obj.__ge__ = <method-wrapper '__ge__' of RecursiveObject object at 0x0000015B8DA091D0>
obj.__getattribute__ = <method-wrapper '__getattribute__' of RecursiveObject object at 0x0000015B8DA091D0>
obj.__gt__ = <method-wrapper '__gt__' of RecursiveObject object at 0x0000015B8DA091D0>
obj.__hash__ = <method-wrapper '__hash__' of RecursiveObject object at 0x0000015B8DA091D0>
obj.__init__ = <bound method RecursiveObject.__init__ of <config.RecursiveObject object at 0x0000015B8DA091D0>>
obj.__init_subclass__ = <built-in method __init_subclass__ of type object at 0x0000015B8D8E2928>
obj.__le__ = <method-wrapper '__le__' of RecursiveObject object at 0x0000015B8DA091D0>
obj.__lt__ = <method-wrapper '__lt__' of RecursiveObject object at 0x0000015B8DA091D0>
obj.__module__ = 'config'
obj.__ne__ = <method-wrapper '__ne__' of RecursiveObject object at 0x0000015B8DA091D0>
obj.__new__ = <built-in method __new__ of type object at 0x00007FFBE68C6EC0>
obj.__reduce__ = <built-in method __reduce__ of RecursiveObject object at 0x0000015B8DA091D0>
obj.__reduce_ex__ = <built-in method __reduce_ex__ of RecursiveObject object at 0x0000015B8DA091D0>
obj.__repr__ = <method-wrapper '__repr__' of RecursiveObject object at 0x0000015B8DA091D0>
obj.__setattr__ = <method-wrapper '__setattr__' of RecursiveObject object at 0x0000015B8DA091D0>
obj.__sizeof__ = <built-in method __sizeof__ of RecursiveObject object at 0x0000015B8DA091D0>
obj.__str__ = <method-wrapper '__str__' of RecursiveObject object at 0x0000015B8DA091D0>
obj.__subclasshook__ = <built-in method __subclasshook__ of type object at 0x0000015B8D8E2928>
obj.__weakref__ = None
obj.bNested = 2
obj.dump = <bound method RecursiveObject.dump of <config.RecursiveObject object at 0x0000015B8DA091D0>>
obj.c = [1, 'two', <config.RecursiveObject object at 0x0000015B8DA09128>, [4]]
obj.dump = <bound method RecursiveObject.dump of <config.RecursiveObject object at 0x0000015B8D9F0550>>
```
