'### Tuesday, 28th October, 25

#### 11:16
- Using the Starobinsky potential $$V = V_0 \left(1 - e^{-\frac{q}{m_p}\phi} \right)^2$$ $V_{end}$ and $V_*$ can be found by using $\phi_{end}$ and $e^{\frac{q}{m_p}\phi} \approx 2q^2N$, resulting in $$V_{end} = V_0 \left(2 + \sqrt{2}q \right)^2 \quad \text{and} \quad V_* = V_0 \left(1 - \frac{1}{2q^2N_*} \right)^2 \quad \text{for} \;  N = N*$$
- Using $N_* = 60$ for $$n_s = 1 - \frac{2}{N} - \frac{3}{q^2N^2} \quad \text{and} \quad r = \frac{8}{q^2 N^2}$$ gives $$n_s: q = 0.6868 \quad \text{and} \quad r: q > 0.282$$ so the range of $q$ is limited to $$ 0.282 < q < 0.6868 $$
### Wednesday, 29th October, 25
#### 17:07
- Rearranged $P_{\zeta}(N)$ to get the equation for  as $$ V_0 = \frac{12 \pi^2 m_p^4 P_{\zeta}(N)}{q^2 N^2 \left(1- \frac{1}{2q^2N} \right)^2}$$ where for $N = N_*$, $P_{\zeta} = A_s$. 
- The equation (62) using the equations for $V_0$, $V_{end}$ and $V_*$ and setting $g_* = 106.75$ reduces to $$N_* = 60.4 + \ln \left( \left(\frac{12 \pi^2 m_p^4 A_s \left( 2 + \sqrt{2}q \right)^{2}}{q^2 N_*^2\left( 1 - \frac{1}{2q^2N_*}\right)^2}\right)^{\frac{1}{4}} \frac{1}{10^{16} \; GeV}\right) + \ln \left( \frac{1 - \frac{1}{2q^2 N_*}}{2 + \sqrt{2}q}\right)$$ which cannot be solved analytically and so must be done numerically to find a value for $N_*$ for each $q$ value within the range. This will then allow for a value for $V_0$ to be found. 
![[Term 1/Derivations/1-8/(86) 7.png]]

### Thursday, 30th October, 25
#### 16:43 
- I have written a python script to numerically integrate, to find the value of $N_*$ for each $q$. 
- I think that I have made a mistake in my derivation of the equation for $N_*$ as I am getting a graph with a negative number of e-foldings.
![[Term 1/Figures/8.0/Initial Plots/N(q) wrong.png]]

#### 18:58
- I have tried to derive $N_*$ again but I got the same results again so I am not sure what is wrong. 

#### 22:57
- Realised that the mistake was a typo in my python script where I set $m_p = 2.43 \times 10^{-18}$ instead of $m_p = 2.43 \times 10^{18}$. The new graph's values are more inline with expected values i.e not negative. 
![[Term 1/Figures/8.0/Initial Plots/N(q) corrected.png]]

#### 23:54
- Plotted a graph for $V_0^{\frac{1}{4}}(q)$ 
![[Term 1/Figures/8.0/Initial Plots/V_0(q).png]]

### Friday, 31st October, 25
#### 00:09
- Plotted the graph of $n_s(q)$ and $r(q)$ using the values of $N_*(q)$ previously found
![[Term 1/Figures/8.0/Initial Plots/V_0(q).png]]

#### 00:18
- Plotted the graph of $n_s(q)$ and $r(q)$ using the values of $N_* \rightarrow N_* - 10$ previously found
![[Term 1/Figures/8.0/Initial Plots/r against n_s N reduced.png]]

#### 00:29
- Plotted $V_{end}^{\frac{1}{4}}(q)$ 
![[Term 1/Figures/8.0/Initial Plots/V_end(q) wrong.png]]

#### 00:38
- In orders to find $w(q)$ for a given $q$, I will use the equation $$\epsilon = \frac{3}{2}\left(1+w\right)$$ which can be recast as $$w = \frac{2}{3} \epsilon -1 \approx \frac{2}{3} \frac{1}{2q^2N_*^2}-1$$
- This equation when plotted against $N_* = N_*(q)$ yields the graph 
![[Term 1/Figures/8.0/Initial Plots/w(N) wrong.png]]

- This graph shows that Starobinsky-type inflation is quasi-de Sitter as $w \approx -1$. 

#### 11:36
- Setting $q = \sqrt{\frac{2}{3}}$ gives values of 
	- $N_* = 57.28 \approx 57$
	- $V_0^\frac{1}{4} = 7.98 \times 10^{15}$
	- $n_s = 0.96371$
	- $r = 0.00365766$

#### 14:01
- In order to solve the horizon problem for the Starobinsky Inflation model I initially tried to use the relation $$e^{N} = \frac{a_{end}}{a_0} \quad \Rightarrow \quad e^{N-N_*} = \frac{a_{end}}{a_*}$$
- which would be recast to  $$e^{N-N_*} = \left(\frac{\rho_*}{\rho_{end}}\right)^\frac{1}{3(1+w)}$$ but since $w \approx -1$, that equation would not give a correct result. 


#### 15:30
- Derived the expression $$N > \ln\left(\frac{T_0 T_{end} R_0 \pi g_*^{\frac{1}{2}}}{ \sqrt{3} \sqrt{30} m_p} \right)$$
- Found the value for minimum number of e-foldings during inflation, as $N > 63.588  \Rightarrow N_{tot} \gt 63$. The solution to the Horizon problem is that $N > 60$ which Starobinsky Inflation with $q = \sqrt{\frac{2}{3}}$ fulfils. 
![[Term 1/Derivations/1-8/(86) 8.png]]

