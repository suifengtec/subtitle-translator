# subtitle translator

srt 字幕自动翻译软件。

[主页](http://coolwp.com/subtitle-translator.html)


## UI

载入字幕文件

![](screenshot/001.png)

选择翻译为什么语种,不选的话,翻译为简体中文

![](screenshot/003.png)

自动翻译后

![](screenshot/002.png)


## 源代码

初始版本的源代码[在这里](./src)

## 所使用的软件

```

eric6
Qt Designer


```

## 依赖的 Python 包
```

pip install PyQt5 fbs requests pysrt  googletrans

```

## 快捷键的使用

Ctrl+F : 查找/打开字幕文件,默认支持srt 类型的字幕；

Ctrl+T: 翻译该字幕文件，如果没有选择语种的话，将默认翻译为简体中文；

Ctrl+S : 保存翻译后的字幕文件；

Ctrl+Alt+S : 保存为双语种字幕文件



## 版本更新

1.0.0 :初始发布;
