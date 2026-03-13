perturbed equation

- equation containing small nonnegative parameter 
---
perturbed equation formula
$$
\begin{aligned}
f(t, x, \epsilon) \\
0 \le \epsilon \ll 1 \\
f = \text{perturbed equation} \\
\epsilon = \text{parameter}
\end{aligned}
$$

---
algebraic equation

- equation involving elementary functions of unknown solution
---
algebraic equation formula
$$
\begin{aligned}
y = f(t, x, \epsilon) \\
f = \text{perturbed equation} \\
t = \text{time} \\
x = \text{solution} \\
\epsilon = \text{parameter}
\end{aligned}
$$

---
differential equation

- equation involving derivatives of unknown solution
---
differential equation formula
$$
\begin{aligned}
\frac{dx}{dt} = f(t, x, \epsilon), x(t=0) = x_0, t \ge 0 \\
f = \text{perturbed equation} \\
t = \text{time} \\
x = \text{solution} \\
\epsilon = \text{parameter}
\end{aligned}
$$

---
regular

- every solution of perturbed equation with positive parameter equal solution of perturbed equation with zero parameter
---
regular formula

$$
\begin{align*}
\# f(t, x, \epsilon) = k, \epsilon > 0 \land \# f(t, x, \epsilon) = k, \epsilon = 0 \\
f = \text{perturbed equation} \\
k = \text{number of solutions} \\
\epsilon = \text{parameter} 
\end{align*}
$$
---
singular

- every solution of perturbed equation with positive parameter not equal solution of perturbed equation with zero parameter
---
singular formula

$$
\begin{align*}
\# f(t, x, \epsilon) = k, \epsilon > 0 \land \# f(t, x, \epsilon) \ne k, \epsilon = 0 \\
f = \text{perturbed equation} \\
k = \text{number of solutions} \\
\epsilon = \text{parameter} 
\end{align*}
$$
---
analytic

- there exists limit of power series near point
---
analytic formula

$$
\begin{align*}
f(t, x, \epsilon) = \sum_{i, j, k = 0}^{\infty}c_{ijk}(t-t_0)^i(x - x_0)^j(\epsilon - \epsilon_0)^k \\
|t-t_0| < \sigma, |x-x_0| < \eta, |\epsilon-\epsilon_0| < \rho \\
f = \text{perturbed equation} \\
\epsilon = \text{parameter} \\
c = \text{coefficient} \\
\sigma, \eta, \rho = \text{radius of convergence}
\end{align*}
$$
---
analytic property

- complex analytic function
- complex analytic variable
- multivariable analytic function
- analytic operation
---
analytic property formula

$$
\begin{align*}
f \in \mathbb C \rightarrow f(t, x, \epsilon) \in C^{\omega} \\
x \in \mathbb C \rightarrow f(t, x, \epsilon) \in C^{\omega} \\
i \ge 1 \rightarrow  f(t, x_i, \epsilon) \in C^{\omega} \\
(+), (\cdot), (\circ), (\frac{df}{dx}), (\int dfdx) \in C^{\omega} 
\end{align*}
$$
---
function notation

- asymptotic behavior of function as parameter approaches limit
---
function notation formula

$$
\begin{align*}
f(\epsilon) = \sum_{n=0}^\infty C_n \epsilon^n \\
\frac{f(\epsilon)}{\epsilon^r} = \sum_{n=r}^\infty C_{n-r} \epsilon^{n-r} \\
f = \text{perturbed equation} \\
\epsilon = \text{parameter} \\
C = \text{constant} 
\end{align*}
$$
---
big-O notation

- size of function less or equal big-O
---
big-O notation formula

$$
\begin{align*}
\lim_{\epsilon \rightarrow 0} |\frac{f(\epsilon)}{\epsilon^r}| \le C \rightarrow f(\epsilon) \le O(\epsilon^r) \\
f = \text{perturbed equation} \\
\epsilon = \text{parameter} \\
C = \text{constant} \\
O = \text{order} 
\end{align*}
$$
---
little-o notation

- size of function much less little-o
---
little-o notation formula

$$
\begin{align*}
\lim_{\epsilon \rightarrow 0} \frac{f(\epsilon)}{\epsilon^r} = 0 \rightarrow f(\epsilon) \ll o(\epsilon^r) \\
f = \text{perturbed equation} \\
\epsilon = \text{parameter} \\
o = \text{order} 
\end{align*}
$$
---
mclaurin series

- approximate function of parameter near zero as infinite polynomial
---
mclaurin series formula

