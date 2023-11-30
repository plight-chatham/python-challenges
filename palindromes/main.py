def is_palindrome(candidate:str) -> bool:
    candidate = candidate.lower()
    leftIndex = 0
    rightIndex = len(candidate) - 1

    while leftIndex < rightIndex:
        if candidate[leftIndex] != candidate[rightIndex]:
            return False
        leftIndex += 1
        rightIndex -= 1
    return True


def for_and_while():
    myList = [i/2 for i in range(10)]

    print( "for loop 1")
    for element in myList:
        print(element * 2)
        if element == 8.0:
            break

    print("for loop 2")
    for i in range(5,8):
        print(myList[i] * 2)

    print("while loop")
    j = 0
    while j < len(myList):
        print(myList[j] * 2)
        j += 1
        if j == 6:
            break






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #words = ["radar", "twice", "sees", "combat", "", "Radar"]
    #for word in words:
    #    print(f"{word} is a palindrome? {is_palindrome(word)}")
    for_and_while()