# Function tack String and print number of unique exits words in sentence





def num_of_words(sentence):
    words = list(set(sentence.split()))
    for word in words:
        print(word , "=" , words.count(word))





num_of_words("hello hello friend how are you today")
