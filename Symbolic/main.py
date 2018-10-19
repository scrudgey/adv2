import inspect
import random
from weakref import WeakKeyDictionary
from collections import defaultdict

PRIMITIVE_TYPES = [str, int, float]

class Symbol(object):
    def __init__(self, values):
        self.parent = None
        self.InitVals(values)
        self.CalcAttributes()
        
    def InitVals(self, values):
        if inspect.isclass(values):
            self.values = []
            for subclass in values.__subclasses__():
                self.values.append(subclass())
        else:
            if type(values) is list:
                self.values = values
            else:
                self.values = [values]
        if len(self.values) == 1:
            self._value = self.values[0]
        else:
            self._value = None
        
    def __repr__(self):
        return str(self.val)
    
    def __getattr__(self, attr):
        # allow self.val to inspect without collapsing my value
        if attr == 'val':
            if self._value:
                return self._value
            else:
                if len(self.values) == 1:
                    return self.values[0]
                else:
                    return self.values
        raise AttributeError("{} object has no attribute {}".format(self.__class__, attr))
    
    def CalcAttributes(self):
        attribute_values = defaultdict(list)
        for value in self.values:
            if type(value) in PRIMITIVE_TYPES:
                continue
            for key, val in AttributesDict(value).items():
                if isinstance(val, Symbol):
                    attribute_values[key].extend(val.values)
                else:
                    attribute_values[key].append(val)
        for key, vals in attribute_values.items():
                symbol = Symbol(vals)
                symbol.parent = self
                setattr(self, key, symbol)
    
    def Observe(self):
        if self._value:
            return self._value
        else:
            return self.Collapse(None)
    
    def Collapse(self, symbol, upwards=True):
        if symbol is None:
            return self.Collapse(Symbol([random.choice(self.values)]))

        self.InitVals(Subset(self, symbol))

        self.Restrict(symbol)

        self.CalcAttributes()

        if upwards:
            # TODO: don't propagate upwards if our values haven't changed
            if self.parent is not None:
                self.parent.Collapse(self.parent, upwards=True)
        return self

    def Restrict(self, symbol):
        # ensure that I have all the attributes of symbol
        new_values = []
        symbol_attributes = AttributesDict(symbol)
        for value in self.values:
            attribues_match = True
            value_attributes = AttributesDict(value)
            for attribute in value_attributes.keys():
                if not attribues_match:
                    continue
                if attribute in symbol_attributes:
                    value_attribute = Subset(value_attributes[attribute], symbol_attributes[attribute])
                    if value_attribute is None:
                        attribues_match = False
                    else:
                        # TODO: is this destructive?
                        setattr(value, attribute, value_attribute)
                else:
                    # adopt missing target values to ensure consistency?
                    pass
            if attribues_match:
                new_values.append(value)
        # self.values = new_values
        self.InitVals(new_values)
        

def AttributesDict(obj):
    filters = [
        lambda key, value: key[0] != '_',
        lambda key, value: not callable(value),
        lambda key, value: key != 'parent' and key != 'values'
    ]
    attributes = {}
    attributes = {i: obj.__getattribute__(i) for i in dir(obj)}
    for fn in filters:
        attributes = {k: v for k, v in attributes.items() if fn(k, v)}
    return attributes

def Subset(value, target, depth=0):
    '''Return the subset of value that spans target. If no
    such subset exists, return None
    '''
#     print('\t'*depth, 'subset: {}, {}'.format(value, target))

    #######################
    ## VALUE IS ITERABLE ##
    #######################

    if type(value) is Symbol:
        return Subset(value.values, target, depth=depth+1)
    if type(value) is list:
        results = [Subset(element, target, depth=depth+1) for element in value]
        results = [result for result in results if result is not None]
        if len(results) == 0:
            return None
        if len(results) == 1:
            return results[0]
        return results
    
    ########################
    ## TARGET IS ITERABLE ##
    ########################

    if type(target) is Symbol:
        return Subset(value, target.values, depth=depth+1)
    if type(target) is list:
        for element in target:
            result = Subset(value, element, depth=depth+1)
            if result is not None:
                return result
        return None
    
    ###################
    # CONCRETE VALUES #
    ###################

    is_subset = False
    if value == target:
        is_subset = True
    if type(value) not in PRIMITIVE_TYPES:
        if type(value) == type(target):
            is_subset = True
        if type(target) in type(value).__subclasses__():
            # TODO: (subclass)Value promotion
            # just take all attributes and methods
            is_subset = True

#     print('\t'*depth, is_subset)
    if not is_subset:
        return None
    
    return value

class Symbolic(object):
    def __init__(self):
        self.symbols = WeakKeyDictionary()
 
    def __get__(self, instance_obj, objtype):
        return self.symbols[instance_obj]
 
    def __set__(self, instance, values):
        self.symbols[instance] = Symbol(values)
 
    def __delete__(self, instance):
        del self.symbols[instance]