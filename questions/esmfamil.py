n, m, k = list(map(int, input().split()))
acceptable_ans = []
starter_letter = []
given_ans = []
total_score = [0 for i in range(n)]
subject_specifier = 0
hasDuplicateVal = False

# put our acceptable ans in a list
for i in range(m):
    acceptable_ans.append(list(input().split()))
# put our starter letter in a list
for i in range(k):
    starter_letter.append(input())
    for i in range(n):  # put given ans in a list
        given_ans.append(list(input().split(' ', m)))

for i in range(m):
    ansToSpecificSub = []
    for j in range(n * k):
        ansToSpecificSub.append(given_ans[j][i])
    for level in range(1,k + 1):
        alist = []
        indexDuplicateVal = []

        for ans in range(n * (level - 1), n * level):
            alist.append(ansToSpecificSub[ans])

        if len(alist) != len(set(alist)):
            hasDuplicateVal = True

        if hasDuplicateVal:
            dupl_c = dict()
            sorted_ind_c = sorted(range(len(alist)), key=lambda x: alist[x])
            for index in range(len(alist) - 1):
                if alist[sorted_ind_c[index]] == alist[sorted_ind_c[index+1]]:
                    dupl_c[sorted_ind_c[index]] = sorted_ind_c[index+1]

            for x, y in dupl_c.items():
                indexDuplicateVal.append(x)
                indexDuplicateVal.append(y)

        for z in range(n):
            if alist[z] in acceptable_ans[i]:
                if alist[z][0] == starter_letter[level - 1]:
                    if z in indexDuplicateVal:
                        total_score[z] += 5
                    else:
                        total_score[z] += 10

for i in total_score:
    print(i, end=' ')

