#histogram of dictionary
def f(word):
  d={}
  for char in word:

     if char not in d:
       d[char]=1
     else:
       d[char]=d[char]+1
  #print(d)
  return d
a=f("mridani.dwivedi")
print(a)
#print item of dictionary
def print_f(a):
  for item in sorted(a):
    print(item,a[item])
print_f(a)
#print dictionary value key
def look(d,v):
  for item in d:
    if d[item]==v:
      return item
    
    
b=look(a,1)
print(b)