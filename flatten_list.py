array = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
my_list = []
def flatten(array):

    for i in array:
        if type(i) == list:
            flatten(i)
        else:
            my_list.append(i)


for i in array:
    if type(i) == list:
        flatten(i)
    else:
        my_list.append(i)
print(my_list)


