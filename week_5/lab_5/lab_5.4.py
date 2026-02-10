def hamming_distance (word1 , word2):
    count = 0
    for pos in range(len(word1)):
        if word1[pos] != word2[pos]:
            count += 1
    print(count)

hamming_distance("abcde", "bcdef")
hamming_distance("abcdef", "abcdef")
hamming_distance("strong", "strung")