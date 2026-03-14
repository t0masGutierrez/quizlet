### random variable
- function of sample space outcome equal real number
---
### random variable formula

$$
\begin{aligned}
X: \Omega \rightarrow \mathbb R, X(\omega) = x\\
X = \text{random variable} \\
\Omega = \text{sample space} \\
x = \text{real number} \\
\omega = \text{outcome}
\end{aligned}
$$

---
### continuous random variable
- random variable whose values are uncountable
---
### continuous random variable formula

$$
\begin{aligned}
(\{0, 1, 2, 3, \dots, n\} \not\sim X) \land (\mathbb N \not\sim X) \\
X = \text{random variable}
\end{aligned}
$$

---
### continuous probability density function
- probability as function of continuous random variable
---
### continuous PDF probability formula

$$
\begin{aligned}
P(X = x) = 0 \\

P(X) = \int_{-\infty}^{\infty}f(x)dx = 1 \\
P(a \le X \le b) = \int_a^b f(x)dx
\end{aligned}
$$

---
### expectation
- expected value of random variable
---
### expectation formula

$$
\begin{aligned}
E[X] =  \int_{-\infty}^{\infty} xf(x)dx \\
x = \text{real number} \\
X = \text{random variable}
\end{aligned}
$$

---
### variation
- variance of random variable around expected value
---
### variation formula

$$
\begin{aligned}
\text{Var}(X) = E[X^2] - (E[X])^2 = E[(X - E[X])^2] \\
E = \text{expectation} \\
X = \text{random variable}
\end{aligned}
$$

---
### uniform probability density function
- probability as function of equally likely events
---
### uniform PDF probability formula

$$
\begin{aligned}
f(x) = \frac{1}{b-a} \\
a = \text{lower endpoint} \\
b = \text{upper endpoint} 
\end{aligned}
$$

---
### uniform PDF expectation formula

$$
\begin{aligned}
\mu = \frac{a+b}{2} \\
a = \text{lower endpoint} \\
b = \text{upper endpoint} 
\end{aligned}
$$

---
### uniform PDF variance formula

$$
\begin{aligned}
\sigma = \sqrt{\frac{(b-a)^2}{12}} \\
a = \text{lower endpoint} \\
b = \text{upper endpoint} 
\end{aligned}
$$

---
### normal probability density function
- probability as function of mean and standard deviation
---
### normal PDF probability formula

$$
\begin{aligned}
f(x) = \frac{\exp(\frac{-(x - \mu)^2}{2\sigma^2})}{\sigma\sqrt {2\pi}} \\
\mu = \text{mean} \\
\sigma = \text{standard deviation}
\end{aligned}
$$

---
### normal PDF expectation formula

$$
\begin{aligned}
E[X] = \mu \\
\mu = \text{mean} 
\end{aligned}
$$

---
### normal PDF variance formula

$$
\begin{aligned}
\text{Var}(X) = \sigma^2 \\
\sigma = \text{standard deviation} 
\end{aligned}
$$

---
### standard normal probability density function
- probability as function of z-score
---
### standard normal PDF probability formula

$$
\begin{aligned}
f(x) = \frac{e^{-x^2/2}}{\sqrt {2\pi}} \\
x = \text{z-score}
\end{aligned}
$$

---
### standard normal PDF expectation formula

$$
\begin{aligned}
\mu = 0 
\end{aligned}
$$

---
### standard  normal PDF variance formula

$$
\begin{aligned}
\sigma = 1
\end{aligned}
$$

---
### exponential probability density function
- probability as function of the amount of time between events
---
### exponential PDF probability formula

$$
\begin{aligned}
f(x) = \lambda e^{-\lambda x} \\
x = \text{amount of time between events} \\
\lambda = \text{average number of events per time}
\end{aligned}
$$

---
### exponential PDF expectation formula

$$
\begin{aligned}
E[X] = \frac{1}{\lambda} \\
\lambda = \text{average number of events per time}
\end{aligned}
$$

---
### exponential PDF variance formula

$$
\begin{aligned}
\text{Var}(X) = \frac{1}{\lambda^2} \\
\lambda = \text{average number of events per time}
\end{aligned}
$$

---
### gamma probability density function
- probability as function of waiting time until the $\alpha$th event
---
### gamma PDF probability formula

$$
\begin{aligned}
f(x) = \frac{\lambda e^{-\lambda x}(\lambda x)^{\alpha-1}}{\Gamma(\alpha)} \\
\Gamma(\alpha) = \int_0^{\infty}e^{-x}x^{\alpha-1}dx \\
\lambda = \text{average number of events per time} \\
x = \text{amount of time between events} \\
\Gamma = \text{gamma} \\
\alpha = \text{event number}
\end{aligned}
$$

---
### gamma PDF expectation formula

$$
\begin{aligned}
E[X] = \frac{\alpha}{\lambda} \\
\alpha = \text{event number} \\
\lambda = \text{average number of events per time} 
\end{aligned}
$$

---
### gamma PDF variance formula

$$
\begin{aligned}
\text{Var}(X) = \frac{\alpha}{\lambda^2} \\
\alpha = \text{event number} \\
\lambda = \text{average number of events per time} 
\end{aligned}
$$

---
### beta probability density function
- probability as function of unit interval
---
### beta PDF probability formula

$$
\begin{aligned}
f(x) = \frac{x^{\alpha-1}(1-x)^{\beta-1}}{B(\alpha, \beta)} \\
B(\alpha, \beta) = \int_0^1 x^{\alpha-1}(1-x)^{\beta-1}dx
\end{aligned}
$$

---
### beta PDF expectation formula

$$
\begin{aligned}
E[X] = \frac{\alpha}{\alpha+\beta} \\
\alpha, \beta = \text{parameter}
\end{aligned}
$$

---
### beta PDF variance formula

$$
\begin{aligned}
\text{Var}(X) = \frac{\alpha \beta}{(\alpha + \beta)^2(\alpha + \beta + 1)} \\
\alpha, \beta = \text{parameter}
\end{aligned}
$$

---
