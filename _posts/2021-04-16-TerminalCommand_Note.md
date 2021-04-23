# Mac Terminal Command

简单的说就是Unix 的一些简单的命令


### Soft link

```sh
ln -s original_file softed_linked_path

readlink (file)
```

### Alias

相当于形成捷径
```sh
alias something_named=' 一个命令 '

```


### For loop

[SO convert an entire directory with ffmpeg](https://stackoverflow.com/questions/5784661/how-do-you-convert-an-entire-directory-with-ffmpeg)
```
for i in *.avi;
  do name=`echo "$i" | cut -d'.' -f1`
  echo "$name"
  ffmpeg -i "$i" "${name}.mov"
done
```

for loop 果然好用,相信这是一切的基础。

```
for i in *.mkv; 
  do name=`echo "$i" | cut -d'.' -f1`; 
  echo "$name";
  ffmpeg -i "$i" -vcodec copy -acodec copy "$name.mp4";
done
```
稍微改编了一下, done！
很方便的把当前文件夹的所有mkv 转成了mp4, 又快又好！

# anaconda

如果要创建环境


根据ymlfile
```bash
conda env create -file environment.yml
conda env create -f environment.yml
```
yml 里面会提供一个名字


直接创建：
```bash
conda create --name myenv
```

然后后来再用yml update 
```bash
conda activate myenv
conda env update --file local.yml

```

检查现在有什么包：

```bash
conda list
```


# Linux Setup


### Create a user and set passward

```sh
useradd tatoao
useradd -e 2022-10-10 tatoao # 设有效期至
passwd tatoao
```

### add user to a group / sudo group

```sh
usermod -aG sudo tatoao

groups tatoao
# list all groups tatoao in
```

-aG append add

[set up permission](https://askubuntu.com/questions/487527/give-specific-user-permission-to-write-to-a-folder-using-w-notation ":)")

```sh

```




[传不同的 变量 pipe result ](https://stackoverflow.com/questions/3437514/bash-how-to-pipe-result-from-the-which-command-to-cd/3437518 ":)")

```sh

cd < `which ranger`

cd $(which oracle)
```



### 在后台跑process

```sh
nohup jupyter notebook 

kill xxxxx(task id)
```



```sh
control + z  # suspend process

bg  # keep running in background
```


## Ranger

Ranger command

F7 mkdir

重命名 I （大写 i 字头开始 ） a 字尾（后缀前）开始编辑    A 最后的最后


t 只是一个标记* 的功能

空格 v 选中


Bulk rename  可以批量编辑文件名


Vim 每行插入。  Control + i, 大写 i ， esc


### Screen

---
title: 2021-04-10
date: 2021-04-10 14:41
---
````sh
screen 
Contral + a ,  C # 创建并跳到新窗口
Control + a， k # 关闭当前窗口
Control + a， "  #（双引号）查看开了几个窗口
Control + a， n #跳到下一个窗口
Control + a , 数字。# 也是跳到对应窗口
Control + a，两次 # 上一个窗口
Control + a， p # 上一个窗口
Control + a， ' #（单引号） 输入一个数字，跳到那个对应窗口
Control + a， a # 光标到行首
Control + a， \ # kill all windows
Control + a ， d # detach 当前对话

screen -ls # 查看有几个回话
screen -r 2514 # 输入任务 id 进入目标对话
kill 2513 # 直接 kill 整个会话
screen -d 2515 # 手动断开一个连接

screen -x 2512 # 可以连接一个已经被连接的会话， 就是两个人同时能看到对方的编辑

```



多屏之间互动
复制东西到别的窗口
```sh
control + a,  [ #复制 
hjkl # 移动光标
空格 # 开始文本复制/ 结束文本复制
control + a， ] # 粘贴
```

分屏
```sh
control + a, S # 上下分屏
control + a，｜ # 左右分屏
control + a ， tab # 在分屏中切换光标 （注意要 contral + a， c 开始会话）
control + a, X # （大写关闭某个分屏（不关闭会话）
```

```sh
watch "data >> test.txt" # 每秒把时间写入到文件最后
tail -f test.txt # 只看最后的几行
```

其他
```sh
control +a , x # 锁住输入
control + a, s # 锁住屏幕
control + a，q #解锁屏幕

control + a， ？ # 查看其他的快捷键
```



### 改zsh 为默认的shell 

```sh
chsh -s $(which zsh)
```


