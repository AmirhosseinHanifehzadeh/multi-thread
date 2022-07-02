n = int(input())
alist = []

for i in range(n): # give input from user
    alist.append(int(input()))
    alist.append(input())

for index in range(0, len(alist), 2): # specify that we want compress or decompress
    word = alist[index + 1]

    if alist[index] == 1:
        counter = 1 
        finall_word = ''

        for i in range(len(word)):
            j = i + 1
            last_letter_index = len(word) - 1
            if i != last_letter_index:
                if word[i] == word[j]:
                    counter += 1

                else:
                    finall_word += word[i]
                    if counter != 1:
                        finall_word += str(counter)
                    counter = 1
            else:
                if word[last_letter_index] == word[len(word) - 2]:
                    finall_word += word[last_letter_index]
                    finall_word += str(counter)
                else:
                    finall_word += word[last_letter_index]

        print(finall_word)
    else:
        decompressed_word = ''
        for i in range(len(word) - 1):
            if word[i].isdigit():
                if word[i + 1].isdigit():
                    decompressed_word += str(word[i - 1]) * (int(str(word[i]) + str(word[i + 1])) - 1)
                else:
                    decompressed_word += str(word[i - 1]) * (int(word[i]) - 1)
            else:
                decompressed_word += word[i]

        if word[len(word) - 1].isdigit():
            decompressed_word += str(word[len(word) - 2]) * (int(word[len(word) - 1]) - 1)
        else:
            decompressed_word += str(word[len(word) - 1])
        print(decompressed_word)
  