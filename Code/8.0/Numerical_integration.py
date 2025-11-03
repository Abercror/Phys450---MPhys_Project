import scipy
import numpy as np
import math
from pathlib import Path
import matplotlib.pyplot as plt

planckMass = 2.43e18
As = 2.0967241e-09
# qValues = [q for q in np.linspace(0.282, 0.6868, 100000)]
qValues = [q for q in np.linspace(0.3810912789127891, 0.6868, 100000)]
parentFolder = Path(__file__).parent

def equation(N, q):
    N = N.item()
    return N - 60.4 - math.log((((12 * math.pi**2 * planckMass**4 * As*((2 + math.sqrt(2)*q)**2))/(q**2 * N**2))**(1/4)) * (1/(10e16))) - (0.5) * math.log(((1 - 1/(2 * q**2 * N))**2) / ((math.sqrt(2)*q + 2)**2))

def findingN():
    NValues = []
    for q in qValues:
        NValue = scipy.optimize.fsolve(equation, 50, args=(q,))
        NValues.append(NValue[0])

    return NValues
NValues = findingN()

def findingV_0():
    V_0Values = []
    for q, N in zip(qValues, NValues):
        V_0 = ((12 * math.pi**2 * planckMass**4 * As) / (q**2 * N**2 * ((1 - 1/(2 * q**2 * N))**2)))**(1/4)
        V_0Values.append(V_0)
    return V_0Values
V_0Values = findingV_0()

def finding_ns_r():
    n_sValues = []
    rValues = []
    for q, N in zip(qValues, NValues):
        n_s = 1 - (2/N) - (3 / (q**2 * N**2))
        r = 8 / (q**2 * N**2)
        rValues.append(r)
        n_sValues.append(n_s)

    return n_sValues, rValues
n_sValues, rValues, = finding_ns_r()

def finding_ns_rReduced():
    n_sValues = []
    rValues = []
    for q, N in zip(qValues, NValues):
        n_s = 1 - (2/(N-10)) - (3 / (q**2 * (N-10)**2))
        r = 8 / (q**2 * (N-10)**2)
        rValues.append(r)
        n_sValues.append(n_s)

    return n_sValues, rValues
n_sReducedValues, rReducedValues, = finding_ns_rReduced()

def findingV_end():
    V_endValues = []
    for q, v in zip(qValues, V_0Values):
        V_end = (v*((2 + math.sqrt(2) * q)**2)**(1/4))
        V_endValues.append(V_end)
    return V_endValues
V_endValues = findingV_end()

def findingw():
    wValues = []
    for q, N in zip(qValues, NValues):
        w = (2/3)*(1/(2 * q**2 * N**2)) - 1
        wValues.append(w)
    return wValues
wValues = findingw()

def PlanckData():
    n_s = 0.9649
    n_sError = 0.0049
    n_sUpper = n_s + n_sError
    n_sLower = n_s - n_sError

    rMax = 0.0028

    

def graph(xValues, yValues, xLabel, yLabel, title, name):
    fig, ax = plt.subplots()
    ax.plot(xValues, yValues)
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    ax.set_title(title)
    figureName = Path(parentFolder, f'{name}.png')
    plt.savefig(figureName)
    plt.show()


# def setq():
#     q = math.sqrt(2/3)
#     NSetqValue = scipy.optimize.fsolve(equation, 50, args=(q,))
#     V_0SetqValue = ((12 * math.pi**2 * planckMass**4 * As) / (q**2 * NSetqValue**2 * ((1 - 1/(2 * q**2 * NSetqValue))**2)))**(1/4)
#     n_sSetqValue = 1 - (2/NSetqValue) - (3 / (q**2 * NSetqValue**2))
#     rSetqValue = 8 / (q**2 * NSetqValue**2)

#     values = f"N = {NSetqValue}, V_0^1/4 = {V_0SetqValue}, n_s = {n_sSetqValue}, r = {rSetqValue}"
#     print(values)``
    



# graph(qValues, NValues, r"$q$", r"$N_*$", r"$N_*(q)$", "N*(q)")
graph(qValues, V_0Values, r"$q$", r"$V_0^{\frac{1}{4}}(q)$, GeV", r"$V_0^{\frac{1}{4}}(q)$", "V_0(q) reduced q—±")
# graph(n_sValues, rValues, r"$n_s$", r"$r$", r"$r$ against $n_s$", "r against n_s")
# graph(n_sReducedValues, rReducedValues, r"$n_s$", r"$r$", r"$r$ against $n_s \quad N_* - 10$", "r against n_s N_* reduced")
# graph(qValues, V_endValues, r"$q$", r"$V_{end}^{\frac{1}{4}}(q)$, GeV", r"$V_{end}^{\frac{1}{4}}(q)$", "V_end(q)")
# graph(NValues, wValues, r"$N_*$", r"$w(N_*)$", r"$w(N_*)$", "w(N) corrected")

# setq()