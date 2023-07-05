"""Implmentation of equations on page 4 of the paper"""
from math import ceil
from algs import DERIVEPERIODICPARAMETERS

def fnR_i(q):
    return J_i + fnw_i(q,B_i + q*C_i) - q*P_i + C_i

def fnw_i(q,w_n):
    # d.i. : E() 
    inst = B_i + E(w_n + C_i) + q*C_i + I_i
    if w_n == inst:
        return w_n
    else:
        fnw_i(q,inst)

def fnt_i(t_n):
    # t_n = eq return t_n
    # d.i : E_i(t_n)
    inst = B_i + E_i(t_n) + sum(ceil((t_n + J(k))/P_i)*C(k) for k in range(1,i+1))
    if t_n == inst:
        return t_n
    else:
        fnt_i(inst)

# TODO: change cushion value
def F(seconds,cushion=5):
    return seconds*(30+cushion)

def E_i(t_i):
    return (31*tbit + max(C(k) for k in range(i,n+1)))*F(t_i) # d.i : F(t_i)

# return P and J for ID=i
def P_J(i):
    return DERIVEPERIODICPARAMETERS(Log,i)

if __name__ == "__main__":
    # taking i>=1 as the ith message in set M
    i = int(input("ID: "))
    n = int(input("Number of messages: ")) # size of set M
    Log = eval("Message Log: ")

    # d.i. : C(i) (define input) 
    P_i,J_i = P_J(Log,i)
    C_i = C(i)
    B_i = max(C(k) for k in range(i+1,n+1))
    t_i = fnt_i(C_i)
    Q_i = ceil((t_i + J_i)/P_i)
    R_i = max(fnR_i(q) for q in range(Q_i))
    
    # TODO: change as per bus speed
    tbit = 0.0003

    
    # d.i. : w_i, T(k)
    # J(k) = P_J(Log,k)[1]
    I_i = sum(ceil((w_i + P_J(Log,k[1]) + tbit)/T(k))*C(k) for k in range(1,i))