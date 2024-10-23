i = 0

for i in range(1, 16):
    if (i % 3 == 0) and (i % 5 == 0):
       print(f"iの値は{i}なので5でも3割り切れるためFizzBuzzです") 
    elif i % 3 == 0:
        print(f"iの値は{i}なのでFizzです")
    elif i % 5 == 0:
        print(f"iの値は{i}なのでBuzzです")
    else:
        print(f"iの値は{i}です")