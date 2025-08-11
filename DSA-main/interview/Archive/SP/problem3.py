result_list=[]
def flatten_list(ele):
    if type(ele)==list:
        for i in ele:
            flatten_list(i)
    else:
        result_list.append(ele)


#question_list=[67, [24, [36, 40], 5], 6, [31, [6, 87]]]
question_list=[67, [24, [36, [40, [50, 60],71]], 5], 6, [31, [6, 87]]]
#for i in question_list:
flatten_list(question_list)
print(result_list)
