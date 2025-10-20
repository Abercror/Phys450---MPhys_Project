import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

a = [i for i in np.linspace(1,10000000000000)]
rhoChi = [(i**(-4)) for i in a]
rhoPhi = [(i**(-3)) for i in a]
print(a)
print(rhoChi)
print(rhoPhi)

log_a = [np.log(i) for i in a]
logRhoChi = [np.log(i) for i in rhoChi]
logRhoPhi = [np.log(i) for i in rhoPhi]
print(log_a)
print(logRhoChi)
print(logRhoPhi)

fig, ax = plt.subplots()

ax.plot(log_a, logRhoChi, label=r'$\rho_\chi \propto a^{-4}$', color='red')
ax.plot(log_a, logRhoPhi, label=r'$\rho_\phi \propto a^{-3}$', color='blue')

ax.set_xlabel(r'Scale factor, $ln(a)$')
ax.set_ylabel(r'Density, $\ln(\rho_x)$')
ax.set_title(r'Decay relationship of $\rho_\phi$ and $\rho_\chi$ with respect to $a$')
ax.legend()

folder = Path(__file__).parent
graph = Path(folder, r"Decay Relationship wrt ln(a).png")
plt.savefig(graph)