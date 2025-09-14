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
    }
}
res=[]
def get_values(v, dict2):
    for key, val in dict2.items():
        if type(val)==dict:
            get_values(v, val)
        else:
            if val==v:
                res.append(key)
get_values(2, dict1)
print(res)
    
