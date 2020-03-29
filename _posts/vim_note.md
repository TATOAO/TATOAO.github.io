# Vim 笔记

## Search and replace


替换全局
`:%s/old/new/gc`


这里有个更棒的方案：

先抓取旧的词，

`YIW`

然后 search ` :<C-r>0` 就是粘贴inner word的方法

然后选一行写入要替换的词，再抓取一次， `YIW`

然后移到目标单词， 用 `CIW<C-r>0` 就是把这个词用 inner word 替换掉

然后我们就可以按 n/N 来移动 光标，然后用 `.` 来替换掉这个旧词

非常的酷



* 
    Put the cursor on `foo`.
* Press `*` to search for the next occurrence.
* Type `ciw` (change inner word) then `bar` then press Escape.
* Press `n` (move to next occurrence) then **`.`** ([repeat change](https://vim.fandom.com/wiki/Repeat_last_change)).
* Repeat last step.

## Vim 的神奇快捷键 1 -Searching

`* ` 光标所在的单词 往下搜索
` # ` 光标所在的单词 往上搜索，并同时在 ` n ` 的功能上留下记录，也就是说，用了# 之后就能用n了，但是 * 之后不能

## vimtex


`\ll    开启/关闭自动编译`
`\le    查看错误日志`
\lc           清楚auxiliary 文件
\lv            开查看器


## 长句子分段表示

`:set wrap`
直接在vim 的界面里打这个就可以啦

## Vimdiff 在vim界面里怎么用 （macvim）

```
:e file1
:diffsplit file2
or
:vert diffsplit file2
```

## Vim 如何安装plugin （with Vindle)

1. 改 vimrc
2. 然后打开vim， `:PluginInstall  ` 然后才会开始安装 vimrc里面的plugin
3. or  `vim +PluginInstall +qall` 也可以在terminal 直接安装



```
`:Plugins 查看已有的plugins`
```



## Vim 的神奇快捷键 2 -   加减文中数字

typing Ctrl-A will increment the next number, and typing Ctrl-X will decrement the next number. 


## Vim 分窗口显示


`：vsplit  分成左右两个`
`: split   分成上下两个`
想在窗口间切换的话，直接 control + w.  然后按 hjkl 方向键转移光标


## 自定义快捷Vim editor commaGnd

重新打开文件 （macvim）


## Vim 多行操作

怎么在很多行的前面加一个字符 

* Press Esc to enter 'command mode'
* Use Ctrl+V to enter visual block mode
* Move Up/Downto select the columns of text in the lines you want to comment.
* Then hit Shift+i and type the text you want to insert.
* Then hit Esc, wait 1 second and the inserted text will appear on every line.

## Vim 的神奇快捷键 3 - 选中段落

vip 是一个神奇的命令，会选中整个语意段


## Vim 的神奇快捷键 4 - 跳号内的内容

% 是 括号之间的转换 比如 （ 就到 ） ， ） 就到（
（  ）是直接找到下一个空白行

## Vim 的神奇快捷键 5 - 用vim command 粘贴到 Clipboard
[Link](	https://vi.stackexchange.com/questions/84/how-can-i-copy-text-to-the-system-clipboard-from-vim "")
```bash
# Norm 模式 复制到clipboard
"*yy
"*p
# " 应该是像转义符一样的东西
```
* 代表clipboard

## VIM 里面yun python


这个就是run 该文件的commend
`!python3 shellescape(@%, 1)<cr>`



## Vim 叼炸天功能1！ qq record
何为叼炸天呢，就是几乎只有vim能做到的功能。 <br>
qq 是 macros 宏 记录 开始 recood。左下角会显示 recording。 <br>
意思就是，此刻开始记录你的所有操作。然后在norm 模式按q 退出记录。

要复现可以点 . 或者 @q 但是因为.会被以后的操作覆盖，所以最后用@q

如果要对多次复现的话 可以用 100. 或 100@q

[甚至文件管理](https://thoughtbot.com/blog/vim-macros-and-you "")

## Vim 叼炸天功能2！ register 粘贴板！
[Stack Exchange 答案](https://vi.stackexchange.com/questions/84/how-can-i-copy-text-to-the-system-clipboard-from-vim "")

首先是我们如何把vim y复制的内容到clipboard里： <br>
在norm模式下按 "+yy  <br>
粘贴的话也是按 "+p

"的含义就是 进入 regist， + 代表的就是 mac OS的 clipboard。所以同理，我们可以自定义要register的符号 比如 "1yy "2 "3 "4 就可以把东西粘在不同的格子里，然后 "1p "2p 把他们取出来。
# Snip

Snip 有自动填充的功能的 Control + N 就会自动弹出来啦


## 跳动自动填充位置。Triggor

control + b 下一个
control + z 上一个 
这些都是能在vimrc里设的

### 常用snip：

1. datatime - 日期和时间
2. 


例子

` snippet t "xxxx" b ` 最后的b是说，只有当这个t是行首的时候才显示

`<${1:div}> ` 
默认是\<div> 的意思，然后后面全部 $1 都会同时变化

要去掉变化，要用另外的代替符：
`</${1/(\w+).*/$1/}>`


## Snip 调用其他的窗口内容 `

`` `v strftime("%c")` `` (`` `v ``)就是用vim窗口的内容， vimL， vim script （有待挖掘）
`` `echo $USER` `` (`` ` ``)就是直接用shell的指令


```bash
`!p
#python code!
`
```

## Snip + python

```python
snip.c    # current value
snip.rc  # return value
```

