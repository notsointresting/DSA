letters = ["x","x","y","y"]
target = "z"

Alphabets = [int(i) for i in range(97,123)]
# Taking 118ms
# a ---> 97
# b ---> 98
# . ---> .
# . ---> .
# z ---> 122

for i in letters:
    if ord(target) < ord(i):
        print(chr(ord(i)))
        break
    res = -1

if res == -1:
    print(letters[0])

