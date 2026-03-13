### 1-sample hypothesis test
- compare sample statistic with population parameter
---
### 2-sample hypothesis test
- compare group 1 with group 2
---
independent sample
 - groups with no meaningful relationship
---
### dependent sample
- groups with meaningful relationship
---
### sample proportion
- point estimate of population proportion
---
### two proportion confidence interval
- find critical value
- calculate test statistic
- calculate margin of error
- $(\hat p_1 - \hat p_2) - E < (\hat p_1 - \hat p_2) < (\hat p_1 - \hat p_2) + E$ 
---
### two proportion z interval formula
$$
\begin{aligned}
\text{2propZint}(x_1, n_1, x_2, n_2, \alpha) \\
x = \text{number of successes} \\
n = \text{sample size} \\
\alpha = \text{confidence level}
\end{aligned}
$$
---
### two proportion hypothesis test
- definition
---
### two proportion z test formula
$$
\begin{aligned}
\text{2propZtest}(x_1, n_1, x_2, n_2, p_1) \\
x = \text{number of successes} \\
n = \text{sample size} \\
p_1 = \text{alternative hypothesis}
\end{aligned}
$$
---
### sample mean
- point estimate of population mean
---
### two mean confidence interval
- find critical value 
- calculate margin of error
- $(\bar x_1 - \bar x_2) - E < (\mu_1 - \mu_2) < (\bar x_1 - \bar x_2) + E$ 
---
### two mean t interval formula
$$
\begin{aligned}
\text{2sampTint}(\bar x_1, s_1, n_1, \bar x_2, s_2, n_2, \alpha, \text{pool}) \\
\bar x = \text{mean} \\
s = \text{standard deviation} \\
n = \text{sample size} \\
\alpha = \text{confidence level} \\
\text{pool} = \text{if equal then yes}
\end{aligned}
$$
---
### two mean hypothesis test
- definition
---
### two mean t test formula
$$
\begin{aligned}
\text{2sampTtest}(\bar x_1, s_1, n_1, \bar x_2, s_2, n_2, \mu_1 : \mu_2, \text{pool}) \\
\bar x = \text{mean} \\
s = \text{standard deviation} \\
n = \text{sample size} \\
\mu_1 : \mu_2 = \text{equality} \\
\text{pool} = \text{no}
\end{aligned}
$$
---
### pool sample variance
- combination of two sample variance into single sample variance  
- population variance unknown and equal
---
### pool sample variance formula
$$
\begin{aligned}
s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2} \\
n = \text{sample size} \\
s = \text{standard deviation}
\end{aligned}
$$
---
### match pair
- meaningful relationship between sample means
---
### match pair confidence interval
- find critical value  
- calculate margin of error
- $\bar d - E < µ < \bar d + E$ 
---
### match pair t interval
$$
\begin{aligned}
\text{tInt}(\text{data}, L_3, f, \alpha) \\
\end{aligned}
$$
---
### match pair hypothesis test
- definition
---
### match pair t test
$$
\begin{aligned}
\text{tTest} (\text{data}, \mu_0, L_3, f, \mu_1)
\end{aligned}
$$
---
### F distribution
- probability distribution of sample statistic that describes the variability of random sampling of the same size from the same population
![[4 Statistics/Images/F distribution.png]]
---
### sample variance
- point estimate of population variance
---
### two variance hypothesis test
- null hypothesis $σ_1^2 = σ_2^2$
- two variance F test
---
### two variance F test formula
$$
\begin{aligned}
\text{2sampFtest}(s, n, \sigma_1) \\
s = \text{standard deviation} \\
n = \text{sample size} \\
\sigma = \text{alternative hypothesis}
\end{aligned}
$$
---
