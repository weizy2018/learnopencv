def test(temperature):
    assert(temperature > 0), "Colder than absolute zero!"
    return (temperature - 273)*1.8 + 32

def fun(level):
    if level < 0:
        raise Exception(level)
    return level



try:
    print(test(10))
    print(test(-10))
except Exception as arg:
    print('hhh', arg)

try:
    print(fun(10))
    print(fun(-10))
except Exception as e:
    print('exception: ', e.args[0])

# print(test(10))
# print(test(-10))
