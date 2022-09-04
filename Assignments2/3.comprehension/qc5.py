# words with less than 5 letters in a string

sample = "Python can be used on a server to create web applications. Python can be used alongside software to create workflows. Python can connect to database systems. It can also read and modify files."
lesser_words = [w for w in sample.split(' ') if len(w.strip('.')) < 5]
print(lesser_words)