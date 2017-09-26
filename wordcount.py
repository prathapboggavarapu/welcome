count = 0
num_lines = 0
#with codecs.open('alice.txt','r',encoding='utf-8') as f:
myfile = open('alice.txt', 'r')
for line in myfile:
     tmplist=line.split()
     num_lines += 1
     print tmplist
#print num_lines
print tmplist

#     count = count + len(tmplist)
#print count
#for line in f.readlines():
 #   lines = len(line.strip())
  #  num_lines += len(lines)
#print num_words