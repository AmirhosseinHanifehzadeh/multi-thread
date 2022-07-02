value = True
inputs_list = []
assignment_counter = []

def voroodi():
    entryElement = input()
    if entryElement.isdigit():
        return int(entryElement)
    else:
        return entryElement


while value:
    var = input()
    if 'agar' in var.split():
        var = var.replace('agar', 'if')
    if 'khoorooji' in var:
        var = var.replace('khoorooji', 'print')
    if '-----' == var:
        value = False
    else:
        inputs_list.append(var)


for code in inputs_list:
    if '=' in code.split():
        indexAssignedVal = code.split().index('=') - 1
        if 'if' not in code.split():
            assignment_counter.append(code.split()[indexAssignedVal])
        else:
            new_code = code.replace(code[code.index(':') + 1:], "assignment_counter.append(code.split()[code.split().index('=') - 1])")
            exec(new_code)
    exec(code)
print(len(set(assignment_counter)))

