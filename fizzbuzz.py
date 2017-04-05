def fizz_buzz(i):
    words = ["Fizz", "Buzz"]
    word = ""

    if (i%3 == 0):
        word = word + words[0]
    if (i%5 == 0):
        word = word + words[1]
    if (i%3 != 0) and (i%5 != 0):
        word = i
    return word
#print solution(40)
