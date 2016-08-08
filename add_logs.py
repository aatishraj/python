log_file = open('/Users/aatishk/PycharmProjects/python_files/log')

log_list = []

for i in log_file:
    log_list.append(i.split()[5])

result = map(float, log_list[2:])
print sum(result)