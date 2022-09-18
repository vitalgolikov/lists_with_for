############## TASK 1 #########################
my_list = [1,2,3,4,5,6,101,102,103]
for number in my_list:
    if number > 100:
        print(number)

############## TASK 2 #########################
my_list = [1,2,3,4,5,6,101,102,103]
my_results =[]
for number in my_list:
    if number > 100:
        my_results.append(number)
print(my_results)


############## TASK 3 #########################
my_list = [1,2,3,4,5,6,101,102,103]
if len(my_list)<2:
    my_list.append(0)
else:
    my_list.append(my_list[-1]+my_list[-2])
print(my_list)
