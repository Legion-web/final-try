def arraylambda():
    array = [22, 45, 78, 56, 82, 38]
    array = list(filter((lambda j: j != 0), list(map((lambda x: x if x % 8 == 0 else 0), array))))
    print(array[0])


arraylambda()

