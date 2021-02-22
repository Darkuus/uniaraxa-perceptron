import numpy as np

numEpocas = 70000
q = 6

peso = np.array([113,122,107,98,115,120])
ph = np.array([6.8,4.7,5.2,3.6,2.9,4.2])

bias = 1

X  = np.vstack((peso, ph))
Y  = np.array([-1, 1, -1, -1, 1, 1])

eta = 0.1

W = np.zeros([1, 3])

e = np.zeros(6)

#degrau bipolar
def funcaoAtivacao(valor):
    if valor < 0.0:
        return(-1)
    else:
        return(1)

for j in range(numEpocas):
    for k in range(q):
        Xb = np.hstack((bias, X[:, k]))

        V = np.dot(W, Xb)

        Yr = funcaoAtivacao(V)
        e[k] = Y[k] - Yr

        W = W + eta*e[k]*Xb

print("V de Erros (e) = " + str(e))

