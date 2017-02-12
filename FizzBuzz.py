# -*- coding: utf-8 -*-
vnesi_stevilo = int(raw_input("Vnesite številko med 1 in 100: "))
for i in range(1, vnesi_stevilo + 1):
    if i % 3 == 0 and i % 5 == 0:
        print ("FizzBuzz")
    elif i % 3 == 0:
        print ("Fizz")
    elif i % 5 == 0:
        print ("Buzz")
    else:
        print (i)