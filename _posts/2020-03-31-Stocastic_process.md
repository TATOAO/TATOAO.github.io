# 随机过程 Markov Chain

没有严格的分章节

想要回答的问题：

1. Markov Chain definition
2. N_step transition
3. \\( \lim_{n \to \infty} P(X_n = i) \\) Markov Chain Basic Limit Theorem of Markov Chain
4. Regular Matrix
5. Doubly
6. Reducible
7. Time Reversible
8. General Function 




## Markov Chain definition

首先，默认所有的vector都是row vector。

Markov Chain:

$$ p_{i,j} = P(X_{n+1} = j | X_n = i) = P(X_{n+1} = j | X_n = i, X_{n-1} = i_{n-1}, X_{n-2} = ....P(X_{n+1} = j | X_n = i)  ) $$

所以是从下标第一个到第二个，对应的从列到行;

Matrix Notation:
$$
\begin{align*}
  \left[ \begin{array}{ccc}
      P_{1, 1} & \cdots & P_{1, 2}\\
      \vdots & \ddots & \vdots \\
      P_{2, 1} & \cdots & P_{2, 2}
    \end{array} \right]
\end{align*}
$$

记住，是从列map到行。

最经典的Random Walker 的例子：

$$
\begin{align*}
  \left[\begin{array}{ccc}
	1 & 0 & 0 & \cdots \\
	q & 0 & p & 0 \\
	0 & q & 0 & p \\
	\vdots &\vdots &\vdots &\vdots 
    \end{array} \right]
\end{align*}
$$

所以这样的话，每一行的和都是 1。 \\( \displaystyle  for\ i \in \mathcal{S}:  \sum_{j \in \mathcal{S}} P_{i,j} = 1\\) 

______
#### Doubly Stochastic Matrix P

<B> All column sums are 1. \\( \displaystyle  for\ j \in \mathcal{S}:  \sum_{i \in \mathcal{S}} P_{i,j} = 1\\) </B>

e.g.: 
$$
\begin{align*} 
	\left[\begin{array}{ccc}
		\boxed{0.1} &	0.9 \\ 
		0.9 &	0.1 \\ 
	\end{array}
	\right]
\end{align*}
$$

其实只有1个free variable, 所以，M x N 只有 (M-1) x (N-1) 个free variable。

相当于，每一个state的进入机会都是相等的，没有偏重。

Matrix: 

if \\(P\\) & \\(Q\\) are both doubly stochastic matrix. \\( \lambda P + (1- \lambda) Q \\)  & \\(PQ\\) is also a doubly stochastic matrix.

Property:  If a doubly stochastic matrix P is regular then:

1. limiting distribution exists. 
2. Hence stationary distribution exists.
3. It is (1,1,...,1)/M. (Uniformly distributed)
4. 


##### Regular

All elements are strictly positive. 

##### Null-recurrent & Positive recurrent (Class property)
Null-recurrent only possible for infinite state. 

Positive recurrent: If starting at state i, the expected time when MC returns to sate i is finite.

why is a class property (lecture 12 -10+)


##### Irreducible 
All state is in one equivalence class. (All state are connected)

If a finite Markov chain is irreducible, then every state is of the same period; and all states are recurrent. (Finite Markov chain should at least have one recurrent state, infinite Markov chain doesn't e.g. 3-D random walk)


##### Return probability \\( f_i\\)
$$
f_i := P(X_n = i \text{ for some }n \ge 1 | X_0 = i).
$$ 
The probability when MC stats at i and will ever return to i.

##### Recurrent & Transient
$$
\begin{align*}
	\text{transient}  &\iff f_i < 1  &\iff \sum_{n = 1}^{ \infty} p_{i,i}^{(n)} < \infty \\
	\text{recurrrent} &\iff f_i = 1  &\iff \sum_{n = 1}^{ \infty} p_{i,i}^{(n)} = \infty\\
\end{align*}
$$

This is also a class property.
(lecture 10)



##### Period 
The period of state \\(i\\) denoted by \\(d_i = GCD \{ n \ge 1: p_{i,j}^{(n)} > 0 \} \\).

This is also a class property.

##### Aperiodic
Every state is of period 1 is Aperiodic.



#### Detailed Balance Condition ####

$$
\pi_{i} P_{ij} = \pi_{j} P_{ji}
$$

Balance Condition 其实就很好理解，它的任意两个状态，1 -> 2, 2->1 的概率是一样的，所以它一定满足stationary distribution的条件。 <br>但显然的，stationary distribution 不一定满足 Detailed Balance Condition。 



---
## N-th step transition

2 step case:  <br>
\\( p_{i,j}^{(2)} \\) =? 从 \\(i\\) 出发，第二步到 \\(j\\) 的概率。

$$
\begin{align*}
	p_{i,j}^{(2)} &= P(X_2 = j | X_0 = i) \\
		      &= \sum_{k \in S}^{} P(X_1 = k | X_0 = i)P(X_2 = j | X_0 = i, X_1 = k)\\
		      &= \sum_{k \in S}^{} P_{i,k} P{k,j}
\end{align*}
$$

<img src="/post_asset/2020-03-31-Stocastic_process_1.png" alt="2020-03-31-Stocastic_process_1.png failed" width="200"/>


所以 \\( PP = P^2\\). 这样的话 \\( P^2_{i,j}\\) 就直接是走两步了。

所以

Chapman-Kolmogorov equation$$P^{m+n}_{i,j} = \sum_{k \in S}^{} P^{(m)}_{i,k} P^{(n)}_{k,j}$$
$$
P^{(m+n)} = P^{(m)} P^{(n)}
$$








## Markov Chain Basic Limit Theorem of Markov Chain

An __irreducible__, __aperiodic__ and __positive recurrent__ Markov chain. Has a unique solution of the static distribution.

$$
\begin{align*}
	\lim_{n \to \infty} p_{j,j}^{(n)} &= {\frac{1}{E(T_j|X_0 = j)}}\\
	\pi_j &= {\frac{1}{E(T_j|X_0 = j)}}
\end{align*}
$$


### To compute the limiting distribution
$$
\begin{align*}
	\pi_j &= \sum_{i \in S}^{} \pi_i p_{i,j} \\
\end{align*}
$$


## Regular Matrix


## Doubly


## Reducible
## Time Reversible

Time reversible, stationary Markov chain:

$$
\forall i,j \in \mathcal{S}, \tilde{p}_{i,j} = p_{i,j} 
$$
Or equivalently detailed balance equation.





## General Function 



<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>


