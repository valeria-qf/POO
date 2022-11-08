def minion_game(string):
    s = len(string)
    kevin_vowel = 0
    stuart_cons = 0

    for i in range(s):
        if string[i] in 'AEIOU':
            kevin_vowel = kevin_vowel + (s - i)

        else:
            stuart_cons = stuart_cons + (s - i)

    if kevin_vowel < stuart_cons:

        print('Stuart', stuart_cons)

    elif kevin_vowel > stuart_cons:
        print('Kevin', kevin_vowel)

    else:
        print('Draw')
