array=[1000000001,1000000002,1000000003,1000000004,1000000005]

def simple_ar(ar):
    s=0
    for i in ar:
        s=s+i
    return s

print(simple_ar(array))