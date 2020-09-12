if __name__=='__main__':
    n,m = map(int,input().split())
    arr = list(map(int,input().split()))
    brr = list(map(int,input().split()))
    count = 0
    for i in range(max(arr),min(brr)+1):
        flag = True
        for j in arr:
            if i%j!=0:
                flag = False
                break
        if flag:
            for k in brr:
                if k%i!=0:
                    flag = False
                    break
        if flag:
            count+=1
    print(count)