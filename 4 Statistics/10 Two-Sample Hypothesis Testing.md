### 1-sample hypothesis test
- compare sample statistic with population parameter
---
### 2-sample hypothesis test
- compare group 1 with group 2
---
independent sample
 - there exists no meaningful relationship between group 1 and group 2
---
### dependent sample
- there exists meaningful relationship between group 1 and group 2
---
### standard error
- standard deviation of sampling distribution
---
### mean difference standard error formula

$$
\begin{aligned}
SE(\bar X_1 - \bar X_2) = \sqrt{\frac{\sigma_1^2}{n_1} + \frac{\sigma_2^2}{n_2}} \\
\sigma = \text{standard deviation} \\
n = \text{sample size}
\end{aligned}
$$

---
### proportion difference standard error formula

$$
\begin{aligned}
SE(\hat p_1 - \hat p_2) = \sqrt{\frac{p_1(1-p_1)}{n_1} + \frac{p_2(1-p_2)}{n_2}} \\
p = \text{proportion} \\
n = \text{sample size}
\end{aligned}
$$

---
### sample proportion
- point estimate of population proportion
---
### two proportion confidence interval
- compute sample proportion
- compute standard error
- find critical value from confidence level
- compute margin of error
- $(\hat p_1 - \hat p_2) - E < (\hat p_1 - \hat p_2) < (\hat p_1 - \hat p_2) + E$ 
---
### two proportion z-interval formula

$$
\begin{aligned}
\text{2propZ-int}(X_1, n_1, X_2, n_2, 1-\alpha) \\
X= \text{number of successes} \\
n = \text{sample size} \\
\alpha = \text{significance level}
\end{aligned}
$$

---
### two proportion hypothesis test
- state hypotheses
- choose significance level  
- calculate test statistic  
- choose method
- reject or fail to reject null hypothesis  
- state conclusion
---
### two proportion z-test formula

$$
\begin{aligned}
\text{2propZ-test}(X_1, n_1, X_2, n_2, p_1) \\
X= \text{number of successes} \\
n = \text{sample size} \\
p_1 = \text{alternative hypothesis}
\end{aligned}
$$

---
### sample mean
- point estimate of population mean
---
### two mean confidence interval
- compute sample proportion
- compute standard error
- find critical value from confidence level
- compute margin of error
- $(\bar X_1 - \bar X_2) - E < (\mu_1 - \mu_2) < (\bar X_1 - \bar X_2) + E$ 
---
### two mean t-interval formula

$$
\begin{aligned}
\text{2avgT-int}(\bar X_1, s_1, n_1, \bar X_2, s_2, n_2, \alpha, \text{pool}) \\
\bar X= \text{sample mean} \\
s = \text{sample standard deviation} \\
n = \text{sample size} \\
\alpha = \text{significance level} \\
\text{pool} = \text{if equal then yes}
\end{aligned}
$$

---
### two mean hypothesis test
- state hypotheses
- choose significance level  
- calculate test statistic  
- choose method
- reject or fail to reject null hypothesis  
- state conclusion
---
### two mean t-test formula

$$
\begin{aligned}
\text{2avgT-test}(\bar X_1, s_1, n_1, \bar X_2, s_2, n_2, \mu_1 = \mu_2, \text{pool}) \\
\bar X= \text{sample mean} \\
s = \text{sample standard deviation} \\
n = \text{sample size} \\
\text{pool} = \text{no}
\end{aligned}
$$

---
### pool variance
- combination of two sample variance into single sample variance  
- population variance unknown and equal
---
### pool variance formula

$$
\begin{aligned}
s_p^2 = \frac{(n_1 - 1)s_1^2 + (n_2-1)s_2^2}{n_1+n_2-2} \\
n = \text{sample size} \\
s = \text{sample standard deviation}
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
