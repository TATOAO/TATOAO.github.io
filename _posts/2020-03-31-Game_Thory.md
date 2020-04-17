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


#### Strictly dominated 

Strategy \\({s_i^\prime}\\) is strictly dominated by strategy \\(s_i^{\prime\prime}\\) if :

$$
\begin{align*}
	u_i({s_i^\prime},s_{-i}) &< u_i({s_i^{\prime\prime}},s_{-i}), \;\; \forall s_{-i} \in S_{-i}.  \\
\end{align*}
$$

#### Best Response

The __best response__ for player \\(i\\)  to the other player's strategies \\(s_{-i} \in S_{-i}\\) is:
$$
\begin{align*}
	R_i(s_{-i}) &= \max_{s_i\in S_i} u_i(s_i,s_{-i}). \\
	R_i(s_{-i}) &\subset S_i \text{ it's a set, can be empty, finit or infinite set}\\
\end{align*}
$$



#### Nash equilibrium

__Definition 4:__ In the n-player normal-form game \\( G = \\{S_1,...,S_n; u_1,...,u_n\\} \\) the strategies \\( (s_1^\*, ..., s_{n}^\*) \\) are a __Nash equilibrium__ if 

$$
\begin{align*}
	s_i^* &= R_i(S_{-i}^*) \; \; \forall i = 1,...,n, \\
		&\iff \\
	u_i(s_i^*, s_{-i}^*) &= \max_{s_i \in S_i} u_i(s_i, s_{-i}^*)\; \; \forall i = 1,...,n 
\end{align*}
$$


###### Graph

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

## Subgame-Perfect
有两个地方出现了这个 Subgame-Perfect
1. Subgame-Perfect Outcome
2. Subgame-Perfect Nash Equilibrium

#### Subgame-Perfect Outcome
课件没有给具体的定义,只有几个example..

我理解的就是直接把每个subgame 找出来,然后把每个combine 每个subgame的NE。


#### Subgame-Perfect Nash Equilibrium

```
A Nash equilibrium is 'subgame-perfect' if the players' strategies consitute a Nash equilibrium in every subgame .
```



## Infinitely repeated games
##### The present value of the sequence of payoffs


$$
\begin{align*}
\pi_1 + \delta \pi_2 + \delta^2 \pi_3 + \dots &= \sum_{t = 1}^{ \infty} \delta^{t-1} \pi_t.\\
1 + \delta + \delta^2 + \dots &= {\frac{1}{1- \delta}}  \\
\delta + \delta^2 + \dots &= {\frac{\delta}{1- \delta}}  \\
\end{align*}
$$



## Trigger strategy \\( T_i\\)

The Prisoners' Dilemma Example:
<img src="/post_asset/2020-03-31-Game_Thory_1.png" alt="2020-03-31-Game_Thory_1.png failed" width="400"/>

\\(R_{}^{}\\)  is cooperate move, \\(L_{}^{}\\) is Non-Cooperate move.

<img src="/post_asset/2020-03-31-Game_Thory_2.png" alt="2020-03-31-Game_Thory_2.png failed" width="550"/>

现在我们要对比合作还是不合作两种策略：
如果一直合作：
$$
4 + 4 \delta + + 4 \delta^2 + \dots = {\frac{4}{1- \delta}} 
$$

如果从,某个时刻开始不合作：

$$
5 + \delta \cdot 1 + \delta^2 \cdot 1 + \dots = 5 + {\frac{ \delta}{1 - \delta}} 
$$

对比就可以解得, \\( \delta\\) 在什么 范围, 大家会一直合作(Trigger strategy is an Nash equilibrium)
<img src="/post_asset/2020-03-31-Game_Thory_4.png" alt="2020-03-31-Game_Thory_4.png failed" width="200"/>

\\( {\frac{1}{4}}\\) 什么水平？ 折现率是每年25%, 今年1块钱的收益,明年只有0.25.

如果我们Generalize 这个example：

<img src="/post_asset/2020-03-31-Game_Thory_5.png" alt="2020-03-31-Game_Thory_5.png failed" width="400"/>

直接带入可以得出：

<img src="/post_asset/2020-03-31-Game_Thory_6.png" alt="2020-03-31-Game_Thory_6.png failed" width="400"/>

## Cournot model
Notation:

$$
\begin{align*}
	q &= \text{ quantity} \\
	c &= \text{ cost of per unit} \\
	p &= \text{ selling price} \\
	\pi &= q(p - c) - c_0\text{ net profit (simply ignore )} c_0 \\
	Q &= q_1 + q_2 \text{ the aggregate quantity of the product} \\
	P(Q) &= 
		\begin{cases} 
		      a - Q &  \text{ if } Q < a \\
		      0     &  \text{otherwise} 
		\end{cases}\\
	& \text{ the price determined by the total quantity} \\
	\pi_i(q_i, q_j) &= P(q_i + q_j) \cdot q_i - c \cdot q_i \text{} \\
	 &= 
	 	\begin{cases} 
	 	      q_i[a - (q_i+ q_j) - c] &  \text{ if } q_i + q_j < a \\
		      -cq_i		      &  \text{ if } q_i + q_j \ge a\\
	 	\end{cases} \\
\end{align*}
$$

所以很简单的, payoff function 是一个二次函数; 最值在：

$$
\begin{align*}
	& \max_{0 \le q_i \le a - q_j^*} q_i[a - c - q_j^* - q_i]  \\
	& \to \bar{q_i} = {\frac{1}{2}}(a - q_j^* - c) \text{ 对称轴 -b/2a}\\
\end{align*}
$$

<img src="/post_asset/2020-03-31-Game_Thory_7.png" alt="2020-03-31-Game_Thory_7.png failed" width="400"/>

Solved:
$$
\begin{align*}
	 	\begin{cases} 
	q_1^* &= {\frac{1}{3}} (a-c) \\
	q_2^* &= {\frac{1}{3}} (a-c) \\
	\pi_1 &= {\frac{(a-c)^2}{9}} \\
	 	\end{cases} \\
\end{align*}
$$

## Collusion between Cournot Duopolists

If the two firms cooperate, then they can maximize their total profit: \\(\boldsymbol{q}_{}^{}\\) 

$$
\begin{align*}
	& \max \boldsymbol{q}(a - \boldsymbol{q} -c) \\
	& \boldsymbol{q_m} = {\frac{a-c}{2}} \\
	& q_1 = {\frac{\boldsymbol{q_m}}{2}} \\
	& \pi_m = {\frac{(a-c)^2}{4}} \\
	& \pi_1 = {\frac{(a-c)^2}{8}} \\
	& \pi_{old} = {\frac{(a-c)^2}{9}}  \\
\end{align*}
$$

However, then if \\( p_i = {\frac{p_m}{2}}\\), the other firm cheat, 

$$
\begin{align*}
	q_1 &= {\frac{q_m}{2}} = {\frac{a-c}{4}}   \\
	\max q_2(a - q_2 - q_1 - c) \to q_2 &= {\frac{a -q_1 - c}{2}} \\
	&= {\frac{3(a-c)}{8}}\\ 
	\pi_d &= {\frac{9(a-c)^2}{64}} > {\frac{(a-c)^2}{8}}  \\
	\pi_c &= {\frac{3(a-c)^2}{32}} \\
\end{align*}
$$

现在对比两个, 一直合作 vs 中途不合作

一直合作：
$$
\begin{align*}
	 &{\frac{(a-c)^2}{8}} (1 + \delta + \delta^2 + \cdots)\\
	 & = {\frac{(a-c)^2}{8}} {\frac{1}{1- \delta}} \\
\end{align*}
$$
中途不合作：
$$
\begin{align*}
& {\frac{9(a-c)^2}{64}} +  {\frac{(a-c)^2}{9}} ( \delta + \delta^2 + \cdots)\\
&= {\frac{9(a-c)^2}{64}} +  {\frac{(a-c)^2}{9}} {\frac{ \delta}{1 - \delta}} \\
\end{align*}
$$

Solved: 
$$
\text{合作} \ge \text{中途不合作}\\
\delta \ge {\frac{9}{17}}
$$








### Chapter 3 不完全信息 静态博弈
### Chapter 4 不完全信息 动态博弈
### Chapter 5 合作博弈



<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>


