# Linear and Network Optimization #
一共有三章:


## 第一部分 Linear Problem 问题
### Simplex 算法
### Duality 对偶性

__Primal__

<img src="/post_asset/2020-03-31-MA3252_Linear_optimation_14.png" alt="2020-03-31-MA3252_Linear_optimation_14.png failed" width="400"/>

__Upper bound__ is easy to find (any feasible \\(x'\\) corresponding \\(c^T x\\))

Define: \\( \displaystyle g(p):= \min_{x\in \mathbb{R}^{n}} c^T x + p^T (b-Ax) \\)

__Lower bound__ can be construct in this form: \\( \displaystyle g(p) \le c^T x^* + p^T (b-Ax^*) \\). where \\((b-Ax^*) \\) should be \\(0\\) and \\(x^*\\) is an optimal solution. <br>等下，如果我们都找到optimal了还要lower bound 做甚？ 

所以 



### Sensitivity Analysis 敏感度分析
就是分析现有的LP，改变一点点条件会如何影响Solution; ( \\(b\\), \\(c\\), \\(A\\), \\(x\\) (new variable), new constraints)

#### Change \\(b\\) 





## 第二部分：  Network Optimisation 网络



##### Flow balance constraint
Flow out - Flow in = Supply


Notation:
$$
\begin{align*}
	x_{ij} &= \text{The amount of flow through arc } (i,j) \in E  \\
	b_i	&= \text{External supply/demand for node } i \\
	b_i	&< 0 \text{ demand node.}\\
	b_i	&> 0 \text{ supply node.}\\
	b_i	&= 0 \text{ transshipment node.}\\
	u_{ij}  &= \text{The upper bound.}\\
	c_{ij}  &= \text{ the post per unit flow on the arc.}
\end{align*}
$$


#### Definition

- Graph
- Cycle
- acyclic		 No cycle
- Tree			 a connected acyclic graph
- Bipartite		 If nodes can be divided into two sets such that the end nodes for each edge lie in different sets.
- Node-arc incidence matrix

<img src="/post_asset/2020-03-31-MA3252_Linear_optimation_1.png" alt="2020-03-31-MA3252_Linear_optimation_1.png failed" width="400"/>


#### Network Flow Formulation
#### Types of network flow problems:
- Shortest Path problem: minimum time/length
- Maximum flow problem: Maximum steady state flow 
- Minimum cost flow problem

####  Minimum cost flow problem
Standard form of a network flow problem:

$$
\begin{align*}
	&min & & c^Tx &\, \\
	&s.t & & Ax = b \\
	&\,  & & 0 \le x  \le u &\, \\
\end{align*}
$$


#### Shortest Path problem: minimum time/length  最短路径问题
Make the node \\(b_{ij} = 0\\) except the one at the start point and the end point. 

\\(b_{start} = 1 \\); <br>
 \\(b_{end} = -1\\)


And also \\(x_{i,j} \in \{ 0,1 \} \\), \\(x\\) variable only determine which road should be picked.

Now: if we relax the binary constrain: From (P1) \\(\to\\) (P2). 

<img src="/post_asset/2020-03-31-MA3252_Linear_optimation_2.png" alt="2020-03-31-MA3252_Linear_optimation_2.png failed" width="400"/>

We have: <br>
##### Theorem 
If there are no negative cycles, then (P2) is also the shortest path problem. (The proof is omitted (will be studied in MA4254 (Discrete Optimization[Dijkstra's algorithm;  and Bellman-Ford and Floyd-Warshall algorithms for negative cycles]))).


###### Negative Cycle:
<img src="/post_asset/2020-03-31-MA3252_Linear_optimation_3.png" alt="2020-03-31-MA3252_Linear_optimation_3.png failed" width="400"/>


##### Three Jug Puzzle Application

<img src="/post_asset/2020-03-31-MA3252_Linear_optimation_4.png" alt="2020-03-31-MA3252_Linear_optimation_4.png failed" width="400"/>

这个也是挺妙的运用。 如何把这个问题转成 最短路径问题: 核心是用坐标表示瓶子的状态： e.g. (5，3)  五升的瓶子有5L水，三升的瓶子有3L水。 然后我们就可以define path 不同瓶子里水倒来倒去。

##### Dynamic Lot Sizing Application

Question Notation: <br>
 \\(T\\) time periods \\( \{ 1,2,...,T \} \\) <br>
\\(d_i\\) Demand of period \\(i\\). <br>
\\(x_i\\) Produce in period \\(i\\) <br>
\\(I_{i-1}\\) Inventory level. <br>
\\(c_i\\) cost of producing one unit product <br>
<img src="/post_asset/2020-03-31-MA3252_Linear_optimation_5.png" alt="2020-03-31-MA3252_Linear_optimation_5.png failed" width="400"/>

可以把这个问题拆成 \\(T\\) 个shortest path problem: <br>
就是可以把每个 \\(d_i\\) 作为一个小终点，然后把所有的solution 加在一起那就是最后的答案了。

- Key Production Property: 最后的solution会
1. Not both carry inventory and produce: 一个node的需求 不会要同时 "生产" & "库存"来满足。[除非上一个库存不要钱(或者甚至是负的)] [而且 setup cost 不为0]
2. Each \\( \displaystyle x_i = \sum_{k\le i}^{} d_k \\) 其实这个也是同理于第一点。


例题： <br>
<img src="/post_asset/2020-03-31-MA3252_Linear_optimation_6.png" alt="2020-03-31-MA3252_Linear_optimation_6.png failed" width="400"/>

待补充。

##### Duality in shortest path problem
<img src="/post_asset/2020-03-31-MA3252_Linear_optimation_7.png" alt="2020-03-31-MA3252_Linear_optimation_7.png failed" width="400"/>

Example:
<img src="/post_asset/2020-03-31-MA3252_Linear_optimation_8.png" alt="2020-03-31-MA3252_Linear_optimation_8.png failed" width="400"/>


Intuitive understanding of the Dual problem:

<img src="/post_asset/2020-03-31-MA3252_Linear_optimation_9.png" alt="2020-03-31-MA3252_Linear_optimation_9.png failed" width="400"/> 

#### Project Management Application

<img src="/post_asset/2020-03-31-MA3252_Linear_optimation_10.png" alt="2020-03-31-MA3252_Linear_optimation_10.png failed" width="400"/>

<img src="/post_asset/2020-03-31-MA3252_Linear_optimation_11.png" alt="2020-03-31-MA3252_Linear_optimation_11.png failed" width="400"/>


#### Maximum Flow Problem

<img src="/post_asset/2020-03-31-MA3252_Linear_optimation_12.png" alt="2020-03-31-MA3252_Linear_optimation_12.png failed" width="400"/>

<img src="/post_asset/2020-03-31-MA3252_Linear_optimation_13.png" alt="2020-03-31-MA3252_Linear_optimation_13.png failed" width="400"/>

##### Duality in maximum flow problem

##### Cut 
A __Cut__ is a partition of V into two subsets \\( \bar{S} = V\setminus  S\\)

- Forward arcs: from nodes in \\(S\\) to nodes in \\(\bar{S}\\). denote \\((S,\bar{S})\\)
- Backward arcs: from nodes in \\(\bar{S}\\) to nodes in \\(S\\). denote \\((\bar{S},S)\\)
- s-t cut, \\( s \in S, t \in \bar{S}\\)
- __capacity__ of a cut: the sum of the capacities of the forward arcs. \\( \displaystyle u(S, \bar{S}) = \sum_{(i,j) \in (S, \bar{S})}^{} u_{i,j}\\)



<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>


