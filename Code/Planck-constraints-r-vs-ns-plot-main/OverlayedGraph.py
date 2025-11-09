import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from pathlib import Path
import numpy as np
import math
import scipy

# Load background PNG
observationalPlanckGraph = mpimg.imread(r"/Users/rhysabercromby/Documents/University/Year 4/Phys450 - Masters Project/Code/Planck-constraints-r-vs-ns-plot-main/2208.00188 graph cropped.png")
height, width, _ = observationalPlanckGraph.shape

planckMass = 2.43e18
As = 2.0967241e-09
qValues = [q for q in np.linspace(0.3810912789127891, 0.6868, 100000)]

parentFolder = Path(__file__).parent

def equation(N, q):
    N = N.item()
    return N - 60.4 - math.log((((12 * math.pi**2 * planckMass**4 * As*((2 + math.sqrt(2)*q)**2))/(q**2 * N**2))**(1/4)) * (1/(1e16))) - (0.5) * math.log(((1 - 1/(2 * q**2 * N))**2) / ((math.sqrt(2)*q + 2)**2))

def findingN():
    NValues = []
    for q in qValues:
        NValue = scipy.optimize.fsolve(equation, 50, args=(q,))
        NValues.append(NValue[0])

    return NValues
NValues = findingN()

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


def plot_planck_constraints():
    dpi = 300
    fig, ax = plt.subplots(figsize=(width/dpi, height/dpi), dpi=dpi)
    # plt.xlim(0.94, 1.0)
    # plt.ylim(0, 0.2)
    x_min, x_max = 0.9301, 1.0
    y_min, y_max = 0, 0.1798

    # Show the image in those coordinates
    ax.imshow(observationalPlanckGraph,
               extent=[x_min, x_max, y_min, y_max],
               aspect='auto')

    ax.plot(n_sValues, rValues, label="Starobinsky Inflation", color='blue')
    ax.plot(n_sReducedValues, rReducedValues, label=r"Starobinsky Inflation, $N_* \rightarrow N_* - 10$", color='red')
    ax.set_yticks([0.05, 0.1, 0.15])

    ax.set_xticks([0.94, 0.96, 0.98, 1.0])
    # Add labels, title, and legend
    plt.xlabel('$n_s$ (Spectral Index)', fontsize=14)
    plt.ylabel('$r$ (Tensor-to-Scalar Ratio)', fontsize=14)
    plt.title('Planck Constraints on $n_s$ and $r$', fontsize=16)
    plt.legend(fontsize=12)

    # Display grid and plot
    # plt.grid(True, linestyle='--', alpha=0.7)

    # plt.axis('off')
    imageName = Path(parentFolder, "Overlayed Graph.png")
    plt.savefig(imageName)


plot_planck_constraints()

