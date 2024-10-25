def split_lines():
    with open('input.txt', 'r') as infile, \
         open('s1.txt', 'w') as evenfile, \
         open('s2.txt', 'w') as oddfile:
        
        for i, line in enumerate(infile):
            if i % 2 == 0:
                oddfile.write(line)
            else:
                evenfile.write(line)

split_lines()