$$
\begin{align*}
f(\epsilon) = \sum_{n=0}^\infty \frac{f^{(n)}(0)}{n!}\epsilon^n \\
f^n = \text{nth derivative} \\
n! = \text{nth factorial} \\
\epsilon = \text{center}
\end{align*}
$$
---
regular algebraic equation

- series solution equal solution of algebraic equation
![[3 Mathematical Modeling/Images/regularly perturbed algebraic equation.png]]
---
regular algebraic equation formula

$$
\begin{align*}
F(x, \epsilon) = 0, x(\epsilon = 0) = x_0 \\
0 \le \epsilon \ll 1 \\
F = \text{regular algebraic equation} \\
x = \text{solution} \\
\epsilon = \text{parameter}
\end{align*}
$$
---
regular algebraic property

- for every analytic algebraic equation there exists analytic solution
---
regular algebraic property formula

$$
\begin{align*}
(C^{\omega} \ni F(x_0, 0) = 0) \land (\frac{\partial F}{\partial x}(x_0, 0) \ne 0 \lor \frac{\partial F}{\partial \epsilon}(x_0, 0) \ne 0) \rightarrow x(\epsilon) \in C^{\omega} \\
F = \text{regular algebraic equation} \\
C^{\omega} = \text{analyticity} \\
x = \text{solution} \\
\epsilon = \text{parameter} 
\end{align*}
$$
---
simple root

- solution of regular algebraic equation equal integer power series
---
simple root formula

$$
\begin{align*}
\frac{\partial F}{\partial x}(x_0, 0) \ne 0 \rightarrow x(\epsilon) = \sum_{n=0}^{\infty} \epsilon^nx_n \\
x = \text{solution} \\
\epsilon = \text{parameter} 
\end{align*}
$$
---
repeated root

- solution of regular algebraic equation equal rational power series
---
repeated root formula

$$
\begin{align*}
\frac{\partial F}{\partial x}(x_0, 0)= 0 \rightarrow x(\delta) = \sum_{n =0}^{\infty} \delta^n x_n \\
\delta = \epsilon^{1/m} \\
x = \text{solution} \\
\epsilon = \text{parameter}  \\
m = \text{order} 
\end{align*}
$$
---
calculate series solution

- compute power series for every term
- compute power series for LHS of equation
- equate terms of equation with corresponding powers of epsilon
- solve equation
---
regular differential equation

- series solution equal solution of differential equation
![[3 Mathematical Modeling/Images/regular differential equation.png]]
---
regular differential equation formula

$$
\begin{align*}
\frac{du}{dt} = F(t, u, \epsilon), u(t=0, \epsilon) = u_0, t\ge 0 \\
0 \le \epsilon \ll 1 \\
F = \text{regular differential equation} \\
u(t, \epsilon ) = \text{solution} \\
\epsilon = \text{parameter}
\end{align*}
$$
---
regular differential property

- for every analytic differential equation there exists analytic solution
---
regular differential property formula

$$
\begin{align*}
F(0, u_0, 0) \in C^{\omega} \rightarrow u(t, \epsilon) \in C^{\omega} \\
F = \text{regular differential equation} \\
C^{\omega} = \text{analyticity} \\
u(t, \epsilon) = \text{solution} \\
\epsilon = \text{parameter} 
\end{align*}
$$
---
secularity

- unbounded growth over time destroy the periodicity of solution
---
secularity formula

$$
\begin{align*}
x_0 = \cos (t) \land x_1 = t\sin(t) \rightarrow x(t) = x_0(t) + \epsilon x_1(t) + O(\epsilon^2) = \cos(t) + \epsilon t \sin(t) \\
\lim_{t \rightarrow \infty} \epsilon t\sin(t) = \infty
\end{align*}
$$
---
poincare-lindstedt

- rescale time
- expand frequency in powers of epsilon
- expand solution in powers of epsilon
- substitute series solution into differential equation
- solve 0th epsilon order
- eliminate secularity with 1st frequency order such that coefficient of resonant term equal zero
- solve 1st epsilon order
- approximate periodic solution of nonlinear differential equation
---
poincare-lindstedt formula

$$
\begin{align*}
x''(t) + x(t) = \epsilon f(t, x, x''), 0 \le \epsilon \ll 1 \\
\omega(\epsilon) = \sum_{n=1}^{\infty} \epsilon^n\omega_n \\
\tau = \omega(\epsilon)t \\
x(t) = \sum_{n=1}^{\infty} \epsilon^nx_n(\tau)
\end{align*}
$$
---
term

- definition
---
term

- definition
---
term

- definition
---
