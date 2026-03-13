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
### discrete random variable
- random variable whose values are max countable
---
### discrete random variable formula
$$
\begin{aligned}
(\{0, 1, 2, 3, \dots, n\} \sim X) \lor (\mathbb N \sim X) \\
X = \text{random variable}
\end{aligned}
$$
---
### discrete probability mass function
- probability as function of discrete random variable
---
### discrete PMF probability formula
$$
\begin{aligned}
\sum_i P(X = x_i) = 1 \\
P(a \le X \le b) = \sum_{i=a}^b P(X = x_i)
\end{aligned}
$$
---
### expectation
- expected value of random variable
---
### expectation formula
$$
\begin{aligned}
E[X] = \sum_i x_iP(X=x_i) \\
x = \text{real number} \\
X = \text{random variable}
\end{aligned}
$$
---
### expectation property
- sum
- linearity
- function
---
### expectation property formula
$$
\begin{aligned}
E[\sum_i X_i] = \sum_i E[X_i] \\
E[aX + bY] = aE[X] + bE[Y] \\
E[g(X)] = \sum_i g(x_i)P(X=x_i) \\
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
### variation property
- addition
- multiplication
---
### variation property formula
$$
\begin{aligned}
\text{Var}(X + c) = \text{Var}(X) \\
\text{Var}(cX) = c^2\text{Var}(X)
\end{aligned}
$$
---
### bernoulli probability mass function
- probability as function of single success
---
### bernoulli PMF assumptions
- single trial
- two outcomes
---
### bernoulli PMF probability formula
$$
\begin{aligned}
P(X = k) = pq^{1-k} \\
X = \text{random variable} \\ 
n = \text{number of trials} \\
p = \text{probability of success} \\
q = \text{probability of failure} 
\end{aligned}
$$
---
### bernoulli PMF expectation formula
$$
\begin{aligned}
E[X] = p \\
X = \text{random variable} \\
p = \text{probability of success}
\end{aligned}
$$
---
### bernoulli PMF variance formula
$$
\begin{aligned}
\text{Var}(X) = pq \\
X = \text{random variable} \\
p = \text{probability of success} \\
q = \text{probability of failure}
\end{aligned}
$$
---
### binomial probability mass function
- probability as function of the number of successes
---
### binomial PMF assumptions
- two outcomes
- fixed number of trials
- constant probability of success
- independent trials
---
### binomial PMF probability formula
$$
\begin{aligned}
P(X = k) = \begin{pmatrix} n \\ k \end{pmatrix}p^kq^{n-k} \\
X = \text{random variable} \\
n = \text{number of trials} \\
k = \text{number of successes} \\
p = \text{probability of success} \\
q = \text{probability of failure} 
\end{aligned}
$$
---
### binomial PMF expectation formula
$$
\begin{aligned}
E[X] = np \\
X = \text{random variable} \\
n = \text{number of trials} \\
p = \text{probability of success}
\end{aligned}
$$
---
### binomial PMF variance formula
$$
\begin{aligned}
\text{Var}(X) = npq \\
X = \text{random variable} \\
n = \text{number of successes} \\
p = \text{probability of success} \\
q = \text{probability of failure}
\end{aligned}
$$
---
### negative binomial probability mass function
- probability as function of the number of trials until rth success
---
### negative binomial PMF assumptions
- two outcomes
- random number of trials
- constant probability of success
- independent trials
---
### negative binomial PMF probability formula
$$
\begin{aligned}
P(X = k) = \begin{pmatrix} k-1 \\ r - 1 \end{pmatrix} p^rq^{k-r} \\
X = \text{random variable} \\
k = \text{number of trials} \\
r = \text{success number} \\
p = \text{probability of success} \\
q = \text{probability of failure} 
\end{aligned}
$$
---
### negative binomial PMF mean formula
$$
\begin{aligned}
E[X] = \frac{r}{p} \\
r = \text{success number} \\
p = \text{probability of success}
\end{aligned}
$$
---
### negative binomial PMF standard deviation formula
$$
\begin{aligned}
\text{Var}(X) = \frac{rq}{p^2} \\
r = \text{success number} \\
q = \text{probability of failure} \\
p = \text{probability of success} 
\end{aligned}
$$
---
### geometric probability mass function
- probability as function of the number of trials until 1st success
- probability as function of the number of failures before 1st success
---
### geometric PMF assumptions
- two outcomes
- random number of trials
- constant probability of success
- independent trials
---
### geometric PMF probability formula
$$
\begin{aligned}
P(X_1 = k_1) = pq^{k_1-1} \\
P(X_2 = k_2) = pq^{k_2} \\
X = \text{random variable} \\
p = \text{probability of success} \\
q = \text{probability of failure} \\
k_1 = \text{number of trials until 1st success} \\
k_2 = \text{number of failures before 1st success}
\end{aligned}
$$
---
### geometric PMF expectation formula
$$
\begin{aligned}
E[X_1] = \frac{1}{p} \\
E[X_2] = \frac{q}{p} \\
X = \text{random variable} \\
p = \text{probability of success} \\
q = \text{probability of failure}
\end{aligned}
$$
---
### geometric PMF variance formula
$$
\begin{aligned}
\text{Var}(X) = \frac{q}{p^2} \\
X = \text{random variable} \\
q = \text{probability of failure} \\
p = \text{probability of success} 
\end{aligned}
$$
---
### hypergeometric probability mass function
- probability as function of the number of items drawn from the group of interest
---
### hypergeometric PMF assumptions
- finite population
- variable probability of success
- dependent trials
---
### hypergeometric PMF probability formula
$$
\begin{aligned}
P(X = k) = \frac{\begin{pmatrix} K \\ k \end{pmatrix}\begin{pmatrix} N-K \\ n-k \end{pmatrix}}{\begin{pmatrix} N \\ n \end{pmatrix}} \\
X = \text{random variable} \\
K = \text{interest group size} \\
k = \text{number of interest items drawn} \\
N = \text{population size} \\
n = \text{number of items drawn}
\end{aligned}
$$
---
### hypergeometric PMF expectation formula 
$$
\begin{aligned}
E[X] = \frac{nK}{N} \\
X = \text{random variable} \\
n = \text{number of items drawn} \\
K = \text{interest group size} \\
N = \text{population size} 
\end{aligned}
$$
---
### hypergeometric PMF variance formula
$$
\begin{aligned}
\text{Var}(X) = (\frac{nK}{N})(1 - \frac{K}{N})(\frac{N-n}{N-1}) \\
X = \text{random variable} \\
n = \text{number of items drawn} \\
K = \text{interest group size} \\
N = \text{population size}
\end{aligned}
$$
---
### poisson probability mass function
- probability as function of the number of events within interval
- approximate binomial PMF with small probability of success and large number of trials
---
### poisson PMF assumptions
- fixed interval
- constant average number of events per interval
- independent events 
- disjoint events
---
### poisson PMF probability formula
$$
\begin{aligned}
P(X = k) = \frac{e^{-\lambda}\lambda^k}{k!} \\
X = \text{random variable} \\
k = \text{number of events within interval} \\
\lambda = \text{average number of events per interval} 
\end{aligned}
$$
---
### poisson PMF expectation formula
$$
\begin{aligned}
E[X] = \lambda \\
X = \text{random variable} \\
\lambda = \text{average number of events per interval}
\end{aligned}
$$
---
### poisson PMF variance formula
$$
\begin{aligned}
\text{Var}(X) = \lambda \\
X = \text{random variable} \\
\lambda = \text{average number of events per interval} 
\end{aligned}
$$
---
