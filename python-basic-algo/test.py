
for y in range(len(sample_list)):
    for x in range(len(sample_list), -1, -1):
        if x-2 >=0:
            current_var = sample_list[x-1]
            current_next_var = sample_list[x-2]
            if current_var < current_next_var:
                print("swap")
                sample_list[x-1] = current_next_var        
                sample_list[x-2] = current_var



