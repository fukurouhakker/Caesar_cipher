before=input("Enter the Caesar cipher:")
before_num=len(before)


i=0
after=[]
answer=[]

for i in range(before_num):
    
    after.append(before[i])
    
 
base=[ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(base)):
    
    base_num=ord(base[i])
    
    
    original=ord(after[0])
    result=original-base_num
    
    for c in after:
        i=ord(c)
    
         
        i2=chr(int(i)-result)
        answer.append(i2)

        print(i2,end="")



    print("")
  
