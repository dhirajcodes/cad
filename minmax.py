import math
import random

def minmax(currentDepth,nodeIndex,maxTurn,score,targetDepth):
    if(currentDepth==targetDepth):
        return score[nodeIndex]
    if(maxTurn):
        return max(minmax(currentDepth+1,nodeIndex*2,False,score,targetDepth),minmax(currentDepth+1,nodeIndex*2+1,False,score,targetDepth))
    else:
        return min(minmax(currentDepth+1,nodeIndex*2,True,score,targetDepth),minmax(currentDepth+1,nodeIndex*2+1,True,score,targetDepth))
    
score=random.sample(range(1,50),4)
print(str(score))
treeDepth=math.log(len(score),2)
print("The optimal value is: ",end="")
print(minmax(0,0,True,score,treeDepth))   
