### Saturday, 25th October, 25
#### 09:34
**8.0. Starobinsky-type Inflation**
- Investigating the potential $$V(\phi) = V_0 \left(1 - e^{\frac{- q \phi }{m_p}} \right)^2 $$ which describe the Starobinsky family of inflation models where $q>0$ is a real dimensionless parameterising constant. 

- I need to calculate the slow-roll parameters $\epsilon(\phi)$ and $|\eta(\phi)|$ for a given $q$

####  13:23
- Derived the equations of $\eta$ and $\epsilon$ as $$\eta = 2 q^2 e^{- \frac{ q \phi}{m_p}} \frac{\left(-1 + 2 e^{- \frac{ q \phi}{m_p}} \right)}{\left(1 - e^{- \frac{ q \phi}{m_p}} \right)^2} \quad \text{and} \quad \epsilon = \frac{2q^2 e^{- \frac{2q \phi}{m_p}}}{\left(1 - e^{-\frac{q \phi}{m_p}} \right)^2} $$
- Inflation ends when either $|\eta|$ or $\epsilon$ is equal to 1 and in this case $\epsilon$ will reach 1 first. 
![[Term 1/Derivations/(86) 1.png]]


#### 13:41
- Found the result for $\phi_{end}$ as $$ \phi_{end} = \frac{m_p}{q} \ln \left( \sqrt{2} q + 1 \right)$$
![[Term 1/Derivations/(86) 2.png]]
#### 19:20
- In order to find $\phi(N)$, I tried to use the integral $$N = \frac{1}{m^2_p} \int^{\phi}_{\phi_{end}} \frac{V}{V'} d\phi $$ and after subbing in the $V$ and $V'$ I got this integral º$$N = \int^{\phi}_{\phi_{end}} \frac{e^\frac{q \phi'}{m_p} - 1}{2qm_p} d\phi' $$ which I integrated. This did not gave me a $\phi$ term in the $e^{\frac{q \phi}{m_p}}$ which meant that it was not straightforward to get a function of $\phi(N)$. I attempted to look up the Lambert function to see if that could be useful as I have seen it used in a similar situation before but after looking I didn't think that it would help very much. I also tried to use a Maclaurin approximation on $e^{\frac{q \phi}{m_p}}$ in the integral, resulting in $$N = \int^{\phi}_{\phi_{end}} \frac{1 - \frac{q}{m_p}\phi' - 1}{2qm_p} d\phi'  = \int^{\phi}_{\phi_{end}} \frac{\phi'}{2m^2_p} d\phi' $$ though I am not sure that this is a valid solution. 
- Integrating the initial form of the equation I was able to get $$N = \frac{1}{2qm_p} \left. \left(\frac{m_p}{q} e^\frac{q \phi}{m_p} - \phi \right) \right|_{\phi_{end}}^{\phi}$$ and then using substitution of $e^\frac{q \phi}{m_p} = x$ I was able to get an equation in the form $$ x - \ln x = 2q^2 N + \left(\sqrt{2}q + 1 \right) + \ln \left(\sqrt{2}q + 1 \right)$$ and taking the approximation that $\ln x \ll x$ for $x > 1$ gives the relation $$x \approx 2q^2 N +  \left( \sqrt{2}q + 1 \right) + \ln \left( \sqrt{2}q + 1 \right)$$ and then saying that $2q^2 N \gg  \left( \sqrt{2}q + 1 \right) + \ln \left( \sqrt{2}q + 1 \right)$ gives the relation $$ e^{\frac{q \phi(N)}{m_p}} \approx 2q^2 N$$ and so $\epsilon$ and $\eta$ are $$\epsilon \approx \frac{1}{2q^2 N^2} \quad \text{and} \quad \eta \approx -\frac{1}{N}$$ 
![[Term 1/Derivations/(86) 3.png]]
![[Term 1/Derivations/(86) 4.png]]
### Sunday, 26th October, 25
#### 13:10
- Using $\eta$ and $\epsilon$, I was able to find the functions $n_s(N)$ and $r(N)$ as $$n_s = 1 - \frac{2}{N} \quad \text{and} \quad r = \frac{8}{q^2 N^2}$$ using the approximation that $\frac{1}{N^2} \ll \frac{1}{N}$ for $n_s$. 

#### 15:19 
- Found $N = 56.98 \approx 57$ for $n_s = 0.9649\pm 0.0042$ which combined with $r < 0.0028$ gave a lower bound for $q > 0.297$. 
![[Term 1/Derivations/(86) 5.png]]

#### 16:20
- Using the equation $$\sqrt{P_{\xi}} = \frac{1}{2\sqrt{3} \pi} \frac{V^{\frac{3}{2}}}{m_p^3 |V'|}$$ it can be recast using $$\epsilon = \frac{1}{2} m_p^2 \left( \frac{V'}{V}^2 \right)$$ into the form $$P_{\xi} = \frac{1}{24 \pi^2} \frac{V}{m_p^4 \epsilon}$$ and subbing in $\epsilon$ gives $P_{\xi} = P_{\xi}(N)$ 

![[Term 1/Derivations/(86) 6.png]]
#### 18:30
- For equation B I need to find $V_{end}^{\frac{1}{4}}$ and $V_*$. Using $\phi_{end}$ I can find $V_{end}^{\frac{1}{4}}$ using the the equation for $P_{\xi}$ and for $V_*$, I can use the relation of $e^{\frac{q \phi(N)}{m_p}} \approx 2q^2 N$ where $N = N_*$. 
- I am unsure of what approximation I can use when subbing into equation (63), and whether I can take $V \approx V_0$ in this question or not. 

### Monday, 27th October, 25
#### 10:48
- Exporting to a PDF to send to Kostas. 