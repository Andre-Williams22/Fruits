fruits = ['apples', 'oranges', 'bananas', 'tangerines', 'pineapples', 'kewi', 'apricots']

def novowel(fruits, num):
    vowel = []
    nvowel = []
    for x in fruits:
        if x[0] == 'a' or x[0] == 'i' or x[0] == 'u' or x[0] == 'e' or x[0] == 'u':
            vowel.append(x)
        else:
            nvowel.append(x)
            