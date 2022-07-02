ans_list = []
value = True

def outer():
    # dict for put in words
    word = dict()
    firstRound = dict()
    count = 0
    def memorized(**kwargs):
        nonlocal word
        nonlocal count
        if firstRound == {}:
            ans_list.append('None')
            firstRound['firstround'] = 'check'
            for key,value in kwargs.items():
                word[key] = value  

        elif word == {}:
            ans_list.append('') # one empty line
            ans_list.append('None')      
            for key,value in kwargs.items():
                word[key] = value  

        else:
            alist = []
            for key,value in word.items():
                alist.append([key, sorted(value.split(', '), key=lambda x: (len(x), x.lower()))])

            alist_sorted = sorted(alist, key=lambda row:row[0].lower())
            ans_list.append('') # one empty line
            for item in alist_sorted:
                ans_list.append(f"{item[0]}: {', '.join(item[1])}")
            word = dict()
            for key,value in kwargs.items():
                word[key] = value        
            
    return memorized

memorize = outer()

try:
    while value:
        if __name__ == '__main__':
            exec(input().replace("\\n", "\n"))
except EOFError:
    for i in ans_list:
        print(i)
        value = False
