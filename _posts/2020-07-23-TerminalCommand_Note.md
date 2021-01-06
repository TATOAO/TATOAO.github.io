# Mac Terminal Command

简单的说就是Unix 的一些简单的命令


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
