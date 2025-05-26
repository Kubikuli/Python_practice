# minitask 5

# Modify the body of function store to double ns['n'] and the sizes of the ns['karr'] and ns['varr'] when the number of actually stored items (with the addition of the new one) reaches 2/3 of total allocated slots ns['n']
# The last print should result in:
# {'actually_stored': 6, 'n': 16, 'karr': [[], ['name', 'friend'], [], ['age'], ['color'], [], ['id'], [], [], [], [], ['husband'], [], [], [], []], 'varr': [[], ['Alice', 'Bob'], [], [25], ['green'], [], [123], [], [], [], [], ['Emil'], [], [], [], []]}

def setup(ns):
    ns['actually_stored'] = 0
    ns['n'] = 8
    ns['karr'] = [[] for i in range(ns['n'])]
    ns['varr'] = [[] for i in range(ns['n'])]

def store(ns, key, value):
    i = hash(key) % ns['n']
    ns['karr'][i].append(key)
    ns['varr'][i].append(value)
    ns['actually_stored'] += 1

    if ns['actually_stored'] >= (2/3 * ns['n']):
        old_karr = ns['karr']
        old_varr = ns['varr']
        ns['n'] = 2 * ns['n']
        ns['karr'] = [[] for i in range(ns['n'])]
        ns['varr'] = [[] for i in range(ns['n'])]

        for karr, varr in zip(old_karr, old_varr):
            for o_key, o_value in zip(karr, varr):
                i = hash(o_key) % ns['n']
                ns['karr'][i].append(o_key)
                ns['varr'][i].append(o_value)

def lookup(ns, key):
    i = hash(key) % ns['n']
    try:
        j = ns['karr'][i].index(key)
    except ValueError:
        raise KeyError(key)
    return ns['varr'][i][j]

ns1={}
setup(ns1)
store(ns1,'name','Alice')
store(ns1,'age',25)
store(ns1,'color','green')
print(lookup(ns1,'name'))
print(ns1)
store(ns1,'friend','Bob')
store(ns1,'id',123)
print(ns1)
store(ns1,'husband','Emil')
print(ns1)
