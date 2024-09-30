n = int(input())
cnt = 0

if n%5==0:
    ans = int(n/5)
    print(ans)

else:
    if n%5!=0:
        ans = int(n/5)
        rest = n%5
        print(ans)
        if rest%3==0:
            ans += 1
            print(ans)
        