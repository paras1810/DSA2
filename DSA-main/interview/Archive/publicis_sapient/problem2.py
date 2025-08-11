# set_generator
from itertools import combinations
def set_generator(input_set):
    n=len(input_set)
    for r in range(n+1):
        for combo in combinations(input_set,r):
            yield list(combo)

def set_generator_backtrack(input_set):
    def backtrack(index, path, result):
        if index==len(input_set):
            result.append(path)
            return 
        backtrack(index+1, path, result)
        backtrack(index+1, path+[input_set[index]], result)
    result=[]
    backtrack(0, [], result)
    return result 

input_set=[1,2,3]
output = list(set_generator(input_set))
print(output)
output2 = set_generator_backtrack(input_set)
print(output2)