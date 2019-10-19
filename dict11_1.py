def fun1():
  d={}
  fin=open('words.txt')
  for word in fin:
    word=word.strip()
   # word=word.split()
    #print(word)
    if word not in d:
       d[word]=1
    else:
       d[word]+=1
  return d
a=fun1()
def wrd(a,word):
  if word in a:
    print(word)
  else:
    print("not found")
wrd(a,'ahead')