import scipy
import numpy as np
import math
from pathlib import Path
import matplotlib.pyplot as plt

parentFolder = Path(__file__).parent
graphsFolder = Path(parentFolder, "3 T-model Graphs")
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
        V0 = ((72 * (math.pi**2) * (planckMass**4) * As * alpha)/(N**2 - 3 * alpha * N))**(1/4)
        m = (((V0**4))/(3 * alpha * (planckMass**2)))**(1/2)
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

    graph(alphaValues, V0_50, r"$N = 50$", alphaValues, V0_60, r"$N = 60$", r"$\alpha$", r"$V_{0}^{\frac{1}{4}}(\alpha)$", r"$V_0^{\frac{1}{4}}(\alpha)$", "T-model V0 against alpha.png")
    graph(alphaValues, m_50, r"$N = 50$", alphaValues, m_60, r"$N = 60$", r"$\alpha$", r"$m(\alpha)$", r"$m(\alpha)$", "T-model mass against alpha.png")
    graph(ns_50, r_50, r"$N = 50$", ns_60, r_60, r"$N = 60$", r"$n_s$", r"$r$", r"$n_s$ against $r$", "T-model r against ns.png")

main()








































# alphaValues = [alpha for alpha in np.linspace(0.001, 5.83, 1000)]

# planckMass = 2.43e18
# As = 2.0967241e-09
# inflatonMass = 3e13


# def findingV0():
#     V0Values = []
#     for alpha in alphaValues:
#         alpharoot = math.sqrt((4/3*alpha) + 1)
#         V0 = (As * 18 * (math.pi**2) * (planckMass**4) * alpha * ((((4*N)/(3*alpha)) + alpharoot + 1)**2))**(1/4)
#         V0Values.append(V0)
#     return V0Values
# V_0Values = findingV0()


# def finding_ns_r():
#     n_sValues50 = []
#     rValues50 = []

#     n_sValues60 = []
#     rValues60 = []
#     for N in [50]:
#         for alpha in alphaValues:
#             n_s = 1 - (2/N)
#             r = (12 * alpha)/(N**2)
#             rValues50.append(r)
#             n_sValues50.append(n_s)

#     for N in [60]:        
#         for alpha in alphaValues:
#             n_s = 1 - (2/N)
#             r = (12 * alpha)/(N**2)
#             rValues60.append(r)
#             n_sValues60.append(n_s)

#     return n_sValues50, rValues50, n_sValues60, rValues60
# n_sValues50, rValues50, n_sValues60, rValues60 = finding_ns_r()


# def graph(xData, yData, linelabel, xLabel, yLabel, title, imagename):
#     fig, ax = plt.subplots()
#     ax.plot(xData, yData, label=linelabel)
#     ax.set_xlabel(xLabel)
#     ax.set_ylabel(yLabel)
#     ax.set_title(title)
#     plt.legend()
#     filename = Path(graphsFolder, imagename)
#     plt.savefig(filename)


# graph(alphaValues, V_0Values, "T-model", r"$\alpha$", r"$V_{0}^{\frac{1}{4}}$", r"T-model: $V_{0}^{\frac{1}{4}}$ against $\alpha$", "T-model V_0 against alpha.png")


# def graph_n_s_r():
#     fig, ax = plt.subplots()
#     ax.plot(n_sValues50, rValues50, label=fr"$N = 50$")
#     ax.plot(n_sValues60, rValues60, label=fr"$N = 60$")
#     ax.set_xlabel(r"$n_s$")
#     ax.set_ylabel(r"$r$")
#     ax.set_title(r"T-model: $n_s$ against $r$")
#     plt.legend()
#     filename = Path(graphsFolder, "T-model n_s against r.png")
#     plt.savefig(filename)

# graph_n_s_r()



# # def alphaValueSelection():
# #     NValuesArray = np.array(NValues)

# #     N50Index = np.argmin(np.abs(NValuesArray - 50))
# #     N60Index = np.argmin(np.abs(NValuesArray - 60))
    
# #     alpha50 = alphaValues[N50Index]
# #     alpha60 = alphaValues[N60Index]

# #     return alpha50, alpha60

# # alpha50, alpha60 = alphaValueSelection()
# # print(alpha50)
# # print(alpha60)