def prime(n):
    return all([(n % j) for j in range(2, int(n**0.5)+1)]) and n>1

def print_factors(x):
    for i in range(1, x + 1):
        if x % i == 0:
            factors.append(i)
             

           

def strange_sum (L, R):
    
    for z in range(L,R+1):
        factors=[]
        print_factors(z)
        for i in factors:
            if prime(i):
                summ+=1 
            else:
                if i==1:
                    continue
                else:
                    for j in range (2,i):
                        a=i/j
                        if i%j==0:
                            while prime(i)!=1 and prime(j)!=1:
                                j
                                





T = int(input())
for _ in range(T):
    factors=[]
    summ=0
    L,R = map(int, input().split())
    out_ = strange_sum(L, R)
    print (out_)
