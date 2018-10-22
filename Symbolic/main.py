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
            if type(values) is Symbol:
                self.values = values.values
            elif type(values) is list:
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
        # TODO: drop deprecated attributes
        attribute_values = defaultdict(list)
        for value in self.values:
            if type(value) in PRIMITIVE_TYPES:
                continue
            for key, val in AttributesDict(value).items():
                if isinstance(val, Symbol):
                    attribute_values[key].extend(val.values)
                elif type(val) is list:
                    attribute_values[key].extend(val)
                else:
                    attribute_values[key].append(val)
        for key, vals in attribute_values.items():
                # implies recursion!
                symbol = Symbol(vals)
                symbol.parent = self
                setattr(self, key, symbol)
    
    def Observe(self):
        if self._value:
            return self._value
        else:
            return self.Collapse(None)
    
    def Collapse(self, symbol):
        # TODO: reject if intersection is 0? some basic rejection 
        if symbol is None:
            return self.Collapse(Symbol([random.choice(self.values)]))
        if type(symbol) is not Symbol:
            symbol = Symbol(symbol)

        # adopt new values
        self.InitVals(Subset(self, symbol))

        # restrict my values to only those whose attributes are also consistent with symbol
        self.Restrict(symbol)

        # recalculate my attributes
        self.CalcAttributes()

        # TODO: don't propagate upwards if our values haven't changed
        # TODO: change this to just recursive restriction
        if self.parent is not None:
            self.parent.Collapse(self.parent)
        return self

    def Restrict(self, symbol):
        def _attributes_match(value, symbol_attributes):
            value_attributes = AttributesDict(value)
            for attribute in value_attributes.keys() & symbol_attributes.keys():
                # TODO: collapse here? recursion
                value_attribute = Subset(value_attributes[attribute], symbol_attributes[attribute])
                if value_attribute is None:
                    return False
                else:
                    setattr(value, attribute, value_attribute)
            for attribute in symbol_attributes.keys() - (value_attributes.keys() & symbol_attributes.keys()):
                # adopt missing values?
                pass
            return True

        new_values = []
        symbol_attributes = AttributesDict(symbol)
        for value in self.values:
            if _attributes_match(value, symbol_attributes):
                new_values.append(value)
        self.InitVals(new_values)
        # TODO: restrict upwards?        

def AttributesDict(obj):
    filters = [
        lambda key, value: key[0] != '_',
        lambda key, value: not callable(value),
        lambda key, value: key != 'parent' and key != 'values' and key != 'val'
    ]
    attributes = {i: obj.__getattribute__(i) for i in dir(obj) if i[0] != '_'}
    for fn in filters:
        attributes = {k: v for k, v in attributes.items() if fn(k, v)}
    return attributes

def Subset(value, target, depth=0):
    '''Return the subset of value that spans target. If no
    such subset exists, return None
    '''

    #######################
    ## VALUE IS ITERABLE ##
    #######################

    if type(value) is Symbol:
        return Subset(value.values, target, depth=depth+1)

    # TODO: explain why this works
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

    # TODO: explain why this works
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

    # print('\t'*depth, is_subset)
    if not is_subset:
        return None
    
    return value

class Symbolic(object):
    def __init__(self):
        self.symbols = WeakKeyDictionary()
 
    def __get__(self, instance_obj, objtype):
        if instance_obj is None:
            return self
        # if instance_obj in self.symbols:
        return self.symbols[instance_obj]
        # else:
        #     # import ipdb; ipdb.set_trace()
        #     return None
 
    def __set__(self, instance, values):
        self.symbols[instance] = Symbol(values)
 
    def __delete__(self, instance):
        del self.symbols[instance]
