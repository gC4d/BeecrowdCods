try:
    while True:
        m,n = [int(x) for x in input().split()]
        mFact = 1
        nFact = 1    
        for i in range(1,n+1): 
            nFact = nFact * i 
        for i in range(1,m+1): 
            mFact = mFact * i 
        print(nFact+mFact)
except EOFError:
    pass