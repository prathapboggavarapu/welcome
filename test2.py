fname = "alice.txt"

num_lines = 0
num_words = 0
num_chars = 0

with open(fname, 'w') as f:
    for line in f:
        words = line.split()

        num_lines += 1
        num_words += len (words)
    print num_words  
