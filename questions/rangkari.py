n, m, k = list(map(int, input().split()))
colors_li = []
home_li = []
diffrent_color = []
counter = '1'

for i in range(k):
    colors_li.append(list(map(int, input().split(' ',3))))

for i in range(n):
    home_li.append(list('0' for i in range(m)))

for i in range(k):
    rowst_home = colors_li[i][0]
    colst_home = colors_li[i][1]
    counter_home = colors_li[i][2]

    for i in range(rowst_home - 1,rowst_home - 1 + counter_home):
        for j in range(colst_home - 1,colst_home - 1 + counter_home):
            home_li[i][j] += counter
    counter = str(int(counter) + 1)

for i in range(n):
    for j in range(m):
        if home_li[i][j] not in diffrent_color:
            diffrent_color.append(home_li[i][j])

print(len(diffrent_color) - 1)