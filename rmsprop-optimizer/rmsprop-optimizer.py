import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    # Write code 
    w = np.asarray(w,dtype = float)
    g = np.asarray(g,dtype = float)
    s= np.asarray(s,dtype = float)

    s_n = beta*s + (1-beta)*g**2
    denom = s_n+ eps
    w_n= w - (lr/(np.sqrt(denom))*g)
    return (w_n,s_n)
    pass