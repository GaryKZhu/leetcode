#Leetcode #48
matrix=[[1, 2, 3],[4, 5, 6],[7, 8, 9]]
print ("original -", matrix)
print ("zip orignial - ", list(zip(*matrix)))
print ("up side down -", *matrix[::-1])
print ("original rotation 90d - ",list(zip(*matrix[::-1])))
print ("reversed rotation 90d - ",list(zip(*matrix))[::-1])
