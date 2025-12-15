### Monday, 17th November, 25

#### 18:23 
- I have written the section on the Horizon Problem and the Flatness problem for my literature review. 

#### 18:49
- Removed the Cosmological Key section from my literature review as I don't think it is necessary or worth the space. 


### Thursday, 20th November, 25

#### 14:35
- I have derived the equations for the E-model: $V_0 (\alpha)$, and $m(\alpha)$ which I will plot for fixed values of $N_*$ and $N_* - 10$ using $N_* = 60$ as the result from the Starobinsky model. 
![[Term 1/Derivations/9.3/E-model finding alpha.png]]
- The range of alpha will be constrained to $0 < \alpha < 5.83$ due to the relation $$ r = \frac{12 \alpha}{N_*^2} \quad \text{where} \quad r < 0.028 \quad \Rightarrow \quad \alpha < \frac{0.028 N_*^2}{12}$$ where for $N_* = 50 \; \alpha < 5.83$ and for $N_* = 60 \; \alpha < 8.4$. The range $0< \alpha < 5.83$ will be used to keep all of the results within the observational range.  

![[Term 1/Figures/9.3/2 E-model Graphs/E-model V0 against alpha.png]]
![[Term 1/Figures/9.3/2 E-model Graphs/E-model mass against alpha.png]]
![[Term 1/Figures/9.3/2 E-model Graphs/E-model r against ns.png]]

### Friday, 21st November, 25

#### 11:35
- Derived the equations for the T-model: which I will plot for the same $N_*$ values and $\alpha$ range. 
![[Term 1/Derivations/9.3/T-model finding alpha wrong.png]]
#### 12:19
- The graphs are not what I expected them to be so I will take another look at the equations and try again

![[Term 1/Figures/9.3/2 T-model Graphs/T-model V0 against alpha.png]]
![[Term 1/Figures/9.3/2 T-model Graphs/T-model mass against alpha.png]]
![[Term 1/Figures/9.3/2 T-model Graphs/T-model r against ns.png]]

#### 13:38
- I have redone the equations for $V_0(\alpha)$ and $m(\alpha)$ using the approximation from the Starobinsky model of $e^{\frac{2}{\sqrt{6 \alpha}} \frac{\phi}{m_p}} \approx \frac{4N}{3 \alpha}$ and using the exponential forms of $\tanh x$ and $\sinh x$. 
![[Term 1/Derivations/9.3/T-model finding alpha corrected.png]]
![[Term 1/Derivations/9.3/T-model finding alpha corrected part 2.png]]
#### 14:20
- Using the newer equations I have derived graphs which look far more like what I would have expected. 

![[Term 1/Figures/9.3/3 T-model Graphs/T-model V0 against alpha.png]]
![[Term 1/Figures/9.3/3 T-model Graphs/T-model mass against alpha.png]]
![[Term 1/Figures/9.3/3 T-model Graphs/T-model r against ns.png]]

- The 2 different models so that they have both different masses for the inflaton and different values for the potential, $V_0^{\frac{1}{4}}$, for the range of $\alpha$, but they have the same graph for the tensor ratio, $r$ against the spectral index, $n_s$, as they both reduce to the same relation. Only $r$ is dependent on $\alpha$, which is what causes these vertical lines in the graph.  
#### 16:52
- Added to my introduction section of my Literature review and I have also changed the contents page to simplify and reduce the number of sections. 

#### 18:47 
- Written some of the section on cosmic inflation describing what it is. I need to now write about primordial density perturbations and how they link to inflation and the reheating to form allow for the Hot Big Bang. 

### Saturday, 22nd November, 25
#### 03:19
- Written about the mathematical formulation of the inflaton scalar field describing the Klein-Gordon equation and leading up to the slow-roll approximation for the next section on slow-roll inflation. 

#### 18:29
- Completed the slow-roll inflation section describing the conditions for slow roll inflation to occur as well as the ending conditions for inflation. 


### Sunday, 23rd November, 25
#### 13:17 
- Starting on the section about how inflation solves the Horizon and the Flatness Problems

### Python Code
#### T-model Code
```python
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
```
#### E-model Code
```python
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
```
### Monday, 24th November, 25
#### 11:49
- Exporting log book to send to Kostas



