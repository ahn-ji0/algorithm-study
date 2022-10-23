# 10972 https://www.acmicpc.net/problem/10972
# 런타임 에러

def main():
    
    N = int(input())
    
    arr = list(map(int,input().split()))

    left = []    
    stop = False
    
    while not stop:    
    
        if len(arr) == 1:
            break
        
        if arr[-1] > arr[-2]:
            left.append(arr.pop())
            val = arr.pop()
            left.append(val)
            arr.append(val + 1)
            left.remove(val+1)
            left.sort()
            arr = arr + left
            stop = True
        else:
            left.append(arr.pop())
    
    if stop == False:
        print('-1')
    else:
        print(' '.join(map(str,arr)))
main()
