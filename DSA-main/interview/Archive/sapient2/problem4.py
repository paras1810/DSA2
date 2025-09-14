dict1={
    'A':1,
    'B':{
        'C':1,
        'D':2
    },
    'E':{
        'F':{
            'G':1
        }
    },
    'H':[{
        'I':3
    },
    {
        'J':5
    }]
}
o1=['E', 'F', 'G']
def json_func(dict2, list2):
    # for key, val in dict2.items():
    #     if key==list2[0] and len(list2)>1 and type(key)==dict:
    #print(list2)
    n=len(list1)
    for i in range(0,n):
        if list2[i] in dict2 and i!=n-1 and type(dict2[list2[i]])==dict:
            json_func(dict2[list2[i]], list2[i+1:n])
            #print(list2[i])
        elif list2[i] in dict2 and i==n-1:
            return dict2[list2[i]]
        else:
            return "Not Found"
list1=['E', 'F', 'G']
#list1=['H', 1, 'J']
print(json_func(dict1, list1))

