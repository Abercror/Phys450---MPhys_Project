import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


parentFolder = Path(__file__).parent
graphsFolder = Path(parentFolder, "Plot")
graphsFolder.mkdir(parents=True, exist_ok=True)


ReducedPlanckMass = 1
alphaValues = [1]
phiValues = [i for i in np.linspace(-1, 1, 100)]
mu = 1
potentialValues = []

for alpha in alphaValues:
    VfValues = []
    for phi in phiValues:
        Vf = ((mu**2)/(3*alpha))*(np.cosh((phi)/(np.sqrt(6 * alpha) * ReducedPlanckMass)))**((6 * alpha)-2)
        VfValues.append(Vf)
    potentialValues.append(VfValues)


fig, ax = plt.subplots()
for i,V in enumerate(potentialValues):
    ax.plot(phiValues, V, label=fr"$\alpha =${alphaValues[i]}")
ax.set_ylabel(r"$V_F(\phi)$")
ax.set_xlabel(r"$\phi$")
ax.set_title(r"Derived Potential $V_F = \frac{\mu^2}{3\alpha}\left(\cosh \left(\frac{\phi}{\sqrt{6\alpha} M_{pl}}\right)\right)^{6\alpha-2}$")
plt.tight_layout()
plt.legend()
figureName = Path(graphsFolder, f'{"Derived Potential for W=muS"}.png')
plt.savefig(figureName)