def count_all_words(body_text: str) -> dict:
    word_count = {}
    words = body_text.split()

    for word in words:
        if word in word_count:
            word_count[word] = word_count[word] + 1
        else:
            word_count[word] = 1

    return word_count

test1 = "quick brown fox the jumps over the lazy dogs" # 'the' -> 2
test2 = "bar foo foo foo foo foo bar bar bar foo bar foo bar" # 'foo' -> 7, 'bar' -> 5
test3 = "i'm alone and i'm an easy target"
test4 = ""
test5 = ",,,,,,,,,,,,,,,,,,,,,,,,"
tests = [test1,test2,test3,test4,test5]

for i,test in enumerate(tests):
    print(f"{i}: {count_all_words(test)}")