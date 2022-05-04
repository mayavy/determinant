def det_matrix(matrix):
    '''input : a nested list square matrix
    output :a float scaler
    if unable to execute, raises error ? : True'''
    
    from copy import deepcopy
    m=deepcopy(matrix)
    try:
        if len(m)==1:
                det=m[0]
                return det
            
        to_sum=[]
        uniq=list(set(map(len, m)) ) 
        if len(uniq)==1 and uniq[0]== len(m): # check is matrix square
            
            if len(m)==2: 
                det= (m[0][0]*m[1][1])-(m[0][1]*m[1][0])
                return det
            
            elif len(m) > 2:
                
                for column in range(len(m)):
                    ele= m[0][column]      
                    sub=deepcopy(m)[1:]
                    for row in range(len(sub)):
                        del sub[row][column]   # delete columnth element from each row of sub matrix
                    
                    to_sum+=[pow(-1,column)*ele*det_matrix(sub)]
                   
            det=sum(to_sum)      
            return det

        else:
            error=TypeError('INPUT IS NOT A SQUARE MATRIX')
            raise error
        
            
    except TypeError:
        print('INPUT IS NOT A SQUARE MATRIX')
