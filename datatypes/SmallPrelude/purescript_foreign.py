println = print
def combineIO(a):
    def ap(b):
        return b
    return ap

def discard(m):
    def ap(k):
        return k(m)
    return ap