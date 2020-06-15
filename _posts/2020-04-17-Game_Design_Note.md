# Principles Game Design 

## 前情提要

一切的principle, 都只是 principle, 但是经常当我们太早的走进理论之后, 它们会给我们产生负面效用, 我们的idea 好像这里不够完善, 那里不够成熟, 往往会很打击我们的积极性, 但是如果你觉得 "看来我的还是太天真了" 这种低级的论调的话, 那你可能确实应该早点放弃。我们之所以学习, 不正是因为知道我们的不足嘛！加油吧少年！慢慢雕琢出最好的Design！ 而不是只是一个 Idea


## Level Design

1. balance between exploration & action (state flow) 
2. e.g. like Inside, once puzzle is solved 它应该是容易复现的,而不是要很多操作的

3. tips of level design: 
-   Begin with conceptual work (why the level exists, how it fits into the whole game; develop a focus for your level; provide variety; grid paper 
-   landmarks (like the carsel in the Disney land)
- Architecture of level (design for purposes = meaningful play, 
- progress report)
- 成长曲线, 先易后难,适时给一些小高潮
- Flow Control: how to prevent him from returning 
- Show the player they are doing right.
- Treat them differently, satisfy different kind of people
- Other tips:
	- Use AI effectively
	- Asset sequencing (don't want them getting stuff too early)
	- Avoid player getting suck
	- Progressively reveal eye candy. (tell them this is now and rewards to them)

## Balance

imbalance 简称 imba - 阴霸 我现在才知道这个词是这么来的

首先, balance 固然是重要的,但是 imbalance 也不全是坏事, 有时候这是玩家很大的乐趣。

Player don't know statistic. Sometimes, we need to sacrifices the perfect equation or the realism.


## User experience

#### Accessibility in games
有时候想想, 聋人, 盲人, 高位截瘫的人, 色盲 等等 他们会用怎样的视角去interact with the game, 

book 《the design of everyday things》


## Input System - Input control

Interesting : 那个弹钢琴的app, 还有那个喊话 跳跳的小游戏。

You are creating the language of action.  可以让你 rethink 的 action 
drag - click, hold, ..

innovate when it is needed. 

## Team work

直接摘抄了

Tips

- 80% of teamwork is showing up
- listen to your team members
- Build trust
- give a second chance
- don't sweat the small things
- have a shared vision and shared ownership
- make progress between meetings
- offer solutions, not excuses
- find a way to love your project and take pride in your work



It's all about people -( every things)



Maybe issues
- Communication
	1. Game documents are for "memory" and "communication
	2. Dividing work
	3. Back up your work

## Project Management

Why is it hard:
1. requirements not clear and changing all the time
2. Analysis paralysis


- Lot of time can be wasted ( 64% of functionality rarely used)

Iterative design

- design prototype evaluate


###### Project management techniques

- Agile Development
- SCRUM
- Extreme programming
- Sigma Six


##### AGILE principles
<img src="/post_asset/2020-04-17-Game Design Note_1.png" alt="2020-04-17-Game Design Note_1.png failed" width="400"/>

好像很没用的样子


##### SCRUM

https://www.youtube.com/embed/XU0llRltyFM

好像很好用的样子

##### Goals of Project Management tools

- Memory of decisions
- Communication across team
- Coordination of tasks
- Management of assets
- Planning
- How to prioritize things




# Unity

## C\# 的辅助工具 (和Unity UI 联动)


``` C#
[Range(0f, 10f)]   // 一个滑条的range

[Tooltip("somethign")] // 把鼠标放在上面会有提示

[HideInInspector] // Public Variable 也可以对Editor隐藏

[SerializeField] // Private Variable 也可以对Editor展示
```


###### Stun effect

player 踩到enemy的时候, enemy会晕掉, 要记得在 stun function 

<img src="/post_asset/2020-04-17-Game_Design_Note_1.png" alt="2020-04-17-Game_Design_Note_2.png failed" width="600"/>

在触碰的瞬间, 跳到第二个layout, 保证只调用一次stun function


# Unity

##### Particles Coll

[2020-06-03]

```C#
void OnParticleCollision(GameObject particleHolderObject){}

void OnCollisionEnter2D(Collision2D other){}
```
是两个不同但效果很类似的function, 一个是指particles 的 一个是其他的。


<img src="/post_asset/2020-04-17-Game_Design_Note_2.png" alt="2020-04-17-Game_Design_Note_2.png failed" width="400"/>

但要触发, OnParticleCollison 需要勾上  倒数第二行的 "Send Collision Messages"


