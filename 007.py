#Write a function that takes in a list of integers and returns True if it contains 007 in order
#spy_game([1,2,4,0,0,7,5]) --> True
# spy_game([1,0,2,4,0,5,7]) --> True
# spy_game([1,7,2,0,4,5,0]) --> False

#list1 = [1, 0, 5, 0, 8, 9, 3, 4]
list1 = []
c = 0
c2 = 0
final = 0
num = int(input("Input the number of elements: "))
print("Input the list: ")
for i in range(0,num):
      n1 = int(input())
      list1.append()

for i in list1:
      
    if i == 0:
      c = 1

    if c == 1:
        if i == 0:
            c2 = 1 
    if c2 == 1:
        if i == 7:
            print("\nTrue ")
            final =1 
if final == 0:
    print("\nFalse")


#############################Mk#########
flag = False
for x in range(0,(len(l)-2)):
    for y in range(x+1,(len(l)-1)):
        for z in range(x+2,len(l)):
            if(l[x]==0 and l[y]==0 and l[z] == 7):
                flag = True
                
if(flag):
    print("007 is present")
else:
    print("007 is not present")
