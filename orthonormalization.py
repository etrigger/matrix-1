def orthonormalize(L):
    '''
    Input: a list L of linearly independent Vecs
    Output: A list T of orthonormal Vecs such that for all i in [1, len(L)],
            Span L[:i] == Span T[:i]
    '''
    from orthogonalization import orthogonalize
    from math import sqrt
    
    return [ v/sqrt(v*v) for v in orthogonalize(L) ]


def aug_orthonormalize(L):
    '''
    Input:
        - L: a list of Vecs
    Output:
        - A pair Qlist, Rlist such that:
            * coldict2mat(L) == coldict2mat(Qlist) * coldict2mat(Rlist)
            * Qlist = orthonormalize(L)
    '''
    
    from matutil import mat2coldict,coldict2mat
    from mat import Mat
    from vec import Vec
    
    Qlist = orthonormalize(L)
    Rlist = list(mat2coldict((coldict2mat(Qlist)).transpose()*coldict2mat(L)).values())
    
    return Qlist,Rlist
    
