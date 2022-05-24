#define a function that can calculate the number of fragments this sequence will be cut into
def countcuts(seq):
    n=seq.count('GAATTC')
    fargment = n + 1
    print(fargment)
#input the given sequence
seq = 'ATGCAATCGACTACGATCAATCGAGGGCC'
#conduct the function
countcuts(seq)

