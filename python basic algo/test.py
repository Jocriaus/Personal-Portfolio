sample_list = [5, 32, 34,234,1,3,8,21, 7, 4, 723, 22,6]
last = []

for x in range(len(sample_list)):
    # for x is equal to the value that we compare
    print(sample_list)
    current_var = sample_list[x]
    smaller_var = current_var
    #print(x)
    #print("x is " + str(current_var))
    for y in range(len(sample_list)-x):
        # for y is equal to the value that we compare x to
        #print("current run is " + str(sample_list[y+x]))
        if smaller_var > sample_list[y+x] :
            smaller_var = sample_list[y+x]
            #print("smaller is " + str(sample_list[y+x]) + " than " + str(current_var))
    
    #print(current_var)
    #print(smaller_var)
    if current_var != smaller_var:    
        sample_list[sample_list.index(smaller_var)] = current_var        
        sample_list[x] = smaller_var    
        #print(sample_list)


print(sample_list)

