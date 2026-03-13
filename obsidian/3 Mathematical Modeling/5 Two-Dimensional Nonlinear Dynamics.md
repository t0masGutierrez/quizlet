### dynamical system
- rule that describes the change of state over time
---
### dynamical system formula
$$
\begin{aligned}
\frac{dx}{dt} = f(x, y, c_1, \dots, c_n), x(t=0) = x_0, t \ge 0 \\
\frac{dy}{dt} = g(x, y, c_1, \dots, c_n), y(t=0) = y_0, t \ge 0 \\
x, y = \text{solution} \\
t = \text{time} \\
x_0, y_0 = \text{initial condition} \\
c = \text{parameter}
\end{aligned}
$$
---
### nonlinear system
- products of variables
- powers of variables
- trascendental variables
- variable coefficients
---
### nonlinear system formula
$$
\begin{aligned}
u_1u_2 \\
u^p \\
\sin(u) \\
\exp(u) \\
u_1(u_2) 
\end{aligned}
$$
---
### taylor series
- approximate function near point as infinite polynomial
---
### taylor series formula
$$
\begin{aligned}
f(u) = \sum_{n=0}^\infty \frac{f^{(n)}(a)}{n!}(u-a)^n \\
f^{(n)} = \text{nth derivative} \\
n! = \text{nth factorial} \\
a = \text{center}
\end{aligned}
$$
---
### linearization
- convert from nonlinear system to linear system
---
### linearization formula
$$
\begin{aligned}
\frac{dv}{dt} = A(v_*)v + R \\
A = \begin{bmatrix} 
\frac{\partial f}{\partial x} & \frac{\partial f}{\partial y} \\
\frac{\partial g}{\partial x} & \frac{\partial g}{\partial y} 
\end{bmatrix} \\
v = \begin{bmatrix} 
x - x_* \\
y - y_*
\end{bmatrix} \\
R = \begin{bmatrix} 
R_1 \\
R_2
\end{bmatrix} \\
v = \text{solution} \\
t = \text{time} \\
v_* = \text{equilibrium point} \\
A = \text{jacobian} \\
R = \text{remainder}
\end{aligned}
$$
---
### continuous differentiability
- derivative exists and derivative continuous
---
### continuous differentiability formula
$$
\begin{aligned}
f, g:D\subset \mathbb R^n \rightarrow \mathbb R^n \land f, g \in C^2(D) \\
f, g = \text{velocity} \\
C^2 = \text{twice continuous differentiable} \\
D = \text{domain} 
\end{aligned}
$$
---
### hyperbolicity
- for every eigenvalue there exists nonzero real part
---
### hyperbolicity
$$
\begin{aligned}
\forall i \le n: \text{Re}(\lambda_i) \ne 0 \\
\lambda = \text{eigenvalue}
\end{aligned}
$$
---
### hartman-grobman property
- local behavior of twice continuously differentiable, hyperbolic, nonlinear system approximately equal behavior of linearized system
---
### hartman-grobman property formula
$$
\begin{aligned}
\lambda_1, \lambda_2 < 0 \rightarrow \forall v_0 \in \mathbb R^2: \lim_{t \rightarrow \infty} v(t) = v_* \\
(\lambda_1 > 0) \land (\lambda_2 < 0) \rightarrow  \forall v_0 \in \mathbb R^2: \lim_{t \rightarrow \infty} v(t) \ne v_* \\
\lambda_1, \lambda_2 > 0 \rightarrow  \forall v_0 \in \mathbb R^2: \lim_{t \rightarrow \infty} v(t) \ne v_* \\
\end{aligned}
$$
---
### periodic solution
- repeating solution with closed orbit
![[3 Mathematical Modeling/Images/periodic solution.png]]
---
### periodic solution formula
$$
\begin{aligned}
\forall t \ge 0: v(t + P) = v(t) \\
v = \text{solution} \\
t = \text{time} \\
P = \text{period}
\end{aligned}
$$
---
### periodic equilibrium property
- for every periodic solution there exists at least 1 equilibrium point inside the closed orbit
![[3 Mathematical Modeling/Images/periodic equilibrium property.png]]
---
### periodic equilibrium property formula
$$
\begin{aligned}
U = \{v|\forall t \ge 0: v(t + P) = v(t)\} \rightarrow \exists v_* \in U \\
U = \text{range} \\
v = \text{solution} \\
t = \text{time} \\
P = \text{period} \\
v_* = \text{equilibrium point} 
\end{aligned}
$$
---
### poincare–bendixson property
- if region enclose but not contain at least 1 equilibrium point and vector field on boundary point into region then there exists periodic solution inside region
![[3 Mathematical Modeling/Images/poincare–bendixson property.png]]
---
### poincare–bendixson property formula
$$
\begin{aligned}
(R' \subset R \subset \mathbb R^2) \\
\land (R \subset \mathbb R^2, \exists v_0 \in \mathbb R^2, \exists (r > 0) \in \mathbb R: B_r(v_0) \supset R) \\
\land (\mathbb R^2 \ni v_* \not\in R) \\
\land (\nabla R \le 0) \\
\rightarrow \exists v \in R, \forall t \ge 0: v(t + P) = v(t) \\
R = \text{compact set} \\
R' = \text{derived set} \\
v_* = \text{equilibrium point} \\
v = \text{solution} \\
t = \text{time} \\
P = \text{period}
\end{aligned}
$$
---
### nonlinear center property
- infinite periodic solution surround neighborhood of first integral extremum
---
### nonlinear center property formula
$$
\begin{aligned}
 \exists\epsilon > 0, \forall v \in N_{\epsilon}(v_*): E(v) \gtrless E(v_*) \rightarrow \exists\epsilon > 0, \forall v \in N_{\epsilon}(v_*), \forall t \ge 0: v(t + P) = v(t) \\
E = \text{first integral} \\
v = \text{solution} \\
t = \text{time} \\
v_* = \text{equilibrium point} \\
N = \text{neighborhood} \\
P = \text{period}
\end{aligned}
$$
---
### bifurcation
- quantitative change of parameter cause qualitative change of phase
---
### bifurcation formula
$$
\begin{aligned}
\Delta h \rightarrow \Delta (v_* \times h)
\end{aligned}
$$
---
### bifurcation example
- $f(u) = hx - x^2$ 
- $u_* = 0, \pm \sqrt h$ 
---
### bifurcation example formula
$$
\begin{aligned}
h \le 0 \rightarrow f'(0) > 0 \\
h > 0 \rightarrow f'(0) < 0 \\
h > 0 \rightarrow f'(\sqrt h) > 0 \\
h > 0 \rightarrow f'(-\sqrt h) > 0 \\
\end{aligned}
$$
---
### bifurcation diagram
- find equilibrium point
- determine stability of equilibrium point
- find parameter where the number, type, or location of stability of equilibria change
- graph the equilibrium point versus the parameter
![[3 Mathematical Modeling/Images/bifurcation diagram.png]]
---
### bifurcation diagram formula
$$
\begin{aligned}
u_* \times h = \{(u_*, h)| f(u, h) = 0\} \\
u_* = \text{equilibrium point} \\
h = \text{parameter}
\end{aligned}
$$
---
