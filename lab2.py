#!/usr/bin/python 
#acleetus

guide = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}

def areComplementary(strand1, strand2):
    global guide
    if (len(strand2) != len(strand1)):
        return False
    for x in xrange(len(strand1)):
        if (strand1[x] != guide.get(strand2[x])):
            return False
        elif ((strand1[x] not in guide.keys()) or (strand2[x] not in guide.keys())):
            return False
    return True

def targetAtIndex(strand, target, i):
    strand = strand[i:]
    if (len(strand) < len(target)):
        return False
    for x in xrange(1,len(target)):
        if(target[x] == '.'):
            pass
        elif(target[x] == 'x'):
                if (strand[x] == 'A' or strand[x] == 'T'):
                    pass
                return False
        elif(target[x] == 'y'): 
                if (strand[x] == 'C' or tax`rget[x] == 'G'):
                    pass
                return False
        elif (strand[x] == target[x]):
            pass
    return True

def findTarget(strand, target):
    if (len(target) > len(strand)):
        return -1
    for x in xrange(0,len(target)):
        if ((targetAtIndex(strand, target, (x-1)) is True):
            return x
    return -1

def testAreComplementary():
    print "Testing areComplementary..."
    assert(areComplementary("A", "T") == True)
    assert(areComplementary("CTAGG", "GATCC") == True)
    assert(areComplementary("CTA", "GATT") == False)
    assert(areComplementary("CTACGC", "GAT") == False)
    assert(areComplementary("GGcT", "CCGA") == False)
    print "All tests passed!"

def testAtIndex():
    print "Testing targetAtIndex..."
    assert(targetAtIndex("A","A",0) == True)
    assert(targetAtIndex("AAAT","AT",2) == True)
    assert(targetAtIndex("AAAT","xT",2) == True)
    assert(targetAtIndex("GCCATA","yA.",2) == True)
    assert(targetAtIndex("GCCATA","TAC",4) == False)
    print "All tests passed!"x`

def testFindTarget():
    print "Testing findTarget..."
    assert(findTarget("A", "A") == 0)
    assert(findTarget("ATCGGA", "GAT") == -1)
    assert(findTarget("ATACGTG","ACGT") == 2)
    assert(findTarget("TTAGTTA","xyT.") == 2)
    print "All tests passed!"

testAreComplementary()
testAtIndex()
testFindTarget()
