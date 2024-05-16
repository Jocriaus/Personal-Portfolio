class designAlgo:

    def selection_sort( sample_list ):
        # time of completion one hour and thirty mins
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
    
    
