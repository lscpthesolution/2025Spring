'''
dj = {0:[1,2,3], 1:[6,5,4], 2:[7,8,9]}
sy = {0:[1,6,7,12,13], 1:[2,5,8,11], 2:[3,4,9,10]}
hm = [[1,2,3], [6,5,4], [7,8,9], [12,11,10]]
'''

def helper(sample : dict) -> None :
    t = list(range(len(sample)))
    t.reverse()
    for each in t:
        for other in sample[each]:
            print(other, end='\t')
        print()


def solution(n, w, num):
    
    height = 0
    if(n % w == 0):
        height = n // w
    else:
        height = n // w + 1

    dj = dict()
    cnt = 0
    for x in range(height):                     # row
        temp = []
        for y in range(w):                      # col
            cnt = cnt +1
            if(cnt <= n):
                temp.append(cnt)
            else:
                temp.append('NaN')
        if(x % 2 == 1):
            temp.reverse()
        else:
            pass
        
        dj[x] = temp
        
        
    # print(dj)
    helper(dj)
            
        
        
        
    
    return height
















# def helper(given : dict) -> None:
#     temp = range(list(given.keys())[-1], -1, -1)
#     for each in temp:
#         for other in given[each]:
#             print(other, end='\t')
#         print()
        
# def solution(n, w, num):
#     sol = dict()
#     maxfloor = 0
#     if(n % w == 0):
#         maxfloor = n // w
#     else :
#         maxfloor = n // w + 1
        
#     count = 1 
#     for each in range(maxfloor):
#         storage = list()
#         for other in range(w):
#             if(count <= n):
#                 if(each % 2 == 0):
#                     storage.append(count)
#                     count = count + 1

#                 else:
#                     storage.insert(0, count)
#                     count = count + 1
#             else:
#                 if(each % 2 == 0):
#                     storage.append('N')
#                 else:
#                     storage.insert(0, 'N')
                
#         sol[each] = storage
        
#     # sample = {0:[1,2,3,4,5,6], 1:[12,11,10,9,8,7], 2:[13,14,15,16,17,18], 3:['N', 'N', 22, 21, 20, 19]}
#     helper(sol)
    
    
#     # find its index
#     idx = -1
#     where = -1
#     for each in sol:
#         if(num in sol[each]):
#             where = each
#             idx = sol[each].index(num)
    
#     answer = 0
#     for each in sol:
#         if(each >= where):
#             if('N' != sol[each][idx]):
#                 answer = answer + 1
    
    
#     return answer



# # def solution(n, w, num):
# #     answer = 0
# #     maxfloor = 0
# #     row = 0
    
# #     # maxfloor of n number of box with w
# #     if(n % w == 0):
# #         maxfloor = n // w
# #     else :
# #         maxfloor = n // w + 1
    
# #     # row and col of the target
# #     if(num % w == 0):
# #         row = num // w
# #     else :
# #         row = num // w + 1  # row
    
# #     col = num % w    # col
# #     if(row % 2 == 0):
# #         col = w - col + 1
    
# #     nleft = w * maxfloor - n
    
# #     if(maxfloor % 2 == 0):
# #         w * maxfloor - n 
        

# #     return maxfloor - row + 1