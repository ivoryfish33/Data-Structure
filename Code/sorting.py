from typing import List

def bubbleSort(alist:List):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]: 
                # temp = alist[i+1]
                # alist[i+1] = alist[i]
                # alist[i] = temp
                alist[i],alist[i+1] = alist[i+1],alist[i]  
                

alist = [54,26,93,17,31,44,55,20]
bubbleSort(alist)
# print(alist)

