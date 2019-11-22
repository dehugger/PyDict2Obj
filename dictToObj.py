class RecursiveObject(object):
    def __init__(self, dic):
        for k in dic.items():
            if type(k[1]) == dict:
                setattr(self, k[0], RecursiveObject(k[1]))
            elif type(k[1]) == list:
                l = []
                for i in k[1]:
                    if type(i) == dict:
                        l.append(RecursiveObject(i))
                    else:
                        l.append(i)
                setattr(self, k[0], l)
            else:
                setattr(self, k[0], k[1])

    def dump(self):
        for attr in dir(self):
            print("obj.%s = %r" % (attr, getattr(self, attr)))
            if type(getattr(self, attr)) == RecursiveObject:
                getattr(self, attr).dump()
