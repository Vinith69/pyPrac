l = (list(input("Enter sentence\n").split()))

for i, word in enumerate(l):
    if word == "[space]":
        l.remove(word)

print(l)
print(len(l))
