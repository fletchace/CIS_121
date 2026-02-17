def is_acronym(acronym, words):
    test_acronym = ''
    for word in words:
        test_acronym += word[0]
    if test_acronym == acronym:
        print("True")
    else:
        print("False")

is_acronym("abc", ["alice", "bob", "charlie"])
is_acronym("a", ["an", "apple"])
is_acronym("ngguoy", ["never", "gonna", "give", "up", "on", "you"])
is_acronym("ab", ["apple", "banana", 'cat'])