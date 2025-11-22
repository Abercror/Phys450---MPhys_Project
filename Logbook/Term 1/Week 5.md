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
![[Term 1/Derivations/9.3/Lagrangian derivation phi.png]]

#### 15:15
- Completed the show that for the T-model

#### 17:47 
- Completed the show that for the E-model
![[Term 1/Derivations/9.3/V(phi) part 1.png]]
![[Term 1/Derivations/9.3/V(phi) part 2.png]]
### Saturday, 8th November, 25
#### 13:29
- Found the value of $\alpha$ for the E-model as $\alpha = \frac{3 \pm 2 \sqrt{2}}{3}$ which equate to $\alpha = 1.943$ and $\alpha = 0.0572$ as well as equations for $n_s$ and $r$, although I am not sure if the equations are in agreement with my value I found for $\alpha$
![[Term 1/Derivations/9.3/E-model part 1.png]]
![[Term 1/Derivations/9.3/E-model part 2.png]]

#### 15:39
- Attempted to find the equations for the T-model though I made a mistake as the algebra does not simplify down to the same functions as the E-model
![[Term 1/Derivations/9.3/1 T-model part 1.png]]
![[Term 1/Derivations/9.3/1 T-model part 2.png]]

### Sunday, 9th November, 25
#### 14:17
- Re-attempting the derivation of $n_s(N)$ and $r(N)$ for the T-model
#### 23:55
- I have redone the derivations for $n_s(N)$ and $r(N)$ though I still do not get the same results as the E-model so I must have made a mistake in my working somewhere.
![[Term 1/Derivations/9.3/2 T-model part 1.png]]
![[Term 1/Derivations/9.3/2 T-model part 2.png]]
![[Term 1/Derivations/9.3/ T-model part 3.png]]


### Monday, 10th November, 25

#### 09:36 
- Exporting log book to send to Kostas