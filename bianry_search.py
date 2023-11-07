'''
Problem:
We Need to write a program to find the position of a given number in a list of 
numbers arranged in decreasing order. We also need to minimize the number of 
times we access elements from the list.

Input:
cards = [13,11,10,9,7,3,2,0,-1]
query = 7

Output:
postion = 4
'''
'Linear Search Apporach'
def locate_card(cards,query):
    turn = 0
    # Create a varibale position with the value 0
    pos = 0
    # Set up a loop for repetition
    while pos < len(cards):
        # Check if element at the current position match the query
        if cards[pos] == query:
            # Answer found! Return and exit
            return pos,turn
        # increment the position
        pos+=1
        turn += 1
    
    return -1
    

        
    

print('Postion: ',locate_card([13,11,10,9,7,3,2,0,-1],7))





'Binary Search Approach'
def Locate_Card(cards,query):
    Left,Right = 0,len(cards)-1

    while Left <= Right:
        mid = (Left+Right)//2
        mid_number = cards[mid]
        
        if mid_number == query:
            return mid
        elif mid_number < query:
            Left = mid + 1
        elif mid_number > query:
            Right = mid - 1
    return -1

print('Postion: ',Locate_Card([13,10,7,2,0,-1],7))

'''What if there are same target numbers, with different position
we need to find position of first target number
just like above, it giving output as 3 but we expected 2.
'''

def test_location(cards,query,mid):
    mid_number = cards[mid]
    #print(f'mid: {mid} mid_number: {mid_number}')
    if mid_number == query:
        if mid-1 >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'left'
    else:
        return 'right'

     
def Refined_Locate_Card(cards,query):
    Left,Right = 0,len(cards)-1

    while Left <= Right:
        mid = (Left+Right)//2
        #mid_number = cards[mid]
        
        result = test_location(cards,query,mid)

        if result == 'found':
            return mid
        elif result == 'left':
            Right = mid - 1
        elif result == 'right':
            Left = mid + 1
    return -1
print(Refined_Locate_Card([13,10,7,2,0,-1],7))