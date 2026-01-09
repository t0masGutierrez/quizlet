metric
- distance between coordinates of set
---
metric formula
$$
\begin{align*}
\forall \vec p, \vec q \in \mathbb R^k: \text{d}(\vec p, \vec q) = \sqrt{\sum_{i=1}^k (\vec p_i - \vec q_i)^2}
\end{align*}
$$
---
metric space
- set whose distance between coordinates equal real number
---
metric space formula
$$
\begin{align*}
\vec p = \vec q \leftrightarrow \text{d}(\vec p, \vec q) = 0 \\
\vec p \ne \vec q \rightarrow \text{d}(\vec p, \vec q) > 0 \\
\text{d}(\vec p, \vec q) = \text{d}(\vec q, \vec p) \\
\text{d}(\vec p, \vec q) \le \text{d}(\vec p, \vec b) + \text{d}(\vec b, \vec q) 
\end{align*}
$$
---
open ball
- sphere with finite radius from the center
---
open ball formula
$$
\begin{align*}
B_r(\vec p) = \{\vec q \in \mathbb R^k |\text{d}(\vec p, \vec q) < r\} \\
\vec q = \text{point} \\
\text{d} = \text{metric} \\
\vec p = \text{center} \\
r = \text{radius}
\end{align*}
$$
---
neighborhood
- region where there exists open ball around center
---
neighborhood formula
$$
\begin{align*}
S \subseteq X, \exists (r > 0) \in \mathbb R: V(x_0) = \{x \in X|B_r(x_0) \subseteq S\} \\
X = \text{metric space} \\
r = \text{radius} \\
x = \text{point} \\
B = \text{open ball} \\
x_0 = \text{center}
\end{align*}
$$
---
limit point
- every neighborhood around limit point contain point from set
---
limit point formula
$$
\begin{align*}
S \subseteq X, \forall (r > 0) \in \mathbb R, \exists x \in V(x_0): (x \ne x_0) \land (x \in S) \\
X = \text{metric space} \\
r = \text{radius} \\
V = \text{neighborhood} \\
x_0 = \text{limit point}
\end{align*}
$$
---
interior point
- every point of neighborhood around interior point equal point of set
---
interior point formula
$$
\begin{align*}
S \subseteq X, \exists (r > 0) \in \mathbb R: V(x_0) \subseteq S \\
X = \text{metric space} \\
r = \text{radius} \\
V = \text{neighborhood} \\
x_0 = \text{interior point}
\end{align*}
$$
---
closed
- every limit point of closed set equal point of closed set
---
closed formula
$$
\begin{align*}
S \subseteq X, \forall x_0 \in S': x_0 \in S \\
S = \text{closed set} \\
X = \text{metric space} \\
S' = \text{derived set} \\
x_0 = \text{limit point}
\end{align*}
$$
---
open
- every point of open set equal interior point of open set
---
open formula
$$
\begin{align*}
S \subseteq X, \forall x \in S, \exists (r > 0) \in \mathbb R: V(x) \subseteq S \\
S = \text{open set} \\
X = \text{metric space} \\
r = \text{radius} \\
V = \text{neighborhood} \\
x = \text{interior point}
\end{align*}
$$
---
perfect
- closed set and every point of perfect set equal limit point of perfect set
---
perfect formula
$$
\begin{align*}
S \subseteq X, \forall x_0 \in S', \forall x \in S: (x_0 \in S) \land (x \in S') \\
S = \text{perfect set} \\
X = \text{metric space} \\
S' = \text{derived set} 
\end{align*}
$$
---
bounded
- every point of bounded set within finite radius from the center
---
bounded formula
$$
\begin{align*}
S \subseteq X, \exists (r > 0) \in \mathbb R, \exists x_0 \in X, \forall x \in S: \text{d}(x, x_0) < r \\
S = \text{bounded set} \\
X = \text{metric space} \\
r = \text{radius} \\
x_0 = \text{center} \\
x = \text{point} \\
\text{d} = \text{metric}
\end{align*}
$$
---
dense
- every point of metric space equal limit point of dense set or equal point of dense set
---
dense formula
$$
\begin{align*}
S \subseteq X, \forall x \in X: x \in (S \cup S') \\
S = \text{dense set} \\
X = \text{metric space} \\
S' = \text{derived set}
\end{align*}
$$
---
open neighborhood property
- every neighborhood around center contain open set including the center
---
open neighborhood property formula
$$
\begin{align*}
\forall (r > 0) \in \mathbb R: x_0 \in B_r(x_0) \subseteq V(x_0) \\
r = \text{radius} \\
B = \text{open ball} \\
x_0 = \text{center} \\
V = \text{neighborhood}
\end{align*}
$$
---
infinite limit point property
- every neighborhood around limit point contain infinite point of set
---
infinite limit point property formula
$$
\begin{align*}
S \subseteq X, \forall (r > 0) \in \mathbb R: |V(x_0) \cap (S \setminus \{x_0\})| = \infty \\
X = \text{metric space} \\
r = \text{radius} \\
V = \text{neighborhood} \\
x_0 = \text{limit point}
\end{align*}
$$
---
finite limit point property
- every point of finite set equal isolated point of finite set
---
finite limit point property formula
$$
\begin{align*}
\exists n \in \mathbb N: |S| = |\{0, 1, 2, 3, \dots, n\}| \rightarrow S \subseteq X, \forall (r > 0) \in \mathbb R, \forall x \in V(x_0): (x = x_0) \lor (x \not\in S) \\
S = \text{finite set} \\
X = \text{metric space} \\
r = \text{radius} \\
x_0 = \text{isolated point}
\end{align*}
$$
---
join complement property
- complement of set union equal intersection of set complement
---
join complement property formula
$$
\begin{align*}
(\bigcup_{i=1} S_i)^c = \bigcap_{i=1} (S_i^c) \\
c = \text{complement}
\end{align*}
$$
---
boundary complement property
- complement of open set equal closed set
- complement of closed set equal open set
---
boundary complement property
$$
\begin{align*}
S \subseteq X, \forall x \in S, \exists (r > 0) \in \mathbb R: V(x) \subseteq S \leftrightarrow \forall x_0 \in (S')^c: x_0 \in S^c \\
S \subseteq X, \forall x_0 \in S': x_0 \in S \leftrightarrow \forall x \in S^c, \exists (r > 0) \in \mathbb R: V(x) \subseteq S^c \\
r = \text{radius} \\
V = \text{neighborhood} \\
x = \text{interior point} \\
c = \text{complement} \\
S' = \text{derived set} \\
x_0 = \text{limit point}
\end{align*}
$$
---
join boundary complement property
- union of open set equal open set
- intersection of closed set equal closed set
- finite intersection of open set equal open set
- finite union of closed set equal closed set
---
join boundary complement property formula
$$
\begin{align*}
S \subseteq X, \forall x \in S, \exists (r > 0) \in \mathbb R: V(x) \subseteq S \rightarrow V(x) \subseteq \bigcup_{i=1} S_i \\
S \subseteq X, \forall x_0 \in S': x_0 \in S \rightarrow x_0 \in \bigcap_{i=1} S_i \\
S \subseteq X, \forall x \in S, \exists (r > 0) \in \mathbb R: V(x) \subseteq S \rightarrow V(x) \subseteq \bigcap_{i=1}^k S_i \\
S \subseteq X, \forall x_0 \in S': x_0 \in S \rightarrow x_0 \in \bigcup_{i=1}^k S_i \\
\end{align*}
$$
---
closure
- set union between set and derived set
---
closure formula
$$
\begin{align*}
\bar S = S' \cup S\\
S' = \text{derived set}
\end{align*}
$$
---
closure property
- closed
- equal
- subset
---
closure property formula
$$
\begin{align*}
\bar S' \subseteq \bar S \subseteq X \\
S' \subseteq S \subseteq X \leftrightarrow \bar S = S \\
(S \subseteq F) \land (F' \subseteq F \subseteq X) \rightarrow \bar S \subseteq F
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
term
- definition
---
