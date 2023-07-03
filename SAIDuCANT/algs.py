"""Pseudocode implementations from page 5 and 6"""
from math import ceil

# Algorithm 1:
def DERIVEPERIODICPARAMETERS(Log,i):
    f_imin, f_imax = 0, float('inf')
    k = 1
    for M_im in Log:
        # TODO: define FindPreviousTimestamp()
        T_lm = FindPreviousTimestamp()
        # TODO: figure out l and m
        Lcur = T_lm - C(l,m)
        # d.i : T(i,k), C(i,k)
        Hcur = T(i,k) - C(i,k)
        if k > 2:
            delL = Lcur - Hpast
            delH = Hcur - Lpast
            if delL > f_imin and delH < f_imax:
                f_imin,f_imax = delL,delH
        Lpast,Hpast = Lcur,Hcur
        k = k+1
    P_i = f_imin
    J_i = f_imax - f_imin
    return (P_i,J_i)

# Algorithm 2:
def DETECT(k,P_i,R_i,T_ik=T(i,k),phi_i=T(i,1)-C(i)):
    min_ts = phi_i + (P_i*k)
    max_ts = min_ts + R_i
    next_mints = min_ts + P_i
    next_maxts = max_ts + P_i
    if T_ik > next_maxts:
        k = ceil((T_ik-phi_i)/P_i)
        return 0
    if min_ts<=T_ik<=max_ts:
        # normal
        return 0
    if max_ts<=T_ik<next_mints:
        # normal
        return 0
    else:
        # anomalous
        return 1