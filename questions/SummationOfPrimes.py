num = 2000000
primenumber_list = []
for i in range(2,num//2):
    if num % i != 0 :
        primenumber_list.append(num)
print(sum(primenumber_list))

