import pdb
def count_zeros(m): 
    pdb.set_trace()																			
    high = len(m[0]) - 1                                                                            
    count = 0                                                                                       
    for i in range(len(m)):                                                                         
        low = 0                                                                                     
        if m[i][high] == 0:                                                                         
            # All zeros in this row                                                                 
            count += high + 1                                                                       
            continue                                                                                
        if m[i][low] == 1:                                                                          
            # No more zeros around                                                                  
            break                                                                                   
        while low <= high:                                                                          
            # Binary search for the                                                                 
            # first one of the row                                                                  
            mid = (low + high)/2                                                                    
            if m[i][mid] == 1:                                                                      
                high = mid - 1                                                                      
                if m[i][mid - 1] == 0:                                                              
                    break                                                                           
            else:                                                                                   
                low = mid + 1                                                                       
        count += high + 1                                                                           
    return count                                                                                      
count_zeros([[0, 0, 1],                                                                      
            [0, 1, 1],                                                                      
            [1, 1, 1]])