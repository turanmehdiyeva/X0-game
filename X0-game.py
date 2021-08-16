def X0():
    import numpy as np
    arr = np.arange(1,10).astype(str).reshape(3,3)
    for i in range(9):
        a = input('Enter X or 0: ')
        x = input('Enter position: ')
        item_index = np.where(arr==x)
        c = item_index[0][0]
        d = item_index[1][0]
        arr[c,d] = a
        print(arr)
        if list(arr[[0,1,2],[0,1,2]])==list('X'*3) or (list(arr[[2,1,0],[0,1,2]])==list('X'*3)) or (list(arr[0,:])==list('X'*3)) or (list(arr[1,:])==list('X'*3)) or (list(arr[2,:])=='X') or (list(arr[:,0])==list('X'*3)) or (list(arr[:,1])==list('X'*3)) or (list(arr[:,2])==list(3*'X')):
            return 'Game over X won'
        elif list(arr[[0,1,2],[0,1,2]])==list('0'*3) or (list(arr[[2,1,0],[0,1,2]])==list('0'*3)) or (list(arr[0,:])==list('0'*3)) or (list(arr[1,:])==list('0'*3)) or (list(arr[2,:])=='0') or (list(arr[:,0])==list('0'*3)) or (list(arr[:,1])==list('0'*3)) or (list(arr[:,2])==list(3*'0')):
            return'Game over 0 won'
        else:
            continue
    print('No winner')
    
print(X0())
