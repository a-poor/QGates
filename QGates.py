import numpy as np



def tens(a,b,*args):
    """
    Computes the tensor product of
    two (or more) vectors/matrices.
    """
    res = np.kron(a,b)
    for c in args:
        res = np.kron(res,c)
    return res


### Defining some qubits to use
QB0  = np.array([1,0])
QB1  = np.array([0,1]) 
QB00 = tens(QB0,QB0)
QB01 = tens(QB0,QB1)
QB10 = tens(QB1,QB0)
QB11 = tens(QB1,QB1)


### Defining some traditional gates
IDEN = np.array([
    [1,0],
    [0,1]])
NOT = np.array([
    [0,1],
    [1,0]])
OR = np.array([
    [1,0,0,0],
    [0,1,1,1]])
AND = np.array([
    [1,1,1,0],
    [0,0,0,1]])
XOR = np.array([
    [1,0,0,1],
    [0,1,1,0]])
NOR  = NOT @ OR
NAND = NOT @ AND
COPY = np.array([
    [1,0],
    [0,0],
    [0,0],
    [0,1]])
SWAP = np.array([
    [1,0,0,0],
    [0,0,1,0],
    [0,1,0,0],
    [0,0,0,1]])


### Defining some quantum gates
CNOT = tens(IDEN,XOR) @ tens(COPY,IDEN)
TOFFOLI = (
    tens(IDEN,IDEN,XOR) @
    (tens(IDEN,IDEN,AND,IDEN) @
    (tens(IDEN,SWAP,IDEN,IDEN) @
    tens(COPY,COPY,IDEN)))
    )
HAD = np.array([[1,1],[1,-1]]) * np.exp2(-1/2)






def state(arr):
    """Creates a state vector
    from either an iterable of
    1s and 0s (or from an int that
    will be converted to a state
    vector based on its binary
    representation.
    """
    if isinstance(arr,int):
        arr = [int(b) for b in list(bin(arr)[2:])]
    s = QB1 if arr[0] else QB0
    for n in arr[1:]:
        if n == 0:
            s = tens(s,QB0)
        else:
            s = tens(s,QB1)
    return s




##### Bell States #####

BELL00 = 2**(-1/2)*state((0,0)) + 2**(-1/2)*state((1,1))
BELL01 = 2**(-1/2)*state((0,1)) + 2**(-1/2)*state((1,0))
BELL10 = 2**(-1/2)*state((0,0)) - 2**(-1/2)*state((1,1))
BELL11 = 2**(-1/2)*state((0,1)) - 2**(-1/2)*state((1,0))






