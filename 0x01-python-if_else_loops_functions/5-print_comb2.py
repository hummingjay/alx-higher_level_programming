#!/usr/bin/python3
for num in range(00, 100):
    if num < 99:
        # to pad a digit less than 2 digits with o before is with :0>2
        print("{:0>2}".format(int(num)), end=", ")
    else:
        print("{}".format(int(num)))
