l = []
l = ((input("Enter the sentence\n").split()))

target = input("Enter target word\n")
print(l)
for i, word in enumerate(l):
    if word == target:
        print(i+1)
        break
