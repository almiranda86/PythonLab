def checkio(text: str) -> str:

    t = text.lower().replace(" ","")

    myDict = {}
    count = 0

    for x in t :
        if x.isalpha():
            if x in myDict:
                myDict[x] += count+1
            else:
                myDict[x] = count+1

    if all(value == 1 for value in myDict.values()):
        return list(sorted(myDict))[0]
    else:
        return max(sorted(myDict), key=myDict.get)

if __name__ == '__main__':
    print("Example:")
    #print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    #assert checkio("Hello World!") == "l", "Hello test"
    #assert checkio("How do you do?") == "o", "O is most wanted"
    #assert checkio("One") == "e", "All letter only once."
    #assert checkio("Oops!") == "o", "Don't forget about lower case."
    #assert checkio("AAaooo!!!!") == "a", "Only letters."
    #assert checkio("abe") == "a", "The First."
    #print("Start the long test")
    #assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    #print("The local tests are done.")
    assert checkio("Lorem ipsum dolor sit amet") == "m", "Hello test"