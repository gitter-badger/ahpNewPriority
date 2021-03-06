import numpy as np


def geom_avg(vals):
    rval=1.0
    count = 0
    for val in vals:
        val = vals[count]
        if val != 0:
            rval *= val
            count+=1
    if count != 0:
        rval = pow(rval, 1.0/count)
    return(rval)

def geom_avg_mat(mat, coeffs = None):
    size = mat.shape[0]
    rval = np.ones([size])
    for row in range(size):
        if np.any(coeffs):
            theRow = mat[row,:] * np.array(coeffs)
        else:
            theRow = mat[row,:]
        rval[row] = geom_avg(theRow)
    return(rval)

def be_priorities(mat, error = 1e-10):
    size = mat.shape[0]
    vec = np.ones([size])
    diff = 1
    count=0
    while diff >= error and count < 100:
        nextv = geom_avg_mat(mat, vec)
        #nextv = nextv/max(nextv)
        diff = max(abs(nextv - vec))
        vec = nextv
        count+=1
    return(vec/sum(vec))

def power_avg(mat, vec):
    size = mat.shape[0]
    rval = np.ones([size])
    for row in range(size):
        powSum=0
        for col in range(size):
            if mat[row,col]!=0:
                powSum += vec[col]
                rval[row] *= mat[row,col] ** vec[col]
        if powSum > 0:
            rval[row] = rval[row] ** (1/powSum)
    return(rval)

def b_priorities2(mat, error = 1e-10, maxCount = 1000):
    size = mat.shape[0]
    vec = np.ones([size])
    diff = 1
    count=0
    while diff >= error and count < maxCount:
        nextv = power_avg(mat, vec)
        diff = max(abs(nextv/max(nextv) - vec/max(vec)))
        vec = nextv
        count += 1
    return(vec/sum(vec))