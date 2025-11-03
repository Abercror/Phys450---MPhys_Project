# Import necessary libraries
import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np
import scipy
from pathlib import Path

planckMass = 2.43e18
As = 2.0967241e-09
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

def findingIndex(array, value):
    array = np.array(array)
    index = (np.abs(array - value)).argmin()
    return index

def findingq():
    qIndex1 = findingIndex(n_sValues, 0.95914609)
    qIndex2 = findingIndex(rValues, 0.01653658)

    print(qIndex1)
    print(qIndex2)
    if qIndex1 == qIndex2:
        N = NValues[qIndex1]
        q = qValues[qIndex1]

        return N, q
    
N, q = findingq()

print(len(n_sValues))
print(len(n_sReducedValues))
print(len(rValues))
print(len(rReducedValues))

print(n_sReducedValues[-1])
print(rReducedValues[-1])
print(qValues[-1])
print(NValues[-1])

# Load and process PLANCK data
csv_path = Path(parentFolder, 'PLANCK Data.csv')
data = pd.read_csv(csv_path)

# Split the single column into multiple columns based on the delimiter ';'
columns_split = data.iloc[:, 0].str.split(';', expand=True)
columns_split.columns = [
    'ns95', 'r95', 'ns65', 'r65', 'nsBK95', 'rBK95', 'nsBK68', 'rBK68', 'nsBAO95', 'rBAO95', 'nsBAO68', 'rBAO68'
]

# Convert all values to numeric, ignoring non-numeric headers
columns_split = columns_split.apply(pd.to_numeric, errors='coerce')

# Plot Planck constraints
def plot_planck_constraints():
    plt.figure(figsize=(10, 6))
    plt.xlim(0.94, 1.0)
    plt.ylim(0, 0.2)
    
    # Fill regions for 68% confidence levels
    plt.fill_between(columns_split['ns65'], 0, columns_split['r65'], color='grey', alpha=0.4, label='68% CL')
    # plt.fill_between(columns_split['nsBK68'], 0, columns_split['rBK68'], color='red', alpha=0.4, label='68% CL BK14')
    # plt.fill_between(columns_split['nsBAO68'], 0, columns_split['rBAO68'], color='blue', alpha=0.4, label='68% CL BAO')

    # Plot 95% confidence levels
    plt.plot(columns_split['ns95'], columns_split['r95'], label='95% CL', color='black', linestyle='--')
    # plt.plot(columns_split['nsBK95'], columns_split['rBK95'], label='95% CL BK14', color='red', linestyle='--')
    # plt.plot(columns_split['nsBAO95'], columns_split['rBAO95'], label='95% CL BAO', color='blue', linestyle='--')

    plt.plot(n_sValues, rValues, label="Starobinsky Inflation", color='blue')
    plt.plot(n_sReducedValues, rReducedValues, label=r"Starobinsky Inflation, $N_* \rightarrow N_* - 10$", color='red')

    # Add labels, title, and legend
    plt.xlabel('$n_s$ (Spectral Index)', fontsize=14)
    plt.ylabel('$r$ (Tensor-to-Scalar Ratio)', fontsize=14)
    plt.title('Planck Constraints on $n_s$ and $r$', fontsize=16)
    plt.legend(fontsize=12)

    # Display grid and plot
    plt.grid(True, linestyle='--', alpha=0.7)
    imageName = Path(parentFolder, "Starobinsky and Planck Observations with N-10 New.png")
    plt.savefig(imageName)
    
# Run the plotting function
if __name__ == "__main__":
    plot_planck_constraints()
