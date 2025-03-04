def helper(given : dict) -> None:
    temp = range(list(given.keys())[-1], -1, -1)
    for each in temp:
        for other in given[each]:
            print(other, end='\t')
        print()
        
def solution(n, w, num):
    sol = dict()
    maxfloor = 0
    if(n % w == 0):
        maxfloor = n // w
    else :
        maxfloor = n // w + 1
        
    count = 1 
    for each in range(maxfloor):
        storage = list()
        for other in range(w):
            if(count <= n):
                if(each % 2 == 0):
                    storage.append(count)
                    count = count + 1

                else:
                    storage.insert(0, count)
                    count = count + 1
            else:
                if(each % 2 == 0):
                    storage.append('N')
                else:
                    storage.insert(0, 'N')
                
        sol[each] = storage
        
    # sample = {0:[1,2,3,4,5,6], 1:[12,11,10,9,8,7], 2:[13,14,15,16,17,18], 3:['N', 'N', 22, 21, 20, 19]}
    helper(sol)
    
    
    # find its index
    idx = -1
    where = -1
    for each in sol:
        if(num in sol[each]):
            where = each
            idx = sol[each].index(num)
    
    answer = 0
    for each in sol:
        if(each >= where):
            if('N' != sol[each][idx]):
                answer = answer + 1
    
    
    return answer
