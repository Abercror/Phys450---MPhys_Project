## Week 1
### Monday, 15th December, 25
- Started going through the Phys488 QFT Notes up to page 16
- Topics covered
	- Lagrangians and Actions
	- Hamiltonians
	- Possion Brackets
	- Harmonic Chain - Phonons
### Wednesday, 17th December 25
- Continued the notes up to page 31
- Topics covered
	- Two point correlation function for the harmonic chain
	- Gaussian integrals
	- Quantum Harmonic Chain
	- Linear Response theory
### Thursday, 18th December, 25
- Completed the notes up to page 42
- Topics Covered 
	- Response functions from Feynman Path integral
		- Green's Function
	- Feynman's Path Integral
	- Effective Action
- I am going to leave the Boson Path integral section and the superfluidity section for now and move onto David Tong's QFT lecture notes as are more related to HEP rather than Condensed Matter Physics which is the main focus of the Phys488 notes.
### Friday, 19th December, 25
- Started [David Tong's QFT Notes](https://www.damtp.cam.ac.uk/user/tong/qft/qft.pdf) and have completed up to page 26

## Week 2
### Monday, 22nd December, 25
- Completed up to $\phi^4$ Theory on page 69 of the notes
### Tuesday, 23rd December, 25
- Completed Chapter 4, page 105
#### Wednesday, 24th December, 25
- Completed up to QED, page 139
### Thursday, 25th December, 25
- Finished the final pages of the notes. I will look at gauge theories now to see what is required for David Tong's Supersymmetry notes. I know that I will need to look at Lie groups and Lie algebras, 

### Friday, 26th December, 25
- Attempted some of the problems from the problem sheets for the QFT notes. I was able to get a couple though the difficulty of them is a step up from my usual worksheets. 

### Sunday, 28th December, 25
- Started [David Tong's Standard Model Notes](https://www.damtp.cam.ac.uk/user/tong/sm/standardmodel.pdf) and got to page 27. 
- I am going to go through sections 1.1,1.2,1.3 and 2.2,2.3 to get an understanding of symmetries and then I might use [David Tong's Gauge Theory Notes](https://www.damtp.cam.ac.uk/user/tong/gaugetheory/gt.pdf) and look at section 2.1 for more understanding of Yang-Mills theory as the rest of the gauge theory notes are very broad and I don't think I need them at this time to look at the supersymmetry notes. 

## Week 3
### Monday, 29th December, 25
- Completed sections 1.1, 1.2, 1.3 about Symmetries
- Completed 2.1 about the Abelian Higgs model
### Wednesday, 31st December, 25
- Completed 2.3 about the non-Abelian Higgs model and a bit of 2.2 on superconductors but I did not take complete notes on the section as it was a bit of a tangent
### Thursday, 1st January, 26
- Started [David Tong's Supersymmetry Notes](https://www.damtp.cam.ac.uk/user/tong/susy/susy.pdf) and got up to page 33 on massive representations. 
### Sunday, 4th January, 26 
- Completed up to page 42
## Week 4
### Monday, 5th January, 26
- Completed up to halfway through page 56
### Tuesday, 6th January, 26
- Completed page 75
### Wednesday, 7th January, 26
- Completed up to Supersymmetry breaking page 82 and reattempted the derivation using the Kahler potential and Superpotential with the Planck mass terms explicit this time as well  $$ K = -3\alpha M_{pl}^2 \ln\left( 1 - \frac{Z\bar{Z} - S\bar{S}}{M_{pl}^2} \right) \quad \text{and} \quad W = \mu S$$
- Here I find the inverse Kahler metric 
![[Term 2/Derivations/Christmas Holidays/Escher in the Sky/(1) Kahler metric part 1.png]]
![[Term 2/Derivations/Christmas Holidays/Escher in the Sky/(2) Kahler metric part 2.png]]

- Using the superpotential $$W = \mu S$$ I found the F-term potential $V_{F_{sugra}}$ and then took the limit $M_{pl} \rightarrow \infty$ which for $3\alpha = 1$ reduced to the global SUSY potential 
![[Term 2/Derivations/Christmas Holidays/Escher in the Sky/(3) F-term potential mu S part 1.png]]
![[Term 2/Derivations/Christmas Holidays/Escher in the Sky/(4) F-term potential mu S part 2.png]]

- I also took the limit $S \rightarrow 0$ as the stabilising fields go to 0 during inflation which for $3\alpha = 1$ also reduces to the same global susy potential but for $3\alpha \neq 1$ it gives a potential $$ V_F = \frac{\mu^2}{3\alpha} \left(1 - \frac{Z \bar{Z}}{M_{pl}^2} \right)^{1-3\alpha}$$ 
![[Term 2/Derivations/Christmas Holidays/Escher in the Sky/(5) F-term potential mu S part 3.png]]

### Friday, 9th January, 26
- Completed section 3 on Chiral Superfields in David Tong's lecture notes on Supersymmetry

### Sunday, 11th January, 26
- For the superpotential and the Kahler potential in the previous derivation I derived the kinetic lagrangian and then initially determined the inflationary potential after taking the canonical normalisation of the $Z$ field using the relation $$ Z = \bar{Z} = \frac{\varphi}{\sqrt{2\alpha}}$$ as in the booklet. 

![[Term 2/Derivations/Christmas Holidays/Escher in the Sky/(6) Kinetic Lagragian Fixed direction.png]]

- I then tried to generalise this, preserving the $U(1)$ symmetry with an axion on the imaginary part. I then found the equations of motion for both the $\varphi$ and the $\sigma$ particles. 

![[Term 2/Derivations/Christmas Holidays/Escher in the Sky/(7) General solution with axion part 1.png]]
![[Term 2/Derivations/Christmas Holidays/Escher in the Sky/(8) General solution with axion part 2.png]]


- For the fixed solution I attempted to plot the potential against $\phi$ to see its shape, however, I think either I made a mistake with my code or the potential does not fit the shape required for inflation as the graph I got was horizontal lines. I was not sure what value $\mu$ should take, and looking it up I read that it should be light $\mu \sim 246$ GeV [source](https://physics.stackexchange.com/questions/44404/what-is-the-mu-problem-in-susy) 

![[Term 2/Derivations/Christmas Holidays/Escher in the Sky/(9) Derived Potential for W=muS.png]]

```python
import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

parentFolder = Path(__file__).parent
graphsFolder = Path(parentFolder, "Plot")
graphsFolder.mkdir(parents=True, exist_ok=True)

ReducedPlanckMass = 2.43e18
alphaValues = [1, 3, 5, 7, 9]
phiValues = [i for i in np.linspace(0,1,1000)]
mu = 246
potentialValues = []

for alpha in alphaValues:
	VfValues = []
	for phi in phiValues:
		Vf = ((mu**2)/(3*alpha))*((1 - (np.tanh(phi/(np.sqrt(6 * alpha)*ReducedPlanckMass)))**2)**(1-3*alpha))
		VfValues.append(Vf)

	potentialValues.append(VfValues)

fig, ax = plt.subplots()
for i,V in enumerate(potentialValues):
	ax.plot(phiValues, V, label=fr"$\alpha =${alphaValues[i]}")
ax.set_ylabel(r"$V_F(\phi)$")
ax.set_xlabel(r"$\phi$")
ax.set_title(r"Derived Potential using $W = \mu S$ and $K = -3\alpha M_{pl}^2 \ln(1 - \frac{Z\bar{Z} - S\bar{S}}{M_{pl}^2})$")
plt.tight_layout()
plt.legend()
figureName = Path(graphsFolder, f'{"Derived Potential for W=muS"}.png')
plt.savefig(figureName)
```

