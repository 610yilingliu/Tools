def binomial(n,k):

    if 0<=k<=n:
        ntok=1
        ktok=1
        for t in range(1,min(k,n-k)+1):
            ntok*=n
            ktok*=t
            n-=1
        return ntok//ktok
    else:
        return 0

def hypergeom(N,M,n,k):
    """
    N:  number of items
    M:  designated items(total)
    n:  number to select
    k:  how many designated items will be selected
    """
    a=binomial(M,k)
    b=binomial((N-M),(n-k))
    c=binomial(N,n)
    pk=a*b/c
    if pk>0:
        print(pk*100,'%')
    else:
        print('100%')