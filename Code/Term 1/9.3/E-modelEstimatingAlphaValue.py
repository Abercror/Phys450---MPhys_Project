import scipy
import numpy as np
import math
from pathlib import Path
import matplotlib.pyplot as plt


parentFolder = Path(__file__).parent
graphsFolder = Path(parentFolder, "E-model Graphs")
graphsFolder.mkdir(parents=True, exist_ok=True)

planckMass = 2.43e18
As = 2.0967241e-09
alphaValues = [alpha for alpha in np.linspace(0.001, 5.83, 1000)]


V0_50 = []
V0_60 = []
m_50 = []
m_60 = []
ns_50 = []
ns_60 = []
r_50 = []
r_60 = []


def V0MassCalculation(N, VArray, mArray):
    for alpha in alphaValues:
        V0 = ((24 * (math.pi**2) * (planckMass**4) * As * ((3 * alpha)/(4*N**2))) / ((1 - ((3*alpha)/(4*N)))**2))**(1/4)
        m = ((4 * (V0**4))/(3 * alpha * (planckMass**2)))**(1/2)
        VArray.append(V0)
        mArray.append(m)


def nsRCalculation(N, nsArray, rArray):
    for alpha in alphaValues:
        ns = 1 - 2/N
        r = (12*alpha)/(N**2)
        nsArray.append(ns)
        rArray.append(r)


def graph(xData1, yData1, linelabel1, xData2, yData2, linelabel2, xLabel, yLabel, title, imagename):
    fig, ax = plt.subplots()
    ax.plot(xData1, yData1, label=linelabel1)
    ax.plot(xData2, yData2, label=linelabel2)
    ax.set_xlabel(xLabel)
    ax.set_ylabel(yLabel)
    ax.set_title(title)
    plt.legend()
    filename = Path(graphsFolder, imagename)
    plt.savefig(filename)

def main():
    for N in [50]:
        V0MassCalculation(N, V0_50, m_50)
        nsRCalculation(N, ns_50, r_50)
    for N in [60]:
        V0MassCalculation(N, V0_60, m_60)
        nsRCalculation(N, ns_60, r_60)

    graph(alphaValues, V0_50, r"$N = 50$", alphaValues, V0_60, r"$N = 60$", r"$\alpha$", r"$V_{0}^{\frac{1}{4}}(\alpha)$", r"$V_0^{\frac{1}{4}}(\alpha)$", "E-model V0 against alpha.png")
    graph(alphaValues, m_50, r"$N = 50$", alphaValues, m_60, r"$N = 60$", r"$\alpha$", r"$m(\alpha)$", r"$m(\alpha)$", "E-model mass against alpha.png")
    graph(ns_50, r_50, r"$N = 50$", ns_60, r_60, r"$N = 60$", r"$n_s$", r"$r$", r"$n_s$ against $r$", "E-model r against ns.png")

main()