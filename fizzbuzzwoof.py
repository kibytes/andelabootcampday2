def solution(N):
    words = ["Fizz", "Buzz", "Woof"]
    
    for i in range(N):
        i = i+1
        word = ""

        if (i%3 == 0):
            word = word + words[0]
        if (i%5 == 0):
            word = word + words[1]
        if (i%7 == 0):
            word = word + words[2]
        if (i%3 != 0) and (i%5 != 0) and (i%7 != 0):
            word = i
        print word
#solution(40)

