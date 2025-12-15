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