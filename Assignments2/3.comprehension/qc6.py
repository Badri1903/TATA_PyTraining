# dictionary comprehension for length of words

sample = "Python can be used on a server to create web applications. Python can be used alongside software to create workflows. Python can connect to database systems. It can also read and modify files."
len_dict = { x.strip('.') : len(x) for x in sample.split(' ')}
print(len_dict)