n = int(input())
nth = 666
count = 0

while True:
    if '666' in str(nth):   
        count+=1            
        # print(count)
    if count == n:          
        print(nth)          
        break               
    nth+=1 
    # print(nth)