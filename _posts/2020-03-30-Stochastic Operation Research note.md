# Stochastic Operation Research note
一共有三章:


1. Queueing Theory <a name="ch1"></a>
2. [Inventory Theory](#ch2 "")

	2.1. Deterministic(#ch2.1 "")
	
	2.2. [Probabilistic](#ch2.2 "")

3. Stochastic Probabilistic

Theory

2.1. [Deterministic](#ch2.1 "")
	
2.2. [Probabilistic](#ch2.2 "")

3. Stochastic Probabilistic


## <a name="ch2"></a> 2. Inventory Theory 库存管理
其实这也是非常intuitive的一章。

Notation:
$$
\begin{aligned}
q &= \text{number of units ordered (decision variable).}\\
D &= \text{random variable (demand)}\\
Pr(D = d) &= p(d) \text{ probability realisation} \\
c(d,q) &= \text{cost function}\\
\end{aligned}
$$

### 2.1. Deterministic Inventory Model <a name="ch2.1"></a>


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
	Pr(X \ge r^*) &= {\frac{hq^*}{C_B \bar{D}}} 
\end{align*}
$$

Note:
1. <u>safety stock</u> - r - 
2. Expected annual holding cost

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
	 q^* &= \sqrt{ {\frac{wK \bar{D}}{h}}}  \\
	 {\frac{\partial TC(q,r)}{\partial r}} &= h + (h + {\frac{C_{LS}\bar{D}}{{q}}) \bar{B_r}^{ \prime}} \\
	 Pr(X \ge r^*) &= {\frac{hq^*}{hq^*+C_{LS} \bar{D}}}
\end{align*}
$$

相比之前的 \\(r^*\\) 就是分母多了个 \\(h q^*\\) 项。


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
  


<script type="text/javascript" async
  src="https://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-MML-AM_CHTML">
</script>


