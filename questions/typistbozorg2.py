import re


n = int(input())
alist = []

for i in range(n): # give input from user
    alist.append(int(input()))
    alist.append(input())

for index in range(0, len(alist), 2): # specify that we want compress or decompress
    word = alist[index + 1]

    if alist[index] == 1:
        finall_word = ""
        counter = 1
        finall_word += word[0]

        for i in range(len(word)-1):
            if(word[i] == word[i+1]):
                counter+=1
            else:
                if(counter > 1):
                    finall_word += str(counter)
                finall_word += word[i+1]
                counter = 1
        if(counter > 1):
            finall_word += str(counter)
        print(finall_word) 
    
    else:
        decompressed_word = ''.join(chr * int(num or 1)
              for chr, num in re.findall(r'(\w)(\d+)?', word))

        print(decompressed_word)

        