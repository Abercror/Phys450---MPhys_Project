### Monday, 3rd November, 25
#### 15:16
- I have looked over the feedback from Kostas on my previous logbook so correct and explain what I did not do before.
![[Term 1/Figures/8.0/Initial Plots/Starobinsky and Planck Observations with N-10 New.png]]
- I corrected the legend for the graph and the final values for the $N_* - 10$ curve were 
	- $n_s = 0.95496$
	- $r = 0.0075$
	- $q = 0.6868$
	- $N_* = 47.39 \approx 48$
- Starobinsky Inflation modelled where $N_* \rightarrow N_* - 10$, falls outside of the range of both the $68\%$ and $95\%$ meaning that, the model predicts that $N=50$ predicts a spectral index value that is too small. 
- The values of $V_0^{\frac{1}{4}}$ and $V_{end}^{\frac{1}{4}}$ are consistent with what is expected as values for the reheating temperature $T_R \sim 10^{15}$, and so the values $V_0^\frac{1}{4} = 7.98 \times 10^{15}$ for $q = \sqrt{\frac{2}{3}}$ and the values on the figures below which range from $1.5 \times 10^{16} \lessapprox V_{end}^{\frac{1}{4}} \lessapprox 1.9 \times 10^{16}$ and $0.9 \times 10^{16} \lessapprox V_{0}^{\frac{1}{4}} \lessapprox 1.2 \times 10^{16}$ for $0.381 < q < 0.6868$

![[Term 1/Figures/8.0/Initial Plots/V_0(q) reduced q.png]]
![[Term 1/Figures/8.0/Initial Plots/V_end(q) corrected.png]]


#### 19:53
- I have read about the different options for part 9 of the project to see what direction I should take my project. I am leaning towards **9.3. $\alpha$-attractors** as it seems like an interesting direction to take my project.


#### Tuesday, 4th November, 25
#### 14:18
- The results I found in the previous graphs were wrong as the number of e-foldings is slightly too low so I will look into why
#### 14:38
- I have found the mistake in my code which is why the number of e-foldings I got was slightly lower than it should have been. In the equation for $N_*$, I wrote $10e16$ in python instead of $1e16$ which meant that I was putting the energy value at $10^{17} \; \text{GeV}$ instead of $10^{16} \; \text{GeV}$. I will rerun the code to regenerate the curves. 
- I have also recalculated the values obtained when setting $q = \sqrt{\frac{2}{3}}$ 
	- $N_* = 59.56 \approx 60$
	- $V_0^\frac{1}{4} = 7.83 \times 10^{15} \; \text{GeV}$ 
	- $n_s = 0.9651$
	- $r = 0.003383$
- These are the curves that were found for the using the correct equation as well as the reduced range of $q$, to $0.381 < q < 0.6868$.
![[Term 1/Figures/8.0/Graphs Corrected N/N(q).png]]
![[Term 1/Figures/8.0/Graphs Corrected N/V_0(q).png]]
![[Term 1/Figures/8.0/Graphs Corrected N/r against n_s N.png]]
![[Term 1/Figures/8.0/Graphs Corrected N/r against n_s N - 10.png]]
![[Term 1/Figures/8.0/Graphs Corrected N/w(N).png]]
![[Term 1/Figures/8.0/Graphs Corrected N/V_end(q).png]]
![[Term 1/Figures/8.0/Graphs Corrected N/Starobinsky and Planck Observations with N-10 New.png]]
- I will now edit the axis for the $n_s - r$ curve and superimpose it onto the most recent observational data. 
![[Term 1/Figures/8.0/Graphs Corrected N/Overlayed Graph.png]]

### Wednesday, 5th November, 25

#### 15:02 
- Completed showing that the associated canonically normalised field $\phi$, for $$\mathcal{L_{kin}} = \frac{\frac{1}{2} \partial_\mu \varphi \partial^{\mu} \varphi}{\left( 1 - \frac{1}{6 \alpha} \left(\frac{\varphi}{m_p} \right)^2 \right)^2}$$ using the kinetic Lagrangian $$\mathcal{L_{kin} = \frac{1}{2}\partial_\mu \phi \partial^\mu \phi}$$
![[Term 1/Derivations/9.3/(1) Lagrangian derivation phi.png]]

#### 15:15
- Completed the show that for the T-model

