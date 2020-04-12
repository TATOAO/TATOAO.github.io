# Game Theory 博弈论 note
一共有四章:

## Definition:

__Notation__

$$
\begin{align*}
	S_1,...,S_n &= \text{strategy spaces} \\
	s_1 &= \text{one selection of player 1's strategy} s_1 \in S_1. \\
	s   &= (s_1,...,s_{i-1},s_i,s_{i+1},...,s_n) = (s_i, s_{-1})\\
	s_{-1} &= (s_1,...,s_{i-1},s_{i+1},...,s_n) \\
	S_{-1} &= S_1 \times \cdots \times S_{i-1} \times S_{i+1} \times \cdots \times S_n \\
	u_1,...,u_n &= \text{payoff functions} \\
	u_i(s_1,...,s_n) &= \text{the payoff value for player i, if s_1..} \\
	Game\; G &= \{ S_1,...,S_n;u_1,...,u_n \} \\
\end{align*}
$$


#### def strictly dominated 

Strategy \\({s_i^\prime}\\) is strictly dominated by strategy \\(s_i^{\prime\prime}\\) if :

$$
\begin{align*}
	u_i({s_i^\prime},s_{-i}) &< u_i({s_i^{\prime\prime}},s_{-i}), \;\; \forall s_{-i} \in S_{-i}.  \\
\end{align*}
$$

#### def Best response

The __best response__ for player \\(i\\)  to the other player's strategies \\(s_{-i} \in S_{-i}\\) is:
$$
\begin{align*}
	R_i(s_{-i}) &= \max_{s_i\in S_i} u_i(s_i,s_{-i}). \\
	R_i(s_{-i}) &\subset S_i \text{ it's a set, can be empty, finit or infinite set}\\
\end{align*}
$$



#### def Nash equilibrium

__Definition 4:__ In the n-player normal-form game \\( G = \\{S_1,...,S_n; u_1,...,u_n\\} \\) the strategies \\( (s_1^\*, ..., s_{n}^\*) \\) are a __Nash equilibrium__ if 

$$
\begin{align*}
	s_i^* &= R_i(S_{-i}^*) \; \; \forall i = 1,...,n, \\
		&\iff \\
	u_i(s_i^*, s_{-i}^*) &= \max_{s_i \in S_i} u_i(s_i, s_{-i}^*)\; \; \forall i = 1,...,n 
\end{align*}
$$


###### def Graph

\\(G(R_i) \\) denote the graph of \\(R_i \\), defined by:

$$
\begin{align*}
	G(R_i) &= \{ (s_i,s_{-i})| s_i \in R_i(s_{-i}), s_{-i} \in S_{-i} \}  \\
	(s_1^*, ..., s_{n}^*) &\in \cap_{i = 1}^n G(R_i)\\
\end{align*}
$$

So to find Nash equilibria

__Measure 1 Direct guess__

For any guess (\\(s_{1}^{\*}\\),\\(s_{1}^{\*}\\))  \\(\in S_1 \times S_2\\), compute the \\(R_{1}^{}(s_2^\*)\\) and \\(R_{2}^{}(s_1^\*)\\). Then (\\(s_{1}^{\*}\\),\\(s_{1}^{\*}\\)) is a Nash equilibrium if \\( s_1^\* \in R_1(s_2^\*) \\\) and \\(s_2^\* \in R_2(s_1^\*) \\).

__Measure 2 Intersection of the graph__

\\( (s_1^\*, s_2^\*) \in G(R_1) \cap G(R_2)\\)


1. 完全信息-静态博弈
2. 完全信息-动态博弈
3. 不完全信息-静态博弈
4. 不完全信息-动态博弈
5. 合作博弈


### Chapter 1 完全信息 静态博弈
### Chapter 2 完全信息 动态博弈
### Chapter 3 不完全信息 静态博弈
### Chapter 4 不完全信息 动态博弈
### Chapter 5 合作博弈



<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>


