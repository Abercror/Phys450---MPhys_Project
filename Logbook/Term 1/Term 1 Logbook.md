## Week 1
### Tuesday, 7th October, 25
#### 13:10
- Created folder for the project containing Logbook, code, and reports and pushed it to a github repository for file backups

####  13:23
**1.0. Universe Dynamics**
- Friedmann Equation
$$H(a)^2 = \frac{8 \pi  G}{3} \rho(t) - \frac{k c^2}{a(t)^2}$$
	- an equation that models the universe as a fluid with density $\rho(t)$ as solely a function of time like the scale factor, $a(t)$. It demonstrates that when $\rho \neq 0$ the universe is not static and states that the expansion rate is related to both the constituents of the universe as well as its shape, denoted by $k$ for the curvature. 

- Continuity Equation 
$$\dot \rho + 3H\left( \rho + \frac{p}{c^2} \right) = 0$$
	- an equation that relates density of the universe to the pressure that it exerts, named the isotropic pressure $p(t)$. It assumes a constant mass for the universe and is also named the fluid equation. 

- Equation of state 
$$ p = w \rho c^2 $$
	- an equation describing a cosmologically perfect fluid that relates the isotropic pressure, $p(t)$, and the density parameter, $\rho(t)$. The two terms are related by the barotropic parameter, $w$, which is defined as  $$w = \frac{\Sigma_i p_i}{(\Sigma_i \rho_i) c^2} ,$$ where $i$ denotes a different constituent of the universe. 
- Acceleration Equation 
$$ \frac{\ddot a}{a} = - \frac{4 \pi G}{3} \left( \rho + \frac{3 p}{c^2} \right) $$
	- a combination of the Friedmann equation and the continuity equation. Demonstrates that accelerated expansion of the universe requires, $w < -\frac{1}{3}$.


### Wednesday, 8th October, 25

#### 10:28
- Completed derivations (6), (7), (8)
![[Derivations/1-8/(6), (7) part 1.png]]![[Derivations/1-8/(7) part 2.png]]
![[Derivations/1-8/(8).png]]
- The expression for the density for radiation in the hot big bang $$ \rho_{\gamma} = \frac{\pi^{2} g_{*}}{30 c^{2} (c \hbar)^3} (k_B T)^4$$ shows that the $\rho_{\gamma} \propto (k_B T)^4$, meaning that the energy density is proportional to the thermal energy of the radiation. The $g_*$ term is the effective relativistic degrees of freedom, which is a combination of degrees of freedom possessed by a collection of relativistic bosons and fermions given by $$g_* \equiv \sum_{bosons}^{i} g_i + \sum_{fermions}^{j} g_j$$ which when only considering light $g_* = 2$, however in the early universe $g_* = O (10-100)$


#### 13:00 
**2.0. Cosmic Inflation**
- In de Sitter spacetime, is a solution to the Einstein equations with 0 matter present and dominated by a cosmological constant, and is maximally symmetric in both space and time. When inflation is dominated by $\Lambda_{eff}$, it is called quasi-de Sitter inflation. This is because inflation must have an end in order for the thot big bang to occur, so spacetime does not respect the maximally symmetrical description of de Sitter space. The density during inflation is also determined by $\Lambda_{eff}$ and so is therefore constant and given by the $$\rho_{inf} \simeq \frac{\Lambda_{eff} c^2}{8 \pi G}$$ which also requires $w = -1$ for the barotropic parameter. 
- Completed derivations (10) - (11)
![[Derivations/1-8/(10).png]]

#### 22:35
**3.0. Solving the Horizon and Flatness Problems**
**3.1. The cosmological Horizon**

- Started derivation (16) and did it incorrectly but going along the right lines.


### Thursday, 9th October, 25
#### 12:10
- Completed the derivation of $D_H$ (16)
![[Derivations/1-8/(16) part 1.png]]
![[Derivations/1-8/(16) part 2.png]]
- Read through the section

#### 12:34
**3.2. Flatness Problem**
- Read through the section

**4.0. Inflationary Paradigm**
- Completed derivation (25)
- Unsure about the relation $\rho + p = \rho_{kin}$ comes from will need to take another look as it seems to suggest that $\rho + p = 2 \rho_{kin}$.  
#### 14:48
- Completed part of (26) to show $w < -\frac{1}{3}$

#### 21:23
- Completed (26) showing $\rho_{kin} < \frac{1}{2} V$
![[Term 1/Derivations/1-8/(26).png]]
- Completed (27)
![[Derivations/1-8/(27).png]]


#### 21:48
- Obtained (28) 
![[Term 1/Derivations/1-8/(28).png]]


### Sunday, 12th October, 25
#### 10:17
- Attempting the derivation of the Klein-Gordon equation again