### Saturday, 1st November, 25
#### 13:58
- I realised that I missed a part of the prompt for plotting spectral index, $n_s$, and the tensor ratio, $r$, as I did not overlay it with the Planck data for a comparison. 
- Using the github repo https://github.com/kdemirel/Planck-constraints-r-vs-ns-plot I was able to plot the ${n_s}_{65\%}$ and the ${n_s}_{95\%}$ confidence level regions with my data resulting. 
![[Term 1/Figures/8.0/Initial Plots/Starobinsky and Planck Observations.png]]
- This shows that the Starobinsky model would take a value of $q$ that is on the upper end of the boundary constraints of $q$, $0.282 < q < 0.6868$, in order to be in the confidence levels of the Planck observational data.

#### 19:29
- Refining the range of $q$, such that the $n_s - r$ is within the $95\%$ confidence region level gives a lower bound as $q > 0.381$ where $N_*(q) = 57.716$. This was done using by using matplotlib to find the values of $n_s$ and $r$ at the $95\%$ boundary and then sorting the arrays to find the respective $q$ and $N_*$ values.

#### 19:57
- Redid the graph of $N_* \rightarrow N_* -10$ with the corrected reduced range of $q$
![[Term 1/Figures/8.0/Initial Plots/Starobinsky and Planck Observations with N-10.png]]

- Redid the graph of $V_{end}^{\frac{1}{4}}(q)$ 
![[Term 1/Figures/8.0/Initial Plots/V_end(q) corrected.png]]

- Redid the graph of $w(N_*)$
![[Term 1/Figures/8.0/Initial Plots/w(N) corrected.png]]

- The graph still shows that Starobinsky inflation is quasi-de Sitter as $w \approx -1$

### Monday, 3rd November, 25
#### 11:14
- Exporting to pdf to send to Kostas


### Python scripts
#### My numerical integration
```python
import scipy
import numpy as np
import math
from pathlib import Path
import matplotlib.pyplot as plt

planckMass = 2.43e18
As = 2.0967241e-09
qValues = [q for q in np.linspace(0.282, 0.6868, 100000)]
# qValues = [q for q in np.linspace(0.3810912789127891, 0.6868, 100000)]
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
  

def graph(xValues, yValues, xLabel, yLabel, title, name):
	fig, ax = plt.subplots()
	ax.plot(xValues, yValues)
	ax.set_xlabel(xLabel)
	ax.set_ylabel(yLabel)
	ax.set_title(title)
	figureName = Path(parentFolder, f'{name}.png')
	plt.savefig(figureName)
	plt.show()

  
  

def setq():
	q = math.sqrt(2/3)
	NSetqValue = scipy.optimize.fsolve(equation, 50, args=(q,))
	V_0SetqValue = ((12 * math.pi**2 * planckMass**4 * As) / (q**2 * NSetqValue**2 * ((1 - 1/(2 * q**2 * NSetqValue))**2)))**(1/4)
	n_sSetqValue = 1 - (2/NSetqValue) - (3 / (q**2 * NSetqValue**2))
	rSetqValue = 8 / (q**2 * NSetqValue**2)  
	values = f"N = {NSetqValue}, V_0^1/4 = {V_0SetqValue}, n_s = {n_sSetqValue}, r = {rSetqValue}"
# print(values)

  
  
  

graph(qValues, NValues, r"$q$", r"$N_*$", r"$N_*(q)$", "N*(q)")
graph(qValues, V_0Values, r"$q$", r"$V_0^{\frac{1}{4}}(q)$, GeV", r"$V_0^{\frac{1}{4}}(q)$", "V_0(q)")
graph(n_sValues, rValues, r"$n_s$", r"$r$", r"$r$ against $n_s$", "r against n_s")
graph(n_sReducedValues, rReducedValues, r"$n_s$", r"$r$", r"$r$ against $n_s \quad N_* - 10$", "r against n_s N_* reduced")
graph(qValues, V_endValues, r"$q$", r"$V_{end}^{\frac{1}{4}}(q)$, GeV", r"$V_{end}^{\frac{1}{4}}(q)$", "V_end(q)")
graph(NValues, wValues, r"$N_*$", r"$w(N_*)$", r"$w(N_*)$", "w(N) corrected")

setq()
```

#### Edited code from https://github.com/kdemirel/Planck-constraints-r-vs-ns-plot
```python 
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

print(N)
print(q)  

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
	plt.plot(n_sReducedValues, rReducedValues, label=r"Starobinsky Inflation $(N_*)$", color='red')
	
	# Add labels, title, and legend
	plt.xlabel('$n_s$ (Spectral Index)', fontsize=14)
	plt.ylabel('$r$ (Tensor-to-Scalar Ratio)', fontsize=14)
	plt.title('Planck Constraints on $n_s$ and $r$', fontsize=16)
	plt.legend(fontsize=12)
	
	# Display grid and plot
	plt.grid(True, linestyle='--', alpha=0.7)
	imageName = Path(parentFolder, "Starobinsky and Planck Observations with N-10.png")
	plt.savefig(imageName)

# Run the plotting function
if __name__ == "__main__":
	plot_planck_constraints()
```
