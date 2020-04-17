# Stochastic Operation Research note
一共有三章:


1. Queueing Theory <a name="ch1"></a>
2. [Inventory Theory](#ch2 "")

	2.1. Deterministic(#ch2.1 "")
	
	2.2. [Probabilistic](#ch2.2 "")

3. Stochastic Programming

Theory

2.1. [Deterministic](#ch2.1 "")
	
2.2. [Probabilistic](#ch2.2 "")

3. Stochastic Programming


# <a name="ch2"></a> 2. Inventory Theory 库存管理
其实这也是非常intuitive的一章。

Notation:
$$
\begin{aligned}
q &= \text{number of units ordered (decision variable).}\\
K &=  \text{set up cost per ordre} \\
C &= \text{Purchase cost per item}\\
h &= \text{holding cost per item per unit time}\\
p &= \text{shortage penalty cost per item per unit time}\\
a &= \text{demand rate}\\
D &= \text{random variable (demand)}\\
Pr(D = d) &= p(d) \text{ probability realisation} \\
c(d,q) &= \text{cost function}\\
\end{aligned}
$$

### 2.1. Deterministic Inventory Model <a name="ch2.1"></a>

最简单的情况：

<img src="/post_asset/2020-03-30-Stochastic Operation Research note_11.png" alt="2020-03-30-Stochastic Operation Research note_11.png failed" width="400"/>

$$
\begin{align*}
	{\frac{q}{a}} 		&= \text{Time length of one cycle.} \\
	{\frac{q}{2}} 	&= \text{average inventory level}\\
	h({\frac{q}{2}})&= \text{holding cost}\\
	aC		&= \text{purchase cost per unit time.}\\
	K \div {\frac{q}{a}}	&= \text{set up cost per unit time.}\\
	TC(q)		&= {\frac{aK}{q}}  + aC + {\frac{hq}{2}} \\
	q^*		&= \sqrt{ {\frac{2aK}{h}} } \\
	{\frac{q^*}{a}} &= \sqrt{ {\frac{2K}{ah}} } \text{  optimal cycle length}\\
\end{align*}
$$

#### 允许Shortage：
<img src="/post_asset/2020-03-30-Stochastic Operation Research note_13.png" alt="2020-03-30-Stochastic Operation Research note_13.png failed" width="400"/>

相当于多了一个option，允许shortage了，所以我们需要一个新的变量决定shortage 多久， \\(S_{}^{}\\) 

$$
\begin{align*}
	S 		&= \text{ the stock at the beginning of a cycle} \\
	q 		&\ge S \\
	{\frac{S}{a}} 	&= \text{ time length of without shortage}\\
	{\frac{q}{a}}   &= \text{ time length of a cycle} \\
	{\frac{hS}{2}} {\frac{S}{a}}  	&= \text{ holding cost per cycle}\\ 
	{\frac{hS}{2}} {\frac{S}{a}} \div {\frac{q}{a}} 	&= \text{ holding cost per unit time}\\ 
	p 		&= \text{ shortage cost per item per unit time} \\
	p( {\frac{q-S}{2}}) ( {\frac{q-S}{a}} ) &= \text{ shortage cost per cycle} \\
	aC		&= \text{ purchasing cost per unit time} \\
	TC(q,S)		&= {\frac{aK}{q}} + aC + {\frac{hS^2}{2q}} + {\frac{p(q-S)^2}{2q}} \\
\end{align*}
$$

Then we can solve:
$$
\begin{align*}
	q^* &= \sqrt{ {\frac{2aK}{h}} } \sqrt{ {\frac{p+h}{p}} } \\
	S^* &= \sqrt{ {\frac{2aK}{h}} } \sqrt{ {\frac{p}{p+h}} } \\
	t^* &= {\frac{q^*}{a}} = \sqrt{ {\frac{2K}{ah}}} \sqrt{ {\frac{p+h}{p}} }\\
	\lim_{p \to \infty} q^* &= \text{ in the previous casa, with shortage cost is infinity}\\
\end{align*}
$$




### 2.2. Probabilistic Inventory Model <a name="ch2.2"></a>

- 2.2.1 Optimal Cost
	1. Without Lead time
	2. With Lead time
	3. Allowed Shortage (Back logged case)
	4. Lost Sales Case 	顾客直接不买了 
	5. (s,S) policies 	如果demand 不连续，一次可能被买穿
- 2.2.2 Service Level 考虑 百分之多少的时间会被买穿
- 2.2.3 Periodic Review Models (R,S) Policies 固定时期要检查一次库存

#### Without Lead time: Marginal Analysis (\\(\frac{\alpha}{\beta}\\) Method) 

$$
\begin{align*}
	C_u(d,q) &= - \alpha q + C_1(d) & \text{Understocking cost}\\
	C_o(d,q) - C_u(d,q)&= \beta (q -d) &\text{Overstocking cost}\\
\end{align*}
$$


Proof: p.68

结论就是： \\(Pr(D \le q^*) = {\frac{ \alpha}{\beta}} \\)


##### Other case, if not fit (\\(\frac{\alpha}{\beta}\\)) - Bidding example

Use General method finding minimum cost (一个普通的最值问题).


---
#### With Lead time - Continuous Review Models

So now we have two decision variable: 

<b> \\(q\\) quantity ordered each time  <br> </b>
<b> \\(r\\) reorder point </b>

__Notation__:

$$
\begin{align*}
	K &= \text{Ordering Cost} \\
	h &= \text{holding Cost} \\
	L &= \text{Lead Time (constain)} \\
	D &= \text{Demand/year} \\
	X &= \text{Demand during lead time} \\
	r - \bar{X} &= \text{safety stock} \\
	C_B &= \text{Cost of each unit back-ordered(shortage)} \\
	B_r &= max\{0,X-r\} \text{number of units of shortage during a cycle} \\
	f(x) &= \text{The distribution of X} \\
	\bar{B_r} &= \int^{\infty}_{r}(x-r)f(x) dx \\
	 & \text{This is a genius part. Putting } r \text{ into the function}
\end{align*}
$$
<img src="/post_asset/2020-03-30-MA4260_note_1.png" alt="2020-03-30-MA4260_note_1.png failed" width="300"> <img src="/post_asset/2020-03-30-MA4260_note_2.png" alt="2020-03-30-MA4260_note_2.png failed" width="300">

每次库存量触碰 r 的时候，呼叫订单。Cost function: <br>
Note: This cost is $xx /year

$$
TC(q,r) = h(r - \bar{X} + q/2) + {\frac{C_B \bar{B_r} \bar{D}  }{q} + {\frac{K \bar{D}}{q}}}
$$

$$
\begin{align*}
	{\frac{ \bar{D}}{q}} &= \text{expected no. of cycles/year} \\
	C_B \bar{B_r} &= \text{expected shortage cost/cycle}
\end{align*}
$$


1. expected holding cost/__year__. 假设了，整个曲线是线性的，然后让expected inventory = \\( {\frac{1}{2}} ([r + q - \bar{X}]\\) 初始量   \\(+ [r - \bar{X)]}\\) 结算量， 这个确实会有误差，即使 \\( r - \bar{X} \ge 0\\)是肯定成立的(没人会把r设得大几率会产生shortage的情况) 但当L时段的需求大于\\( \bar{X}\\) ，它是不需要交holding cost的，所以实际是把holding cost高估了。 

[2020-04-09] 这门课就是假设shortage的holding cost的影响忽略不计，我花了不少时间查证这个(有时候不懂就要翻翻textbook，自己瞎想容易走火入魔「想不出来容易拖延，干别的(想不出来容易自闭和怀疑自己智商)」，下次问问自己，对这个是不是真的感兴趣，真的感兴趣也要想想有没有时间深入，这个内容是不是真的重要，能不能以后需要用再仔细研究？仔细权衡利弊，做好计划和记录再开始！切记, 有舍有得才是赢家！)

2. expected shortage cost/year.
3. expected ordering cost/year. 

$$
\begin{align*}
	{\frac{\partial TC(q,r)}{\partial q}} &= {\frac{h}{2}} - {\frac{C_B \bar{B_r} \bar{D} + K \bar{D}}{q^2}}  \\
	{\frac{\partial TC(q,r)}{\partial r}} &= h + {\frac{C_B \bar{D}}{q}} \cdot {\frac{d \bar{B_r}}{d r}}
\end{align*}
$$


结论是: 这是一个二元方程，两个偏导数=0 求解比较麻烦，所以直接让

$$
\begin{align*}
q^* &= \sqrt{ {\frac{2K \bar{D}}{ h}}}\\
\end{align*}
$$

可以解出答案：
$$
\begin{align*}
	Pr(X \ge r^*) &= {\frac{hq^*}{C_B \bar{D}}} \\
	Pr(X \ge r^*) &= Pr(Z \ge {\frac{r^* - \bar{X}}{\sigma}} )
\end{align*}
$$

Note:
1. <u>safety stock</u> \\( r^\* - \bar{X}\\)
2. If \\( {\frac{h q^*}{C_B \bar{D}}} > 1\\), then we cannot use the above formula to determine \\( r^*\\). In this case we simply set r* to a small value. (like epsilon? or negative value?)



##### N?
For example:

$$
\text{ Every year}\\
D \thicksim N(1000, 40.8^2) \\
\text{X is every week, 1/26 year} \\
X \thicksim N( {\frac{1000}{26}} , {\frac{40.8^2}{26}}) \\
$$

$$
\begin{align*}
	Pr(X\ge r^*) &= Pr(Z\ge {\frac{r^* - {\frac{1000}{26}} }{ {\frac{40.8}{\sqrt{26}}} }})   \\
\end{align*}
$$



#### Lost sale case (Shortage not allow) 短缺的需求不会在未来兑现

<img src="/post_asset/2020-03-30-Stochastic Operation Research note_1.png" alt="2020-03-30-Stochastic Operation Research note_1.png failed" width="400"/>

(图里的L为什么不是一样长的，但是我们这个课只讨论是constant的情况。)

Notation: <br>
\\( C_{LS} = \\) cost of 1 unit of lost sale (already include penalty for loss of future goodwill and profit lost because of lost sale)

Expected inventory level in a cycle:
$$
\begin{align*}
	 &= (r - \bar{X} + {\frac{q}{2}}) + (expected shoratages/cycle) \\
	 &= (r - \bar{X} + {\frac{q}{2}}) + \bar{B_r} \\
\end{align*}
$$

前半部分和back-logged一样，然后再加一个 \\( \bar{B_r}\\). 就是说，lost 掉的那部分订单没了，存货多了，相应的库存就增加了。 (这里也顺便验证前面的，课本直接忽略了那部分 库存 \\(\le 0\\) 的情况)

$$
\begin{align*}
	TC(q,r) &= h(r - \bar{X} + {\frac{q}{2}} + \bar{B_r}) + {\frac{C_{LS} \bar{B_r} \bar{D} }{q}} + {\frac{K \bar{D}}{q}}  \\
\end{align*}
$$
还是 Holding cost + shortage cost + setup cost。 <br>
shortage cost 也是简单的把 \\(C_B\\) 变成 \\( C_{LS}\\)

$$
\begin{align*}
	 q^* &= \sqrt{ {\frac{2K \bar{D}}{h}}}  \\
	 {\frac{\partial TC(q,r)}{\partial r}} &= h + {\frac{d \bar{Br}}{dr}} (h + \frac{C_{LS}\bar{D}}{q}) \\
	 Pr(X \ge r^*) &= {\frac{hq^*}{hq^*+C_{LS} \bar{D}}}
\end{align*}
$$

相比之前的 \\(r^\*\\) 就是分母多了个 \\(h q^\*\\) 项。


##### (s,S) policies: 补到 S 这么多

之前是简单的补 \\(q\\) 这么多的货，加上一个条件是，如果需求曲线不是连续的，可能会跳过r点以下，这样就要补更它的差货： \\( r^* - I(t)\\) 到 \\(S\\). 


#### Service Level Approach

因为经常，shortage penalty cost 比较难界定，所以会用Service level approach。就只是换了个衡量标准，不再用cost 来衡量。


###### Service Level measure 1
$$
\begin{align*}
	SLM_1 &= \text{expected fraction of demand met on time.} \\
	1 - SLM_1 &= {\frac{ \text{expected shortages/year}}{ \text{expected demand/year}}} = {\frac{ \bar{B_r} \bar{D}  / q}{ \bar{D}}} = {\frac{ \bar{B_r}}{q}}
\end{align*}
$$
规定，至少% 多少的时间要满足需求。 每个circle，进货 \\(q\\)， 平均 \\( \bar{B_r}\\) 的shortage. 



###### Service Level measure 2
用%多少个周期来衡量
$$
\begin{align*}
	SML_2 &= \text{expected number of cycles per year during which a shortage occurs}  \\
	SML_2 &=  \text{(Prob of stockout) x (number of cycles/year).} \\
	SML_2 &=  Pr(X > r) {\frac{ \bar{D}}{q}} \\
\end{align*}
$$

###### To calculate B_r Normal Loss function 

$$
\begin{align*}
	f(x) &= {\frac{1}{\sigma_x \sqrt{2\pi} }} e^{ - {\frac{(x - \bar{X})^2}{2 \sigma_x^2}} } \\
	\bar{B_r} &= \int^{\infty}_{r}(x-r)f(x) dx \\
	\bar{B_r} &= {\frac{1}{\sigma_x \sqrt{2\pi} }} \int_{r}^{\infty} (x-r)   e^{ - {\frac{(x - \bar{X})^2}{2 \sigma_x^2}} } dx  \\
		  &= {\frac{\sigma_x}{\sqrt{2\pi}}} \int_{ {\frac{r - \bar{X}}{\sigma_x}} }^{\infty} (z - {\frac{r - \bar{X}}{\sigma_x}}) e^{ -{\frac{z^2}{2}} } dz \\

	NL( \alpha) &= {\frac{1}{\sqrt{2\pi}}} \int_{ \alpha}^{\infty} (z - \alpha) e^{- {\frac{z^2}{2}} } dz \\
	\bar{B_r} &= \sigma_x NL( {\frac{r - \bar{X}}{\sigma_x}} )
\end{align*}
$$

Then we can check the table of \\(NL_{}^{}\\) .


#### Periodic Review Models: (R,S) Policies 定期检查策略
这个策略是假设我们已经决定了 \\(R\\), 然后我们来找出 \\(S\\)。

##### Back-logged case
$$
\begin{align*}
	S &= \text{On-hand inventory + inventory ordered} \\
	R &= \text{review interval.}\\
	D_{L+R} &= \text{demand during a time interval of length L + R.}\\
	E(D_{L+R}) &= {\bar{D}}_{L+R} \text{ std. dev. } \sigma_{D_{L+R}} \text{ } f(x) \\
	J &= \text{cost of reviewing inventory level.}
\end{align*}
$$


简单的说就是，定期查看库存，得到 \\(I(t_i)\\) 然后补充 \\(S - I(t_i)\\) 的货到 \\(S\\). 所以这个model的optimal会比 (r，q) model 更差一些(成本更高)，因为这个model不光固定了，进货量，还固定了了Circle的时长。A more restricted model.


<img src="/post_asset/2020-03-30-Stochastic Operation Research note_2.png" alt="2020-03-30-Stochastic Operation Research note_2.png failed" width="400"/>


###### Inventory level in a cycle 库存量
同样是approximate 不用太深究。(期初 + 期末) /2。乍看下面这个表达会让人一头雾水，这么会有 \\(\bar{D}_{L+R}\\) 这种重复时段的表达呢，其实还是有点微妙的，


$$
\begin{align*}
	 &= {\frac{1}{2}} [(S - \bar{D}_{L+R}) + (S - \bar{D}_{L+R} + \bar{D}R)] \\
	 &= (S - \bar{D}_{L+R} + {\frac{ \bar{D}R}{2}})
\end{align*}
$$


<img src="/post_asset/Stochastic Operation Research had wrtiting note.jpeg" alt="Stochastic Operation Research had wrtiting note.jpeg failed" width="400"/>

其实这个表达也是有点坑的，但老师的这个note本来就是简略版的，所以就原谅他吧(可能就是想说这个内容并不重要..)

然后顺理成章的，我们有 setup cost + holding cost + expected shortage cost：(cost/year)

$$
\begin{align*}
	TC(R,S) &= {\frac{K+J}{R}} + h[S - \bar{D}_{L+R} + {\frac{ \bar{D}R}{2}}]	+ {\frac{C_B}{R}} \int_{S}^{\infty} (x-S)f(x) dx \\
\end{align*}
$$

先解S，然后conventionally 用EOQ 代q --> \\( {\frac{EOQ}{ \bar{D}}} \\) 代 \\(R_{}^{\*}\\) (周期长)。

$$
\begin{align*}
	Pr(D_{L+R} > S^*) &= {\frac{Rh}{C_B}}   \\
	R^* &= {\frac{EOQ}{ \bar{D}}} = \sqrt{\frac{2(K+J)}{h \bar{D}}} 
\end{align*}
$$

##### Lost-sale case

<img src="/post_asset/2020-03-30-Stochastic Operation Research note_4.png" alt="2020-03-30-Stochastic Operation Research note_4.png failed" width="400"/>


对比 Back-logged case 的expected inventory level, 其实就是多加了一个\\( \int_{S}^{\infty} (x-S)f(x) dx\\). 

所以同理咯，只是全部加一项。

<img src="/post_asset/2020-03-30-Stochastic Operation Research note_5.png" alt="2020-03-30-Stochastic Operation Research note_5.png failed" width="400"/>


# 第三部分 Stochastic Programming 

## General model of two-stage stochastic program.

The introduction example:

<img src="/post_asset/2020-03-30-Stochastic Operation Research note_6.png" alt="2020-03-30-Stochastic Operation Research note_6.png failed" width="400"/>


$$
\begin{align*}
	x_1 &= \text{wheat (acres of land)} \\
	x_2 &= \text{corn (acres of land)} \\
	x_3 &= \text{sugar beets (acres of land)} \\
	& \\
	w_1 &= \text{wheat sold (tons)}\\
	w_2 &= \text{corn eat sold (tons)}\\
	w_3 &= \text{sugar beets sold (favorable price) (tons)}\\
	w_4 &= \text{sugar beets sold (lower price) (tons)}\\
	& \\
	y_1 &= \text{wheat purchased (tons)}\\
	y_2 &= \text{corn purchased (tons)}\\
	y_3 &= \text{sugar beets purchased (tons)}\\
\end{align*}
$$

$$
\begin{align*}
	&\min & 150x_1 + 230x_2 + 260x_3  &\\
	& \;  &+238y_1 + 210y^2 &\\
	& \;  &-170w_1 - 150w_2 - 36w_3 - 10w_4 &\\
	& & & \\
	& s.t.&x_1 + x_2 + x_3 \le 500, &\text{ Total arcs} \\
	& \;  &\fbox{2.5}x_1 + y_1 - w_1 \ge 200, & \text{ left of wheat minimum, link the yield as well} \\
	& \;  &\fbox{3}x_2 + y_2 - w_2 \ge 240, & \text{ left of corn minimum, link the yield as well} \\
	& \;  &w_3 + w_4 \le 20x_3 & \text{ sugar beets less or equal to grow}\\
	& \;  &w_3 \le 6000, & \text{ good price no exeed quote} \\
	& \;  & \text{ all variable} \ge 0 &
\end{align*}
$$

现在问题是，画方块的参数，收成是不确定的，不能保证每亩地的长出的麦子/玉米和以前一样。

所以，假设，有三种情况，低收成，中等收成，高收成，分别是1/3 的概率。

那么我们的variables里的， \\(x_1, x_2, x_3\\) 不变，但是 \\(y, w\\) 变成：

$$
y_{11}\; y_{12} \;y_{13}\; \text{三种情况的麦子的买入量} \\
w_{11}\; w_{12} \;w_{13}\; \text{三种情况的麦子的卖出量} \\
...
$$

##### First stage variable: like the arcs.
就像开头的example里的，种多少地，\\(x_{1}, x_2, x_3\\) 这个是不随收成高低而变化的决策，(种什么是一开始就要确定的)
##### Second stage variable: The realization of same random vector  
像\\(y_{11}, y_{12}, y_{13} \\) 这种是我们收割完粮食，可以在后面决定的决策。 After full information is received <u> on the realization of some random vector</u> \\(\xi\\)  , the second-stage or corrective actions \\(y\in \mathbb{R}^{n2}\\) are taken.

## General form
$$
\begin{align*}
	&\min c^Tx + \mathbb{E}_\xi Q(x,\xi) \\
	&s.t. Ax = b, x\ge 0. \\
\end{align*}
$$

$$
\begin{align*}
	Q(x,\xi) &= \min \{\mathbf{q}^Ty| Wy = \mathbf{h}-\mathbf{T}x,y\ge 0 \} \\
\end{align*}
$$

所以这里 \\(\boldsymbol{\xi}\\) 由三个部分组成 \\( \boldsymbol{q}, \mathbf{h}, \mathbf{T}\\) 是三个random variables可能的，分别对应 c / b / A 三种可能的stochastic的形式。这里的 \\(y_{}^{}\\) 也是free variable，相等于是后发行动的选择(买卖多少小麦)。


<u>Notation</u>: <br>
a indicator function of a set \\( C \subseteq \mathbb{R}^{n}\\)
$$
\begin{align*}
\delta_C(x) &= 
	\begin{cases} 
	      0 &  \text{ if } x \in C \\
	      + \infty & \text{otherwise} 
	\end{cases} \\
\end{align*}
$$

$$
\begin{align*}
	K_1 &= \{ x| Ax = b, x \le 0 \}  \\
	K_2(\xi) &= \{ x| \exists y\le 0 \; s.t. Wy = h - Tx \}  \\
\end{align*}
$$

Then now, we can define cost function:
$$
\displaystyle
\min_{x\in \mathbb{R}^{n_1}} c^Tx + \mathbb{E}_{\xi} Q(x,\xi) + \delta_{K_1}(x)
$$ 就是，如果这个 \\(x_{}^{}\\) 不在feasible region的话，optimal是正无穷(infeasible) 

$$
\begin{align*}
	z(x,\xi) &= c^Tx + Q(x,\xi) + \delta_{K_1}(x) \\
	         &= c^Tx +  \min \{\mathbf{q}^Ty| Wy = \mathbf{h}-\mathbf{T}x,y\ge 0 \} + \delta_{K_1}(x) \\
	& \\
	K_2(\xi) &= \{ x| \exists y \le 0 \; s.t. Wy = h - Tx \} \\
\end{align*}
$$

K2 同样也可以理解为某种scenario \\(\xi\\) 里的 feasible region。

所以：

$$
\begin{align*}
z(x,\xi) &= 
	\begin{cases} 
	      + \infty &  \text{ if } x \notin K_1 \cap K_2(\xi) \\
	      - \infty &  \text{ if Q is unbounded below}  
	\end{cases} \\
\end{align*}
$$

所以最后，two-stage stochastic program can be written as

$$
	\displaystyle \min_{x\in \mathbb{R}^{n_1}} \mathbb{E}_{\xi} z(x,\xi) 
$$


#### The expected Value of Perfect information
Note assumption: 

1. There is at least one \\(\xi\\) that give finite optimal.
2. \\( \bar{x}(\xi)\\) denotes some optimal solution. with optimal objective value is \\(z(\bar{x}(\xi), \xi)\\).

#### "wait and see" (WS) & "here and now" (RP)

WS: 能遇见未来的情况
RP：更真实的情况

Expected value of perfect information.
$$
\begin{align*}
	 EV PI &= RP - WS\\
	 WS &= -\$115,426 ( as {\frac{z_1 + z_2 + z_3}{3}}) \\
	 RP &= -\$108,390  \text{ 如果不能遇见收成}\\
	 EV PI &= $7,016\\
\end{align*}
$$

#### Value of the stochastic solution (VSS) (Expected value problem)

$$
\begin{align*}
	&EV &= &\min_{x} z(x, \bar{\xi})  \\
	&\bar{x}( \bar{\xi}) &= &\text{the optimal solution of EV} \\
	&EEV &= &\mathbb{E}(z(x, \bar{\xi}))  \\
	&VSS &= &EEV - RP. \text{Value of Stochastic Solution}\\
	&WS &\le &RP \le EEV. \\
\end{align*}
$$

先用 \\(\bar{\xi}\\) 确定 \\( \bar{x}\\)，让后带入 \\(z( \bar{x}( \bar{\xi}), \xi)\\), 然后再求 \\(z_{}^{}\\) 的Expectation 这就是为什么有 两个 E.


#### Example 9.1


<img src="/post_asset/2020-03-30-Stochastic Operation Research note_8.png" alt="2020-03-30-Stochastic Operation Research note_8.png failed" width="600"/>

##### WS
<img src="/post_asset/2020-03-30-Stochastic Operation Research note_9.png" alt="2020-03-30-Stochastic Operation Research note_9.png failed" width="600"/>

##### EEV
<img src="/post_asset/2020-03-30-Stochastic Operation Research note_10.png" alt="2020-03-30-Stochastic Operation Research note_10.png failed" width="500"/>

书上其实写的挺清楚的了。直接摘抄了.















<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>


