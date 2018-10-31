list1 = []
list2 = []
list3 = []
with open('sample_text.rtf', 'r') as f:
    content = f.readlines()
    for x in content:
        row = x.split()
        list1.append(int(row[0]))
        list2.append(int(row[1]))
        list3.append(int(row[2]))