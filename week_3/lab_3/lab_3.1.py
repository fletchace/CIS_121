# a)4, 3, 8, 18
# b)odd not 3, 3, even (-infinity,10], even [12,infinity)
my_var = ''
if my_var % 2 == 1 :
    if my_var ** 3 != 27 :
        my_var = my_var +4 #Assignment 1
    else:
        my_var /= 1.5 #Assignment 2
else:
    if my_var <= 10:
        my_var *= 2 #Assignment 3
    else:
        my_var -= 2 #Assignment 4
print( my_var )