import sys

fo = open(sys.argv[1],"r+")
lo = open(sys.argv[2],"r+")
str = fo.readlines()
str1 = lo.readlines()
k=0
for j in str1:
 str1[k] = str1[k].replace("\n"," ")
 k=k+1
print str1
k=0
for i in str1:
  if i in str[k]:
    print "1"
  else:
   print "0"
  k=k+1
  
fo.close()
lo.close()