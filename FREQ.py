import operator


def Count(l1):
    d1 = {}
    for items in l1:
        d1[items] = operator.countOf(l1, items)

    for key, value in d1.items():
        print("% d : % d" % (key, value))


l1 = [1, 1, 1, 5, 5, 3, 1, 3, 3, 1, 4, 4, 4, 2, 2, 2, 2]
print("RESULT:")
Count(l1)
