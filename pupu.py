from __future__ import print_function
def dp():
  p=(51,7,0,50,10,0,49,11,0,48,13,0,48,13,4,3,0,48,12,1,11,0,48,25,0,49,25,0,34,8,8,25,0,32,10,10,22,0,29,13,11,21,0,29,13,10,20,0,23,24,4,7,2,10,0,19,38,0,16,40,0,14,44,0,13,46,0,12,48,0,11,49,0,10,51,0,10,52,0,9,13,3,15,3,19,0,9,10,3,4,2,9,2,4,2,17,0,9,10,1,8,1,6,2,8,1,16,0,10,8,1,9,1,6,1,9,2,15,0,10,8,1,10,1,5,1,10,1,15,0,10,8,1,10,1,5,1,10,1,15,0,8,10,1,10,1,5,1,10,1,17,0,7,11,1,9,1,6,1,10,1,19,0,6,13,1,8,1,7,2,7,2,20,0,5,16,6,11,7,22,0,4,63,0,4,63,0,4,63,0,4,63,0,5,61,0,6,59,0,7,58,0,8,56,0,9,53,0,12,48,0,16,39,0)
  s= "";x=0
  for i,k in enumerate(p):
    if k:
      s+='*'*k if (i-x)%2 else ' '*k
    else:
      print(s);s="";x+=1
if __name__ == '__main__':
    dp()