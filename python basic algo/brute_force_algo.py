class designAlgo:

    def selection_sort( sample_list ):
        # no repeating numbers should be inside the array
        # duration : one hour and thirty mins
        for x in range(len(sample_list)):
            # for x is equal to the value that we compare
            current_var = sample_list[x]
            smaller_var = current_var
            for y in range(len(sample_list)-x):
                # for y is equal to the value that we compare x to
                if smaller_var > sample_list[y+x] :
                    smaller_var = sample_list[y+x]

            if current_var != smaller_var:    
                # if the current value has its place as the next smaller value
                sample_list[sample_list.index(smaller_var)] = current_var        
                sample_list[x] = smaller_var    
    
    def bubble_sort( sample_list ):    
        # duration: thirty mins
        for y in range(len(sample_list)):
            for x in range(len(sample_list), -1, -1):
                # will start at the end of the array 
                # putting the largest to the furtherst index
                if x-2 >=0:
                    current_var = sample_list[x-1]
                    current_next_var = sample_list[x-2]
                    if current_var < current_next_var:
                        print("swap")
                        sample_list[x-1] = current_next_var        
                        sample_list[x-2] = current_var
    
    def sequential_search(sample_list, value):
        # duration: ten mins
        index = 0
        found = False
        for x in range(len(sample_list)):
            if value == sample_list[x]:
                index = x
                found = True
                break


    
