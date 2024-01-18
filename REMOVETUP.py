def Remove(t1):
    for i in t1:
        if (len(i) == 0):
            t1.remove(i)
    return t1
t1 = [(),
      ('Hargun', 'Japnoor', 'Harshita'),
      (),
      ('Kashvi', 'Khusshi'),
      ('Keshav', 'Karan', 'Naman'),
      ()]
print("______RESULT_______")
print("ORIGINAL TUPLE: \n", t1)
print()
print("AFTER EMPTY SPACES REMOVED: \n", Remove(t1))
