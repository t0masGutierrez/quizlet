### probability distribution function
- height of curve equal probability
---
### PDF formula

$$
\begin{aligned}
P(X=x)
\end{aligned}
$$

---
### cumulative distribution function
- area under curve equal probability
---
### CDF formula

$$
\begin{aligned}
P(X \le x)
\end{aligned}
$$

---
### z-score
- number of standard deviations from the mean
---
### z-score formula

$$
\begin{aligned}
z = \frac{X - \mu}{\sigma} \\
X = \text{datum} \\
\mu = \text{mean} \\
\sigma = \text{standard deviation}
\end{aligned}
$$

---
### standardization
- convert from random variable to standardized random variable
---
### standardization formula

$$
\begin{aligned}
(X = x) \sim (\mu, \sigma) \rightarrow (Z = z) \sim N(0, 1) \\
X = \text{random variable} \\
x = \text{real number} \\
Z = \text{standardized random variable} \\
z = \text{z-score}
\end{aligned}
$$

---
### normal
- probability as function of mean and standard deviation
---
### normal formula

$$
\begin{aligned}
X \sim N(x, \mu, \sigma) = P(X = x) \\
X \sim N(a, b, \mu, \sigma) = P(a \le X \le b) \\
x = \text{number of successes} \\
\mu = \text{mean} \\
\sigma = \text{standard deviation} \\
a = \text{lower number of successes} \\
b = \text{upper number of successes} 
\end{aligned}
$$

---
### inverse normal
- value of random variable as function of cumulative distribution function
---
### inverse normal formula

$$
\begin{aligned}
x= N^{-1}(c, \mu, \sigma, \text{tail}) \\
c = \text{cumulative probability of success} \\
\mu = \text{mean} \\
\sigma = \text{standard deviation} \\
\text{tail} = \text{direction of accumulation}
\end{aligned}
$$

---
### standard normal
- probability as function of z-score
---
### standard normal formula

$$
\begin{aligned}
Z \sim N(x, 0, 1) = P(Z = z) \\
Z \sim N(a, b, 0, 1) = P(a \le Z \le b) \\
z = \text{z-score} \\
a = \text{lower z-score} \\
b = \text{upper z-score}
\end{aligned}
$$

---
### inverse standard normal
- z-score as function of cumulative distribution function
---
### inverse standard normal formula

$$
\begin{aligned}
z = N^{-1}(c, 0, 1, \text{tail}) \\
c = \text{cumulative probability of success} \\
\text{tail} = \text{direction of accumulation}
\end{aligned}
$$

---
### binomial
- probability as function of the number of successes
---
### binomial formula

$$
\begin{aligned}
X \sim B(n, p, x) = P(X = x) \\
X \sim B(n, p, x) = P(X \le x) \\
n = \text{number of trials} \\
p = \text{probability of success} \\
x = \text{number of successes}
\end{aligned}
$$

---
### inverse binomial
- value of random variable as function of the cumulative distribution function
---
### inverse binomial formula

$$
\begin{aligned}
x = B^{-1}(c, n, p) \\
x \ge B^{-1}(c, n, p) \\
c = \text{cumulative probability of success} \\
n = \text{number of trials} \\
p = \text{probability of success} \\
x = \text{number of successes}
\end{aligned}
$$

---
### geometric
- probability as function of the number of trials until 1st success
---
### geometric formula

$$
\begin{aligned}
X \sim G(p, x) = P(X = x) \\
X \sim G(p, x) = P(X \le x) \\
p = \text{probability of success} \\
x = \text{number of successes}
\end{aligned}
$$

---
### poisson
- probability as function of the number of events within interval
---
### poisson formula

$$
\begin{aligned}
X \sim P(\lambda, x) = P(X = x) \\
X \sim P(\lambda, x) = P(X \le x) \\
\lambda = \text{average number of events per interval} \\
x = \text{number of events within interval} 
\end{aligned}
$$

---
### student
- probability as function of t-score
---
### student formula

$$
\begin{aligned}
T \sim S(t, \text{d}) = P(T = t) \\
T \sim S(a, b, \text{d}) = P(a \le T \le b) \\
t = \text{t-score} \\
\text{d} = \text{degrees of freedom} \\
a = \text{lower t-statistic} \\
b = \text{upper t-statistic} 
\end{aligned}
$$

---
### inverse student
- t-score as function of cumulative distribution function
---
### inverse student formula

$$
\begin{aligned}
t = S^{-1}(c, \text{d}) \\
c = \text{cumulative probability of success} \\
\text{d} = \text{degrees of freedom}
\end{aligned}
$$

---
### chi-squared
- probability as function of $\chi^2$-statistic
---
### chi-squared formula

$$
\begin{aligned}
X \sim \chi^2(x, \text{d}) = P(X = x) \\
X \sim \chi^2(x, \text{d}) = P(X \le x) \\
x = \text{$\chi^2$-statistic} \\
\text{d} = \text{degrees of freedom} 
\end{aligned}
$$

---
### F
- probability as function of F-statistic
---
### F formula

$$
\begin{aligned}
F \sim \chi^2(f, \text{d}_1, \text{d}_2) = P(U = u) \\
V \sim \chi^2(v, \text{d}_1, \text{d}_2) = P(V = v) \\
F = \frac{U/\text{d}_1}{V/\text{d}_2} \\
u, v = \text{F-statistic} \\
\text{d} = \text{degrees of freedom} 
\end{aligned}
$$
---
