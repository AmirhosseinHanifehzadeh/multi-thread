word = input()
counter = 0
print(word)
for i in range(1, len(word)):
    counter += 1
    print(word[i]*counter+word[i:])
