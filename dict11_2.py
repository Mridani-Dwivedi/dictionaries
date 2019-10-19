def fun1():
  d={}
  fin=open('name.txt')
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
#print(a)
def inver(d):
  dic={}
  for key in d:
    val=d[key]
    
    dic.setdefault(val, []).append(key)
    
  print(dic)
inver(a)
