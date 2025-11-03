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
![[Derivations/(6), (7) part 1.png]]![[Derivations/(7) part 2.png]]
![[Derivations/(8).png]]
- The expression for the density for radiation in the hot big bang $$ \rho_{\gamma} = \frac{\pi^{2} g_{*}}{30 c^{2} (c \hbar)^3} (k_B T)^4$$ shows that the $\rho_{\gamma} \propto (k_B T)^4$, meaning that the energy density is proportional to the thermal energy of the radiation. The $g_*$ term is the effective relativistic degrees of freedom, which is a combination of degrees of freedom possessed by a collection of relativistic bosons and fermions given by $$g_* \equiv \sum_{bosons}^{i} g_i + \sum_{fermions}^{j} g_j$$ which when only considering light $g_* = 2$, however in the early universe $g_* = O (10-100)$


#### 13:00 
**2.0. Cosmic Inflation**
- In de Sitter spacetime, is a solution to the Einstein equations with 0 matter present and dominated by a cosmological constant, and is maximally symmetric in both space and time. When inflation is dominated by $\Lambda_{eff}$, it is called quasi-de Sitter inflation. This is because inflation must have an end in order for the thot big bang to occur, so spacetime does not respect the maximally symmetrical description of de Sitter space. The density during inflation is also determined by $\Lambda_{eff}$ and so is therefore constant and given by the $$\rho_{inf} \simeq \frac{\Lambda_{eff} c^2}{8 \pi G}$$ which also requires $w = -1$ for the barotropic parameter. 
- Completed derivations (10) - (11)
![[Derivations/(10).png]]

#### 22:35
**3.0. Solving the Horizon and Flatness Problems**
**3.1. The cosmological Horizon**

- Started derivation (16) and did it incorrectly but going along the right lines.


### Thursday, 9th October, 25
#### 12:10
- Completed the derivation of $D_H$ (16)
![[Derivations/(16) part 1.png]]
![[Derivations/(16) part 2.png]]
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
![[Term 1/Derivations/(26).png]]
- Completed (27)
![[Derivations/(27).png]]


#### 21:48
- Obtained (28) 
![[Term 1/Derivations/(28).png]]


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
![[Term 1/Derivations/(29).png]]

#### 13:02
- completed derivation (30)
![[Term 1/Derivations/(30).png]]

#### 13:09
**5.0. Slow-Roll Inflation**
- Beginning (32)

#### 14:45
- Completed derivation (32)
![[Term 1/Derivations/(33).png]]

- The slow-roll parameter $\epsilon$ is defined as $$ \epsilon \equiv - \frac{\dot{H}}{H^2}$$ which allows for the parameterisation of the condition for accelerated expansion. 

#### 15:38
- Completed the derivation, (35), of $$ \frac{\ddot{a}}{a} = \dot{H} + H^2 \quad \quad$$ and proof that inflation is possible only if $\epsilon < 1$.
![[Term 1/Derivations/(35).png]]

#### 15:56
- An e-fold refers to the time taken for the scale factor to increase by a factor of $e$, meaning that the number of e-folds in a given time represents how much the universe has expanded during a set timeframe. The relations $dN = -H dt$ and $\epsilon \equiv \frac{\dot{H}}{H^2}$, when combined result in the expression $\frac{dH}{H} = \epsilon dN$. The condition for the accelerated expansion of the universe is $\epsilon < 1$, and so if $\epsilon \ll 1$, the rate of accelerated expansion would be very high. This means that $dH \gg 1$ and since $dH \propto dN$, $dN \gg 1$. $\epsilon$ allows for inflation to be described by the number of expansions that the universe has undergone rather than the expansion time. 
![[Term 1/Derivations/(36).png]]

#### 16:20 
- Starting the derivation of (37)

#### 20:20
- Attempted (37) again but could not solve it
### Monday, 13th October, 25
#### 09:30
- Exporting logbook to pdf to send to Kostas