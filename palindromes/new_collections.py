
myList = ["phil", 42, "Stanton Heights"]
myTuple = ("phil", 42, "Stanton Heights")

print(myList[-1])

myList.append("has baby")

myList[1] = 43

print(myList.insert(5,0))
print(myTuple)
"""

s = set([])
s.add(4)
s.add("narcolepsy")
s.add(3)
s.add(3)
s.add(2)
for item in s:
    print(item)


test1 = "quick brown fox the jumps over the lazy dogs" # 'the' -> 2
test2 = "bar foo foo foo foo foo bar bar bar foo bar foo bar" # 'foo' -> 7, 'bar' -> 5
test3 = "i'm alone and i'm an easy target"
test4 = ""
test5 = ",,,,,,,,,,,,,,,,,,,,,,,,"
tests = [test1,test2,test3,test4,test5]

for test in tests:
    ordered_words = test.split()
    words_in_test = set(ordered_words)
    print(words_in_test)
"""