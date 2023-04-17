"""Note:- This is Binary Search Therefor please provide the input in asending order"""
def binery(li,s,l,h):
    if l>h:
        print("item not found")
        exit()
    mid=(l+h)//2
    if s == li[mid]:
        print("item found")
        exit()
    elif s > li[mid]:
        return binery(li,s,mid+1,h)
    else:
        return binery(li,s,l,mid-1)

li1 = []
i = input("Enter the size of a list: ")
print("enter the item :")
m=0
for _ in range(int(i)):
    li1.append(int(input()))
for _ in range(len(li1)):
    if li1[m] < li1[m+1]:
        m += 1
        continue
    else:
        print("Invalid Input")
        exit()
f = int(input("enter the searching element: "))
low=0
high=len(li1)-1
binery(li1,f,low,high)
