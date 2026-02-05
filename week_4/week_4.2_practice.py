word1 = "table"
word2 = "technology"
a_check = False

for letter in word1:
    if letter == 'a':
        a_check = True

if a_check == True:
    print("Yes")
if a_check == False:
    print("No")

x = "hello world"
for index in range(4, 7 + 1):
    print(x[index])

print(x[6:10 + 1])
print(x[:])
print(len(x))

for index in range(0,len(x)):
    print(index, x[index])


entered_word = input("")
vowel_count = 0
for letter in entered_word:
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
        vowel_count += 1
print(vowel_count)