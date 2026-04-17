# var_name = open('filename with extension', 'argument for what we want to do')
# w - write, r - read, a - append, ...
"""
my_file = open("sample.txt", "w")

my_file.write("hello world\n")
my_file.write("party time!")

my_file.close()
"""
family_file = open("week_12\\family.txt", "w")

family_file.write('Pippi,22\n')
family_file.write('Liberty,22\n')
family_file.write('Griffen,23\n')
family_file.write('Carter,23\n')

family_file.close()
