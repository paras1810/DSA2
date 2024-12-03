import copy
def check_recur(d, g):
    for key, value in d.items():
        if (isinstance(value, dict)):
            check_recur(d[key], g[key])
        else:
            if key[0] == '$':
                g.pop(key)
        print(type(value))


if __name__ == "__main__":    
    d = {   
        'a' : {
            'b':{
                '$abc' : 'Pars',
                'c' : 'Ris'
            },
            'd':{
                'e':"Shubham"
            },
            '$fgh': "Suraj"
        },
        '$pqr': "Abcde"
    }
    g = copy.deepcopy(d)
    check_recur(d, g)
    print(g)