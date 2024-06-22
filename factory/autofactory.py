from inspect import getmembers, isclass, isabstract
import factory


class AutoFactory(object):
    autos = {}

    def __init__(self):
        self.load_autos()

    def load_autos(self):
        classes = getmembers(factory, lambda m: isclass(m) and not isabstract(m))
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, factory.AbsAuto):
                self.autos.update([[name, _type]])

    def create_instance(self, carname):
        if carname in self.autos:
            return self.autos[carname]()
        else:
            pass
