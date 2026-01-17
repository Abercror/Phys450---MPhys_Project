import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path


parentFolder = Path(__file__).parent
graphsFolder = Path(parentFolder, "Plot")
graphsFolder.mkdir(parents=True, exist_ok=True)


ReducedPlanckMass = 1
alphaValues = [1]
phiValues = [i for i in np.linspace(-1, 1, 100)]
mu = 243
potentialValues = []

for alpha in alphaValues:
    VfValues = []
    for phi in phiValues:
        Vf = ((mu**2)/(3*alpha))*((np.sinh((phi)/(np.sqrt(6*alpha)*ReducedPlanckMass)))**2)*((np.cosh((phi)/(np.sqrt(6*alpha)*ReducedPlanckMass)))**((6*alpha) - 4))
        VfValues.append(Vf)
    potentialValues.append(VfValues)


fig, ax = plt.subplots()
for i,V in enumerate(potentialValues):
    ax.plot(phiValues, V, label=fr"$\alpha =${alphaValues[i]}")
ax.set_ylabel(r"$V_F(\phi)$")
ax.set_xlabel(r"$\phi$")
ax.set_title(r"Derived Potential $V_F = \frac{\mu^2}{3\alpha}\sinh^2\left(\frac{\phi}{\sqrt{6\alpha}M_{pl}}\right)\left(\cosh \left(\frac{\phi}{\sqrt{6\alpha} M_{pl}}\right)\right)^{6\alpha-4}$")
plt.tight_layout()
plt.legend()
figureName = Path(graphsFolder, f'{"Derived Potential for W=muSZ"}.png')
plt.savefig(figureName)
plt.show()