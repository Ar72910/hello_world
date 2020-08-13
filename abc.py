for _ in range(int(input())):
    s={}
    z={}
    n=int(input())
    a=[i for i in input().split(" ")]
    a=set(a)
    s=min(a)
    m1=int(min(a))
    a=a-s
    m2=int(min(a))
    print(m1+m2)