#### 11:12 
- Completed the derivation of the Klein-Gordon equation
$$ \ddot{\phi} + 3H \dot{\phi} + V' = 0 $$
- The Klein-Gordon equation resembles the equation of motion for a particle in the form $$ m \ddot{x} + \mu \dot{x} + \frac{dU}{dx} = 0$$ where $x(t)$ is the positional coordinate, $m$ is the mass, $U$ is the potential and $\mu$ is the frictional coefficient. This is analogous where 
	- $3H$ aligns with $\mu$ 
	- $V'$ aligns with $\frac{dU}{dx}$
	- $x$ aligns with $\phi$ 
- meaning that physically the scalar field behaves in a similar way to a particle rolling in a potential (i.e. down a hill) where the frictional component $H$ comes from the expansion of the universe. The result of this is that the frictional, $H$, component scales with the size of the universe, $H \propto \frac{1}{a} \propto \frac{1}{t}$, after inflation. During inflation where $H$ is constant and large friction dominates the scalar field but as $t \rightarrow \infty$, $H \rightarrow 0$, meaning that the field will oscillate about its minimum potential, $V(\phi)$, $$ \lim_{H \rightarrow 0} \left( \ddot{\phi} + 3H \dot{\phi} + V' = 0 \right) \quad \Rightarrow \quad \ddot{\phi} + V' = 0 $$
#### 11:48 
- Starting the derivation of $$ \ddot{\phi} + V' = \frac{1}{\dot{\phi}} \frac{d}{dt} \left( \rho_{kin} + V \right) $$
#### 12:43 
- completed derivation (29)
![[Term 1/Derivations/1-8/(29).png]]

#### 13:02
- completed derivation (30)
![[Term 1/Derivations/1-8/(30).png]]

#### 13:09
**5.0. Slow-Roll Inflation**
- Beginning (32)

#### 14:45
- Completed derivation (32)
![[Term 1/Derivations/1-8/(33).png]]

- The slow-roll parameter $\epsilon$ is defined as $$ \epsilon \equiv - \frac{\dot{H}}{H^2}$$ which allows for the parameterisation of the condition for accelerated expansion. 

#### 15:38
- Completed the derivation, (35), of $$ \frac{\ddot{a}}{a} = \dot{H} + H^2 \quad \quad$$ and proof that inflation is possible only if $\epsilon < 1$.
![[Term 1/Derivations/1-8/(35).png]]

#### 15:56
- An e-fold refers to the time taken for the scale factor to increase by a factor of $e$, meaning that the number of e-folds in a given time represents how much the universe has expanded during a set timeframe. The relations $dN = -H dt$ and $\epsilon \equiv \frac{\dot{H}}{H^2}$, when combined result in the expression $\frac{dH}{H} = \epsilon dN$. The condition for the accelerated expansion of the universe is $\epsilon < 1$, and so if $\epsilon \ll 1$, the rate of accelerated expansion would be very high. This means that $dH \gg 1$ and since $dH \propto dN$, $dN \gg 1$. $\epsilon$ allows for inflation to be described by the number of expansions that the universe has undergone rather than the expansion time. 
![[Term 1/Derivations/1-8/(36).png]]

#### 16:20 
- Starting the derivation of (37)

#### 20:20
- Attempted (37) again but could not solve it
### Monday, 13th October, 25
#### 09:30
- Exporting logbook to pdf to send to Kostas

## Week 2
### Monday, 13th October, 25
#### 12:35
- Completed derivation of (37)

#### 17:49 
- Completed show that for (38) $$ \epsilon \ll 1 \leftrightarrow \rho_{kin} \ll V$$
![[Term 1/Derivations/1-8/(38).png]]
#### 18:07
- Derived the expression (40) $$\epsilon = \frac{3}{2}(1 + w)$$
![[Term 1/Derivations/1-8/(40).png]]
- The second slow-roll parameter $\eta$ is is defined by the expression $$\eta \equiv m^2_{p} \frac{V''}{V}$$ which when $|\eta| < 1$maintains that the fractional change of $\epsilon$ is small per e-fold. This is required as accelerated expansion will only be sustained for a long enough time period if the conversion of kinetic energy to potential energy is slow enough which required the condition $$ |\ddot{\phi} |\ll |V'|$$ 
#### 18:33
- Completed show that (42)
![[Term 1/Derivations/1-8/(42).png]]

#### 22:39
- Creating and configuring the .tex file for my literature review

#### 23:43
- Set up the .tex file in vscode with the .bib file working. Configured the settings.json such that the latex recipe uses biber for the references rather than bibtex. 

#### 23:53
- Completed the configuration for the layout of the title page and contents page and added some preliminary section names in. Added comments to improve readability of the latex source file. 


### Thursday, 16th October, 25
#### 16:39
**6.0. Density Perturbations**
- read through sections **6.1.** and **6.2. Inflaton perturbations** 
#### 16:53
- Found the first part of (52) but need to complete the rest and check the derivation
### Friday, 17th October, 25
#### 11:58
- Completed the derivation of (52) as well as solving when $V'' = m^2$ and $m \ll H$

![[Term 1/Derivations/1-8/(52).png]]
- Since $H \approx$ const. the solution to (52) and the amplitude of the oscillations is $\delta \phi = -3H \approx$ const. This means that the field obtains a "scale-invariant" spectrum of perturbations as $H$ defines the rate of expansion and since that is constant the perturbations will not change with over time. As the universe expands the oscillations will remain the same and so the field will not change, ergo "scale-invariant"
#### 13:07
**6.3. The curvature perturbation**
- completed (55)

![[Term 1/Derivations/1-8/(55).png]]

#### 13:22 
- completed show that (57)

![[Term 1/Derivations/1-8/(57) part 1.png]]
![[Term 1/Derivations/1-8/(57) part 2.png]]
- completed show that (58)

![[Term 1/Derivations/1-8/(58).png]]
#### 13:27
**6.4. $N_*$ and the pivot scale**
- Starting the derivation of (65)

#### 18:06
- Have completed the derivation for (65) partially though I have an extra term of $-\frac{1}{3} \ln \left( \frac{V^{\frac{1}{4}}_{end}}{T_{dec}} \right)$ and the numerical values do not equate to 65.8

#### 18:20
- realised that I had forgotten to write a $V^{\frac{1}{4}}_{end}$ term in the working
![[Term 1/Derivations/1-8/(65) part 1.png]]
![[Term 1/Derivations/1-8/(65) part 2.png]]
- Going to continue it again tomorrow

### Saturday, 18th October, 25
#### 11:21
- Attempting (65) again

#### 12:23
- Managed to get (65) into this form though I am unsure about how to get the correct numerical values for the solution and I think I have made a mistake at tome point, although the general form of the equation is correct
![[Term 1/Derivations/1-8/(65) part 3.png]]
- I am going to move onto the next part and come back to this at a later time

#### 12:26
**6.5. Spectral indexes**
- Starting derivation (71)

#### 12:50
- Attempted derivation (71) and while I got the form correct the coefficients where the incorrect numerical values so I will reattempt to to see where I went wrong

#### 13:03
- Re-attempted (71) and found my mistake of writing 2 as 1/2 in my working. Completed the derivation with the correct values. 
![[Term 1/Derivations/1-8/(71) part 1.png]]
![[Term 1/Derivations/1-8/(71) part 2.png]]


#### 13:13
- completed the show that for the spectral index of gravity waves generated during inflation (75)
![[Term 1/Derivations/1-8/(75) part 1.png]]
![[Term 1/Derivations/1-8/(75) part 2.png]]

#### 13:21
**7.0. Reheating**
**7.1. Perturbative Reheating**

#### 15:26
- Shown that $m \sim \sqrt{V''(\phi_0)}$ and that $\rho_{\phi} \propto a^{-3}$
![[Term 1/Derivations/1-8/(78) 7.0.png]]

#### 17:12
- completed show that (79) and (80)
![[Term 1/Derivations/1-8/(79).png]]
![[Term 1/Derivations/1-8/(80).png]]
#### 17:40
- completed derivation (81)
![[Term 1/Derivations/1-8/(81).png]]
#### 18:23
- I have attempted show that (82), however, I am not sure how to do it. I am going to retry derivation (65) as I did not get that one correct and this builds upon that 

### Sunday, 19th October, 25
#### 11:23
- retrying the derivation of (65) as that is required before (85) can be done

#### 15:49
- I have made some progress with (65), realising my one of my mistakes in my previous working where I tried to use the a relation of $N$ and $N_*$, though I am struggling to get it into the correct form and unsure what value $w$ should take

#### 20:38
- I have completed (65) however, I have gotten an incorrect value, instead of 65.8 I have gotten 66.6 so I will need to take another look at this
![[Term 1/Derivations/1-8/(65) redo part 1.png]]
![[Term 1/Derivations/1-8/(65) redo part 2.png]]
![[Term 1/Derivations/1-8/(65) redo part 3.png]]
#### 21:10
**7.2. Preheating**
- I have read through the section and am beginning to make a start on plotting the graph of the density of the inflaton, $\rho_\phi$, and the decay products, $\rho_\chi$, with respect to the scale factor, $a$. 
#### 21:28
- Written a basic python script to visually show the relationship of the decays of the different scalar fields, though I am unsure if this is exactly what the task is or if I have misread it. 
```python
import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

a = [i for i in np.linspace(1,10000000000000)]
rhoChi = [(i**(-4)) for i in a]
rhoPhi = [(i**(-3)) for i in a]

log_a = [np.log(i) for i in a]
logRhoChi = [np.log(i) for i in rhoChi]
logRhoPhi = [np.log(i) for i in rhoPhi]

fig, ax = plt.subplots()
ax.plot(log_a, logRhoChi, label=r'$\rho_\chi \propto a^{-4}$', color='red')
ax.plot(log_a, logRhoPhi, label=r'$\rho_\phi \propto a^{-3}$', color='blue')
ax.set_xlabel(r'Scale factor, $ln(a)$')
ax.set_ylabel(r'Density, $\ln(\rho_x)$')
ax.set_title(r'Decay relationship of $\rho_\phi$ and $\rho_\chi$ with respect to $a$')
ax.legend()
  
folder = Path(__file__).parent
graph = Path(folder, "Decay Relationship to a.png")
plt.savefig(graph)
```
![[Term 1/Figures/7.0/Decay Relationship wrt ln(a).png]]


### Monday, 20th October, 25
#### 10:27
- Exporting to pdf to send to Kostas

## Week 3
### Saturday, 25th October, 25
#### 09:34
**8.0. Starobinsky-type Inflation**
- Investigating the potential $$V(\phi) = V_0 \left(1 - e^{\frac{- q \phi }{m_p}} \right)^2 $$ which describe the Starobinsky family of inflation models where $q>0$ is a real dimensionless parameterising constant. 

- I need to calculate the slow-roll parameters $\epsilon(\phi)$ and $|\eta(\phi)|$ for a given $q$

####  13:23
- Derived the equations of $\eta$ and $\epsilon$ as $$\eta = 2 q^2 e^{- \frac{ q \phi}{m_p}} \frac{\left(-1 + 2 e^{- \frac{ q \phi}{m_p}} \right)}{\left(1 - e^{- \frac{ q \phi}{m_p}} \right)^2} \quad \text{and} \quad \epsilon = \frac{2q^2 e^{- \frac{2q \phi}{m_p}}}{\left(1 - e^{-\frac{q \phi}{m_p}} \right)^2} $$
- Inflation ends when either $|\eta|$ or $\epsilon$ is equal to 1 and in this case $\epsilon$ will reach 1 first. 
![[Term 1/Derivations/1-8/(86) 1.png]]


#### 13:41
- Found the result for $\phi_{end}$ as $$ \phi_{end} = \frac{m_p}{q} \ln \left( \sqrt{2} q + 1 \right)$$
![[Term 1/Derivations/1-8/(86) 2.png]]
#### 19:20
- In order to find $\phi(N)$, I tried to use the integral $$N = \frac{1}{m^2_p} \int^{\phi}_{\phi_{end}} \frac{V}{V'} d\phi $$ and after subbing in the $V$ and $V'$ I got this integral º$$N = \int^{\phi}_{\phi_{end}} \frac{e^\frac{q \phi'}{m_p} - 1}{2qm_p} d\phi' $$ which I integrated. This did not gave me a $\phi$ term in the $e^{\frac{q \phi}{m_p}}$ which meant that it was not straightforward to get a function of $\phi(N)$. I attempted to look up the Lambert function to see if that could be useful as I have seen it used in a similar situation before but after looking I didn't think that it would help very much. I also tried to use a Maclaurin approximation on $e^{\frac{q \phi}{m_p}}$ in the integral, resulting in $$N = \int^{\phi}_{\phi_{end}} \frac{1 - \frac{q}{m_p}\phi' - 1}{2qm_p} d\phi'  = \int^{\phi}_{\phi_{end}} \frac{\phi'}{2m^2_p} d\phi' $$ though I am not sure that this is a valid solution. 
- Integrating the initial form of the equation I was able to get $$N = \frac{1}{2qm_p} \left. \left(\frac{m_p}{q} e^\frac{q \phi}{m_p} - \phi \right) \right|_{\phi_{end}}^{\phi}$$ and then using substitution of $e^\frac{q \phi}{m_p} = x$ I was able to get an equation in the form $$ x - \ln x = 2q^2 N + \left(\sqrt{2}q + 1 \right) + \ln \left(\sqrt{2}q + 1 \right)$$ and taking the approximation that $\ln x \ll x$ for $x > 1$ gives the relation $$x \approx 2q^2 N +  \left( \sqrt{2}q + 1 \right) + \ln \left( \sqrt{2}q + 1 \right)$$ and then saying that $2q^2 N \gg  \left( \sqrt{2}q + 1 \right) + \ln \left( \sqrt{2}q + 1 \right)$ gives the relation $$ e^{\frac{q \phi(N)}{m_p}} \approx 2q^2 N$$ and so $\epsilon$ and $\eta$ are $$\epsilon \approx \frac{1}{2q^2 N^2} \quad \text{and} \quad \eta \approx -\frac{1}{N}$$ 
![[Term 1/Derivations/1-8/(86) 3.png]]
![[Term 1/Derivations/1-8/(86) 4.png]]
### Sunday, 26th October, 25
#### 13:10
- Using $\eta$ and $\epsilon$, I was able to find the functions $n_s(N)$ and $r(N)$ as $$n_s = 1 - \frac{2}{N} \quad \text{and} \quad r = \frac{8}{q^2 N^2}$$ using the approximation that $\frac{1}{N^2} \ll \frac{1}{N}$ for $n_s$. 

#### 15:19 
- Found $N = 56.98 \approx 57$ for $n_s = 0.9649\pm 0.0042$ which combined with $r < 0.0028$ gave a lower bound for $q > 0.297$. 
![[Term 1/Derivations/1-8/(86) 5.png]]

#### 16:20
- Using the equation $$\sqrt{P_{\xi}} = \frac{1}{2\sqrt{3} \pi} \frac{V^{\frac{3}{2}}}{m_p^3 |V'|}$$ it can be recast using $$\epsilon = \frac{1}{2} m_p^2 \left( \frac{V'}{V}^2 \right)$$ into the form $$P_{\xi} = \frac{1}{24 \pi^2} \frac{V}{m_p^4 \epsilon}$$ and subbing in $\epsilon$ gives $P_{\xi} = P_{\xi}(N)$ 

![[Term 1/Derivations/1-8/(86) 6.png]]
#### 18:30
- For equation B I need to find $V_{end}^{\frac{1}{4}}$ and $V_*$. Using $\phi_{end}$ I can find $V_{end}^{\frac{1}{4}}$ using the the equation for $P_{\xi}$ and for $V_*$, I can use the relation of $e^{\frac{q \phi(N)}{m_p}} \approx 2q^2 N$ where $N = N_*$. 
- I am unsure of what approximation I can use when subbing into equation (63), and whether I can take $V \approx V_0$ in this question or not. 

### Monday, 27th October, 25
#### 10:48
- Exporting to a PDF to send to Kostas. 
## Week 4

### Tuesday, 28th October, 25

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

## Week 5
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



## Week 6
### Tuesday, 11th November, 25
#### 14:48
- Attempting to redo the derivation to find $\alpha$ for the E-model
#### 16:02
- Couldn't complete it so I will reattempt the derivations for the T-model instead
#### 18:13
- Completed the derivation of $n_s(N)$ and $r(N)$ for the T-model 

![[Term 1/Derivations/9.3/(4) 3 T-model part 1.png]]
![[Term 1/Derivations/9.3/(4) 3 T-model part 2.png]]
![[Term 1/Derivations/9.3/(4) 3 T-model part 3.png]]
![[Term 1/Derivations/9.3/(4) 3 T-model part 4.png]]


### Wednesday, 12th November, 25

#### 12:28
- I am not sure how I am meant to use the observational values of $V_0$ in order to find the value for $\alpha$ as I cannot figure this out. So I will move on to the next section and ask Kostas in the next meeting.
#### 13:53
- Completed showing that the kinetic lagrangian can be found using the Kahler potential

![[Term 1/Derivations/9.3/(5) Kinetic Lagrangian derivation.png]]
#### 15:21
- Attempted to demonstrate the $\eta$-problem using the minimal Kahler potential. I read through the section about this in both the Tasi Lectures on inflation and Cosmic Inflation and Large scale structure but I am not sure how to derive it, so I will attempt another time. 

### Thursday, 13th November

#### 11:39
- Beginning to write my literature review

#### 13:29
- Composed the contents page and begun to start the introduction

#### 16:17
- Written the start of my introduction though it could use some more work. I also configured my Zotero to automatically update my .bib file in for my references in my git repo on both my devices so my references will not be lost. 
- I have chosen to have my introduction section to be a bit of a history of cosmology post Einstein's publication of "The Foundation of The General Theory of Relativity", discussing Friedmann publishing his equations and the de Sitter / Einstein universe models. 
- Then I will have a key for each of the main variables used so that the reader may refer back if the get stuck. Next I will write a kind of mini lecture / crash course in cosmology so that the reader is acquainted with the basics of the topic before moving onto cosmology. 
![[Term 1/Lit Review images/Contents page 14.11.25.png]]

- This is just a preliminary contents page that I may change in the future, specifically I think I may remove the $\alpha$-attractors section as I don't think I will have enough space to write about it after covering the other topics as well. I will keep it as this for now but it is likely to change, as well as the section titles. 


### Friday, 14th November, 25
#### 12:31
- Starting to write the crash course section which will cover the basics of the different equations, relations and key variables. 

#### 18:12
- Completed my first draft of the crash course section. 

#### 19:01
- Completed showing the $\eta$-problem for the F-potential

![[Term 1/Derivations/9.3/(5) eta-problem.png]]
- I am unsure if this is completely correct. I think it is based off of the book Cosmological Inflation and Large-Scale Structure as when the potential and its derivative are evaluated at the origin the expression reduces to $\eta \approx 1$. The reason that this is known as the $\eta$-problem is that in order for slow-roll inflation to occur the condition $\eta \ll 1$ must be fulfilled and inflation ends when $|\eta |,\epsilon = 1$. For supergravity to be acceptable the inflaton mass must be very small, $$\eta = 1 + \frac{m_p ^2 \tilde{V}''}{\tilde{V}} \quad \Rightarrow \quad \frac{m_p^2 m_\varphi^2}{V} = 1 + \frac{m_p ^2 \tilde{V}''}{\tilde{V}},$$ in order to keep $\eta$ small. 

### Monday, 17th November, 25

#### 10:47 
- Exporting logbook to send to Kostas. 
## Week 7
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




## Week 8
### Tuesday, 25th November, 25

#### 12:19
- I need to add a designated section to my literature review to discuss the Tensor ratio and spectral index, how it forms and why it is important. This is because inflation solves the Horizon and the flatness problems but slow-roll inflation aligns with the observational values for the tensor ratio and the spectral index <1. 

#### 14:24
- Added to my section on how inflation solves the Horizon and the Flatness problems. 

#### 19:01
- Reading the papers from the references of "On the Present Status of Inflationary Cosmology" to find other Kahler potentials that I could explore and recreate the calculations

- Kahler Potentials
	-  [Minimal Supergravity Models of Inflation](https://arxiv.org/pdf/1307.7696)
		- SU(1,1) 
			- $$ K = -3\alpha \ln \left(\frac{z + \overline{z} }{2}\right) - \frac{3}{2}\beta \left(z + \overline{z}\right)$$
	- [Universality Class in Conformal Inflation](https://arxiv.org/pdf/1306.5220) 
		-  fixed U(1) symmetry by taking $X^0 = \overline{X^0} = \sqrt{3}$ with $X^1 \equiv \varPhi$ 
			- $$ K = -3 \ln \left(1 - \frac{|\varPhi|^2 + |S^2|}{3} + \zeta \frac{(S \overline{S})^2}{3 - |\varPhi|^2}\right) $$
	- [Escher in the Sky](https://arxiv.org/pdf/1503.06785)
		- Super conformal $\alpha$-attractor models (page 6)
			- in half-plain coordinates $$ K = -3 \alpha \log \left(T + \overline{T}\right)$$
		- From Moduli space to cosmology (page 8)
			- Consider both general value of $\alpha$ and $3\alpha = 1$ $$ K = -3 \alpha \ln \left(1 - Z\overline{Z} - S\overline{S}\right) $$
	- [A universal attractor for inflation at strong coupling](https://arxiv.org/pdf/1310.3950)
		- Supergravity embedding
			- $$ K = -3 \log \left( \frac{1}{2} \left( \Omega \left(\sqrt{2}\varPhi \right) + \Omega \left( \sqrt{2}\over{\varPhi} \right) \right) - \frac{1}{3} S\overline{S} + \frac{1}{6} \left(\varPhi - \overline{\varPhi} \right)^2 + \zeta \frac{\left(S\overline{S}\right)^2}{\Omega \left(\sqrt{2}\varPhi \right) + \Omega \left(\sqrt{2}\overline{\varPhi}\right)} \right) $$
	- [Large field inflation and double alpha-attractors](https://link.springer.com/article/10.1007/JHEP08(2014)052#preview)
		- Superconformal Kahler potential 
			- $$ \mathcal{N}(X,\overline{X}) = - |X^0|^2 \left(1-\frac{|X^1|^2 + |S|^2}{|X^0|^2}\right)^\alpha$$


### Wednesday, 26th November, 25

#### 18:02
- Attempted to derived the kinetic Lagrangian for the Kahler Potential $$ K = -3\alpha \ln (T + \overline{T})$$ however, I realise that I made a mistake and I tried to do it for Cartesian coordinates. I will reattempt this tomorrow to correct the mistakes that I made.
![[Term 1/Derivations/Beyond/(1) Kahler potential derivation.png]]
![[Term 1/Derivations/Beyond/(1) Kahler potential derivation part 2.png]]
### Thursday, 27th November, 25

#### 12:29
- I have written a small section outlining what Starobinsky inflation is showing the additional $R^2$ term in the Lagrangian as well as the potential. I need to add to it describing its successes and recent tension with the Atacama observations

#### 14:32
- Made another mistake during my attempt at deriving the Kinetic lagrangian but I will attempt again and not try to put $T$ in terms of $Z$
![[Term 1/Derivations/Beyond/(2) Kahler potential derivation.png]]

#### 15:12
- I have derived the kinetic Lagrangian for the previously mentioned Kahler potential and transformed it into the non-canonical scalar field term. 
![[Term 1/Derivations/Beyond/(3) Kahler potential derivation.png]]
- I am not sure if I did it fully correct or if I should have not substituted $T$ for $\varphi$ before canonically normalising. 
- I recovered the equation for $\varphi$ from the booklet (using the notation of $m_p = 1$) which is good as the Kahler potential that I used for this was simply a rewriting of the other potential that I used from the booklet in a half-disk coordinate system. 
#### 23:22
- Reading in [Introduction to supergravity](https://arxiv.org/abs/1112.3502) I found this for a superpotential 
	- MSSM $$ W = \mu H_uH_d + y_uH_uQU^C + y_dH_dQD^C + y_lH_dLE^C$$ 
- The minimal superpotential is obtained by coupling the MSSM with $\mathcal{N} = 1$ supergravity, chiral superfields plus guage superfields. 

#### 23:58
- For the Kahler potential used the superpotental is set to 0 and with $3\alpha = 1$, when associating the posonic model with $\mathcal{N} = 1$ supergravity $$ K = -3\alpha \log \left( T + \overline{T} \right), \quad W = 0$$
- I am not sure if another superpotential can be used with this Kahler potential or if that cannot be used. I am not sure if the combining of a Kahler potential and a superpotential can be done arbitrarily or if a link between them is required. 
### Friday, 28th November, 25

#### 00:27
- Looking at section 9 in [Escher in the Sky](https://arxiv.org/pdf/1503.06785) I think I will look into the Kahler potential with the superpotential $$K = -3\alpha \ln(1 - Z\overline{Z} - S\overline{S}), \quad W = A(Z) + SB(Z)$$ where S is an additional chiral superfield. I will attempt to derive the F-term potential for this Kahler potential and superpotential $$ V_F = e^K \sum_{Z, \overline{Z}} \left( \left(W_Z + W K_Z \right)K^{Z \overline{Z}} \left(W_{\overline{Z}} + WK_{\overline{Z}} \right) -3 |W|^2 \right)  $$ in order to investigate potential models akin to the E-model and T-model. The paper also mentions other superpotentials that I can look into later.  

### Sunday, 30th November, 25

#### 12:29
- Completed the section on $\alpha$-attractors and I will now work on the section of the problems of inflationary cosmology and write about the alternatives to inflation within that section. The 2 alternatives that I will briefly touch upon will be String Gas cosmology and Matter bounce. 

#### 14:43
- Completed the first draft of the sections on String Gas cosmology and Matter bounce as well as my first draft of the conclusion though I will need to add to it. 
- For the String Gas cosmology section I am a little unsure of how much to include and how much explanation is required. As it will need to be understood by a wide audience and so I don't know how much explanation is required into things such as toroids, string dualities and dimensional compactification. 
- I now need to go back over the previous sections and add in more about the spectral index and tensor ratio and make it clear that slow-roll inflation is what solves this problem rather than cosmic inflation as a whole. I will also likely reorder the sections to allow for this to be more succinct. 


#### 17:49
- Added a section describing the density perturbations to the problems with the Hot Big Bang section
- Added to the description of Cosmic inflation to include the details of the tensor ratio and the spectral index that I will then build upon in the slow-roll inflation section. 

#### 19:35
- Completed the section describing how inflation solves the Flatness and Horizon Problems. I also added to the slow-roll inflation section to include the recasting of the tensor ratio and the spectral index using the slow-roll parameters. 


#### 21:20
- For the Kahler potential mentioned before $$K = -3\alpha \ln(1 - Z\overline{Z} - S\overline{S})$$ I found that the kinetic term is given by $$\mathcal{L}_{kin} = \frac{1 - S\overline{S}}{1 - Z\overline{Z} - S\overline{S}} \partial Z \partial\overline{Z}$$

### Monday, 1st December, 25
#### 10:43
-  I attempted to find the F-term potential for the Kahler potential and the superpotential $$ W = \mu S$$ however, I am a bit unsure if I did it correctly. In the paper section 9 eq (9.29) it says that S is a superfield that can be arranged to vanish during and after inflation. I am not sure how this vanishes whether it is a limit to 0 or the term just disappears. I think the sum is meant to be summing over all the superfields, i.e $S$ and $Z$, but I am not sure if I did that correctly or not. 
- I am meant to find that $$ V_F = \mu^2$$ and I don't as it does not cancel down to that. So I will need to comeback to this and reattempt this derivation. 

![[Term 1/Derivations/Beyond/(4) F-term Potential derivation attempt 1.png]]
![[Term 1/Derivations/Beyond/(4) F-term Potential derivation attempt 2.png]]


#### 10:50
- Exporting logbook to pdf to send to Kostas. 
## Week 9
### Monday, 1st December, 25

#### 12:39
- Beginning to edit my Literature review to reduce the length in order to get it within the page limit. 

#### 14:18
- I have edited the section on String Gas Cosmology to correct it for some mistakes that I made. 

#### 15:10
- I have written the abstract for the lit review. 

#### 17:32
- I have added some extra references for the sections and rewritten some of the Cosmic inflation to improve the readability. 
- Sent the first draft to Kostas. 

### Wednesday, 3rd December, 25
#### 17:07
- I realised my mistake on the previous attempt. I did not compute the summation properly. I realised that I was misunderstanding what was being summed over, so I will make note of the different equations using more formalised notation so that I do not forget again.  
- This gives the F-term potential in the form $$ \begin{align} V_F &= e^K ((\partial_iW + W\partial_iK)g^{ij^*} (\partial_jW + W\partial_jK)^* - 3|W|^2) \\& = e^K(g^{ij^*}D_iW (D_jW)^* - 3|W|^2), \quad D_iW = \partial_iW + W\partial_iK \end{align}$$ so for the above I need to sum over each of the different superfields in K.
- For the kinetic Lagrangian $$ \mathcal{L}_{kin} = K_{ij^*} \partial_{\mu} \phi^i \partial^{\mu} {\phi^*}^{j^*}  $$
### Thursday, 4th December, 25
#### 13:42
- I have reattempted the derivation using the Kahler potential $$ K = -3\alpha \ln\left(1 - Z\overline{Z} - S\overline{S} \right)$$ though it is not quite finished yet. 
![[Term 1/Derivations/Beyond/(5) Paper derivation (1).png]]
![[Term 1/Derivations/Beyond/(5) Paper derviation (2).png]]
![[Term 1/Derivations/Beyond/(5) Paper derivation (3).png]]

#### 16:28
- I have attempted to derive a generalised version of the SUGRA $V_F$ however, I think I may have made a mistake as applying the limit of $m_p \rightarrow \infty$, I think leads to indeterminacy. This may be a mistake as I did not include the $m_p$ originally which I will do in the future, though I am unsure of if it would be a coefficient for $Z$ and $S$ in a similar way to in the Poncaire disk potential
![[Term 1/Derivations/Beyond/(5) Potential and Susy potential.png]]
![[Term 1/Derivations/Beyond/(5) Sugra Potential.png]]

- I will attempt this again including the $m_p$ term explicitly, to see if I made a mistake. 
### Friday, 5th December, 25
#### 16:55
- Added a section on VSL to my literature review and I will now add a section on the Ekroptic scenario. 

#### 17:49
- Completed the section on the Ekroptic scenario. 
- I will try to find some figures for the Horizon and Flatness Problems. 

#### 18:50
- Added a figure for the Horizon Problem, the one from the Tasi Inflation notes
- The figure for the Flatness Problem I screenshotted from Introduction to Inflation and dark energy by Kostas but the quality of the screenshot is not great so I will try to find a better one.

### Saturday, 6th December, 25

#### 15:20
- I have edited and reduced the sections on String gas cosmology and Matter bounce to reduce them in their length. I now have about a page to cut down as I am at 11 pages with the extra figures. 
- I think that I will reduce the introduction section a bit and the cosmic inflation section as I think they could be reduced without causing problems. 


### Monday, 8th December, 25

#### 09:12 
- Exporting to pdf to send to Kostas. 
## Week 10

### Tuesday, 9th December, 25
#### 17:48
- I am going to go over my literature review to check for errors and to try and remove some unnecessary sections so that I am within the page constraints. 
#### 18:24
- I have removed the section on the Matter Bounce hypothesis as it was the weakest of the 4 alternatives and was difficult to try and summarise in little space. I added a small paragraph introducing the alternatives and mentioned it as another possibility. 
- I also swapped the image for the Flatness Problem with one from the Phys265 lecture notes and it is much less blurry now.
- I been editing the first sections for spelling, and sentence structure issues making sure to define each symbol the first time I use it. 

#### 19:11
- I have fixed a lot of the spelling and punctuation errors throughout the paper. I now am over the page limit by just under half a page so I will need to either cut some more out or find a way to condense. 

#### 20:21
- After some re-configuring the layout a bit and removing some unnecessary sections I am within the page limit. 
- I will read through the whole document tomorrow to check if it all makes sense. 
- I need to sort out my logbook as well at some point, exporting all the different weeks to pdfs and then combining. I will need to make sure that all the images are visible and not cut in half by the page breaks and then combine the pdfs into 1. 

### Thursday, 11th December, 25
#### 11:09
- Finished reading through my Literature review highlighting mistake and sentences that I need to change. 

#### 15:24
- Rewritten the section on slow-roll inflation to make it more understandable

#### 18:54
- Moved the density perturbation descriptions in the cosmic inflation section to the primordial density perturbation section to make it more consistent. 

### Friday, 12th December, 25
#### 01:14
- I have edited a lot of the Literature review. Most of the sections have been edited, reworded or rewritten. I have added back the Matter bounce section as I had saved space from cutting down on the previous sections. 

#### 09:44
- Corrected a few mistakes in the VSL and Ekpyrotic sections and edited the conclusion slightly for better readability and grammar. 
- Edited the first paragraph about solving the Horizon and Flatness problems to remove a phrasing error. 

#### 10:21
- Edited the introduction to be more accurate as I made a mistake by implying that the de Sitter model was proposed by Einstein and Willem de Sitter not just de Sitter. I have corrected the phrasing of that as well as a mistake near the end where I got the order of Guth and Starobinsky publishing wrong. 

#### 11:48
- Rewrote the captions for the figures of the Horizon and Flatness Problem to better explain the images and added a citation for the Phys265 lecture notes. 
- I also added the metric signature after the Einstein-Hilbert action equation for completeness

#### 12:15
- Corrected some missing square terms from the $\epsilon$ equation and the slow roll condition in one place

#### 12:52
- Added in the equations for the spectral index and tensor ratio for the Starobinsky model and the $\alpha$-attractor models
- Added a reference for the atacama telescope data and rewrote the paragraph

#### 13:14
- Made some tweaks to the Cosmic inflation section again around the existence of scalar fields and the discovery of the Higgs field. 

#### 13:24
- Fixed some awkward phrasing in the conclusion 

#### 14:10
- added some extra references in

#### 14:29
- Made a few final clarity changes 

## Git History 

![[Term 1/Git History/(8).png]]
![[Term 1/Git History/(7).png]]
![[Term 1/Git History/(6).png]]
![[Term 1/Git History/(5).png]]
![[Term 1/Git History/(4).png]]
![[Term 1/Git History/(3).png]]
![[Term 1/Git History/(2).png]]
![[Term 1/Git History/(1).png]]

