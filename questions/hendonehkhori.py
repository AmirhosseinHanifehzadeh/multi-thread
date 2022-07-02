# give the watermelone numbers that she eat
watermelone_number = int(input('how many watermelons did you eat? '))
# enter the watermelone's weight that she ate
watermelone_weight = list(
    map(int, input("enter watermelones weight?").split()))

if watermelone_number == len(watermelone_weight):
    # give the maximum value of watermelone_weight
    max_weight = max(watermelone_weight)
    # give the index of maximum value of watermelon_weight
    max_index_weight = watermelone_weight.index(max_weight)
    # print the index of maximum value of watermelone_weight
    print(max_index_weight + 1)
else:
    print('you put more or less number!!!')
