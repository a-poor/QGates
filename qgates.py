"""
qgates.py

created by Austin Poor
"""

from typing import Union, Iterable

from functools import reduce as _reduce
from operator import matmul as _matmul

import numpy as np

__version__ = "0.0.5"


def tens(a: Union[int,float,list,np.ndarray],*b: Union[int,float,list,np.ndarray]):
    """
    Computes the tensor product of
    two (or more) vectors/matrices.

    :param a: Start value for tensor product
    :param b: One or more other values for tensor product
    """
    return _reduce(np.kron,b,a)

def matmul(a: np.ndarray,*b: np.ndarray):
    """
    Performs matrix multiplication between
    two or more 

    :param a: Start value for matrix multiplication
    :param b: One or more other values for tensor product
    """
    return _reduce(_matmul,b,a)

def state(arr: Union[int,Iterable]):
    """Creates a state vector
    from either an iterable of
    1s and 0s (or from an int that
    will be converted to a state
    vector based on its binary
    representation.

    :param arr: Int or iterable for creating state vector
    """
    if isinstance(arr,int):
        arr = [int(b) for b in bin(arr)[2:]]
    s = QB1 if arr[0] else QB0
    for n in arr[1:]:
        if n == 0:
            s = tens(s,QB0)
        else:
            s = tens(s,QB1)
    return s


def conjugate(v: Union[complex,list,np.ndarray],*args,**kwargs):
    """
    Returns the complex conjugate of v.

    :param v: number, vector, or matrix to conjugate
    """
    return np.conjugate(v,*args,**kwargs)


### Defining some qubits to use
QB0  = np.array([1,0])
QB1  = np.array([0,1]) 
QB00 = tens(QB0, QB0)
QB01 = tens(QB0, QB1)
QB10 = tens(QB1, QB0)
QB11 = tens(QB1, QB1)


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


##### Bell States #####

BELL00 = 2**(-1/2)*state((0,0)) + 2**(-1/2)*state((1,1))
BELL01 = 2**(-1/2)*state((0,1)) + 2**(-1/2)*state((1,0))
BELL10 = 2**(-1/2)*state((0,0)) - 2**(-1/2)*state((1,1))
BELL11 = 2**(-1/2)*state((0,1)) - 2**(-1/2)*state((1,0))