#### 17:47 
- Completed the show that for the E-model
![[Term 1/Derivations/9.3/(2) V(phi) part 1.png]]
![[Term 1/Derivations/9.3/(2) V(phi) part 2.png]]
### Saturday, 8th November, 25
#### 13:29
- Found the value of $\alpha$ for the E-model as $\alpha = \frac{3 \pm 2 \sqrt{2}}{3}$ which equate to $\alpha = 1.943$ and $\alpha = 0.0572$ as well as equations for $n_s$ and $r$, although I am not sure if the equations are in agreement with my value I found for $\alpha$
![[Term 1/Derivations/9.3/(3) E-model part 1.png]]
![[Term 1/Derivations/9.3/(3) E-model part 2.png]]

#### 15:39
- Attempted to find the equations for the T-model though I made a mistake as the algebra does not simplify down to the same functions as the E-model
![[Term 1/Derivations/9.3/(4) 1 T-model part 1.png]]
![[Term 1/Derivations/9.3/(4) 1 T-model part 2.png]]

### Sunday, 9th November, 25
#### 14:17
- Re-attempting the derivation of $n_s(N)$ and $r(N)$ for the T-model
#### 23:55
- I have redone the derivations for $n_s(N)$ and $r(N)$ though I still do not get the same results as the E-model so I must have made a mistake in my working somewhere.
![[Term 1/Derivations/9.3/(4) 2 T-model part 1.png]]
![[Term 1/Derivations/9.3/(4) 2 T-model part 2.png]]
![[Term 1/Derivations/9.3/(4) 3 T-model part 3.png]]


### Python Code

```python

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

graphsFolder = Path(parentFolder, "Graphs Corrected N")

graphsFolder.mkdir(parents=True, exist_ok=True)

  

def equation(N, q):

N = N.item()

return N - 60.4 - math.log((((12 * math.pi**2 * As*((2 + math.sqrt(2)*q)**2))/(q**2 * N**2))**(1/4)) * (planckMass/(1e16))) - math.log(((1 - 1/(2 * q**2 * N))) / ((math.sqrt(2)*q + 2)))

  

def findingN():

NValues = []

for q in qValues:

NValue = scipy.optimize.fsolve(equation, 60, args=(q,))

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

  
  

  

# def graph(xValues, yValues, xLabel, yLabel, title, name):

# fig, ax = plt.subplots()

# ax.plot(xValues, yValues)

# ax.set_xlabel(xLabel)

# ax.set_ylabel(yLabel)

# ax.set_title(title)

# plt.tight_layout()

# figureName = Path(graphsFolder, f'{name}.png')

# plt.savefig(figureName)

  

def setq():

q = math.sqrt(2/3)

NSetqValue = scipy.optimize.fsolve(equation, 60, args=(q,))

V_0SetqValue = ((12 * math.pi**2 * planckMass**4 * As) / (q**2 * NSetqValue**2 * ((1 - 1/(2 * q**2 * NSetqValue))**2)))**(1/4)

n_sSetqValue = 1 - (2/NSetqValue) - (3 / (q**2 * NSetqValue**2))

rSetqValue = 8 / (q**2 * NSetqValue**2)

  

values = f"N = {NSetqValue}, V_0^1/4 = {V_0SetqValue}, n_s = {n_sSetqValue}, r = {rSetqValue}"

print(values)

  
  
  

# graph(qValues, NValues, r"$q$", r"$N_$", r"$N_(q)$", "N*(q)")

# graph(qValues, V_0Values, r"$q$", r"$V_0^{\frac{1}{4}}(q)$, GeV", r"$V_0^{\frac{1}{4}}(q)$", "V_0(q)")

# graph(n_sValues, rValues, r"$n_s$", r"$r$", r"$r$ against $n_s$", "r against n_s N_")

# graph(n_sReducedValues, rReducedValues, r"$n_s$", r"$r$", r"$r$ against $n_s \quad N_ - 10$", "r against n_s N_ - 10")

# graph(qValues, V_endValues, r"$q$", r"$V_{end}^{\frac{1}{4}}(q)$, GeV", r"$V_{end}^{\frac{1}{4}}(q)$", "V_end(q)")

# graph(NValues, wValues, r"$N_$", r"$w(N_)$", r"$w(N_)$", "w(N)")

  

# def ns_rGraph():

# fig, ax = plt.subplots()

# ax.plot(n_sValues, rValues)

# ax.plot(n_sReducedValues, rReducedValues)

# ax.set_xlim(0.92, 1)

# ax.set_ylim(0, 0.2)

# ax.axis('off')

# plt.tight_layout()

# figureName = Path(graphsFolder, f'{"n_s - r graph for superimposing"}.png')

# plt.savefig(figureName, dpi = 342)

  

# ns_rGraph()

  
  

setq()
```

### Monday, 10th November, 25

#### 09:36 
- Exporting log book to send to Kostas


